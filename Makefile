STYLES=githubsurvivor/web/static/styles
LESSC ?= $(shell which lessc 2> /dev/null || echo "./node_modules/less/bin/lessc")

.PHONY: build css clean dist

build: css

$(STYLES)/%.css: $(STYLES)/%.less
	$(LESSC) $< >$@

css: $(patsubst $(STYLES)/%.less,$(STYLES)/%.css,$(wildcard $(STYLES)/*.less))

clean:
	rm $(STYLES)/*.css

dist: clean build
	python setup.py clean sdist upload
