all: classes dot_generator.png classes.png

.PHONY: classes
classes:
	$(MAKE) -C autopuml

%.png: %.puml
	plantuml $<