# Fast-api-Example

# FastAPI Crash Course

Welcome to the FastAPI Crash Course ! This guide will help you set up and build a simple FastAPI application, useful for real-time machine learning projects.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setting Up the Environment](#setting-up-the-environment)
3. [Creating the FastAPI Application](#creating-the-fastapi-application)
4. [Running the Application](#running-the-application)
5. [Interactive API Documentation](#interactive-api-documentation)
6. [Additional Information](#additional-information)

## Prerequisites

- Python 3.10
- Conda (for creating virtual environments)
- A terminal or command line interface
- `requirements.txt` file with necessary dependencies

## Setting Up the Environment

1. **Create a Virtual Environment:**
    ```bash
    conda create -n fastapi-env python=3.10
    ```
    Confirm the creation by typing `y`.

2. **Activate the Virtual Environment:**
    ```bash
    conda activate fastapi-env
    ```

3. **Install Dependencies:**
    Ensure you are in the directory containing `requirements.txt`, then run:
    ```bash
    pip install -r requirements.txt
    ```

## Creating the FastAPI Application

1. **Create a Python Script:**
    Create a file named `main.py` with the following content:

    ```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello world from FastAPI"}

    @app.get("/demo")
    def demo_function():
        return {"message": "This is output from demo function"}

    @app.post("/post_demo")
    def demo_post():
        return {"message": "This is output from post demo function"}
    ```

## Running the Application

1. **Start the Uvicorn Server:**
    Run the following command to start the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

2. **Access the Application:**
    Open your browser and navigate to `http://127.0.0.1:8000`. You should see the message:
    ```json
    {
        "message": "Hello world from FastAPI"
    }
    ```

## Interactive API Documentation

FastAPI automatically generates interactive API documentation. You can access it using Swagger UI or ReDoc.

1. **Swagger UI:**
    Navigate to `http://127.0.0.1:8000/docs` to see the Swagger UI interactive documentation.

2. **ReDoc:**
    Navigate to `http://127.0.0.1:8000/redoc` to see the ReDoc interactive documentation.

## Additional Information

### HTTP Methods Supported

- **GET**: Fetches data from the server.
- **POST**: Sends data to the server.
- **PUT**: Updates existing data on the server.
- **DELETE**: Deletes data from the server.

### Decorators

- **@app.get("/path")**: Handles GET requests.
- **@app.post("/path")**: Handles POST requests.
- **@app.put("/path")**: Handles PUT requests.
- **@app.delete("/path")**: Handles DELETE requests.

### Error Handling

Ensure you handle errors and exceptions appropriately in your application to maintain robustness and reliability.

### Testing with Postman

1. **GET Request:**
    - URL: `http://127.0.0.1:8000/demo`
    - Expected Output:
      ```json
      {
          "message": "This is output from demo function"
      }
      ```

2. **POST Request:**
    - URL: `http://127.0.0.1:8000/post_demo`
    - Expected Output:
      ```json
      {
          "message": "This is output from post demo function"
      }
      ```

For further details, refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).

---

Happy coding! Enjoy building your FastAPI applications for MLOps projects.