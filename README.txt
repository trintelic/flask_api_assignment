# flask_api_assignment

!SETUP!

1. Open Anaconda Prompt
2. Ensure Python is installed by:
	python --version

3. Make a new folder for project by:
	mkdir flask_api_assignment
	cd flask_api_assignment 

4. Create the environment by:
	python -m venv venv

5. Activate environment by:
	venv\Scripts\activate

	!(venv) SHOULD NOW DISPLAY AT BEGINNING!
6. Install Flask within the environment by:
	pip install Flask

	!TO ENSURE INSTALLATION!:
	pip show Flask
7. Create application file by creating a file named app.py within Visual Studio Code
	
8. In that file, enter this text:
“
from flask import Flask, request, jsonify

app = Flask(__name__)


# GET endpoint
@app.get("/hello")
def hello():
    # Get optional name from URL
    name = request.args.get("name", "world")
    return jsonify({"message": f"Hello, {name}!", "status": "success"})


# POST endpoint
@app.post("/sum")
def sum_numbers():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    numbers = data.get("numbers")

    total = sum(numbers)

    return jsonify({"sum": total, "status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
“
9. Run it by pressing the play button arrow in the upper right hand corner and press Run Python File in Dedicated Terminal. If you do not see the play button, look to see if there is a blue banner and click it to trust the file.

10. Copy and paste http://127.0.0.1:5000/hello into the URL bar in your browser to test GET endpoint.

11. “Hello, world. success” should show.

12. To test POST endpoint copy: 
	curl -X POST http://127.0.0.1:5000/sum -H "Content-Type: application/json" -d "{\"numbers\":[1,2,3]}"
	!OR ANY OTHER NUMBERS AS LONG AS THEY ARE IN THAT FORMAT!
    into your Anaconda Prompt terminal. You should see {
  "status": "success",
  "sum": 6
} 
	or something similar.

13. To execute running server in Anaconda prompt:
	python app.py

14. TO EXECUTE TESTS ensure that pytest is installed!
	pip install pytest

15. In the same flask_api_assignment folder, create a new file in Visual Studio Code called test_app.py

16. Enter this code:
“
from app import app

client = app.test_client()


def test_hello():
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello, world!"


def test_sum():
    response = client.post("/sum", json={"numbers": [1, 2, 3]})

    assert response.status_code == 200
    assert response.get_json()["sum"] == 6
“
17. Run it by pressing the play button arrow in the upper right hand corner and press Run Python File in Dedicated Terminal.

18. Go to Anaconda prompt and enter:
	pytest test_app.py



Here are my outcomes:

app.py
PS C:\Users\Trine\flask_api_assignment> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& c:\Users\Trine\flask_api_assignment\venv\Scripts\Activate.ps1)
(venv) PS C:\Users\Trine\flask_api_assignment> & c:\Users\Trine\flask_api_assignment\venv\Scripts\python.exe c:/Users/Trine/flask_api_assignment/app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 440-769-411
127.0.0.1 - - [27/Oct/2026 16:40:26] "GET /hello HTTP/1.1" 200 -
127.0.0.1 - - [27/Oct/2026 16:41:57] "POST /sum HTTP/1.1" 200 -
 * Detected change in 'c:\\Users\\Trine\\flask_api_assignment\\test_app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 440-769-411
 * Detected change in 'c:\\Users\\Trine\\flask_api_assignment\\test_app.py', reloading
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 440-769-411


test_app.py
(venv) (base) C:\Users\Trine\flask_api_assignment>pytest test_app.py
================================================= test session starts =================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.7.0
rootdir: C:\Users\Trine\flask_api_assignment
collected 2 items

test_app.py ..                                                                                                   [100%]
================================================== 2 passed in 0.21s ==================================================



All coding in Anaconda Prompt Terminal for setup:
(base) C:\Users\Trine>mkdir flask_api_assignment

(base) C:\Users\Trine>cd flask_api_assignment

(base) C:\Users\Trine\flask_api_assignment>python -m venv venv

(base) C:\Users\Trine\flask_api_assignment>venv\Scripts\activate

(venv) (base) C:\Users\Trine\flask_api_assignment>pip install Flask
Collecting Flask
  Using cached flask-3.1.3-py3-none-any.whl.metadata (3.2 kB)
Collecting blinker>=1.9.0 (from Flask)
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click>=8.1.3 (from Flask)
  Using cached click-8.5.0-py3-none-any.whl.metadata (2.6 kB)
Collecting itsdangerous>=2.2.0 (from Flask)
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2>=3.1.2 (from Flask)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe>=2.1.1 (from Flask)
  Using cached markupsafe-3.0.4-cp314-cp314-win_amd64.whl.metadata (2.8 kB)
Collecting werkzeug>=3.1.0 (from Flask)
  Using cached werkzeug-3.1.9-py3-none-any.whl.metadata (4.1 kB)
Using cached flask-3.1.3-py3-none-any.whl (103 kB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.5.0-py3-none-any.whl (125 kB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached markupsafe-3.0.4-cp314-cp314-win_amd64.whl (14 kB)
Using cached werkzeug-3.1.9-py3-none-any.whl (228 kB)
Installing collected packages: markupsafe, itsdangerous, click, blinker, werkzeug, jinja2, Flask
Successfully installed Flask-3.1.3 blinker-1.9.0 click-8.5.0 itsdangerous-2.2.0 jinja2-3.1.6 markupsafe-3.0.4 werkzeug-3.1.9

[notice] A new release of pip is available: 26.1.2 -> 26.2.2
[notice] To update, run: python.exe -m pip install --upgrade pip

(venv) (base) C:\Users\Trine\flask_api_assignment>pip show Flask
Name: Flask
Version: 3.1.3
Summary: A simple framework for building complex web applications.
Home-page:
Author:
Author-email:
License-Expression: BSD-3-Clause
Location: C:\Users\Trine\flask_api_assignment\venv\Lib\site-packages
Requires: blinker, click, itsdangerous, jinja2, markupsafe, werkzeug
Required-by:

(venv) (base) C:\Users\Trine\flask_api_assignment>curl -X POST http://127.0.0.1:5000/sum -H "Content-Type: application/json" -d "{\"numbers\":[1,2,3]}"
{
  "status": "success",
  "sum": 6
}

(venv) (base) C:\Users\Trine\flask_api_assignment>python app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 440-769-411

(venv) (base) C:\Users\Trine\flask_api_assignment>pytest tesp_app.py
================================================= test session starts =================================================
platform win32 -- Python 3.14.6, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\Trine\flask_api_assignment
plugins: anyio-4.12.1
collected 0 items

================================================ no tests ran in 0.03s ================================================
ERROR: file or directory not found: tesp_app.py


(venv) (base) C:\Users\Trine\flask_api_assignment>pip install pytest
Collecting pytest
  Using cached pytest-9.1.1-py3-none-any.whl.metadata (7.6 kB)
Collecting colorama>=0.4 (from pytest)
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting iniconfig>=1.0.1 (from pytest)
  Using cached iniconfig-2.3.1-py3-none-any.whl.metadata (2.8 kB)
Collecting packaging>=22 (from pytest)
  Using cached packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pluggy<2,>=1.5 (from pytest)
  Using cached pluggy-1.7.0-py3-none-any.whl.metadata (5.0 kB)
Collecting pygments>=2.7.2 (from pytest)
  Using cached pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
Using cached pytest-9.1.1-py3-none-any.whl (386 kB)
Using cached pluggy-1.7.0-py3-none-any.whl (27 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Using cached iniconfig-2.3.1-py3-none-any.whl (7.6 kB)
Using cached packaging-26.3-py3-none-any.whl (129 kB)
Using cached pygments-2.21.0-py3-none-any.whl (1.3 MB)
Installing collected packages: pygments, pluggy, packaging, iniconfig, colorama, pytest
Successfully installed colorama-0.4.6 iniconfig-2.3.1 packaging-26.3 pluggy-1.7.0 pygments-2.21.0 pytest-9.1.1

[notice] A new release of pip is available: 26.1.2 -> 26.2.2
[notice] To update, run: python.exe -m pip install --upgrade pip

(venv) (base) C:\Users\Trine\flask_api_assignment>pytest test_app.py
================================================= test session starts =================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.7.0
rootdir: C:\Users\Trine\flask_api_assignment
collected 0 items

================================================ no tests ran in 0.03s ================================================

(venv) (base) C:\Users\Trine\flask_api_assignment>pytest test_app.py
================================================= test session starts =================================================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.7.0
rootdir: C:\Users\Trine\flask_api_assignment
collected 2 items

test_app.py ..                                                                                                   [100%]

================================================== 2 passed in 0.21s ==================================================

(venv) (base) C:\Users\Trine\flask_api_assignment>