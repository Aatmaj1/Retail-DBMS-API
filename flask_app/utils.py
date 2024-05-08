
# Importing database utility modules and pandas for data handling.
from posgresql_util import pgdao
from posgresql_util import psycopg2

import pandas as pd

# Connection dictionary containing credentials and details for PostgreSQL connection.

conn_dict = {
    'host':'localhost' ,
    'port' :'5432', 
    'database' :'your_db_name' ,
    'user':'your_username', 
    'password':'your_password'}

def order_history(customers_email = None, customer_telephone = None,):
    # Initialize a database access object.
    p1 = pgdao(conn_dict)

    # SQL query to retrieve order details based on either customer email or telephone.
    order_query = """
                    SELECT 
                      c.email
                    , c.telephone
                    , concat(c.first_name, ' ' ,c.last_name) as CUSTOMER_NAME
                    , o.order_id
                    , ol.product_id
                    , ba.street                        as BILLING_STREET
                    , ba.city                          as BILLING_CITY
                    , ba.state                         as BILLING_STATE
                    , ba.zip_code                      as BILLING_ZIP_CODE
                    , ba.address_type                  as BILLING_ADD_TYPE
                    , sa.street                        as SHIPPING_STREET
                    , sa.city                          as SHIPPING_CITY
                    , sa.state                         as SHIPPING_STATE
                    , sa.zip_code                      as SHIPPING_ZIP_CODE
                    , sa.address_type                  as SHIPPING_ADD_TYPE
                    
                    FROM orders            as o
                    
                    JOIN orders_lines      as ol 
                        ON o.order_id = ol.order_id
                    JOIN addresses         as ba 
                        ON o.billing_address_id = ba.address_id
                    JOIN addresses         as sa 
                        ON ol.shipment_address_id = sa.address_id
                    JOIN customers         as c 
                        ON c.customer_id = o.customer_id
    """
    customers_email_clause = "WHERE c.email = :customer_email"
    customers_phone_clause = "WHERE c.telephone = :customer_phone"
    
    # Handling no input scenario.
    if not customers_email and not customer_telephone:
        return {'result' : {},
               'success_code' : 0}
    
    # Fetch results based on email or telephone.
    if customers_email:
        result = p1.query(order_query + customers_email_clause, {'customer_email' : customers_email})
    else:
        result = p1.query(order_query + customers_phone_clause, {'customer_phone' : customer_telephone})
    
    # Returning a dictionary containing the query results and a success code.
    return {'result' : result.to_dict(orient = 'index'),
            'success_code' : 1}

def get_orders_by_billing_zip_codes(ascending = False):

    # Initialize a database access object and perform query.
    p1 = pgdao(conn_dict)

    order_query = """
                    SELECT 
                      ba.zip_code as ZIP_CODE
                    , COUNT(o.order_id) as ORDER_COUNT
                    
                    FROM orders as o
                    
                    JOIN addresses as ba 
                        ON o.billing_address_id = ba.address_id
                    GROUP BY ba.zip_code
    """
    
    
    result = p1.query(order_query)
    
    # Sort and convert result to dictionary.
    return {'result' : list(result.sort_values(by = 'ORDER_COUNT', ascending = ascending).to_dict(orient = 'index').values()),
           'success_code': 1}

def get_orders_by_shipping_zip_codes(ascending = False):
    
    # Similar to billing, this function retrieves and sorts orders by shipping zip code.
    p1 = pgdao(conn_dict)

    order_query = """
                    SELECT 
                      sa.zip_code as zip_code
                    , COUNT(DISTINCT o.order_id) as order_count
                    
                    FROM orders as o
                    
                    JOIN orders_lines as ol 
                        ON ol.order_id = o.order_id
                    JOIN addresses AS sa 
                        ON ol.shipment_address_id = sa.address_id
                    GROUP BY sa.zip_code
    """
    
    result = p1.query(order_query)
    return {'result' : list(result.sort_values(by = 'ORDER_COUNT', ascending = ascending).to_dict(orient = 'index').values()),
           'success_code': 1}


def get_hour_most_purchases():
    
    # Query to find the hour with the most purchases.
    p1 = pgdao(conn_dict)

    order_query = """
                    SELECT 
                      o.order_date
                    , o.order_id
                    
                    FROM orders AS o
                    
                    WHERE o.order_type = 'in-store'
    """
    result = p1.query(order_query)
    # Convert ORDER_DATE to datetime and extract the hour, then group by hour and count orders.
    result['ORDER_DATE'] = pd.to_datetime(result['ORDER_DATE'])
    result['ORDER_HOUR'] = result['ORDER_DATE'].dt.hour
    result_gb = result.groupby('ORDER_HOUR', as_index = False)['ORDER_ID'].count()
    result_gb = result_gb.sort_values('ORDER_ID', ascending = False)
    # Return the hour with the highest number of purchases.
    return {'result' : str(result_gb.iloc[0,0]),
           'success_code' : 1}
