# Code duplication detector

## How to run the tests
First, make sure you have added the package to the Python path of your machine.

From root folder execute the test
```
python3 tests/test_duplication.py
```

## Adding a Package to the Python Path

### Linux and macOS:
Use the following command to export the path to the package directory to the `PYTHONPATH` variable:
```bash
export PYTHONPATH="/path/to/package/directory:${PYTHONPATH}"
```
To make this change permanent, add the export command to your shell's profile file (e.g., `~/.bashrc` for Bash).

### Windows:
   - Open the Control Panel.
   - Go to System and Security > System.
   - Click on "Advanced system settings" in the sidebar.
   - In the System Properties window, click on the "Environment Variables..." button.
   - In the Environment Variables window, under "System variables", click on "New...".
   - Enter `PYTHONPATH` as the variable name and the path to your package directory as the variable value.
   - Click "OK" to save the changes.

