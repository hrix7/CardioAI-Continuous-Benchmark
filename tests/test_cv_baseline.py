import unittest
import pipeline as p
class CVBaselineTests(unittest.TestCase):
 def test_training_means_and_hand_calculated_boundary(self):
  means=p.fit_cv_baseline([([.1,100],0),([.3,-100],0),([.7,10],1),([.9,20],1)])
  self.assertAlmostEqual(means[0],.2);self.assertAlmostEqual(means[1],.8)
  self.assertEqual(p.predict_cv_baseline(means,[.4,9999]),0)
  self.assertEqual(p.predict_cv_baseline(means,[.6,-9999]),1)
 def test_no_test_values_enter_fit_and_reversed_orientation(self):
  training=[([1,0],0),([0,0],1)];means=p.fit_cv_baseline(training)
  self.assertEqual(p.predict_cv_baseline(means,[.1,4]),1)
  for x in [[99,99],[-99,-99]]:p.predict_cv_baseline(means,x)
  self.assertEqual(means,p.fit_cv_baseline(training));self.assertEqual(p.predict_cv_baseline([.5,.5],[.5,1]),0)
 def test_invalid_training_and_inference_rejected(self):
  for samples in ([],[([1,2],0)],[([1,float('nan')],0),([2,3],1)]):
   with self.assertRaises(ValueError):p.fit_cv_baseline(samples)
  with self.assertRaises(ValueError):p.predict_cv_baseline([0,1],[float('inf'),1])
