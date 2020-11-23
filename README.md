# Sample repository

This repository demonstrates an integration between two different third-party CI services, `circleci` and `mergequeue`.

- `circleci` runs tests.
- `mergequeue` manages concurrent pull-requests.

## `circleci`

Configuration of this service is centralized in `.circleci/config.yml`.

## `mergequeue`

Rules for this service are managed through a Github Application dashboard accessible through github.
