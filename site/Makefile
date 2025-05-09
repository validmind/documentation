# Define source and destination directories
DEST_DIR_NB := notebooks
DEST_DIR_PYTHON := validmind
DEST_DIR_TESTS := tests
GIT_BRANCH := $(shell git rev-parse --abbrev-ref HEAD)
INSTALLATION_BRANCH := main
LIBRARY_BRANCH ?= $(or $(BRANCH),main)
SRC_ROOT := _source
SRC_DIR := $(SRC_ROOT)/validmind-library

# Define .PHONY target for help section
.PHONY: help clean clone copy-installation delete-demo-branch deploy-demo-branch deploy-prod deploy-staging docker-build docker-serve docker-site docker-site-lite docs-site execute get-source jupyter-widget notebooks python-docs release-notes test-descriptions yearly-releases

# Help section
help:
	@echo "Available targets:"
	@echo "  help                 Display this help message (default target)"
	@echo "  clean                Remove the _source/ directory"
	@echo "  clone                Clone the validmind-library repository into _source/"
	@echo "                       Optional, for PR testing: BRANCH=<branch-name>"
	@echo "  copy-installation    Copy customer-managed installation docs into installation/"
	@echo "  delete-demo-branch   Delete docs demo site in s3://docs-ci-cd-demo/site/pr_previews/$(GIT_BRANCH)/"
	@echo "  deploy-demo-branch   Deploy docs demo site to s3://docs-ci-cd-demo/site/pr_previews/$(GIT_BRANCH)/"
	@echo "  deploy-prod          Deploy docs prod site to s3://docs-ci-cd-prod/site/"
	@echo "  deploy-staging       Deploy docs staging site to s3://docs-ci-cd-staging/site/"
	@echo "  docker-build         Builds a Docker image of the docs site"
	@echo "  docker-serve         Serves the docs site at http://localhost:4444/"
	@echo "  docker-site          Get source, render site with Docker profile, execute notebooks"
	@echo "  docker-site-lite     Get source and render site with Docker profile (skips notebook execution)"
	@echo "  docs-site            Get all source files and render the production docs site with Quarto"
	@echo "  execute              Execute a Jupyter Notebook or notebook directory"
	@echo "  get-source           Get all source files (clean, clone, copy-installation, notebooks, python-docs, test-descriptions)"
	@echo "  jupyter-widget       Retrieve the latest juptyer-widget for notebook output widget rendering"
	@echo "  notebooks            Copy Jupyter notebooks into notebooks/"
	@echo "  python-docs          Copy the Python library docs into validmind/"
	@echo "  release-notes        Generate release notes from pull requests since latest tag and update releases sidebar"
	@echo "  test-descriptions    Copy the ValidMind tests docs into tests/"
	@echo "  yearly-releases      Collate releases by year into a listing landing and update releases sidebar"

# Clean up source directory
clean:
	@echo "\nDeleting copies of files sourced from other repos ..."
	rm -rf $(SRC_DIR)
	rm -rf $(SRC_ROOT)
	rm -rf notebooks/EXECUTED/model_development/

# Prompt for a branch or release tag and clone the repository
clone:
	@if [ -n "$(LIBRARY_BRANCH)" ] && [ "$(LIBRARY_BRANCH)" != "main" ]; then \
		echo "\nWARNING: Cloning non-release files from $(LIBRARY_BRANCH) — DO NOT COMMIT"; \
		echo "\nCloning validmind-library repo from $(LIBRARY_BRANCH) ..."; \
		CHECKOUT="$(LIBRARY_BRANCH)"; \
	else \
		read -p "Enter release tag (example: v2.8.10, or HEAD for latest): " TAG; \
		if [ "$$TAG" = "HEAD" ]; then \
			echo "\nWARNING: Cloning latest non-release files — DO NOT COMMIT"; \
			echo "\nCloning validmind-library repo at HEAD ..."; \
			CHECKOUT="$(LIBRARY_BRANCH)"; \
		else \
			echo "\nCloning validmind-library repo at $$TAG ..."; \
			CHECKOUT="$$TAG"; \
		fi \
	fi; \
	git clone --depth 1 -b $$CHECKOUT git@github.com:validmind/validmind-library.git $(SRC_DIR)

	@echo "\nCloning installation repo from $(INSTALLATION_BRANCH) ..."; \
	git clone  --depth 1 -b $(INSTALLATION_BRANCH) git@github.com:validmind/installation.git $(SRC_ROOT)/installation

copy-installation:
	cp -r $(SRC_ROOT)/installation/site/installation installation

# Delete PR branch on https://docs-demo.vm.validmind.ai/
delete-demo-branch:
	@aws s3 rm s3://docs-ci-cd-demo/site/pr_previews/$(GIT_BRANCH)/ --recursive && aws cloudfront create-invalidation --distribution-id E38AINJY5CYN6P --paths "/*" --no-cli-pager > /dev/null; 
	@echo "\nDeleted https://docs-demo.vm.validmind.ai/pr_previews/$(GIT_BRANCH)/"

# Deploy PR branch to https://docs-demo.vm.validmind.ai/
deploy-demo-branch:
	@quarto render --profile development && aws s3 sync ./_site s3://docs-ci-cd-demo/site/pr_previews/$(GIT_BRANCH)/ --delete && aws cloudfront create-invalidation --distribution-id E38AINJY5CYN6P --paths "/*" --no-cli-pager > /dev/null; 
	@echo "\nDeployed to https://docs-demo.vm.validmind.ai/pr_previews/$(GIT_BRANCH)/index.html"

# Deployment to https://docs.validmind.ai/
deploy-prod:
	@if [ "`git rev-parse --abbrev-ref HEAD`" != "prod" ]; then \
		echo "You're not on the prod branch, no action taken."; \
	else \
		echo "\nDeploying prod site ..."; \
		cp -r $(SRC_ROOT)/installation/site/installation installation
		quarto render --profile production && aws s3 sync ./_site s3://docs-ci-cd-prod/site/ --delete --exclude "site/installation/helm-repo/*" && aws cloudfront create-invalidation --distribution-id E2I9R40IH01NW3 --paths "/*" --no-cli-pager > /dev/null; \
	fi

# Deployment to https://docs-staging.validmind.ai/
deploy-staging:
	@if [ "`git rev-parse --abbrev-ref HEAD`" != "staging" ]; then \
		echo "You're not on the staging branch, no action taken."; \
	else \
		echo "\nDeploying staging site ..."; \
		cp -r $(SRC_ROOT)/installation/site/installation installation
		quarto render --profile staging && aws s3 sync ./_site s3://docs-ci-cd-staging/site/ --delete --exclude "site/installation/helm-repo/*" && aws cloudfront create-invalidation --distribution-id E2FB73KGY63MV6 --paths "/*" --no-cli-pager > /dev/null; \
	fi

docker-build: docker-site-lite
	@echo "\nBuilding the Docker image ..."
	@docker build -f ../Dockerfile -t validmind-docs ..

docker-serve:
	@echo "\nStarting the Docker container on http://localhost:4444/ ..."
	@docker run -p 4444:80 validmind-docs

docker-site: get-source
	@echo "\nRendering the configurable static HTML site for Docker ..."
	quarto render --profile docker 2>&1 | grep -v "WARN:" 1>&2
	@$(MAKE) execute PROFILE=exe-prod

docker-site-lite: get-source
	@echo "\nRendering the configurable static HTML site for Docker (skip notebook execution) ..."
	quarto render --profile docker 2>&1 | grep -v "WARN:" 1>&2

# Get all source docs
docs-site: get-source
	@echo "\nRendering the static HTML site ..."
	quarto render --profile production
	@$(MAKE) execute PROFILE=exe-prod

# Execute Juptyer Notebooks with a profile & provided credentials
execute:
	@$(MAKE) jupyter-widget
	@echo "Duplicating jupyter-widget into model_development for notebook access"
	@cp -r developer/embed-amd.js notebooks/EXECUTED/model_development/embed-amd.js
	@echo "DDuplicating jupyter-widget into model_validation for notebook access"
	@cp -r developer/embed-amd.js notebooks/EXECUTED/model_validation/embed-amd.js
	@bash -c ' \
	echo "Select PROFILE:"; \
	echo "1) exe-demo"; \
	echo "2) exe-staging"; \
	echo "3) exe-prod"; \
	read -p "Enter choice [1-3] (default: 1): " PROFILE_CHOICE; \
	if [ "$$PROFILE_CHOICE" = "1" ] || [ -z "$$PROFILE_CHOICE" ]; then PROFILE="exe-demo"; \
	elif [ "$$PROFILE_CHOICE" = "2" ]; then PROFILE="exe-staging"; \
	elif [ "$$PROFILE_CHOICE" = "3" ]; then PROFILE="exe-prod"; \
	else echo "Invalid choice"; exit 1; fi; \
	echo "Select FILE_PATH:"; \
	echo "1) notebooks/EXECUTED/model_development"; \
	echo "2) notebooks/EXECUTED/model_validation"; \
	echo "3) Enter custom filepath"; \
	read -p "Enter choice [1-3]: " FILE_CHOICE; \
	if [ "$$FILE_CHOICE" = "1" ]; then FILE_PATH="notebooks/EXECUTED/model_development"; \
	elif [ "$$FILE_CHOICE" = "2" ]; then FILE_PATH="notebooks/EXECUTED/model_validation"; \
	elif [ "$$FILE_CHOICE" = "3" ]; then read -p "Enter custom FILE_PATH: " CUSTOM_FILE_PATH; FILE_PATH="$$CUSTOM_FILE_PATH"; \
	else echo "Invalid choice"; exit 1; fi; \
	read -p "Enter VM_API_HOST (default: https://api.prod.validmind.ai/api/v1/tracking): " INPUT_VM_API_HOST; \
	VM_API_HOST=$${INPUT_VM_API_HOST:-https://api.prod.validmind.ai/api/v1/tracking}; \
	read -p "Enter VM_API_KEY: " VM_API_KEY; \
	read -p "Enter VM_API_SECRET: " VM_API_SECRET; \
	read -p "Enter VM_API_MODEL: " VM_API_MODEL; \
	env_file="temp.env"; \
	echo "VM_API_HOST=$$VM_API_HOST" > $$env_file; \
	echo "VM_API_KEY=$$VM_API_KEY" >> $$env_file; \
	echo "VM_API_SECRET=$$VM_API_SECRET" >> $$env_file; \
	echo "VM_API_MODEL=$$VM_API_MODEL" >> $$env_file; \
	set -a; \
	source $$env_file; \
	set +a; \
	quarto render --profile "$$PROFILE" "$$FILE_PATH"; \
	rm $$env_file '

# Get all source files
get-source: clean clone copy-installation notebooks python-docs test-descriptions

# Retrieves the latest Jupyter Notebook widget package for output rendering
jupyter-widget:
	curl -L -o developer/embed-amd.js https://unpkg.com/@jupyter-widgets/html-manager@*/dist/embed-amd.js
	@echo "Updated developer/embed-amd.js to latest version from unpkg CDN"

# Copy over Jupyter notebooks and supporting files
notebooks:
	@echo "\nUpdating notebook source ..."
	@rm -f notebooks.zip
	@rm -rf $(DEST_DIR_NB)/ && mkdir -p $(DEST_DIR_NB)
	@cp -r $(SRC_DIR)/notebooks/. $(DEST_DIR_NB)/
	@echo "Duplicating all files from notebooks/tutorials/model_development/ for execution"
	@mkdir -p notebooks/EXECUTED/model_development/
	@cp -r notebooks/tutorials/model_development/* notebooks/EXECUTED/model_development/
	@echo "Duplicating all files from notebooks/tutorials/model_validation/ for execution"
	@mkdir -p notebooks/EXECUTED/model_validation/
	@cp -r notebooks/tutorials/model_validation/* notebooks/EXECUTED/model_validation/
	@echo "Copying LICENSE into notebooks ..."
	@cp -r $(SRC_DIR)/LICENSE $(DEST_DIR_NB)/
	@rm -rf $(DEST_DIR_NB)/code_sharing
	@echo "Moving Quickstart notebook into the root of notebooks/ ..."
	@if [ -f "$(DEST_DIR_NB)/code_samples/quickstart_customer_churn_full_suite.ipynb" ]; then mv $(DEST_DIR_NB)/code_samples/quickstart_customer_churn_full_suite.ipynb $(DEST_DIR_NB)/quickstart_customer_churn_full_suite.ipynb; fi
	@echo "Copying _metadata.yml into notebooks/ ..."
	@cp developer/_metadata.yml $(DEST_DIR_NB)/_metadata.yml
	@echo "Zip up notebooks.zip ..."
	@zip -r notebooks.zip $(DEST_DIR_NB) > /dev/null 2>&1

# Make Python library docs & copy them over
python-docs:
	@if [ -d "$(SRC_DIR)/docs" ]; then \
		echo "\nUpdating Python source ..."; \
		rm -rf $(DEST_DIR_PYTHON); \
		mkdir -p $(DEST_DIR_PYTHON); \
		rsync -av --exclude '_build' --exclude 'templates' $(SRC_DIR)/docs/ $(DEST_DIR_PYTHON)/; \
	fi

# Generate release notes
release-notes:
	@python ../release-scripts/generate_release_objects.py; \
	if [ $$? -eq 0 ]; then \
		cd ../; \
		git status | grep -v 'release-scripts/'; \
		cd site/; \
		quarto preview; \
	else \
		echo "Release note generation failed, git status and quarto preview"; \
	fi

test-descriptions:
	@echo "\nUpdating test descriptions source ..."
	@cd _source/validmind-library && make install && poetry run python scripts/extract_descriptions.py validmind/tests
	@cd ../../
	@rm -rf $(DEST_DIR_TESTS)
	@mkdir -p $(DEST_DIR_TESTS)
	@cp -r $(SRC_DIR)/build/_test_descriptions/validmind/tests/. $(DEST_DIR_TESTS)
	@echo "Copying _metadata.yml into tests/ ..."
	@cp developer/_metadata.yml $(DEST_DIR_TESTS)/_metadata.yml

# Collate yearly releases
yearly-releases:
	@python ../release-scripts/yearly_cleanup.py
	cd ../
	git status | grep -v 'release-scripts/'
	quarto preview
