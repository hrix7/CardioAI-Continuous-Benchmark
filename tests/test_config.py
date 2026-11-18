import copy,json,unittest
from unittest.mock import patch
import pipeline as p
class ConfigTests(unittest.TestCase):
 def setUp(self):self.config=json.loads((p.ROOT/'config.json').read_text())
 def test_invalid_config_fails_before_generator(self):
  invalid=[('seeds',[]),('seeds',[1,1]),('seeds',[True]),('train_subjects',1),('test_subjects',0),('beats',2),('beats',3.0),('noise_shift',-1),('noise_shift',float('nan')),('noise_shift',True)]
  with patch.object(p,'rhythm',side_effect=AssertionError('generation must not start')) as generator:
   for key,value in invalid:
    config={**self.config,key:value}
    with self.subTest(key=key,value=value):
     with self.assertRaises(ValueError):p.run(config)
   config=copy.deepcopy(self.config);del config['beats']
   with self.assertRaises(ValueError):p.run(config)
   generator.assert_not_called()
 def test_smallest_class_disjoint_cohorts_and_odd_counts(self):
  config={**self.config,'seeds':[7],'train_subjects':3,'test_subjects':3,'beats':3,'noise_shift':0}
  original=copy.deepcopy(config);rows,metrics=p.run(config)
  self.assertEqual(config,original);self.assertEqual(len(rows)-1,27)
  self.assertEqual(metrics['experiments'][0]['in_distribution']['n_test_subjects'],3)
