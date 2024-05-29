# Installation

## Create a virtual environment using `pyenv` and `pyenv-virtualenv`

To create a virtual environment using a specific version of Python that you have installed via `pyenv` on macOS, follow these steps:

1. **Install `pyenv`** (if not already installed):

   ```sh
   brew install pyenv
   ```

2. **Install the desired Python version using `pyenv`** (if not already installed):

   ```sh
   pyenv install <python-desired-version>
   ```

3. **Set the local Python version to the one you just installed**:

   ```sh
   pyenv local <python-desired-version>
   ```

4. **Install `pyenv-virtualenv`** (if not already installed):

   ```sh
   brew install pyenv-virtualenv
   ```

5. **Create a virtual environment using the installed Python version**:

   ```sh
   pyenv virtualenv <version> <venv-name>
   ```

   or if Python version was selected with `pyenv local` command, you can create a virtual environment without specifying the:

   ```sh
   pyenv virtualenv <venv-name>
   ```

6. **Activate the virtual environment**:

   ```sh
   pyenv activate <venv-name>
   ```

7. **Verify the Python version in the virtual environment**:

   ```sh
   python --version
   ```

## Remove a virtual environment using `pyenv` and `pyenv-virtualenv`

To remove a virtual environment created with `pyenv` and `pyenv-virtualenv`, follow these steps:

1. **Deactivate the virtual environment** (if it's currently active):

   ```sh
   pyenv deactivate
   ```

2. **Uninstall the virtual environment**:

   ```sh
   pyenv virtualenv-delete <venv-name>
   ```

Alternatively, you can use:

```sh
pyenv uninstall <venv-name>
```

## Create a virtual environment using `venv`

To create a virtual environment using `venv` and a specific version of Python managed by `pyenv`, follow these steps:

1. **Set the local Python version to the one you just installed**:

   ```sh
   pyenv local <version>
   ```

2. **Create a virtual environment using `venv`**:

   ```sh
   python -m venv <venv-directory>
   ```

3. **Activate the virtual environment**:

   ```sh
   source <venv-directory>/bin/activate
   ```

4. **Verify the Python version in the virtual environment**:

   ```sh
   python --version
   ```
