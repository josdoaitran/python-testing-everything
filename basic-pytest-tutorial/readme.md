# Basic Lessons about Pytest


## Running Tests
pytest has many command line options with a powerful discovery mechanism:
```
python -m pytest
# To discover and run all tests from the current directory

python -m pytest -v 
# To explicitly print the result of each test as it is run

python -m pytest tests/test_calc_func.py 
# To run only the math function tests

python -m pytest tests/test_calc_class.py 
# To run only the Calculator class tests

python -m pytest --junitxml=results.xml 
# To generate a JUnit-style XML test report

python -m pytest -h 
# for command line help
```

It is also possible to run pytest directly with the "pytest" or "py.test" command, instead of using the longer "python -m pytest" module form. However, the shorter command does not append the current directory path to PYTHONPATH.