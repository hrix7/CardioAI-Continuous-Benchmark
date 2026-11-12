import copy
import json
import math
from pathlib import Path
import random
import subprocess
import sys
import tempfile
import unittest
import pipeline as p

class Reproducibility(unittest.TestCase):
    def test_repeatable(self):
        self.assertEqual(p.experiment(), p.experiment())
    def test_all_metrics_finite(self):
        result = json.loads(p.experiment()['results.json'])
        def walk(x):
            if isinstance(x, float): self.assertTrue(math.isfinite(x))
            elif isinstance(x,dict):
                for v in x.values(): walk(v)
            elif isinstance(x,list):
                for v in x: walk(v)
        walk(result)
    def test_verifier_rejects_tampering(self):
        with tempfile.TemporaryDirectory() as d:
            cmd=[sys.executable,str(p.ROOT/'pipeline.py'),'--output',d]
            subprocess.run(cmd,check=True,capture_output=True)
            subprocess.run(cmd+['--verify'],check=True,capture_output=True)
            path=Path(d)/'data.csv'
            path.write_text('tampered')
            self.assertNotEqual(subprocess.run(cmd+['--verify'],capture_output=True).returncode,0)

class BenchmarkTests(unittest.TestCase):
    def test_hand_calculated_confusion(self):
        r=p.scores([0,0,1,1],[0,1,0,1])
        self.assertEqual(r['confusion_matrix_rows_true'],[[1,1],[1,1]])
        self.assertEqual(r['balanced_accuracy'],.5)
    def test_feature_contract(self):
        self.assertEqual(p.features([1,1,1]),[0,0])
        with self.assertRaises(ValueError): p.features([1,-1,1])
    def test_no_subject_overlap(self):
        import csv,io
        rows=list(csv.DictReader(io.StringIO(p.experiment()['data.csv'].decode())))
        splits={s:{r['subject'] for r in rows if r['split']==s} for s in ('train','test','shifted_test')}
        self.assertFalse(splits['train'] & splits['test'])
        self.assertFalse(splits['train'] & splits['shifted_test'])
        self.assertEqual(len(splits['test']),240)
    def test_training_only_fit(self):
        training=[([0,0],0),([1,1],1),([.1,.2],0),([.9,.8],1)]
        original=copy.deepcopy(training)
        model=p.fit(training)
        p.predict(model,[100,100])
        self.assertEqual(training,original)
        self.assertEqual(model,p.fit(training))

class EvaluationContractTests(unittest.TestCase):
    def test_missing_or_extra_predictions_rejected(self):
        for predicted in ([0], [0,1,1]):
            with self.subTest(predicted=predicted):
                with self.assertRaisesRegex(ValueError,'equally sized'):
                    p.scores([0,1],predicted)

    def test_empty_and_single_class_truth_rejected(self):
        for truth,predicted in (([],[]),([0,0],[0,1]),([1],[1])):
            with self.subTest(truth=truth):
                with self.assertRaises(ValueError): p.scores(truth,predicted)

    def test_unsupported_labels_rejected_in_either_vector(self):
        for bad in (-1,2,float('nan'),float('inf'),'0',None):
            for truth,predicted in (([0,1],[0,bad]),([bad,1],[0,1])):
                with self.subTest(truth=truth,predicted=predicted):
                    with self.assertRaisesRegex(ValueError,'binary labels'):
                        p.scores(truth,predicted)

    def test_constant_predictor_is_valid_and_counts_all_subjects(self):
        result=p.scores([0,0,0,1],[0,0,0,0])
        self.assertEqual(result['accuracy'],.75)
        self.assertEqual(result['balanced_accuracy'],.5)
        self.assertEqual(sum(map(sum,result['confusion_matrix_rows_true'])),4)
