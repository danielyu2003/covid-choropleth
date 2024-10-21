
data:
	curl -o data/us-states.csv https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

clean:
	test -e data/us-states.csv && rm data/us-states.csv || true
	test -e models/__pycache__ && rm -rf models/__pycache__ || true
	test -e utils/__pycache__ && rm -rf utils/__pycache__ || true

.PHONY: data clean
