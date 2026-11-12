# CardioAI-Continuous-Benchmark

Subject-disjoint synthetic rhythm classification benchmark. Reproducible educational biomedical engineering project, with daily verified experiment reports.

**Synthetic data only. No clinical validity, diagnostic performance or medical-device suitability is claimed.** Every metric in [the report](results/report.md) is computed by the pipeline. There are no hand-entered performance claims.

## Run locally

Requires Python 3.11 and Git. No packages, credentials, network access, special hardware or downloaded datasets are required.

```sh
python3 -m unittest discover -s tests -v
python3 pipeline.py
python3 pipeline.py --verify
```

Run commands from this repository's root. `--output /tmp/experiment` supports isolated results. `--verify` recomputes data and metrics and compares every artifact byte and manifest; it exits nonzero on missing or modified results. To change an experiment, edit `config.json`, run tests, regenerate, verify and review the diff before committing.

## Method and provenance

Generate independent subjects with 40 RR intervals each. Regular and irregular labels select Gaussian jitter SD 0.025 and 0.14 seconds around a subject baseline drawn uniformly from 0.7–1.1 seconds. Irregular values are clipped at 0.3 seconds. Train on 100 subjects and evaluate on 80 new subjects per condition and seed (1729, 2718, 3141). Subject IDs include split and seed. Features are coefficient of variation and normalized RMSSD; standardization and nearest-centroid fitting use training subjects only. Compare against a class-zero majority baseline. A second, independently generated holdout adds 0.08 seconds to both jitter SDs to test distribution shift. Balanced accuracy and complete confusion matrices are reported for each seed and condition. No hyperparameter tuning uses either holdout. These deliberately separable generator labels are not arrhythmia diagnoses. Synthetic accuracy cannot predict real ECG performance.

See [data provenance](DATA_PROVENANCE.md) for units, assumptions, origin and limitations. The configuration lists all experiment settings and seeds. There is no automatic patient-data ingestion.

## Repository layout

- `pipeline.py`: generator, method, metrics, report and verification CLI.
- `config.json`: versioned experiment protocol.
- `tests/`: mathematical, reproducibility and tamper-detection checks.
- `results/`: generated CSV, measured JSON, Markdown report and checksum manifest.
- `.github/workflows/daily.yml`: test, reproduce, verify, then publish changed results.

## Daily automation and setup

The workflow runs on pushes, pull requests, manual dispatch and daily at `37 9 * * *` UTC. Schedules use the default branch; GitHub can delay scheduled runs and can disable schedules on inactive public repositories. Enable Actions in repository settings and inspect the Actions page after the first push. No personal access token or external secrets are needed.

Validation has read-only repository permissions and never retains checkout credentials. Only the separate publish job receives `contents: write`; it runs after successful validation on default-branch schedule/manual events. It reruns tests and verification before committing only `results/`, using the built-in token. Pull requests cannot publish. All external actions are pinned to commit SHAs. Concurrency prevents overlapping publishers; pushes use normal fast-forward semantics and fail safely on competing changes. Branch protection may intentionally block direct bot pushes; in that case reports remain in run artifacts and maintainers can adopt a PR publishing policy.

Each successful run uploads its verified report/data artifact for 30 days and displays the report in the run summary. Identical results produce no empty commits. A daily rerun verifies reproducibility; it does not invent research progress or autonomously modify algorithms. Notifications and branch protections are controlled in GitHub settings. Public repositories may need schedule reactivation after inactivity.

## Numerical and evaluation safeguards

Evaluation requires nonempty vectors of equal length, binary labels and both true classes. Missing predictions or invalid labels raise ValueError rather than being silently omitted; single-class truth is rejected because this benchmark requires both recalls. A constant predictor remains valid.

## Development history

See [completed improvements and validation](DEVELOPMENT_LOG.md) and the [ordered development backlog](DEVELOPMENT_BACKLOG.md).

## Roadmap

Add independently sourced, license-reviewed public data, stronger baselines and uncertainty estimates before any real-data claims. Keep synthetic and public-data results visibly separate. Clinical deployment is outside this project's scope.

## License

MIT; see [LICENSE](LICENSE).
