PY_SRC := $(wildcard *.py)
PUML_SRC := $(addprefix $(PUML_PREFIX), $(notdir $(PY_SRC:.py=.puml)))

all: $(PUML_SRC)
	$(MAKE) PY2PUML=$(PY2PUML) PUML_PREFIX=$(PUML_PREFIX)connection.  -C connection
	$(MAKE) PY2PUML=$(PY2PUML) PUML_PREFIX=$(PUML_PREFIX)device.  -C device
	$(MAKE) PY2PUML=$(PY2PUML) PUML_PREFIX=$(PUML_PREFIX)network.  -C network

$(PUML_SRC): $(PY_SRC)
	python3 $(PY2PUML) --package $(PUML_PREFIX)  $(subst $(PUML_PREFIX),,$(@:.puml=.py)) $@


