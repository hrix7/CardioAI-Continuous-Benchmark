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

## 2026-11-13

Class-stratified subject bootstrap percentile intervals for balanced accuracy.

Reports 400 class-stratified subject bootstrap replicates with nearest-rank 2.5/97.5 percentiles and fixed seed offsets, separately for each holdout cohort and fitted model. Resampling RNG is independent of data generation. Intervals condition on the fitted model and cohort; they exclude training and cross-seed uncertainty and may degenerate on all-correct or all-wrong cohorts. No test-set tuning.

Validation: full unittest suite, pipeline regeneration and byte-for-byte verifier, diff review; GitHub validation outcome is tracked after push. No workflow/permission changes.

## 2026-11-14

Independent training-only CV-feature baseline on both holdout cohorts.

Adds a one-feature comparator using nearest training-class mean of coefficient of variation. It ignores the second feature, chooses class 0 on exact ties, and never fits to holdouts. Class means and complete confusion/accuracy metrics are reported for both cohorts, alongside the primary two-feature standardized model. No improvement is assumed or fabricated.

Validation before publication: full unittest suite, regenerated pipeline artifacts, byte-for-byte verification and diff review. Workflow configuration/permissions unchanged; existing policy tests pass. Hosted CI is followed after the tested source is published.

## 2026-11-15

Validate both fitted baselines and primary-model inference inputs.

Both model fits require finite feature pairs with integer binary labels and both training classes. Primary inference rejects nonfinite feature/model vectors and nonpositive standardization scales before distance evaluation. A single training subject in each class remains valid. No test-set fitting or threshold changes.

Validation before publication: full unittest suite, pipeline regeneration/byte verifier, diff review and existing workflow-policy tests. Workflows and permissions unchanged. Hosted validation is followed after publication.

## 2026-11-17 — Training resampling sensitivity

Completed the retained, unpublished implementation from November 16. Added class-stratified resampling of training subjects with normalization and centroids refit each replicate, evaluated on two fixed holdouts. This descriptive training-perturbation sensitivity is separate from the existing holdout-subject bootstrap intervals; its quantiles are not calibrated confidence limits. Tests verify repeatability, nonmutation and that only training rows enter refits. Full unit tests, pipeline regeneration and artifact verification run before publication; no workflow or permission changes.

## 2026-11-18 — Validate generator configuration before sampling

Validate unique integer seeds, class-capable train/test sizes, minimum beat count and finite nonnegative shift before any rhythm generation. Tests spy on the generator to prove invalid configurations fail before sampling and exercise small odd-sized cohorts. No holdout tuning or new clinical interpretation. Full suite: 25 tests passed; pipeline generation, independent --verify and diff checks passed before publication. No workflow/permission changes; workflow policy tests passed.

## 2026-11-19 — Paired temporal-order mismatch probe

Added a sorted-order copy of each in-distribution holdout RR sequence. Marginal values, sample counts and labels are retained while temporal structure changes. The already fitted training-only model is evaluated without refitting or threshold selection. This nonphysiological paired perturbation is not an additional independent cohort. Report normalized RMSSD changes, preserved CV and measured confusion results. Tests verify nonmutation, no refit and independent feature/score recomputation. Full suite: 27 tests passed; pipeline generation, independent --verify and diff checks passed before publication. No workflow or permission changes; workflow policy tests passed.

## 2026-11-20 — Paired bootstrap of temporal-order effects

Added class-stratified paired subject bootstrap of original-minus-sorted balanced accuracy using the fixed fitted model. Subject pairs remain together; nearest-rank percentile intervals are conditional on this cohort and omit training/population uncertainty. Tests cover identical pairs with errors, class imbalance, sign, reproducibility and invalid vectors. No holdout fitting or threshold selection. Full suite: 30 tests passed; pipeline generation, independent --verify and diff checks passed before publication. Workflow policy tests passed without workflow/permission changes.

## 2026-11-21 — Expose paired bootstrap discordances

Export per-class subject counts and original-only/perturbed-only/equal correctness counts. Independently reconstruct the balanced-accuracy delta from these discordances. Fixed fitted model, paired subjects and bootstrap RNG unchanged; conditional uncertainty remains nonclinical.

Validation: full existing suite plus new tests (31 passed), pipeline generation and independent --verify, scoped diff review and git diff --check before publication. Hosted CI is followed after pushing. Existing read-only validation/publisher workflows unchanged; workflow-policy tests included.
