# Define source and destination directories
SRC_DIR := _source/developer-framework
DEST_DIR_NB := notebooks
DEST_DIR_PYTHON := _site/validmind
DEST_DIR_TESTS := tests

# Define .PHONY target for help section
.PHONY: help clean clone notebooks python-docs docs-site deploy-demo deploy-prod release-notes

# Help section
help:
	@echo "Available targets:"
	@echo "  clean          Remove the _source/ directory"
	@echo "  clone          Clone the developer-framework repository into _source/"
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
	git clone -b prod git@github.com:validmind/developer-framework.git $(SRC_DIR)

# Copy over Jupyter notebooks and supporting files
notebooks:
	@echo "\nUpdating notebook source ..."
	@rm -f notebooks.zip
	@rm -rf $(DEST_DIR_NB)/ && mkdir -p $(DEST_DIR_NB)
	@cp -r $(SRC_DIR)/notebooks/. $(DEST_DIR_NB)/
	@echo "Copying LICENSE into notebooks ..."
	@cp -r $(SRC_DIR)/LICENSE $(DEST_DIR_NB)/
	@rm -rf $(DEST_DIR_NB)/code_sharing
	@echo "Moving Quickstart notebook into the root of notebooks/ ..."
	@if [ -f "$(DEST_DIR_NB)/code_samples/quickstart_customer_churn_full_suite.ipynb" ]; then mv $(DEST_DIR_NB)/code_samples/quickstart_customer_churn_full_suite.ipynb $(DEST_DIR_NB)/quickstart_customer_churn_full_suite.ipynb; fi
	@echo "Zip up notebooks.zip ..."
	@zip -r notebooks.zip $(DEST_DIR_NB) > /dev/null 2>&1
    # This line fixes text casing in Quarto when notebooks are embedded via wildcard
	@echo "Renaming code_samples/nlp_and_llm to fix Quarto sidebar ..."
	@if [ -d "$(DEST_DIR_NB)/code_samples/nlp_and_llm" ]; then mv $(DEST_DIR_NB)/code_samples/nlp_and_llm $(DEST_DIR_NB)/code_samples/LLM_and_NLP; fi


# Make Python library docs & copy them over
python-docs:
	@echo "\nUpdating Python documentation ..."
	@rm -rf $(DEST_DIR_PYTHON)
	@mkdir -p $(DEST_DIR_PYTHON)
	@cp -r $(SRC_DIR)/docs/_build/. $(DEST_DIR_PYTHON)

test-descriptions:
	@echo "\nUpdating test descriptions source ..."
	@cd _source/developer-framework && poetry run python scripts/extract_descriptions.py validmind/tests
	@cd ../../
	@rm -rf $(DEST_DIR_TESTS)
	@mkdir -p $(DEST_DIR_TESTS)
	@cp -r $(SRC_DIR)/build/_test_descriptions/validmind/tests/. $(DEST_DIR_TESTS)

# Get all source files
get-source: clean clone notebooks python-docs test-descriptions

# Get all source files
docs-site: clean clone notebooks python-docs test-descriptions
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
	@python generate_release_notes.py