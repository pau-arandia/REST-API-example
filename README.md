# A working example of a REST API using Flask and SQLAlchemy

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
