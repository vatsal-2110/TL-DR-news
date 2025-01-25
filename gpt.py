from flask import Flask, request, render_template

app = Flask(__name__)

# Home route to render the input form
@app.route('/')
def home():
    return '''
    <h1>Number Input App</h1>
    <form action="/process" method="post">
        <label for="number">Enter a number:</label>
        <input type="number" id="number" name="number" required>
        <button type="submit">Submit</button>
    </form>
    '''

# Route to process the input and display the result
@app.route('/process', methods=['POST'])
def process():
    number = request.form['number']
    return f'''
    <h1>You entered: {number}</h1>
    <a href="/">Go Back</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)