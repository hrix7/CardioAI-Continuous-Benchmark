import unittest
from unittest.mock import patch
import pipeline as p
class ShiftedOrderTests(unittest.TestCase):
 def test_named_cohort_preserves_pairs_and_never_refits(self):
  samples=[([.7,.9,.8,1.0],0),([.6,1.1,.7,1.0],1)]
  model=p.fit([(p.features(rr),y) for rr,y in samples])
  with patch.object(p,'fit',side_effect=AssertionError('holdout fit')):
   r=p.sorted_order_probe(model,samples,33,'noise_shift')
  self.assertEqual(r['cohort'],'noise_shift');self.assertAlmostEqual(r['max_abs_cv_difference'],0)
  expected=p.scores([y for rr,y in samples],[p.predict(model,p.features(rr)) for rr,y in samples])
  self.assertEqual(r['original'],expected)
  self.assertEqual(r,p.sorted_order_probe(model,samples,33,'noise_shift'))
 def test_unknown_cohort_rejected(self):
  with self.assertRaises(ValueError):p.sorted_order_probe({},[],cohort='pooled')
