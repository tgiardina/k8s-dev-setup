from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_root():
    return 'Hi, I\'m the app'
    # return 'Whoa, the app has changed'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
