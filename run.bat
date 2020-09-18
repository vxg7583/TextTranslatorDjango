@echo off
:: Check for Python Installation
python --version 3>NUL
if errorlevel 1 goto errorNoPython
pip.exe install --user virtualenv
python -m venv env
\env\Scripts\activate.bat
pip install -r requirements.txt
python manage.py runserver
:: Once done, exit the batch file -- skips executing the errorNoPython section
goto:eof

:errorNoPython
echo.
echo Error: Python 3+ not installed or not set as environment variable