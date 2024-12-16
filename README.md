# FastAPI Product API

This is a FastAPI-based REST API for managing products. It allows creating,
reading, updating, and deleting products with validation and constraints.

---

## Requirements

Make sure you have the following installed:

- Python 3.8 or higher
- pip

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Bogdan-Rylov/test-task-1.git
   cd test-task-1
   ```

2. Install dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    alembic upgrade head
    ```

4. Run the development server:
    ```bash
    uvicorn main:app --reload
    ```

## Postman Collection

You can import the [Postman Collection](./postman_collection.json) to easily test the API endpoints.

To import the collection in Postman:
1. Open Postman.
2. Click on the "Import" button in the top left corner.
3. Select the "Link" tab and paste the link to the collection JSON file or import the downloaded file directly.
