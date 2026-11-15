import unittest
import pipeline as p
class TrainingContractTests(unittest.TestCase):
 def test_both_models_reject_invalid_training(self):
  bad=[[],[([0,1],0)],[([0,1],0),([2,float('nan')],1)],[([0,1],0),([2],1)],[([0,1],False),([2,3],1)],[([0,'bad'],0),([2,3],1)]]
  for samples in bad:
   for method in (p.fit,p.fit_cv_baseline):
    with self.subTest(samples=samples,method=method.__name__):
     with self.assertRaises(ValueError):method(samples)
 def test_inference_refuses_invalid_feature_or_scale(self):
  model=p.fit([([0,1],0),([2,3],1)])
  for x in ([1],[1,float('inf')],['bad',1]):
   with self.assertRaises(ValueError):p.predict(model,x)
  with self.assertRaises(ValueError):p.predict(([0,0],[0,1],[[0,0],[1,1]]),[1,1])
 def test_single_subject_per_class_remains_valid(self):
  training=[([0,1],0),([2,3],1)];model=p.fit(training)
  self.assertEqual([p.predict(model,x) for x,y in training],[0,1])
