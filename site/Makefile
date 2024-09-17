# Define source and destination directories
SRC_DIR := _source/developer-framework
DEST_DIR_NB := notebooks
SRC_DIR_PYTHON := python-docs
DEST_DIR_PYTHON := _site/validmind
DEST_DIR_TESTS := tests
GIT_BRANCH := $(shell git rev-parse --abbrev-ref HEAD)

# Define .PHONY target for help section
.PHONY: help clean clone notebooks python-docs docs-site deploy-demo deploy-demo-branch delete-demo-branch deploy-prod deploy-staging release-notes

# Help section
help:
	@echo "Available targets:"
	@echo "  clean                Remove the _source/ directory"
	@echo "  clone                Clone the developer-framework repository into _source/"
	@echo "  notebooks            Copy Jupyter notebooks into notebooks/"
	@echo "  python-docs          Copy the Python library docs into _site/validmind"
	@echo "  get-source           Get all source files (clean, clone, notebooks, python-docs)"
	@echo "  docs-site            Get all source files and render the docs site with Quarto"
	@echo "  deploy-demo          Deploy docs demo site to s3://docs-ci-cd-demo/site/"
	@echo "  deploy-demo-branch   Deploy docs demo site to s3://docs-ci-cd-demo/site/pr_previews/$(GIT_BRANCH)/"
	@echo "  delete-demo-branch   Delete docs demo site in s3://docs-ci-cd-demo/site/pr_previews/$(GIT_BRANCH)/"
	@echo "  deploy-prod          Deploy docs prod site to s3://docs-ci-cd-prod/site/"
	@echo "  deploy-staging       Deploy docs staging site to s3://docs-ci-cd-staging/site/"
	@echo "  help                 Display this help message (default target)"
	@echo "  release-notes        Generate release notes from pull requests since latest tag and update _quarto.yml"

# Clean up source directory
clean:
	@echo "\nDeleting copies of files sourced from other repos ..."
	rm -rf $(SRC_DIR)

# Clone the source repository we need
clone:
	@echo "\nCloning source repos ..."
	git clone -b main git@github.com:validmind/developer-framework.git $(SRC_DIR)

# Copy over Jupyter notebooks and supporting files
notebooks:
	@echo "\nUpdating notebook source ..."
	@rm -f notebooks.zip
	@rm -rf $(DEST_DIR_NB)/ && mkdir -p $(DEST_DIR_NB)
	@cp -r $(SRC_DIR)/notebooks/. $(DEST_DIR_NB)/
	@echo "Checking out intro_for_model_developers_EXECUTED.ipynb from main ..."
	@git checkout main -- notebooks/tutorials/intro_for_model_developers_EXECUTED.ipynb
	@echo "Copying LICENSE into notebooks ..."
	@cp -r $(SRC_DIR)/LICENSE $(DEST_DIR_NB)/
	@rm -rf $(DEST_DIR_NB)/code_sharing
	@echo "Moving Quickstart notebook into the root of notebooks/ ..."
	@if [ -f "$(DEST_DIR_NB)/code_samples/quickstart_customer_churn_full_suite.ipynb" ]; then mv $(DEST_DIR_NB)/code_samples/quickstart_customer_churn_full_suite.ipynb $(DEST_DIR_NB)/quickstart_customer_churn_full_suite.ipynb; fi
	@echo "Zip up notebooks.zip ..."
	@zip -r notebooks.zip $(DEST_DIR_NB) > /dev/null 2>&1

# Make Python library docs & copy them over
python-docs:
	@if [ -d "$(SRC_DIR)/docs/_build/" ]; then \
		echo "\nUpdating Python documentation ..."; \
		rm -rf $(SRC_DIR_PYTHON); \
		mkdir -p $(SRC_DIR_PYTHON); \
		cp -r $(SRC_DIR)/docs/_build/. $(SRC_DIR_PYTHON); \
	fi; \
	echo "Copying Python documentation into docs site ..."; \
	rm -rf $(DEST_DIR_PYTHON); \
	mkdir -p $(DEST_DIR_PYTHON); \
	cp -r $(SRC_DIR_PYTHON)/. $(DEST_DIR_PYTHON);

test-descriptions:
	@echo "\nUpdating test descriptions source ..."
	@cd _source/developer-framework && make install && poetry run python scripts/extract_descriptions.py validmind/tests
	@cd ../../
	@rm -rf $(DEST_DIR_TESTS)
	@mkdir -p $(DEST_DIR_TESTS)
	@cp -r $(SRC_DIR)/build/_test_descriptions/validmind/tests/. $(DEST_DIR_TESTS)

# Get all source files
get-source: clean clone notebooks python-docs test-descriptions

# Get all source files
docs-site: clean clone notebooks python-docs test-descriptions
	quarto render --profile development
#	quarto render notebooks/how_to/explore_tests.ipynb --execute
#	quarto render notebooks/how_to/explore_test_suites.ipynb --execute

# Deployment to https://docs-demo.vm.validmind.ai/
deploy-demo:
	@if [ "`git rev-parse --abbrev-ref HEAD`" != "docs-demo" ]; then \
		echo "You're not on the docs-demo branch, no action taken."; \
	else \
		echo "\nDeploying docs-demo site ..."; \
		quarto render --profile development && aws s3 sync ./_site s3://docs-ci-cd-demo/site/ && aws cloudfront create-invalidation --distribution-id E38AINJY5CYN6P --paths "/*" --no-cli-pager > /dev/null; \
	fi

# Deploy PR branch to https://docs-demo.vm.validmind.ai/
deploy-demo-branch:
	@quarto render --profile development && aws s3 sync ./_site s3://docs-ci-cd-demo/site/pr_previews/$(GIT_BRANCH)/ --delete && aws cloudfront create-invalidation --distribution-id E38AINJY5CYN6P --paths "/*" --no-cli-pager > /dev/null; 
	@echo "\nDeployed to https://docs-demo.vm.validmind.ai/pr_previews/$(GIT_BRANCH)/index.html"

# Delete PR branch on https://docs-demo.vm.validmind.ai/
delete-demo-branch:
	@aws s3 rm s3://docs-ci-cd-demo/site/pr_previews/$(GIT_BRANCH)/ --recursive && aws cloudfront create-invalidation --distribution-id E38AINJY5CYN6P --paths "/*" --no-cli-pager > /dev/null; 
	@echo "\nDeleted https://docs-demo.vm.validmind.ai/pr_previews/$(GIT_BRANCH)/"

# Deployment to https://docs.validmind.ai/
deploy-prod:
	@if [ "`git rev-parse --abbrev-ref HEAD`" != "prod" ]; then \
		echo "You're not on the prod branch, no action taken."; \
	else \
		echo "\nDeploying prod site ..."; \
		quarto render --profile production && aws s3 sync ./_site s3://docs-ci-cd-prod/site/ --delete && aws cloudfront create-invalidation --distribution-id E2I9R40IH01NW3 --paths "/*" --no-cli-pager > /dev/null; \
	fi

# Deployment to https://docs.validmind.ai/
# TO DO Fix Cloudfront distribution ID
deploy-staging:
	@if [ "`git rev-parse --abbrev-ref HEAD`" != "nrichers/sc-6277/deploy-staging-docs-site-workflow" ]; then \
		echo "You're not on the staging branch, no action taken."; \
	else \
		echo "\nDeploying staging site ..."; \
		quarto render --profile staging && aws s3 sync ./_site s3://docs-ci-cd-staging/site/ --delete && aws cloudfront create-invalidation --distribution-id E2FB73KGY63MV6 --paths "/*" --no-cli-pager > /dev/null; \
	fi

# Generate release notes
release-notes:
	@python ../release-scripts/generate_release_objects.py