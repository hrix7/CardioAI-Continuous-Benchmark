"""Deterministic experiment runner. Python standard library only."""
import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import random
import statistics

ROOT = Path(__file__).resolve().parent

def digest(data):
    return hashlib.sha256(data).hexdigest()

def encode(obj):
    return (json.dumps(obj, indent=2, sort_keys=True, allow_nan=False) + "\n").encode()

def table(rows):
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerows(rows)
    return stream.getvalue().encode()

def mean(xs):
    return statistics.mean(xs)

def rhythm(rng, label, beats, shift=0):
    # Deliberately simplified RR patterns, not physiological disease simulation.
    baseline = rng.uniform(.7, 1.1)
    if label == 0:
        return [baseline + rng.gauss(0, .025 + shift) for _ in range(beats)]
    return [max(.3, baseline + rng.gauss(0, .14 + shift)) for _ in range(beats)]

def features(rr):
    if len(rr) < 3 or any(x <= 0 or not math.isfinite(x) for x in rr):
        raise ValueError('RR intervals must be finite and positive; at least three required')
    return [statistics.stdev(rr) / mean(rr),
            math.sqrt(mean([(b-a)**2 for a,b in zip(rr, rr[1:])])) / mean(rr)]

def fit(samples):
    # Nearest centroid baseline; fit standardization exclusively on training subjects.
    center = [mean([x[j] for x,y in samples]) for j in range(2)]
    scale = [statistics.stdev([x[j] for x,y in samples]) or 1 for j in range(2)]
    centroids = [[mean([(x[j]-center[j])/scale[j] for x,y in samples if y == k])
                  for j in range(2)] for k in (0,1)]
    return center, scale, centroids

def predict(model, x):
    center, scale, centroids = model
    z = [(x[j]-center[j])/scale[j] for j in range(2)]
    return min(range(2), key=lambda k: sum((a-b)**2 for a,b in zip(z, centroids[k])))

def scores(truth, predicted):
    # Never let zip silently discard missing predictions or unsupported labels.
    if not truth or len(truth) != len(predicted):
        raise ValueError('truth and predictions must be nonempty and equally sized')
    if any(y not in (0, 1) for y in truth) or any(y not in (0, 1) for y in predicted):
        raise ValueError('truth and predictions must contain only binary labels 0 and 1')
    if set(truth) != {0, 1}:
        raise ValueError('balanced accuracy requires both true classes in this benchmark')
    cm = [[sum(y == a and p == b for y,p in zip(truth,predicted)) for b in (0,1)] for a in (0,1)]
    recalls = [cm[k][k]/sum(cm[k]) for k in (0,1)]
    return {'confusion_matrix_rows_true': cm, 'balanced_accuracy': mean(recalls),
            'accuracy': sum(y == p for y,p in zip(truth,predicted))/len(truth),
            'n_test_subjects': len(truth)}

def run(config):
    rows = [['seed', 'split', 'subject', 'label', 'beat', 'rr_seconds']]
    experiments = []
    for seed in config['seeds']:
        rng = random.Random(seed)
        train, test, shifted = [], [], []
        for split, n, dest, shift in [('train',config['train_subjects'],train,0),
                                      ('test',config['test_subjects'],test,0),
                                      ('shifted_test',config['test_subjects'],shifted,config['noise_shift'])]:
            for subject in range(n):
                label = subject % 2
                rr = rhythm(rng,label,config['beats'],shift)
                rows.extend([seed,split,f'{seed}-{split}-{subject}',label,i,format(x,'.12g')] for i,x in enumerate(rr))
                dest.append((features(rr),label))
        model = fit(train)
        experiments.append({'seed':seed, 'in_distribution':scores([y for x,y in test],[predict(model,x) for x,y in test]),
                            'noise_shift':scores([y for x,y in shifted],[predict(model,x) for x,y in shifted]),
                            'majority_baseline':scores([y for x,y in test],[0]*len(test)),
                            'model':model})
    return rows, {'experiments':experiments, 'interpretation':'Synthetic regular versus irregular RR patterns. Labels are generator settings, not diagnoses. No clinical inference.'}

def experiment():
    config = json.loads((ROOT / 'config.json').read_text())
    rows, metrics = run(config)
    data = table(rows)
    result = dict(schema_version=1, project=ROOT.name, data_kind='synthetic',
                  config=config, config_sha256=digest((ROOT/'config.json').read_bytes()),
                  source_sha256=digest(Path(__file__).read_bytes()),
                  data_sha256=digest(data), metrics=metrics)
    result_bytes = encode(result)
    report = ('# Verified synthetic experiment\n\n'
              'Educational engineering benchmark. No clinical validity is claimed.\n\n'
              'Generated from `config.json` by `pipeline.py`. Metrics are computed, never hand-entered.\n\n'
              '```json\n' + json.dumps(metrics, indent=2, sort_keys=True, allow_nan=False) + '\n```\n\n'
              'Result SHA-256: `' + digest(result_bytes) + '`\n').encode()
    return {'data.csv':data,'results.json':result_bytes,'report.md':report}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true',help='Recompute and compare every result byte; do not overwrite')
    parser.add_argument('--output',type=Path,default=ROOT/'results')
    args = parser.parse_args()
    files = experiment()
    manifest = {name:digest(data) for name,data in files.items()}
    files['manifest.json'] = encode(manifest)
    if args.verify:
        for name,data in files.items():
            path = args.output/name
            if not path.exists() or path.read_bytes() != data:
                raise SystemExit('Verification failed: '+name)
        print('Verified: deterministic recomputation and all artifact checksums match')
    else:
        args.output.mkdir(parents=True,exist_ok=True)
        for name,data in files.items():
            (args.output/name).write_bytes(data)
        print('Generated synthetic data, measured results, report and checksums')

if __name__ == '__main__':
    main()
