## Flask-Powered Retail Order Management System

The **routes.py** Flask application defines a REST API with routes to manage order data. It initializes with debugging enabled on port 6003.
The /orderHistory route retrieves customer order histories using email or telephone. The /ordersByBilling and /ordersByShipping routes sort
orders based on billing or shipping zip codes, respectively, with sort order controlled by a boolean input. The /peakHour route identifies 
the busiest purchasing hour with no input required. Errors are handled with a 400 status code and descriptive messages. The app uses 
utility functions from an external utils module for data operations.

The **utils.py** file contains utility functions for interacting with a PostgreSQL database, using modules like pgdao and pandas. 
It manages functions to fetch and process order data for a retail application, including retrieving order history, sorting orders 
by billing or shipping zip codes, and identifying peak purchasing hours. Each function prepares and executes SQL queries to extract
detailed data from linked tables, and returns results in structured formats. This module supports the API endpoints defined in the 
Flask application, ensuring robust data management and retrieval capabilities.
