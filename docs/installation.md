# Installation

This page should give you basic information on how to install this library.

## Python Version

It's recommended to use the latest version of [Python](https://www.python.org/). The minimal supported version is 3.8.

## Dependencies

This library is dependant of the following packages:

* [Flask](https://pypi.org/project/Flask/) is a simple HTTP framework.
* [Flask-Cors](https://pypi.org/project/Flask-Cors/) to support cross-origin requests.
* [matplotlib](https://pypi.org/project/matplotlib/) to render simple figures, graphs and plots.

## Virtual Environments

It's recommended to create and use a [virtual environment](https://docs.python.org/3/library/venv.html) when
programming an exercise with this library. You can create a virtual environment with the following command:

```shell
python -m venv venv
```

The advantage of a virtual environment is, you don't need to install your site packages in the global scope.
Therefore, you can omit unwanted site effects with other applications and Python projects on your system.
In order to use an existing virtual environment, you need to activate it first:

```shell
source venv/bin/activate
```

## Requirements

This library has the following requirements:

* Python, greater or equal version 3.8.
* A plain text editor ([PyCharm](https://www.jetbrains.com/pycharm/)
  or [Visual Studio Code](https://code.visualstudio.com/) is recommended)
* Bash compatible terminal (e.g. [Git Bash](https://gitforwindows.org/) or [Cygwin](https://www.cygwin.com) on Windows)
* The use of [Git](https://git-scm.com/) as a [version control system](https://en.wikipedia.org/wiki/Version_control) is
  highly recommended.

## Install the Library with Pip

To install the library with [Pip](https://pip.pypa.io/en/stable/), activate the virtual environment and execute the
following command:

```shell
pip install pytmlib
```

## Install the Library with a Requirements File

Create or edit the `requirements.txt` file and add the following line:

```requirements.txt
pytmlib>=1.0.0
```

To install the requirements, open a new console window, activate the virtual environment and execute the following
command:

```shell
pip install -r requirements.txt
```
