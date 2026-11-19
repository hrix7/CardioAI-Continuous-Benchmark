import copy,unittest
from unittest.mock import patch
import pipeline as p
class OrderProbeTests(unittest.TestCase):
 def test_paired_marginals_nonmutation_and_no_fit(self):
  rr=[([1.,1.1,.9,1.05],0),([.6,1.4,.7,1.3],1)];before=copy.deepcopy(rr);model=p.fit([(p.features(x),y) for x,y in rr])
  with patch.object(p,'fit',side_effect=AssertionError('no holdout fit')):
   r=p.sorted_order_probe(model,rr)
  self.assertEqual(rr,before);self.assertLess(r['max_abs_cv_difference'],1e-12);self.assertLess(r['mean_sorted_normalized_rmssd'],r['mean_original_normalized_rmssd'])
  for key in ('original','sorted_order'):self.assertEqual(r[key]['n_test_subjects'],2)
 def test_hand_derived_rmssd_and_confusion(self):
  rr=[([1,2,1],0),([3,1,3],1)];model=p.fit([(p.features(x),y) for x,y in rr]);r=p.sorted_order_probe(model,rr)
  expected=sum(p.features(sorted(x))[1] for x,y in rr)/2
  self.assertEqual(r['mean_sorted_normalized_rmssd'],expected)
  self.assertEqual(r['sorted_order'],p.scores([0,1],[p.predict(model,p.features(sorted(x))) for x,y in rr]))
