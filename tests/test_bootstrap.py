import unittest
import pipeline as p
class BootstrapTests(unittest.TestCase):
 def test_degenerate_perfect_and_inverted_subjects(self):
  for pred,value in [([0,0,1,1],1),([1,1,0,0],0)]:
   ci=p.bootstrap_scores([0,0,1,1],pred,123)['balanced_accuracy_bootstrap_95_percentile']
   self.assertEqual(ci['lower'],value);self.assertEqual(ci['upper'],value)
 def test_class_strata_not_pooled_accuracy(self):
  # Unequal strata, with constant correctness within each: BA=.5, accuracy=.75.
  s=p.bootstrap_scores([0,0,0,1],[0,0,0,0],20)
  self.assertEqual(s['accuracy'],.75);self.assertEqual(s['balanced_accuracy'],.5)
  self.assertEqual(s['balanced_accuracy_bootstrap_95_percentile']['lower'],.5)
  self.assertEqual(s['balanced_accuracy_bootstrap_95_percentile']['upper'],.5)
 def test_reproducible_nonmutating_and_nonzero_width(self):
  a=[0,0,1,1];b=[0,1,1,0]
  first=p.bootstrap_scores(a,b,9);self.assertEqual(first,p.bootstrap_scores(a,b,9));self.assertEqual(a,[0,0,1,1]);self.assertEqual(b,[0,1,1,0])
  ci=first['balanced_accuracy_bootstrap_95_percentile'];self.assertLess(ci['lower'],ci['upper'])
  with self.assertRaises(ValueError):p.bootstrap_scores(a,b,9,1)
