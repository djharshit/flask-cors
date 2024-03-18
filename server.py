from flask import Flask, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="assets", static_url_path="/assets")

CORS(app)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    # Check if the path is for a file (e.g., .js, .css, .png, etc.)
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    # For any other routes, serve index.html
    return send_from_directory(".", "index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
