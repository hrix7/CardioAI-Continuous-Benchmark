# Development log

## 2026-11-12 — correctness and reproducibility

Prevented zip truncation and unsupported labels from silently corrupting evaluation denominators or confusion matrices. Explicitly reject empty or unequal vectors and missing true classes.

Regression cases cover missing/extra predictions, empty and single-class truth, unsupported labels in both vectors, and an imbalanced cohort with a constant predictor.

Validation before publication (Python 3.11.0, macOS):

- Full suite: 12 tests passed with `python3 -m unittest discover -s tests -v`.
- `python3 pipeline.py` regenerated the checked-in data, measured results, report and manifest.
- `python3 pipeline.py --verify` passed independent byte-for-byte recomputation.
- `git diff --check` and actionlint 1.7.12 passed; workflow configuration is unchanged. Optional shellcheck integration is unavailable locally.

Metrics were regenerated, not edited by hand. Source hashes and artifact checksums were refreshed. Linux may differ from macOS in final floating-point bits; CI generates and verifies results within its own runtime. Synthetic data only; no clinical validation is claimed.

Hosted results are available on this repository's [Actions page](https://github.com/hrix7/CardioAI-Continuous-Benchmark/actions). This entry records local checks, not a claim that an as-yet-unobserved hosted run succeeded.
