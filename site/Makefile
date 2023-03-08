# Copy source over from other ValidMind repositories
get-source:

    # Jupyter notebooks
	rm -rf notebooks/
	mkdir notebooks
	cp -r ../../validmind-python/notebooks/. notebooks/

    # Output from `mkdocstrings` converted to Markdown via Pandoc 
	rm -rf python-library/
	mkdir python-library
	cp -r ../../validmind-python/site/. python-library/
