# Verified synthetic experiment

Educational engineering benchmark. No clinical validity is claimed.

Generated from `config.json` by `pipeline.py`. Metrics are computed, never hand-entered.

```json
{
  "experiments": [
    {
      "cv_baseline_class_means_training_only": [
        0.02846532104514196,
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
          0.09834448285642335
        ],
        [
          [
            -0.9623464750270672,
            -0.9588254932405906
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
      "noise_shift_sorted_order_probe": {
        "cohort": "noise_shift",
        "max_abs_cv_difference": 0.0,
        "mean_original_normalized_rmssd": 0.2583230424652657,
        "mean_sorted_normalized_rmssd": 0.033836264340113796,
        "method": "Pair each subject of the named holdout cohort with its sorted RR values: same labels, length and marginal values, deliberately altered order. Fixed already-fitted training model; no refit/selection/tuning. This nonphysiological temporal-order mismatch is separate from independent-noise holdouts and is not an extra independent cohort.",
        "original": {
          "accuracy": 0.6,
          "balanced_accuracy": 0.6,
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
        "paired_delta": {
          "lower": -0.45,
          "method": "Paired class-stratified subject bootstrap of original-minus-perturbed balanced accuracy; preserve each subject pair, fixed fitted model. Nearest-rank 95% percentile interval conditional on this holdout cohort; excludes training/population/model-selection uncertainty and may degenerate.",
          "original_minus_perturbed": -0.38750000000000007,
          "pairing_by_class": [
            {
              "equal_correctness": 9,
              "label": 0,
              "original_only_correct": 0,
              "perturbed_only_correct": 31,
              "subjects": 40
            },
            {
              "equal_correctness": 40,
              "label": 1,
              "original_only_correct": 0,
              "perturbed_only_correct": 0,
              "subjects": 40
            }
          ],
          "replicates": 400,
          "seed": 501729,
          "upper": -0.325
        },
        "sorted_order": {
          "accuracy": 0.9875,
          "balanced_accuracy": 0.9875,
          "confusion_matrix_rows_true": [
            [
              39,
              1
            ],
            [
              0,
              40
            ]
          ],
          "n_test_subjects": 80
        }
      },
      "reversal_controls": {
        "in_distribution": {
          "max_abs_feature_difference": 0.0,
          "method": "Predeclared negative control: reverse each same-subject RR sequence; CV and squared adjacent differences are mathematically invariant to reversal (floating-point summation may differ). Fixed training model, no refit or tuning. Sorting is a distinct nonphysiological perturbation; neither is clinical validation.",
          "original": {
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
          "prediction_disagreements": 0,
          "reversed": {
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
          }
        },
        "noise_shift": {
          "max_abs_feature_difference": 0.0,
          "method": "Predeclared negative control: reverse each same-subject RR sequence; CV and squared adjacent differences are mathematically invariant to reversal (floating-point summation may differ). Fixed training model, no refit or tuning. Sorting is a distinct nonphysiological perturbation; neither is clinical validation.",
          "original": {
            "accuracy": 0.6,
            "balanced_accuracy": 0.6,
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
          "prediction_disagreements": 0,
          "reversed": {
            "accuracy": 0.6,
            "balanced_accuracy": 0.6,
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
          }
        }
      },
      "seed": 1729,
      "sorted_order_probe": {
        "cohort": "in_distribution",
        "max_abs_cv_difference": 0.0,
        "mean_original_normalized_rmssd": 0.130145530370877,
        "mean_sorted_normalized_rmssd": 0.016380059841753045,
        "method": "Pair each subject of the named holdout cohort with its sorted RR values: same labels, length and marginal values, deliberately altered order. Fixed already-fitted training model; no refit/selection/tuning. This nonphysiological temporal-order mismatch is separate from independent-noise holdouts and is not an extra independent cohort.",
        "original": {
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
        "paired_delta": {
          "lower": 0.25,
          "method": "Paired class-stratified subject bootstrap of original-minus-perturbed balanced accuracy; preserve each subject pair, fixed fitted model. Nearest-rank 95% percentile interval conditional on this holdout cohort; excludes training/population/model-selection uncertainty and may degenerate.",
          "original_minus_perturbed": 0.32499999999999996,
          "pairing_by_class": [
            {
              "equal_correctness": 40,
              "label": 0,
              "original_only_correct": 0,
              "perturbed_only_correct": 0,
              "subjects": 40
            },
            {
              "equal_correctness": 14,
              "label": 1,
              "original_only_correct": 26,
              "perturbed_only_correct": 0,
              "subjects": 40
            }
          ],
          "replicates": 400,
          "seed": 401729,
          "upper": 0.3875
        },
        "sorted_order": {
          "accuracy": 0.675,
          "balanced_accuracy": 0.675,
          "confusion_matrix_rows_true": [
            [
              40,
              0
            ],
            [
              26,
              14
            ]
          ],
          "n_test_subjects": 80
        }
      },
      "training_resample_sensitivity": {
        "in_distribution": {
          "maximum": 1.0,
          "mean": 1.0,
          "minimum": 1.0,
          "q025": 1.0,
          "q975": 1.0
        },
        "method": "Class-stratified training-subject bootstrap with refitted normalization and centroids; fixed holdout cohorts. Descriptive resampled-model sensitivity, not a calibrated confidence interval or cohort-sampling uncertainty; no model selection.",
        "noise_shift": {
          "maximum": 0.6375,
          "mean": 0.600625,
          "minimum": 0.5625,
          "q025": 0.5625,
          "q975": 0.6375
        },
        "replicates": 100,
        "seed": 301729
      }
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
            0.928217552704073
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
      "noise_shift_sorted_order_probe": {
        "cohort": "noise_shift",
        "max_abs_cv_difference": 0.0,
        "mean_original_normalized_rmssd": 0.26229690991520754,
        "mean_sorted_normalized_rmssd": 0.03329839006919572,
        "method": "Pair each subject of the named holdout cohort with its sorted RR values: same labels, length and marginal values, deliberately altered order. Fixed already-fitted training model; no refit/selection/tuning. This nonphysiological temporal-order mismatch is separate from independent-noise holdouts and is not an extra independent cohort.",
        "original": {
          "accuracy": 0.5375,
          "balanced_accuracy": 0.5375,
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
        "paired_delta": {
          "lower": -0.475,
          "method": "Paired class-stratified subject bootstrap of original-minus-perturbed balanced accuracy; preserve each subject pair, fixed fitted model. Nearest-rank 95% percentile interval conditional on this holdout cohort; excludes training/population/model-selection uncertainty and may degenerate.",
          "original_minus_perturbed": -0.4375,
          "pairing_by_class": [
            {
              "equal_correctness": 5,
              "label": 0,
              "original_only_correct": 0,
              "perturbed_only_correct": 35,
              "subjects": 40
            },
            {
              "equal_correctness": 40,
              "label": 1,
              "original_only_correct": 0,
              "perturbed_only_correct": 0,
              "subjects": 40
            }
          ],
          "replicates": 400,
          "seed": 502718,
          "upper": -0.3875
        },
        "sorted_order": {
          "accuracy": 0.975,
          "balanced_accuracy": 0.975,
          "confusion_matrix_rows_true": [
            [
              38,
              2
            ],
            [
              0,
              40
            ]
          ],
          "n_test_subjects": 80
        }
      },
      "reversal_controls": {
        "in_distribution": {
          "max_abs_feature_difference": 0.0,
          "method": "Predeclared negative control: reverse each same-subject RR sequence; CV and squared adjacent differences are mathematically invariant to reversal (floating-point summation may differ). Fixed training model, no refit or tuning. Sorting is a distinct nonphysiological perturbation; neither is clinical validation.",
          "original": {
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
          "prediction_disagreements": 0,
          "reversed": {
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
          }
        },
        "noise_shift": {
          "max_abs_feature_difference": 0.0,
          "method": "Predeclared negative control: reverse each same-subject RR sequence; CV and squared adjacent differences are mathematically invariant to reversal (floating-point summation may differ). Fixed training model, no refit or tuning. Sorting is a distinct nonphysiological perturbation; neither is clinical validation.",
          "original": {
            "accuracy": 0.5375,
            "balanced_accuracy": 0.5375,
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
          "prediction_disagreements": 0,
          "reversed": {
            "accuracy": 0.5375,
            "balanced_accuracy": 0.5375,
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
          }
        }
      },
      "seed": 2718,
      "sorted_order_probe": {
        "cohort": "in_distribution",
        "max_abs_cv_difference": 0.0,
        "mean_original_normalized_rmssd": 0.1281472003875333,
        "mean_sorted_normalized_rmssd": 0.015769811350558813,
        "method": "Pair each subject of the named holdout cohort with its sorted RR values: same labels, length and marginal values, deliberately altered order. Fixed already-fitted training model; no refit/selection/tuning. This nonphysiological temporal-order mismatch is separate from independent-noise holdouts and is not an extra independent cohort.",
        "original": {
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
        "paired_delta": {
          "lower": 0.2375,
          "method": "Paired class-stratified subject bootstrap of original-minus-perturbed balanced accuracy; preserve each subject pair, fixed fitted model. Nearest-rank 95% percentile interval conditional on this holdout cohort; excludes training/population/model-selection uncertainty and may degenerate.",
          "original_minus_perturbed": 0.3125,
          "pairing_by_class": [
            {
              "equal_correctness": 40,
              "label": 0,
              "original_only_correct": 0,
              "perturbed_only_correct": 0,
              "subjects": 40
            },
            {
              "equal_correctness": 15,
              "label": 1,
              "original_only_correct": 25,
              "perturbed_only_correct": 0,
              "subjects": 40
            }
          ],
          "replicates": 400,
          "seed": 402718,
          "upper": 0.375
        },
        "sorted_order": {
          "accuracy": 0.6875,
          "balanced_accuracy": 0.6875,
          "confusion_matrix_rows_true": [
            [
              40,
              0
            ],
            [
              25,
              15
            ]
          ],
          "n_test_subjects": 80
        }
      },
      "training_resample_sensitivity": {
        "in_distribution": {
          "maximum": 1.0,
          "mean": 0.996375,
          "minimum": 0.9875,
          "q025": 0.9875,
          "q975": 1.0
        },
        "method": "Class-stratified training-subject bootstrap with refitted normalization and centroids; fixed holdout cohorts. Descriptive resampled-model sensitivity, not a calibrated confidence interval or cohort-sampling uncertainty; no model selection.",
        "noise_shift": {
          "maximum": 0.5375,
          "mean": 0.5263749999999999,
          "minimum": 0.5125,
          "q025": 0.5125,
          "q975": 0.5375
        },
        "replicates": 100,
        "seed": 302718
      }
    },
    {
      "cv_baseline_class_means_training_only": [
        0.02898790563282907,
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
            -0.9415177127185426,
            -0.9280553985029478
          ],
          [
            0.9415177127185423,
            0.9280553985029476
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
      "noise_shift_sorted_order_probe": {
        "cohort": "noise_shift",
        "max_abs_cv_difference": 0.0,
        "mean_original_normalized_rmssd": 0.25899128731237203,
        "mean_sorted_normalized_rmssd": 0.03222416923251538,
        "method": "Pair each subject of the named holdout cohort with its sorted RR values: same labels, length and marginal values, deliberately altered order. Fixed already-fitted training model; no refit/selection/tuning. This nonphysiological temporal-order mismatch is separate from independent-noise holdouts and is not an extra independent cohort.",
        "original": {
          "accuracy": 0.5375,
          "balanced_accuracy": 0.5375,
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
        "paired_delta": {
          "lower": -0.4875,
          "method": "Paired class-stratified subject bootstrap of original-minus-perturbed balanced accuracy; preserve each subject pair, fixed fitted model. Nearest-rank 95% percentile interval conditional on this holdout cohort; excludes training/population/model-selection uncertainty and may degenerate.",
          "original_minus_perturbed": -0.45000000000000007,
          "pairing_by_class": [
            {
              "equal_correctness": 3,
              "label": 0,
              "original_only_correct": 0,
              "perturbed_only_correct": 37,
              "subjects": 40
            },
            {
              "equal_correctness": 39,
              "label": 1,
              "original_only_correct": 1,
              "perturbed_only_correct": 0,
              "subjects": 40
            }
          ],
          "replicates": 400,
          "seed": 503141,
          "upper": -0.39999999999999997
        },
        "sorted_order": {
          "accuracy": 0.9875,
          "balanced_accuracy": 0.9875,
          "confusion_matrix_rows_true": [
            [
              40,
              0
            ],
            [
              1,
              39
            ]
          ],
          "n_test_subjects": 80
        }
      },
      "reversal_controls": {
        "in_distribution": {
          "max_abs_feature_difference": 0.0,
          "method": "Predeclared negative control: reverse each same-subject RR sequence; CV and squared adjacent differences are mathematically invariant to reversal (floating-point summation may differ). Fixed training model, no refit or tuning. Sorting is a distinct nonphysiological perturbation; neither is clinical validation.",
          "original": {
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
          "prediction_disagreements": 0,
          "reversed": {
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
          }
        },
        "noise_shift": {
          "max_abs_feature_difference": 0.0,
          "method": "Predeclared negative control: reverse each same-subject RR sequence; CV and squared adjacent differences are mathematically invariant to reversal (floating-point summation may differ). Fixed training model, no refit or tuning. Sorting is a distinct nonphysiological perturbation; neither is clinical validation.",
          "original": {
            "accuracy": 0.5375,
            "balanced_accuracy": 0.5375,
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
          "prediction_disagreements": 0,
          "reversed": {
            "accuracy": 0.5375,
            "balanced_accuracy": 0.5375,
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
          }
        }
      },
      "seed": 3141,
      "sorted_order_probe": {
        "cohort": "in_distribution",
        "max_abs_cv_difference": 0.0,
        "mean_original_normalized_rmssd": 0.12719436906641476,
        "mean_sorted_normalized_rmssd": 0.017445586368673497,
        "method": "Pair each subject of the named holdout cohort with its sorted RR values: same labels, length and marginal values, deliberately altered order. Fixed already-fitted training model; no refit/selection/tuning. This nonphysiological temporal-order mismatch is separate from independent-noise holdouts and is not an extra independent cohort.",
        "original": {
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
        "paired_delta": {
          "lower": 0.2375,
          "method": "Paired class-stratified subject bootstrap of original-minus-perturbed balanced accuracy; preserve each subject pair, fixed fitted model. Nearest-rank 95% percentile interval conditional on this holdout cohort; excludes training/population/model-selection uncertainty and may degenerate.",
          "original_minus_perturbed": 0.32499999999999996,
          "pairing_by_class": [
            {
              "equal_correctness": 40,
              "label": 0,
              "original_only_correct": 0,
              "perturbed_only_correct": 0,
              "subjects": 40
            },
            {
              "equal_correctness": 14,
              "label": 1,
              "original_only_correct": 26,
              "perturbed_only_correct": 0,
              "subjects": 40
            }
          ],
          "replicates": 400,
          "seed": 403141,
          "upper": 0.4
        },
        "sorted_order": {
          "accuracy": 0.675,
          "balanced_accuracy": 0.675,
          "confusion_matrix_rows_true": [
            [
              40,
              0
            ],
            [
              26,
              14
            ]
          ],
          "n_test_subjects": 80
        }
      },
      "training_resample_sensitivity": {
        "in_distribution": {
          "maximum": 1.0,
          "mean": 1.0,
          "minimum": 1.0,
          "q025": 1.0,
          "q975": 1.0
        },
        "method": "Class-stratified training-subject bootstrap with refitted normalization and centroids; fixed holdout cohorts. Descriptive resampled-model sensitivity, not a calibrated confidence interval or cohort-sampling uncertainty; no model selection.",
        "noise_shift": {
          "maximum": 0.6375,
          "mean": 0.549875,
          "minimum": 0.525,
          "q025": 0.525,
          "q975": 0.625
        },
        "replicates": 100,
        "seed": 303141
      }
    }
  ],
  "interpretation": "Synthetic regular versus irregular RR patterns. Labels are generator settings, not diagnoses. No clinical inference."
}
```

Result SHA-256: `289aa80cb07150b61f75290856d359b353060ce61c2c19735e37d08e1119a3cd`
