import math,unittest
import pipeline as p
class FeatureScalingTests(unittest.TestCase):
 def test_extreme_finite_scales_preserve_dimensionless_features(self):
  x=[1,2,1,3];expected=[math.sqrt(11/12)/(7/4),math.sqrt(2)/(7/4)]
  for scale in (1,1e200,1e-200):
   got=p.features([v*scale for v in x])
   for a,b in zip(got,expected):self.assertTrue(math.isclose(a,b,rel_tol=1e-12),(got,expected))
 def test_identical_smallest_subnormal_intervals_are_zero(self):
  self.assertEqual(p.features([math.ulp(0.0)]*3),[0,0])
