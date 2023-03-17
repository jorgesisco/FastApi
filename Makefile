install:
	pipenv install -r requirements.txt
	pipenv shell

run:
	pipenv run python -m pytest tests || exit 1
	pipenv run python run.py

test:
	pipenv run python -m pytest tests

freeze:
	pip3 freeze > requirements.txt