from mira_sdk import MiraClient, Flow
import os
from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

# Home route to render the input form
@app.route('/')
def home():
    print("Kaam Chalu h")
    # api_key = os.getenv("my_API_KEY")
    api_key ='sb-d8a0e3d0fbafb3ff3c64d1872c3e0a34'

    client = MiraClient(config={"API_KEY": api_key})     # Initialize Mira Client
    # print(api_key)
    # Basic test
    flow = Flow(source="./flow.yaml")                    # Load flow configuration
    category = request.args.get('category', '')  # Default to an empty string if not provided
    number = request.args.get('number', '')
    category = str(category)
    number  = str(number)
    input_dict = {"category": category,"number":number}
    response = client.flow.test(flow, input_dict)
    print("Kaam ho gya")
    return response

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# Route to process the input and display the result
# @app.route('/process', methods=['POST'])
# def process():
#     number = request.form['number']
#     return f'''
#     <h1>You entered: {number}</h1>
#     <a href="/">Go Back</a>
#     '''

if __name__ == '__main__':
    app.run(debug=True)