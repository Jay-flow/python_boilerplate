# Python boilerplate

Python + VSCode + 𝖳𝗒𝗉𝖾 hint(mypy, pylint)

This repositry is a repositry that created a booilerplate for Linting in a Visual Studio Code environment.

---

## Getting started with Visual Studio Code

1. Install [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from Visual Studio Code.

2. Please make a `.env` file by copying the `.env_example` file for the proejct.

```bash
cp .env_example .env
```

3. Please make a `.vscode/.env` file by copying the `.vscode/.env_example` file for the vscode.

```bash
cp .vscode/.env_example .vscode/.env
```

4. Write the project root path in the following variables in file `.vscode/.env`

```env
PYTHONPATH=/project_root_path
```

5. Create a Python virtual environment in Root through the command below.

```bash
python -m venv venv
```

6. To enter the virtual environment, if the terminal is already open, close and reopen or enter the command below in the terminal.

```bash
source venv/bin/activate
```

7. Please install the package by entering the command below.
   The list of packages to be installed can be found through [this link](https://github.com/Jay-flow/python_boilerplate/blob/main/requirements.txt).

```bash
pip install -r requirements.txt
```

8. To set up [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH), modify the PYTHONPATH in the `.vscode/.env` file to suit the project root path.
   For example.

```
PYTHONPATH=/Users/jay/PythonProjects/python_boilerplate
```

9. (Optional) If you want to change the alert that Pylint ignores. Please modify the variable below in the `.vscode/settings.json` file.

```json
{
  "python.linting.pylintArgs": [
    "--disable=missing-docstring",
    "--disable=too-few-public-methods",
    "--diisable=no-self-use"
  ]
}
```
