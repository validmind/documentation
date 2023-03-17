# Define source and destination directories
SRC_DIR := _source/validmind-python
DEST_DIR_NB := notebooks
DEST_DIR_PYTHON := validmind

# Define .PHONY target for help section
.PHONY: help clean clone notebooks python-docs docs-site

# Help section
help:
	@echo "Available targets:"
	@echo "  clean        Remove the _source/ directory"
	@echo "  clone        Clone the validmind-python repository into _source/"
	@echo "  notebooks    Copy the Jupyter notebooks to notebooks/"
	@echo "  python-docs  Build the Python library docs and copy to validmind/"
	@echo "  get-source   Get all source files (clean, clone, notebooks, python-docs)"
	@echo "  docs-site    Get all source files and render the docs site"
	@echo "  help         Display this help message (default target)"

# Clean up source directory
clean:
	rm -rf $(SRC_DIR)

# Clone the source repository we need
clone:
	git clone git@github.com:validmind/validmind-python.git $(SRC_DIR)

# Copy over Jupyter notebooks
notebooks:
	rm -rf $(DEST_DIR_NB)
	mkdir -p $(DEST_DIR_NB)
	cp -r $(SRC_DIR)/notebooks/. $(DEST_DIR_NB)

# Make Python library docs & copy them over
python-docs:
	rm -rf $(DEST_DIR_PYTHON)
	mkdir -p $(DEST_DIR_PYTHON)
	cp -r $(SRC_DIR)/docs/_build/markdown/. $(DEST_DIR_PYTHON)

# Get all source files
get-source: clean clone notebooks python-docs

# Get all source files
docs-site: clean clone notebooks python-docs
	quarto render

