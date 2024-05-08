
# Retail DBMS API

## Overview
This repository contains the code for a Retail Database Management System (DBMS) API. The system integrates a PostgreSQL database with a Python Flask backend to manage and analyze retail data. It includes utility scripts, database management, API routes, and testing functionalities.

## Getting Started

### Prerequisites

- Python 3.x
- PostgreSQL
- Flask

### Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Aatmaj1/Take-home-test.git
   cd Take-home-test
   ```

2. **Environment Setup**
   - It is recommended to use a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - Install required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Database Configuration**
   
   **Setup Postgres Database** : Before you begin, ensure you have Docker installed on your machine. If you don't have Docker installed, you can download and install Docker Desktop from [Docker's official website](https://www.docker.com/products/docker-desktop).
Please go through the link,it provides a detail way to setup Postgres in your system. [Postgresql Setup Link](https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/)
   - Ensure PostgreSQL is installed and running on your system.
   - Create a new database and user as needed.
   
   **posgresql_util.py** : Python module defines the pgdao class for PostgreSQL database management. It handles database connections, manages cursors, and executes SQL queries. 
Features include initializing and maintaining database connections, changing databases, and executing parameterized queries. It supports rolling back transactions to maintain consistency and offers methods to execute queries and fetch results in batches, 
ideal for large datasets. Utility functions assist in query building and execution, 
providing options for dry runs and debug outputs, enhancing the robustness and flexibility for database operations in Python.
   - Modify the `posgresql_util.py` file with your database connection settings.

4.  **Database Setup And Management Notebook**

- **Retail DBMS.ipynb** provide postgressql credentials connection details under create_connection()
- Insert functions are built that help to insert values into each table.
- **execute()** : Main function to manage database operations.It does end to end table creation and data insertion.
- Run the entire jupyter notebook with proper connection details as required.

   **Retail DBMS.ipynb** : Jupyter notebook manages a retail database using PostgreSQL. It includes functions to establish database connections, create necessary tables (customers, addresses, orders, order lines), and insert initial data. It also manages data integrity through foreign key constraints and includes utilities for updating and deleting records. This foundational tool is designed for robust database management, facilitating data entry, updates, and ensuring relational links between different data entities in a retail business setting.


5. **Running the Application**
   - Start the Flask application:
     ```bash
     python flask_app/routes.py 
     ```

### API Usage
1. The API is accessible via `http://127.0.0.1:[Port-Number]` once the Flask server is running.
2. API answer the following questions:
* Given a customer’s email or telephone, provide an order history functionality.
  * List all orders, and any billing or shipping addresses.
* Analytics:
  * Show a total count of orders aggregated by billing zip code, descending or
ascending.
  * Show a total count of orders aggregated by shipping zip code, descending or
ascending.
* Can you tell me what times of day most in-store purchases are made?
  * Detailed API endpoints and their usage can be found in the `routes.py` file.

## Testing
- Run the tests using:
  ```bash
  pytest test-flask-API/test_api.py
  ```
## Example API Functionalities
- Here is an example of a JSON response from the API calls:
  * Given a customer’s email or telephone, provide an order history functionality -> API call : http://127.0.0.1:6008/orderHistory?data=8378139380&type=telephone
``` json
{
    "result": {
        "0": {
            "BILLING_ADD_TYPE": "home",
            "BILLING_CITY": "Smalltown",
            "BILLING_STATE": "CA",
            "BILLING_STREET": "1267 Elf Street",
            "BILLING_ZIP_CODE": "12344",
            "CUSTOMER_NAME": "John Doe",
            "EMAIL": "john.doe@google.com",
            "ORDER_ID": 1,
            "PRODUCT_ID": 101,
            "SHIPPING_ADD_TYPE": "home",
            "SHIPPING_CITY": "Smalltown",
            "SHIPPING_STATE": "CA",
            "SHIPPING_STREET": "1267 Elf Street",
            "SHIPPING_ZIP_CODE": "12344",
            "TELEPHONE": "8378139380"
        },
        "1": {
            "BILLING_ADD_TYPE": "home",
            "BILLING_CITY": "Smalltown",
            "BILLING_STATE": "CA",
            "BILLING_STREET": "1267 Elf Street",
            "BILLING_ZIP_CODE": "12344",
            "CUSTOMER_NAME": "John Doe",
            "EMAIL": "john.doe@google.com",
            "ORDER_ID": 1,
            "PRODUCT_ID": 102,
            "SHIPPING_ADD_TYPE": "home",
            "SHIPPING_CITY": "Smalltown",
            "SHIPPING_STATE": "CA",
            "SHIPPING_STREET": "1234 Elm Street",
            "SHIPPING_ZIP_CODE": "12345",
            "TELEPHONE": "8378139380"
        },
        "2": {
            "BILLING_ADD_TYPE": "home",
            "BILLING_CITY": "Smalltown",
            "BILLING_STATE": "CA",
            "BILLING_STREET": "1234 Elm Street",
            "BILLING_ZIP_CODE": "12345",
            "CUSTOMER_NAME": "John Doe",
            "EMAIL": "john.doe@google.com",
            "ORDER_ID": 4,
            "PRODUCT_ID": 104,
            "SHIPPING_ADD_TYPE": "office",
            "SHIPPING_CITY": "Smalltown",
            "SHIPPING_STATE": "CA",
            "SHIPPING_STREET": "5678 Oak Street",
            "SHIPPING_ZIP_CODE": "12345",
            "TELEPHONE": "8378139380"
        }
    },
    "success_code": 1
}
```

* Show a total count of orders aggregated by billing zip code in ascending order -> API call : http://127.0.0.1:6009/ordersByBilling?data=True

```json
{
    "result": [
        {
            "ORDER_COUNT": 1,
            "ZIP_CODE": "12344"
        },
        {
            "ORDER_COUNT": 3,
            "ZIP_CODE": "12345"
        }
    ],
    "success_code": 1
}
```

* Show a total count of orders aggregated by shipping zip code, descending order -> API call : http://127.0.0.1:6009/ordersByShipping?data=False

```json
  {
    "result": [
        {
            "ORDER_COUNT": 2,
            "ZIP_CODE": "12345"
        },
        {
            "ORDER_COUNT": 2,
            "ZIP_CODE": "67890"
        },
        {
            "ORDER_COUNT": 1,
            "ZIP_CODE": "12344"
        }
    ],
    "success_code": 1
}
```

* Can you tell me what times of day most in-store purchases are made? -> API call : http://127.0.0.1:6005/peakHour

```json
{
    "result": "15",
    "success_code": 1
}
```

## Deploy Flask App :

We can deploy our Flask app on Amazon EC2 using Docker image of app. The following are simple steps you can take to deploy the app:
- First, create a Docker image of your Flask app
- Next, launch an EC2 instance, choosing an appropriate AMI and setting security groups to allow HTTP traffic
- Install Docker on the EC2 instance via SSH.
- Transfer the Docker image directly from your local machine to the EC2 instance
- Load and Run Docker Image on EC2
- Finally, access your application by navigating to the public IP address of your EC2 instance in a browser




