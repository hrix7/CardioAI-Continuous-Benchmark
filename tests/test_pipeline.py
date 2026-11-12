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
