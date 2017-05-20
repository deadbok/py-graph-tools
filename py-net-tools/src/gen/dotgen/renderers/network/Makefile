PY_SRC := $(wildcard *.py)
PUML_SRC := $(addprefix $(PUML_PREFIX), $(notdir $(PY_SRC:.py=.puml)))

all: $(PUML_SRC)

$(PUML_SRC): $(PY_SRC)
	python3 $(PY2PUML) --package $(PUML_PREFIX)  $(subst $(PUML_PREFIX),,$(@:.puml=.py)) $@