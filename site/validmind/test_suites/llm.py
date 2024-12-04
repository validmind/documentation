# Copyright © 2023-2024 ValidMind Inc. All rights reserved.
# See the LICENSE file in the root of this repository for details.
# SPDX-License-Identifier: AGPL-3.0 AND ValidMind Commercial

"""
Test suites for LLMs
"""

from validmind.vm_models import TestSuite

from .classifier import ClassifierDiagnosis, ClassifierMetrics, ClassifierPerformance
from .text_data import TextDataQuality


class PromptValidation(TestSuite):
    """
    Test suite for prompt validation
    """

    suite_id = "prompt_validation"
    tests = [
        "validmind.prompt_validation.Bias",
        "validmind.prompt_validation.Clarity",
        "validmind.prompt_validation.Conciseness",
        "validmind.prompt_validation.Delimitation",
        "validmind.prompt_validation.NegativeInstruction",
        "validmind.prompt_validation.Robustness",
        "validmind.prompt_validation.Specificity",
    ]


class LLMClassifierFullSuite(TestSuite):
    """
    Full test suite for LLM classification models.
    """

    suite_id = "llm_classifier_full_suite"
    tests = [
        {
            "section_id": TextDataQuality.suite_id,
            "section_description": TextDataQuality.__doc__,
            "section_tests": TextDataQuality.tests,
        },
        {
            "section_id": ClassifierMetrics.suite_id,
            "section_description": ClassifierMetrics.__doc__,
            "section_tests": ClassifierMetrics.tests,
        },
        {
            "section_id": ClassifierPerformance.suite_id,
            "section_description": ClassifierPerformance.__doc__,
            "section_tests": ClassifierPerformance.tests,
        },
        {
            "section_id": ClassifierDiagnosis.suite_id,
            "section_description": ClassifierDiagnosis.__doc__,
            "section_tests": ClassifierDiagnosis.tests,
        },
        {
            "section_id": PromptValidation.suite_id,
            "section_description": PromptValidation.__doc__,
            "section_tests": PromptValidation.tests,
        },
    ]
