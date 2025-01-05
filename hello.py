# Import flask
from flask import flask

#Creating flask application instance
app = Flask(__name__)

# Define route to serve "Hello, World!"
@app.route('/')

def hello_world():
    return "Hello, World! Welcome to my Flask app on AWS Elastic Beanstalk!"

# Run the app (for local development)
if __name__ == "__main__":
    app.run(debug=True)
