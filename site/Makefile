# Define source and destination directories
SRC_DIR := _source/validmind-python
SRC_DIR_DOC := _source/documentation
SRC_DIR_FRONTEND := _source/frontend
SRC_DIR_BACKEND := _source/backend
DEST_DIR_NB := notebooks
DEST_DIR_PYTHON := _site/validmind

# Define .PHONY target for help section
.PHONY: help clean clone notebooks python-docs docs-site deploy-demo deploy-prod 

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

# Clean up source directory
clean:
	rm -rf $(SRC_DIR)
	rm -rf $(SRC_DIR_DOC)
	rm -rf $(SRC_DIR_FRONTEND)
	rm -rf $(SRC_DIR_BACKEND)

# Clone the source repository we need
clone:
	git clone -b prod git@github.com:validmind/validmind-python.git $(SRC_DIR)
	git clone -b prod git@github.com:validmind/documentation.git $(SRC_DIR_DOC)
	git clone -b prod git@github.com:validmind/frontend.git $(SRC_DIR_FRONTEND)
	git clone -b prod git@github.com:validmind/backend.git $(SRC_DIR_BACKEND)

# Copy over Jupyter notebooks
notebooks:
	rm -rf $(DEST_DIR_NB)/how_to
	mkdir -p $(DEST_DIR_NB)/how_to
	cp -r $(SRC_DIR)/notebooks/how_to/. $(DEST_DIR_NB)/how_to
	rm -rf $(DEST_DIR_NB)/time_series
	mkdir -p $(DEST_DIR_NB)/time_series
	cp -r $(SRC_DIR)/notebooks/time_series/tutorial_time_series_forecasting.ipynb $(DEST_DIR_NB)/time_series/

# Make Python library docs & copy them over
python-docs:
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
	@if [ "`git rev-parse --abbrev-ref HEAD`" != "docs-demo" ]; then \
		echo "You're not on the docs-demo branch, no action taken."; \
	else \
		echo "You're on the docs-demo branch. Deploying docs-demo site ..."; \
        quarto render && \
        aws s3 sync ./_site s3://docs-ci-cd-demo/site/ --delete && \
        aws cloudfront create-invalidation --distribution-id E38AINJY5CYN6P --paths "/*" --no-cli-pager > /dev/null; \
    fi

# Deployment to https://docs.validmind.ai/
deploy-prod:
	@if [ "`git rev-parse --abbrev-ref HEAD`" != "main" ] && [ "`git rev-parse --abbrev-ref HEAD`" != "prod" ]; then \
		echo "You're not on the main or prod branches, no action taken."; \
	else \
		echo "You're on the main or prod branch. Deploying prod site ..."; \
		quarto render && \
		aws s3 sync ./_site s3://docs-ci-cd-prod/site/ --delete && \
		aws cloudfront create-invalidation --distribution-id E2I9R40IH01NW3 --paths "/*" --no-cli-pager > /dev/null; \
	fi
