# PythonForTester
- Here is the repository to guide the lessons from basic level to advanced level as Python For Tester/QA/QC.

# Setup local environment - Python Installation
- Install Python
https://www.python.org/downloads/
You should select the proper installation version for your operation types (Windows, MacOSX, Linux)
- How to configure multiple Python versions in your local environment.
#TBD
https://realpython.com/intro-to-pyenv/

- Configure Python Virtual environment in your workspace
On all my tutorials, I suggest you follow my steps to set up the virtual environment instead of using the base python environment.

```
python3 -m pip install --user virtualenv
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

- Check whether python was installed on your computer or NOT.
```
$ python --version
Python 2.7.12
$ python3 --version
Python 3.5.2
```

# Basic Questions

## Question 1

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method

[Answer](https://github.com/josdoaitran/PythonForTester/blob/master/BasicQuestions/Q1.py)
## Question 2
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

[Answer](https://github.com/josdoaitran/PythonForTester/blob/master/BasicQuestions/Q2.py)


## Question 3

With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()

[Answer](https://github.com/josdoaitran/PythonForTester/blob/master/BasicQuestions/Q3.py)

## Question 4
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple

[Answer](https://github.com/josdoaitran/PythonForTester/blob/master/BasicQuestions/Q4.py)

## Question 5:
Write a program which check a number is prime or not


## Question 6:
Write a program which print all of couple sequence prime.


# Basic for Python

we write Script to Read a file given in the command-line argument and print the number of
lines, words and characters - similar to UNIX's wc utility.

# References:

https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt

