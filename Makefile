.PHONY: markdownlint actionlint yamllint lint

markdownlint:
	markdownlint '**/*.md' --dot

actionlint:
	actionlint

yamllint:
	yamllint .

lint: markdownlint actionlint yamllint
