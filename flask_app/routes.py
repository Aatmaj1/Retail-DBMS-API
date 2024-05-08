from flask import request
from flask import jsonify,make_response
from flask import Flask
from utils import *

# Initialize Flask application
app = Flask(__name__)
app.debug = True # Set to True for debugging during development, false in production
port = 6005  # Port where the Flask app will run
 
 
@app.route('/orderHistory', methods = ['POST'])
def get_order_history():
    """
    Route to retrieve order history based on customer email or telephone.
    Expects data to be POSTed with 'data' and 'type' fields where type can be 'email' or 'telephone'.
    """
    data = request.form["data"]
    type = request.form["type"]

    # Call order_history from utils based on the input type
    if type == "telephone":
        resp = order_history(customers_email = None, customer_telephone = data)
    elif type == "email":
        resp = order_history(customers_email = data, customer_telephone = None)
    else:
        # Return error response for bad request
        return make_response(jsonify({"Error":"Bad Request"}), 400)
    
    return make_response(jsonify(resp), 200)
 
@app.route('/ordersByBilling', methods = ['POST'])
def get_orders_by_billing():
    """
    Route to fetch orders sorted by billing zip codes.
    Expects a POST request with 'data' field that should be either 'True' or 'False' indicating ascending order.
    """
    value = request.form["data"]
    
    # Fetch and return the orders by billing depending on the boolean value of 'data'
    if value == 'True' :
        resp = get_orders_by_billing_zip_codes(True)
    elif value == 'False':
        resp = get_orders_by_billing_zip_codes(False)
    else:
        # Return error response for bad request
        return make_response(jsonify({"Error":"Bad Request"}), 400)
    
    return make_response(jsonify(resp), 200)

@app.route('/ordersByShipping', methods = ['POST'])
def get_orders_by_shipping():
    """
    Route to fetch orders sorted by shipping zip codes.
    Expects a POST request with 'data' field that should be either 'True' or 'False' indicating ascending order.
    """
    value = request.form["data"]
    
    if value == 'True' :
        resp = get_orders_by_shipping_zip_codes(True)
    elif value == 'False':
        resp = get_orders_by_shipping_zip_codes(False)
    else:
        return make_response(jsonify({"Error":"Bad Request"}), 400)
    
    return make_response(jsonify(resp), 200)

@app.route('/peakHour', methods = ['POST'])
def get_peak_hour():
    """
    Route to find the hour of the day with the most purchases.
    Does not expect any data to be POSTed.
    """
    resp = get_hour_most_purchases()
    return make_response(jsonify(resp), 200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port = port)
