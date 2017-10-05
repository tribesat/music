ifndef CI
ifndef VIRTUAL_ENV
$(error Please use virtualenv)
endif
endif

PACKAGE_NAME := "tribesat_music"

install: requirements
	python setup.py install

develop: requirements
	python setup.py develop

.PHONY: requirements
requirements:
	pip install -r requirements.txt

test: unit-test style-review

.PHONY: unit-test
unit-test:
	nosetests \
		--verbose \
		--nocapture \
		--with-coverage \
		--cover-tests \
		--cover-erase \
		--cover-package=$(PACKAGE_NAME) \
		tests

pretty:
	yapf --in-place --recursive --parallel tribesat_music tests

.PHONY: style-review
style-review:
	@output="$$(yapf --parallel --diff --recursive nodelib tests)"; \
		if [ -n "$$output" ]; then \
			echo "$$output"; \
			echo "run 'make pretty'"; \
			exit 1; \
		fi
	@echo "Looks good"
