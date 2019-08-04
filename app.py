from flask import Flask

app = Flask(__name__)

@app.route("/hook1", strict_slashes=False, methods=['GET'])
def hook1():

   return "hook1 complete"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

