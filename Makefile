LESS=res/less
CSS=githubsurvivor/web/static/styles

.PHONY: build css clean dist

build: css

$(CSS)/%.css: $(LESS)/%.less
	lessc $< >$@

css: $(patsubst $(LESS)/%.less,$(CSS)/%.css,$(wildcard $(LESS)/*.less))

clean:
	rm $(CSS)/*.css

dist: clean build
	python setup.py clean sdist upload
