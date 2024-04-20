## About ValidMind

ValidMind is a platform for managing model risk, including risk associated with AI and statistical models. You use the ValidMind Developer Framework to automate documentation and validation tests, and then use the ValidMind AI Risk Platform UI to collaborate on model documentation. Together, these products simplify model risk management, facilitate compliance with regulations and institutional standards, and enhance collaboration between yourself and model validators.

### Before you begin

This notebook assumes you have basic familiarity with Python, including an understanding of how functions work. If you are new to Python, you can still run the notebook but we recommend further familiarizing yourself with the language. 

If you encounter errors due to missing modules in your Python environment, install the modules with `pip install`, and then re-run the notebook. For more help, refer to [Installing Python Modules](https://docs.python.org/3/installing/index.html).

### New to ValidMind?

If you haven't already seen our [Get started with the ValidMind Developer Framework](https://docs.validmind.ai/guide/get-started-developer-framework.html), we recommend you explore the available resources for developers at some point. There, you can learn more about documenting models, find code samples, or read our developer reference.

::: {.callout-tip}

For access to all features available in this notebook, create a free ValidMind account.

Signing up is FREE — [**Sign up now**](https://app.prod.validmind.ai)

:::

### Key concepts

**Model documentation**: A structured and detailed record pertaining to a model, encompassing key components such as its underlying assumptions, methodologies, data sources, inputs, performance metrics, evaluations, limitations, and intended uses. It serves to ensure transparency, adherence to regulatory requirements, and a clear understanding of potential risks associated with the model’s application.

**Documentation template**: Functions as a test suite and lays out the structure of model documentation, segmented into various sections and sub-sections. Documentation templates define the structure of your model documentation, specifying the tests that should be run, and how the results should be displayed.

**Tests**: A function contained in the ValidMind Developer Framework, designed to run a specific quantitative test on the dataset or model. Tests are the building blocks of ValidMind, used to evaluate and document models and datasets, and can be run individually or as part of a suite defined by your model documentation template.

**Metrics**: A subset of tests that do not have thresholds. In the context of this notebook, metrics and tests can be thought of as interchangeable concepts.

**Custom metrics**: Custom metrics are functions that you define to evaluate your model or dataset. These functions can be registered with ValidMind to be used in the platform.

**Inputs**: Objects to be evaluated and documented in the ValidMind framework. They can be any of the following:

  - **model**: A single model that has been initialized in ValidMind with [`vm.init_model()`](https://docs.validmind.ai/validmind/validmind.html#init_model).
  - **dataset**: Single dataset that has been initialized in ValidMind with [`vm.init_dataset()`](https://docs.validmind.ai/validmind/validmind.html#init_dataset).
  - **models**: A list of ValidMind models - usually this is used when you want to compare multiple models in your custom metric.
  - **datasets**: A list of ValidMind datasets - usually this is used when you want to compare multiple datasets in your custom metric. See this [example](https://docs.validmind.ai/notebooks/how_to/run_tests_that_require_multiple_datasets.html) for more information.

**Parameters**: Additional arguments that can be passed when running a ValidMind test, used to pass additional information to a metric, customize its behavior, or provide additional context.

**Outputs**: Custom metrics can return elements like tables or plots. Tables may be a list of dictionaries (each representing a row) or a pandas DataFrame. Plots may be matplotlib or plotly figures.

**Test suites**: Collections of tests designed to run together to automate and generate model documentation end-to-end for specific use-cases.

Example: the [`classifier_full_suite`](https://docs.validmind.ai/validmind/validmind/test_suites/classifier.html#ClassifierFullSuite) test suite runs tests from the [`tabular_dataset`](https://docs.validmind.ai/validmind/validmind/test_suites/tabular_datasets.html) and [`classifier`](https://docs.validmind.ai/validmind/validmind/test_suites/classifier.html) test suites to fully document the data and model sections for binary classification model use-cases.
