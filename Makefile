.PHONY: run test clean

run:
	mkdir -p img
	python src/main.py

install:
	pip install numpy pandas matplotlib sklearn

test:
	mkdir -p test
	python src/test.py

clean:
	mkdir -p img
	rm img/*
	mkdir -p test
	rm test/*
