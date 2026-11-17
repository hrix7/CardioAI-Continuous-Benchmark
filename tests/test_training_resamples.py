import unittest,copy
from unittest.mock import patch
import pipeline as p
class TrainingResampleTests(unittest.TestCase):
 def test_separable_hand_fixture_and_repeatability(self):
  train=[([.0,.0],0),([.1,.1],0),([.9,.9],1),([1.,1.],1)];test=[([.05,.05],0),([.95,.95],1)]
  original=copy.deepcopy(train);a=p.training_resample_scores(train,test,test,123,20)
  self.assertEqual(a,p.training_resample_scores(train,test,test,123,20));self.assertEqual(train,original)
  for name in ('in_distribution','noise_shift'):
   self.assertEqual(a[name]['minimum'],1);self.assertEqual(a[name]['maximum'],1)
 def test_only_training_rows_enter_refits(self):
  train=[([0.,0.],0),([1.,1.],1)];test=[([-100.,-100.],0),([100.,100.],1)]
  with patch.object(p,'fit',wraps=p.fit) as fit:
   p.training_resample_scores(train,test,test,8,20)
  self.assertEqual(fit.call_count,20)
  for call in fit.call_args_list:
   self.assertTrue(all(row in train for row in call.args[0]));self.assertEqual({y for x,y in call.args[0]},{0,1})
  with self.assertRaises(ValueError):p.training_resample_scores(train,test,test,8,1)
