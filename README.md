# A working example of a REST API using Flask and SQLAlchemy

## Create and activate virtual environment using the `virtualenv` tool

1. Install `virtualenv` through the CMD.

    ```bash
    pip install virtualenv
    ```

    If you're in an active virtual environment, `pip` installs the dependency into that environment. Otherwise, it installs it globally on your system.

2. Create a virtual environment inside the project folder.

    ```bash
    python -m virtualenv env
    ```

    `env` is the name of the environment as well as the name of the folder in which the environment is built. Calling this folder `env` is a convention, but any other name can be used.

    The `-m` flag is a command-line option that allows you to run a module as a script. This means you can execute Python code directly from the command line without the need for an external script file. Basically, we're activating Python first and then we're using the `virtualenv` tool.

    Since virtual environments are not portable, it typically does not make sense to commit them for others to use. Hence why `virtualenv` automatically generates a `.gitignore` file inside the `env` folder. This text file only contains a `*` character, meaning that the whole `env` folder will get omitted when comitting changes.

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

    As mentioned above, environments are not portable, so the best tool for other developers to work under the same conditions that your project was developed in is to provide this text file including all libraries and its versions.

    Also, the following command will give us a list of all the dependencies that are currently found within the active environment:

    ```bash
    pip freeze
    ```

5. Deactivate the environment when finished.

    Run the `deactivate.bat` file located inside the `\Scripts` folder:

    ```bash
    env\Scripts\deactivate.bat
    ```

-------------------

## Launch the project

1. To create the database, run the `create_sql_db.py` script from the cmd on the same route that this file is stored by executing this command on the cmd:

    ```bash
    python create_sql_db.py
    ```
    
    This only needs to be done if the database does not exist.

    Running `application.py` without running `create_sql_db.py` first will not work.

2. To start the Flask server, run these commands in cmd to create environment variables (this needs to be done every time the cmd is closed):

    ```bash
    set FLASK_APP=application.py
    set FLASK_ENV=development
    ```

    Then run:

    ```bash
    flask run
    ```

    This will return the port where the website is running. Copy the URL into a web browser to check the API responses.


---
Created by: @pau-arandia