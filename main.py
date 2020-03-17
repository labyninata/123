import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "пандемия коронавируса. на 17.03.20 185 067 случаев. 7330 смертей"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

