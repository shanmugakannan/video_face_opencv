from flask import Flask
app = Flask(__name__)

port = int(os.environ.get("PORT", 33507))

@app.route("/")
def main():
    return "Upload video"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
