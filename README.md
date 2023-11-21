**How to run playwright tests in Python**

basic command:
pytest

running in headed mode:
pytest --headed

running in a different browser:
pytest --browser chromium

running specific test file:
pytest tests/test_example.py

running specific test:
pytest -k test_checks_that_i_can_visit_wikipedia

with tracing:
pytest --tracing on

with tracing, but only keeping failures:
pytest --tracing retain-on-failure

open trace: 
playwright show-trace test-results/tests-test-example-py-test-fails-on-purpose-chromium/trace.zip
