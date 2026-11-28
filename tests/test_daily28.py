import unittest,random,copy
import pipeline as p
class Permutations(unittest.TestCase):
 def test_against_explicit_index_oracle_and_nonmutation(self):
  subjects=[([.5,.6,1.,.7,.8],0),([.3,1.4,.4,1.8,.7],1)]
  model=p.fit([(p.features(rr),y) for rr,y in subjects]);before=copy.deepcopy(subjects)
  result=p.permutation_order_probe(model,subjects,seeds=(11,22))
  original=[p.predict(model,p.features(rr)) for rr,y in subjects]
  for row,seed in zip(result['cases'],(11,22)):
   rng=random.Random(seed);indices=[];prediction=[]
   for rr,y in subjects:
    ix=list(range(len(rr)));rng.shuffle(ix);indices.append(ix)
    perm=[rr[i] for i in ix];self.assertEqual(sorted(perm),sorted(rr))
    prediction.append(p.predict(model,p.features(perm)))
   self.assertEqual(row['index_order_sha256'],p.digest(p.encode(indices)))
   self.assertEqual(row['metrics'],p.scores([0,1],prediction))
   self.assertEqual(row['prediction_disagreements'],sum(a!=b for a,b in zip(original,prediction)))
  self.assertEqual(subjects,before)
  self.assertEqual(result,p.permutation_order_probe(model,subjects,seeds=(11,22)))
 def test_bad_seeds(self):
  for seeds in ([],[True],[1,1],['1']):
   with self.assertRaises(ValueError):p.permutation_order_probe(None,[],seeds)
