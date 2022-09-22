# scheduler-core
Contains code for the constraint scheduler, to be run locally in a python virtual environment. 

This codebase uses contraint solver provided with [Google OR Tools](https://developers.google.com/optimization) suite. Google OR Tools is an opensource optimization suite packaging many different solvers and can be run in C++, Python, Java, and C#. Furthur docmentation can be found [here](https://developers.google.com/optimization/reference).

### Initializing the virtual environment 

Use the following script to setup project and install dependencies. 
```
  python3 -m venv .venv
  source .venv/bin/activate
  pip install --upgrade pip
  pip install ortools
```
For using venv with VSCode see [here](https://code.visualstudio.com/docs/python/environments). 
