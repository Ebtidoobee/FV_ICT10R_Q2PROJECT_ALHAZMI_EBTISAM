from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def index():
    # Renders the 'index.html' template
    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    # Set debug=True for easier development/testing
    app.run(debug=True)

