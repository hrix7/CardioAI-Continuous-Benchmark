# Development backlog

## Completed

- 2026-11-12: Reject mismatched evaluation vectors and unsupported labels before computing classification metrics; require both true classes for balanced accuracy.

## Completed — 2026-11-13

Class-stratified subject bootstrap intervals.

## Completed — 2026-11-14

Independent training-only CV-feature baseline on both holdout cohorts.

## Completed — 2026-11-15

Validate both fitted baselines and primary-model inference inputs.

## Completed — 2026-11-17

Training resampling sensitivity.

## Completed — 2026-11-18

Validate generator configuration before sampling.

## Completed — 2026-11-19

Paired temporal-order mismatch probe.

## Completed — 2026-11-20

Paired bootstrap of temporal-order effects.

## Next priorities

1. Compare paired perturbation sensitivity across independent cohorts.
2. Add predeclared temporal perturbation families without tuning on holdouts.
3. Review public ECG annotation mappings and subject-disjoint validation.

## Completed — 2026-11-21

Expose paired bootstrap discordances.

## Completed — 2026-11-24

Temporal-order mismatch on shifted holdouts.

## Current ordered next steps

1. Predeclare reversal/time-permutation controls and compare separate cohorts without test-set tuning.
2. Review public-data terms, exact release/checksums and subject mappings before ingestion; keep synthetic and public-data evaluation distinct.

## Completed — 2026-11-25

Reversal negative controls.

## Current next steps

1. Add independent predeclared permutations with explicit provenance, without choosing a favorable perturbation.
2. Review real-data license/version/checksums and subject mappings before ingestion.
