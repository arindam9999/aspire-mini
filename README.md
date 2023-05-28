# Mini Aspire Project

## Setup & Installation

Make sure you have the support for latest format strings format in python.

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

## Test the app
All tests, can be found in `test/test_website.py`

```bash
pytest
```

Following ouput is observed currently (all tests passing!)
```bash

(venv) apple@Apples-MacBook-Air aspire-mini % pytest -s                      
=========================================================== test session starts ===========================================================
platform darwin -- Python 3.9.6, pytest-7.3.1, pluggy-1.0.0
rootdir: /Users/apple/Desktop/dev/aspire-mini
collected 4 items                                                                                                                         

test/test_website.py ....

============================================================ warnings summary =============================================================
test/test_website.py::test_signup
test/test_website.py::test_login
test/test_website.py::test_loan
  /Users/apple/Desktop/dev/aspire-mini/website/auth.py:55: UserWarning: The 'sha256' password method is deprecated and will be removed in Werkzeug 3.0. Migrate to the 'scrypt' method.
    new_user = User(email=email, first_name=first_name, password=generate_password_hash(

test/test_website.py::test_login
test/test_website.py::test_loan
  /Users/apple/Desktop/dev/aspire-mini/website/auth.py:18: UserWarning: The 'sha256' password method is deprecated and will be removed in Werkzeug 3.0. Migrate to the 'scrypt' method.
    if check_password_hash(user.password, password):

test/test_website.py::test_loan
  /Users/apple/Desktop/dev/venv/lib/python3.9/site-packages/flask_login/utils.py:126: DeprecationWarning: 'werkzeug.urls.url_decode' is deprecated and will be removed in Werkzeug 2.4. Use 'urllib.parse.parse_qs' instead.
    md = url_decode(parsed_result.query)

test/test_website.py::test_loan
  /Users/apple/Desktop/dev/venv/lib/python3.9/site-packages/flask_login/utils.py:130: DeprecationWarning: 'werkzeug.urls.url_encode' is deprecated and will be removed in Werkzeug 2.4. Use 'urllib.parse.urlencode' instead.
    netloc=netloc, query=url_encode(md, sort=True)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
====================================================== 4 passed, 7 warnings in 0.12s ======================================================
(venv) apple@Apples-MacBook-Air aspire-mini % 
```


