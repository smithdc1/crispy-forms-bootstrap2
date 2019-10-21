.PHONY: develop test

develop:
	pip install -q -r requirements.txt
	pip install -q -e .

test: develop
	DJANGO_SETTINGS_MODULE=crispy-forms-bootstrap2.tests.test_settings py.test crispy-forms-bootstrap2/tests --cov=crispy-forms-bootstrap2