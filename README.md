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

### Scheduler output type definition

Assume following parameters

```
  Number of days in the month = n_days
  Number of shifts per day = n_shifts
  Number of doctors per shift = n_strenth
  Number of doctors in unit = n_doctors
```
Then the output of the scheduler will be in the format of a list with dimentions ``` n_days x n_shifts x n_strenth ```. 


