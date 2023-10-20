#!/usr/bin/env bash

git config --global --add safe.directory /home/docs/project

exec "$@"
