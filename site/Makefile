# Define source and destination directories
SRC_DIR := _source/validmind-python
DEST_DIR_NB := notebooks
DEST_DIR_PYTHON := _site/validmind

# Define .PHONY target for help section
.PHONY: help clean clone notebooks python-docs docs-site deploy-demo deploy-prod release-notes

# Help section
help:
	@echo "Available targets:"
	@echo "  clean          Remove the _source/ directory"
	@echo "  clone          Clone the validmind-python repository into _source/"
	@echo "  notebooks      Copy Jupyter notebooks into notebooks/"
	@echo "  python-docs    Copy the Python library docs into _site/validmind"
	@echo "  get-source     Get all source files (clean, clone, notebooks, python-docs)"
	@echo "  docs-site      Get all source files and render the docs site with Quarto"
	@echo "  deploy-demo    Render the docs site & deploy to docs-ci-cd-demo and clear cache"
	@echo "  deploy-prod    Render the docs site & deploy to docs-ci-cd-prod and clear cache"
	@echo "  help           Display this help message (default target)"
	@echo "  release-notes  Generate release notes from pull requests since latest tag and update _quarto.yml"

# Clean up source directory
clean:
	@echo "\nDeleting copies of files sourced from other repos ..."
	rm -rf $(SRC_DIR)

# Clone the source repository we need
clone:
	@echo "\nCloning source repos ..."
	git clone -b prod git@github.com:validmind/validmind-python.git $(SRC_DIR)

# Copy over Jupyter notebooks

NOTEBOOKS = \
    notebooks/external_test_providers_demo.ipynb \
    notebooks/external_tests/tests/MyCustomTest.py \
    notebooks/how_to/implementing_custom_tests.ipynb \
    notebooks/how_to/explore_test_suites_test_plans_and_tests.ipynb \
    notebooks/how_to/run_a_template.ipynb \
    notebooks/how_to/run_a_test.ipynb \
    notebooks/how_to/run_a_test_plan.ipynb \
    notebooks/how_to/run_a_test_suite.ipynb \
    notebooks/nlp/nlp_sentiment_analysis_catboost_demo.ipynb \
    notebooks/time_series/tutorial_time_series_forecasting.ipynb \
    notebooks/llm/hugging_face_integration_demo.ipynb \
    notebooks/probability_of_default/credit_risk_scorecard_development_demo.ipynb \
    notebooks/probability_of_default/credit_risk_scorecard_validation_demo.ipynb \
    notebooks/probability_of_default/helpers/scorecard_model.py \
    notebooks/probability_of_default/helpers/model_development.py

notebooks:
	@echo "\nUpdating notebook source ..."
	@rm -f notebooks.zip > /dev/null 2>&1
	@rm -rf $(DEST_DIR_NB)/ > /dev/null 2>&1 && mkdir -p $(DEST_DIR_NB)
	@$(foreach notebook,$(NOTEBOOKS), \
		dest_dir=$(DEST_DIR_NB)/$(patsubst notebooks/%,%,$(dir $(notebook))); \
		mkdir -p $$dest_dir > /dev/null 2>&1; \
		cp -r $(SRC_DIR)/$(notebook) $$dest_dir > /dev/null 2>&1; \
		echo "Updated $(notebook)"; \
	)
	@echo "\nCopying additional notebooks from Google Drive ..."
	cp "$(HOME)/Google Drive/Shared drives/ValidMind Demo/Notebooks/Quickstart_Customer Churn_full_suite.ipynb" $(DEST_DIR_NB)/
	cp "$(HOME)/Google Drive/Shared drives/ValidMind Demo/Notebooks/Introduction_Customer_Churn.ipynb" $(DEST_DIR_NB)/
	@echo "\nZipping up notebooks into notebooks.zip ..."
	@zip -r notebooks.zip $(DEST_DIR_NB) > /dev/null 2>&1

# Make Python library docs & copy them over
python-docs:
	@echo "\nUpdating Python documentation ..."
	rm -rf $(DEST_DIR_PYTHON)
	mkdir -p $(DEST_DIR_PYTHON)
	cp -r $(SRC_DIR)/docs/_build/. $(DEST_DIR_PYTHON)

# Get all source files
get-source: clean clone notebooks python-docs

# Get all source files
docs-site: clean clone notebooks python-docs
	quarto render

# Deployment to https://docs-demo.vm.validmind.ai/
deploy-demo:
	quarto render && aws s3 sync ./_site s3://docs-ci-cd-demo/site/ --delete && aws cloudfront create-invalidation --distribution-id E38AINJY5CYN6P --paths "/*" --no-cli-pager > /dev/null; \

# Deployment to https://docs.validmind.ai/
deploy-prod:
	@if [ "`git rev-parse --abbrev-ref HEAD`" != "main" ] && [ "`git rev-parse --abbrev-ref HEAD`" != "prod" ]; then \
		echo "You're not on the main or prod branches, no action taken."; \
	else \
		echo "\nDeploying prod site ..."; \
		quarto render && aws s3 sync ./_site s3://docs-ci-cd-prod/site/ --delete && aws cloudfront create-invalidation --distribution-id E2I9R40IH01NW3 --paths "/*" --no-cli-pager > /dev/null; \
	fi

# Generate release notes
release-notes:
	@echo "\nGenerating release notes ..."
	python generate_release_notes.py