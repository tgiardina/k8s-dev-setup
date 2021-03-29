from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_root():
    return 'Bleep bloop, I\'m the api'
    # return 'Boom! The api has changed!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
