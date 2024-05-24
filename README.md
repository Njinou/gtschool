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
    ```

## Running Tests
Execute the main script to run the test:
    ```bash
    python src/main.py
    ```

## Project Structure
