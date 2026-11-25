import unittest
from unittest.mock import patch
import pipeline as p
class ReversalTests(unittest.TestCase):
 def test_hand_sequences_preserve_features_and_predictions_without_fit(self):
  subjects=[([.8,.9,.7,1.0],0),([.5,1.4,.6,1.2],1)];model=p.fit([(p.features(rr),y) for rr,y in subjects])
  with patch.object(p,'fit',side_effect=AssertionError('no refit')):r=p.reversal_order_probe(model,subjects)
  self.assertEqual(r['prediction_disagreements'],0);self.assertEqual(r['original'],r['reversed']);self.assertLess(r['max_abs_feature_difference'],1e-14)
 def test_reported_disagreements_are_counted_not_forced_to_zero(self):
  subjects=[([.8,.9,.7],0),([.5,1.4,.6],1)]
  with patch.object(p,'predict',side_effect=[0,1,1,1]):r=p.reversal_order_probe({},subjects)
  self.assertEqual(r['prediction_disagreements'],1)
