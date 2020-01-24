from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
#export FLASK_APP=flask_example.py

# Run the the Command line
    #set FLASK_APP="flask_example.py"
    #flask run
if __name__ == "__main__":
    app.run()