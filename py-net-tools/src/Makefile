PY_SRC := $(wildcard *.py)
PUML_SRC := $(PY_SRC:.py=.puml)
PUML_PREFIX :=

%.puml: %.py
	python3 $(PY2PUML) $< $(PUML_PREFIX)$@

all: $(PUML_SRC)
	$(MAKE) PY2PUML=$(PY2PUML) PUML_PREFIX=$(PUML_PREFIX)gen. -C gen

