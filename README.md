# Mini Aspire Project

## Setup & Installation

Please make sure you have the support for latest format strings format in python.

```bash
git clone <repo-url>
```

```bash
pip install -r requirements.txt
```

## Running The App

```bash
python main.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`

## Test The App
All tests, can be found in `test/test_website.py`
Following command should be run to execute all the tests.

```bash
pytest --verbose --disable-warnings
```

Following ouput is observed currently (all tests passing!)
```bash
(venv) apple@Apples-MacBook-Air aspire-mini % pytest --verbose   --disable-warnings
=========================================================== test session starts ===========================================================
platform darwin -- Python 3.9.6, pytest-7.3.1, pluggy-1.0.0 -- /Users/apple/Desktop/dev/venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/apple/Desktop/dev/aspire-mini
collected 4 items                                                                                                                         

test/test_website.py::test_signup PASSED                                                                                            [ 25%]
test/test_website.py::test_login PASSED                                                                                             [ 50%]
test/test_website.py::test_loan PASSED                                                                                              [ 75%]
test/test_website.py::test_invalid_login PASSED                                                                                     [100%]

====================================================== 4 passed, 7 warnings in 0.11s ======================================================
(venv) apple@Apples-MacBook-Air aspire-mini %
```


