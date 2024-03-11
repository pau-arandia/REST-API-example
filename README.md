# Create and activate virtual environment using the `virtualenv` tool

1. Install `virtualenv` through the CMD.

    ```bash
    pip install virtualenv
    ```

    If you're in an active virtual environment, `pip` installs the dependency into that environment. Otherwise, it installs it globally on your system.

2. Create a virtual environment inside the project folder.

    ```bash
    python -m virtualenv env
    ```

    `env` is the name of the environment as well as the name of the folder in which the environment is built. Calling this folder `env` is a convention.

    The `-m` flag is a command-line option that allows you to run a module as a script. This means you can execute Python code directly from the command line without the need for an external script file. Basically, we're activating Python first and then we're using the `virtualenv` tool.

3. Activate the environment.
    
    WARNING: This step only works for cmd. For PowerShell, see: https://stackoverflow.com/questions/1365081/virtualenv-in-powershell
    
    Run the `activate.bat` file located inside the `\Scripts` folder:
    
    ```bash
    env\Scripts\activate.bat
    ```

    This command will access the `\Scripts` folder that gets created automatically inside `env` when setting up the environment with `virtualenv`, and then it will execute the `activate.bat` file.

    The way to check that the environment has been successfully activated is by looking for the `(env)` part at the beginning of the command line. It should look like this:

    ```bash
    (env) C:\Users\...\project\api>
    ```

4. Install the required dependencies (libraries) to run the project.

    We might already have a text file that contains the names and versions of all the necessary dependencies. If this is the case, the following commmand must be run in the CMD to install the dependencies that are cited in the text file:

    ```bash
    pip install -r requirements.txt
    ```
    ... where "requirements.txt" is the name of said file.

    On the contrary, to create such a file, we must run the following command on the project's main folder route and while the environment is active:
    
    ```bash
    pip freeze > requirements.txt
    ```
    
    This will create a file called "requirements.txt" on the project's main folder which contains all the libraries and packages installed through `pip` in the environment that is currently active (the one we previously named `env`).

    Also, the following command will give us a list of all the dependencies that are currently found within the active environment:

    ```bash
    pip freeze
    ```

5. Deactivate the environment when finished.

    Run the `deactivate.bat` file located inside the `\Scripts` folder:

    ```bash
    env\Scripts\deactivate.bat
    ```
