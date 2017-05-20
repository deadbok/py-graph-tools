all: docs

PY2PUML=$(shell pwd)/../py-puml-tools/py2puml/py2puml.py

.PHONY: docs
docs:
	$(MAKE) PY2PUML=$(PY2PUML) -C src
	$(MAKE) PY2PUML=$(PY2PUML) -C docs
