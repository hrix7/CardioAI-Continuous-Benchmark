# Verified synthetic experiment

Educational engineering benchmark. No clinical validity is claimed.

Generated from `config.json` by `pipeline.py`. Metrics are computed, never hand-entered.

```json
{
  "experiments": [
    {
      "cv_baseline_class_means_training_only": [
        0.028465321045141965,
        0.1619375441582662
      ],
      "cv_baseline_in_distribution": {
        "accuracy": 1.0,
        "balanced_accuracy": 1.0,
        "confusion_matrix_rows_true": [
          [
            40,
            0
          ],
          [
            0,
            40
          ]
        ],
        "n_test_subjects": 80
      },
      "cv_baseline_method": "Nearest training-class mean of coefficient of variation alone; no holdout tuning; exact ties choose class 0.",
      "cv_baseline_noise_shift": {
        "accuracy": 0.575,
        "balanced_accuracy": 0.575,
        "confusion_matrix_rows_true": [
          [
            6,
            34
          ],
          [
            0,
            40
          ]
        ],
        "n_test_subjects": 80
      },
      "in_distribution": {
        "accuracy": 1.0,
        "balanced_accuracy": 1.0,
        "balanced_accuracy_bootstrap_95_percentile": {
          "lower": 1,
          "method": "Class-stratified subject resampling; fixed fitted model; nearest-rank percentile; conditional on this holdout cohort, not training or cross-seed uncertainty.",
          "replicates": 400,
          "seed": 101729,
          "upper": 1
        },
        "confusion_matrix_rows_true": [
          [
            40,
            0
          ],
          [
            0,
            40
          ]
        ],
        "n_test_subjects": 80
      },
      "majority_baseline": {
        "accuracy": 0.5,
        "balanced_accuracy": 0.5,
        "confusion_matrix_rows_true": [
          [
            40,
            0
          ],
          [
            40,
            0
          ]
        ],
        "n_test_subjects": 80
      },
      "model": [
        [
          0.09520143260170408,
          0.1349127166028861
        ],
        [
          0.06934728113872406,
          0.09834448285642336
        ],
        [
          [
            -0.9623464750270672,
            -0.9588254932405904
          ],
          [
            0.9623464750270673,
            0.9588254932405906
          ]
        ]
      ],
      "noise_shift": {
        "accuracy": 0.6,
        "balanced_accuracy": 0.6,
        "balanced_accuracy_bootstrap_95_percentile": {
          "lower": 0.5375,
          "method": "Class-stratified subject resampling; fixed fitted model; nearest-rank percentile; conditional on this holdout cohort, not training or cross-seed uncertainty.",
          "replicates": 400,
          "seed": 201729,
          "upper": 0.6625
        },
        "confusion_matrix_rows_true": [
          [
            8,
            32
          ],
          [
            0,
            40
          ]
        ],
        "n_test_subjects": 80
      },
      "seed": 1729
    },
    {
      "cv_baseline_class_means_training_only": [
        0.027856955633989263,
        0.14949525696964147
      ],
      "cv_baseline_in_distribution": {
        "accuracy": 1.0,
        "balanced_accuracy": 1.0,
        "confusion_matrix_rows_true": [
          [
            40,
            0
          ],
          [
            0,
            40
          ]
        ],
        "n_test_subjects": 80
      },
      "cv_baseline_method": "Nearest training-class mean of coefficient of variation alone; no holdout tuning; exact ties choose class 0.",
      "cv_baseline_noise_shift": {
        "accuracy": 0.525,
        "balanced_accuracy": 0.525,
        "confusion_matrix_rows_true": [
          [
            2,
            38
          ],
          [
            0,
            40
          ]
        ],
        "n_test_subjects": 80
      },
      "in_distribution": {
        "accuracy": 1.0,
        "balanced_accuracy": 1.0,
        "balanced_accuracy_bootstrap_95_percentile": {
          "lower": 1,
          "method": "Class-stratified subject resampling; fixed fitted model; nearest-rank percentile; conditional on this holdout cohort, not training or cross-seed uncertainty.",
          "replicates": 400,
          "seed": 102718,
          "upper": 1
        },
        "confusion_matrix_rows_true": [
          [
            40,
            0
          ],
          [
            0,
            40
          ]
        ],
        "n_test_subjects": 80
      },
      "majority_baseline": {
        "accuracy": 0.5,
        "balanced_accuracy": 0.5,
        "confusion_matrix_rows_true": [
          [
            40,
            0
          ],
          [
            40,
            0
          ]
        ],
        "n_test_subjects": 80
      },
      "model": [
        [
          0.08867610630181537,
          0.12424515041319059
        ],
        [
          0.06456621124426333,
          0.09126866711582003
        ],
        [
          [
            -0.9419656116685932,
            -0.928217552704073
          ],
          [
            0.9419656116685933,
            0.9282175527040731
          ]
        ]
      ],
      "noise_shift": {
        "accuracy": 0.5375,
        "balanced_accuracy": 0.5375,
        "balanced_accuracy_bootstrap_95_percentile": {
          "lower": 0.5,
          "method": "Class-stratified subject resampling; fixed fitted model; nearest-rank percentile; conditional on this holdout cohort, not training or cross-seed uncertainty.",
          "replicates": 400,
          "seed": 202718,
          "upper": 0.575
        },
        "confusion_matrix_rows_true": [
          [
            3,
            37
          ],
          [
            0,
            40
          ]
        ],
        "n_test_subjects": 80
      },
      "seed": 2718
    },
    {
      "cv_baseline_class_means_training_only": [
        0.028987905632829068,
        0.1618663874955769
      ],
      "cv_baseline_in_distribution": {
        "accuracy": 1.0,
        "balanced_accuracy": 1.0,
        "confusion_matrix_rows_true": [
          [
            40,
            0
          ],
          [
            0,
            40
          ]
        ],
        "n_test_subjects": 80
      },
      "cv_baseline_method": "Nearest training-class mean of coefficient of variation alone; no holdout tuning; exact ties choose class 0.",
      "cv_baseline_noise_shift": {
        "accuracy": 0.55,
        "balanced_accuracy": 0.55,
        "confusion_matrix_rows_true": [
          [
            4,
            36
          ],
          [
            0,
            40
          ]
        ],
        "n_test_subjects": 80
      },
      "in_distribution": {
        "accuracy": 1.0,
        "balanced_accuracy": 1.0,
        "balanced_accuracy_bootstrap_95_percentile": {
          "lower": 1,
          "method": "Class-stratified subject resampling; fixed fitted model; nearest-rank percentile; conditional on this holdout cohort, not training or cross-seed uncertainty.",
          "replicates": 400,
          "seed": 103141,
          "upper": 1
        },
        "confusion_matrix_rows_true": [
          [
            40,
            0
          ],
          [
            0,
            40
          ]
        ],
        "n_test_subjects": 80
      },
      "majority_baseline": {
        "accuracy": 0.5,
        "balanced_accuracy": 0.5,
        "confusion_matrix_rows_true": [
          [
            40,
            0
          ],
          [
            40,
            0
          ]
        ],
        "n_test_subjects": 80
      },
      "model": [
        [
          0.095427146564203,
          0.13486315659493406
        ],
        [
          0.07056610835237179,
          0.10158207987176086
        ],
        [
          [
            -0.9415177127185425,
            -0.9280553985029478
          ],
          [
            0.9415177127185425,
            0.9280553985029477
          ]
        ]
      ],
      "noise_shift": {
        "accuracy": 0.5375,
        "balanced_accuracy": 0.5375,
        "balanced_accuracy_bootstrap_95_percentile": {
          "lower": 0.5,
          "method": "Class-stratified subject resampling; fixed fitted model; nearest-rank percentile; conditional on this holdout cohort, not training or cross-seed uncertainty.",
          "replicates": 400,
          "seed": 203141,
          "upper": 0.575
        },
        "confusion_matrix_rows_true": [
          [
            3,
            37
          ],
          [
            0,
            40
          ]
        ],
        "n_test_subjects": 80
      },
      "seed": 3141
    }
  ],
  "interpretation": "Synthetic regular versus irregular RR patterns. Labels are generator settings, not diagnoses. No clinical inference."
}
```

Result SHA-256: `4955d605c82d1f8a9c872933c288ca00d071254a627f5249ddf1965425837817`
