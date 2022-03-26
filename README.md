# Python boilerplate

Python + VSCode + 𝖳𝗒𝗉𝖾 hint(mypy, pylint)

This repositry is a repositry that created a booilerplate for Linting in a Visual Studio Code environment.

The project depends on the [pipenv](https://pipenv.pypa.io/en/latest/) package manager.

If you haven't installed it, please use the following command to install it.

```bash
$ pip install --user pipenv
```

---

## Getting started with Visual Studio Code

1. Install [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from Visual Studio
   Code.

2. Please make a `.env` file by copying the `.env_example` file for the proejct.

```bash
$ cp .env_example .env
```

3. Please make a `.vscode/.env` file by copying the `.vscode/.env_example` file for the vscode.

```bash
$ cp .vscode/.env_example .vscode/.env
```

4Create a Python virtual environment in Root through the command below.

```bash
$ pipenv shell
```

5.Please install the package by entering the command below. The list of packages to be installed can be found
through [this link](https://github.com/Jay-flow/python_boilerplate/blob/main/Pipfile).

```bash
$ pipenv -d install
```

6. To set up [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH), modify the PYTHONPATH in
   the `.vscode/.env` file to suit the project root path. For example, you can write down the path of the python
   executable in the following format

```
PYTHONPATH=/Users/jay/PythonProjects/python_boilerplate
```

7. The Python interpreter configuration is required to automatically run the virtual environment for VSCode. you need to
   modify the file of path `.vscode/settings.json`, which varies from project to project

```
{
  "python.defaultInterpreterPath": "/Users/jay/.local/share/virtualenvs/[project_name]/bin/python3.10",
  ...
}
```

8. (Optional) If you want to change the alert that Pylint ignores. Please modify the variable below in
   the `.vscode/settings.json` file.

```json
{
  "python.linting.pylintArgs": [
    "--disable=missing-docstring",
    "--disable=too-few-public-methods",
    "--diisable=no-self-use"
  ]
}
```
