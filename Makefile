STYLES=githubsurvivor/web/static/styles

.PHONY: build css clean dist

build: css

$(STYLES)/%.css: $(STYLES)/%.less
	lessc $< >$@

css: $(patsubst $(STYLES)/%.less,$(STYLES)/%.css,$(wildcard $(STYLES)/*.less))

clean:
	rm $(STYLES)/*.css

dist: clean build
	python setup.py clean sdist upload
