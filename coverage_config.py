[tox]
envlist = py39
skipsdist = true

[testenv]
deps =
    pytest
    coverage
commands =
    coverage run -m pytest
    coverage xml

[coverage:run]
relative_files = true
source = src
branch = true
