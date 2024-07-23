
data:
	curl -o data/us-states.csv https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

clean:
	test -e data/us-states.csv && rm data/us-states.csv || true
	test -e model/__pycache__ && rm -rf model/__pycache__ || true

.PHONY: data clean
