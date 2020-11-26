# Sample repository

This repository demonstrates an integration between two different third-party CI services, `circleci` and `mergify`.

- `circleci` runs tests.
- `mergify` manages concurrent pull-requests.

## `circleci`

Configuration of this service is centralized in `.circleci/config.yml`.

## `mergify`

A merge queue is managed by `mergify`. Configuration is centralized in `.mergify.yml`.

### Rules

If a pull-request is labeled with "on-merge-queue" that pull-request will be merged, regardless of the number of commits included. Please rebase prior to adding to merge queue! If you don't, your commits will be deleted from upstream.
