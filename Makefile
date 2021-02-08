clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

test: clean
	@black orbit
	@black tests
	@flake8 orbit
	@pytest --cov orbit -s --cov-report term-missing
