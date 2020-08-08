from flask import Flask

app = Flask(__name__)
@app.route('/')
def main():
   return 'Hello, world!<br/>This endpoint is not yet configured to send any data, but it is alive!'
