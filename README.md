# Appium Test Project

## Setup
1. Install the required Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Set up the Appium server and ensure it is running at `http://localhost:4723/wd/hub`.

3. Create a `.env` file in the root directory with the following content:
    ```env
    APPIUM_SERVER_URL=http://localhost:4723/wd/hub
    APP_PACKAGE=com.gtschoolapp
4.On the line 23 of main.py change the email and password and username to test a different one and the function either signup or logging as this templates 
    login_page.logging_in("example@gmail.com", "password")
    login_page.signing_up("example@gmail.com", "Password"," username")
    ```

## Running Tests
Execute the main script to run the test:
    ```bash
    python src/main.py
    ```

## Project Structure
