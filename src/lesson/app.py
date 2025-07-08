from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_lesson():
    return "<p> Hello from Lesson! </p>"

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)
