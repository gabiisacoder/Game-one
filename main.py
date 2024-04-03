from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Flask project!'

@app.route('/about')
def about():
    return 'This is a simple Flask project.'

@app.route('/contact')
def contact():
    return 'You can contact us at example@example.com.'

if __name__ == '__main__':
    app.run(debug=True)