.PHONY: markdownlint actionlint yamllint lint clean hooks

markdownlint:
	markdownlint '**/*.md' --dot

actionlint:
	actionlint

yamllint:
	yamllint .

lint: markdownlint actionlint yamllint

clean:
	rm -rf .venv venv env
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete

hooks:
	python3 -m pip install --quiet --break-system-packages pre-commit
	python3 -m pre_commit install
