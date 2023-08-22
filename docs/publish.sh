#!/usr/bin/env bash

BASE=$(dirname "${BASH_SOURCE[0]}")

cd "${BASE}/../dist/docs"

touch .nojekyll

git init
git checkout -b page
git remote add origin git@github.com:ofabel/pytm-bootstrap.git
git add . && git commit -m "publish web page"
git push origin page --force

rm -rf .git .nojekyll

exit 0
