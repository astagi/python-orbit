clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

test: clean
	@flake8 orbit
	@pytest --cov orbit -s --cov-report term-missing

format:
	@black orbit
	@black tests
