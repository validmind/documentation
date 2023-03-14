# Define source and destination directories
SRC_DIR := _source/validmind-python
DEST_DIR_NB := notebooks
DEST_DIR_PYTHON := validmind

# Define .PHONY target for help section
.PHONY: help clean clone notebooks python-docs

# Help section
help:
	@echo "Available targets:"
	@echo "  clean        Remove the _source/ directory"
	@echo "  clone        Clone the validmind-python repository into _source/"
	@echo "  notebooks    Copy Jupyter notebooks to notebooks/"
	@echo "  python-docs  Build the Python library docs and copy to validmind/"
	@echo "  get-source   Get all source files (clean, clone, notebooks, python-docs)"
	@echo "  help         Display this help message (default target)"

# Clean up source directory
clean:
	rm -rf $(SRC_DIR)

# Clone the source repository we need
clone:
	git clone https://github.com/validmind/validmind-python.git $(SRC_DIR)

# Copy over Jupyter notebooks
notebooks:
	rm -rf $(DEST_DIR_NB)
	mkdir -p $(DEST_DIR_NB)
	cp -r $(SRC_DIR)/notebooks/. $(DEST_DIR_NB)

# Make Python library docs & copy them over
python-docs: 
	$(MAKE) -C $(SRC_DIR)/docs markdown
	rm -rf $(DEST_DIR_PYTHON)
	mkdir -p $(DEST_DIR_PYTHON)
	cp -r $(SRC_DIR)/docs/_build/markdown/. $(DEST_DIR_PYTHON)

# Get all source files
get-source: clean clone notebooks python-docs
