# Python boilerplate

<img src="https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="100" />
<img src="https://e7.pngegg.com/pngimages/354/728/png-clipart-plus-and-minus-signs-computer-icons-emoji-logo-plus-thumbnail.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="100" />
This repositry is a repositry that created a booilerplate for Linting in a Visual Studio Code environment.

---

## Getting started with Visual Studio Code.

1. Install [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) from Visual Studio Code.

2. Create a Python virtual environment in Root through the command below.

```bash
python -m venv venv
```

3. To enter the virtual environment, if the terminal is already open, close and reopen or enter the command below in the terminal.

```bash
source venv/bin/activate
```

4. Please install the package by entering the command below.
   The list of packages to be installed can be found through [this link](https://github.com/Jay-flow/python_boilerplate/blob/main/requirements.txt).

```bash
pip install -r requirements.txt
```

5. To set up [PYTHONPATH](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH), modify the PYTHONPATH in the `.vscode/.env` file to suit the project root path.
   For example.

```
PYTHONPATH=/Users/jay/PythonProjects/python_boilerplate
```

6. (Optional) If you want to change the alert that Pylint ignores. Please modify the variable below in the `.vscode/settings.json` file.

```json
{
  "python.linting.pylintArgs": [
    "--disable=missing-docstring",
    "--disable=too-few-public-methods",
    "--diisable=no-self-use"
  ]
}
```
