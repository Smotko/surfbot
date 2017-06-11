#!/bin/bash

log_error () {
  if [ $1 == 0 ]; then
    echo "  ✅  $2";
  else
    echo "  ❌  $2 failed with:"
    cat /tmp/error
    if [ "$2" = "flake8" ]; then
      echo; fi; fi
  return $1
}

. venv/bin/activate
PATH=$PATH:venv/bin/

EXIT_FLAKE8=0
EXIT_PYLINT=0
EXIT_MYPY=0
flake8 src 1> /tmp/error || EXIT_FLAKE8=$?
log_error $EXIT_FLAKE8 "flake8"
pylint src 1> /tmp/error || EXIT_PYLINT=$?
log_error $EXIT_PYLINT "pylint"
mypy src 1> /tmp/error || EXIT_MYPY=$?
log_error $EXIT_MYPY "mypy"

EXIT=$(($EXIT_FLAKE8 + $EXIT_PYLINT + $EXIT_MYPY))
exit $EXIT
