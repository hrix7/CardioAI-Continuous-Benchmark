import unittest
import pipeline as p
class PairedDeltaTests(unittest.TestCase):
 def test_identical_pairs_always_zero_even_with_errors(self):
  r=p.paired_bootstrap_delta([0,0,1,1],[0,1,0,1],[0,1,0,1],8)
  self.assertEqual((r['original_minus_perturbed'],r['lower'],r['upper']),(0,0,0))
 def test_class_balance_not_pooled_accuracy_and_sign(self):
  r=p.paired_bootstrap_delta([0,0,0,1],[0,0,0,1],[0,0,0,0],4)
  self.assertEqual((r['original_minus_perturbed'],r['lower'],r['upper']),(.5,.5,.5))
  reverse=p.paired_bootstrap_delta([0,0,0,1],[0,0,0,0],[0,0,0,1],4)
  self.assertEqual(reverse['lower'],-.5)
 def test_reproducible_and_invalid_inputs(self):
  args=([0,0,1,1],[0,0,1,0],[1,0,0,1],9)
  self.assertEqual(p.paired_bootstrap_delta(*args),p.paired_bootstrap_delta(*args))
  for truth,a,b in [([0,1],[0],[0,1]),([0,1],[0,1],[0]),([0,1],[0,1],[0,2])]:
   with self.assertRaises(ValueError):p.paired_bootstrap_delta(truth,a,b,1)
  with self.assertRaises(ValueError):p.paired_bootstrap_delta(*args,replicates=1)

 def test_discordant_pair_counts_independently_reconstruct_balanced_delta(self):
  truth=[0,0,0,1,1];a=[0,1,0,0,1];b=[1,0,0,1,1]
  r=p.paired_bootstrap_delta(truth,a,b,13)
  self.assertEqual(r['pairing_by_class'],[
   dict(label=0,subjects=3,original_only_correct=1,perturbed_only_correct=1,equal_correctness=1),
   dict(label=1,subjects=2,original_only_correct=0,perturbed_only_correct=1,equal_correctness=1)])
  expected=sum((g['original_only_correct']-g['perturbed_only_correct'])/g['subjects'] for g in r['pairing_by_class'])/2
  self.assertAlmostEqual(r['original_minus_perturbed'],expected)
