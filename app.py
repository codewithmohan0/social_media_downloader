from flask import Flask, request, render_template, send_file, redirect, url_for
import os
from downloader import download_media
from utils import save_history, load_history
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

DOWNLOAD_DIR = "downloads"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        result = download_media(url, DOWNLOAD_DIR)
        if result["status"] == "success":
            save_history(result)
            return render_template("index.html", result=result)
        else:
            return render_template("index.html", error=result["msg"])
    return render_template("index.html")

@app.route("/history")
def history():
    history_list = load_history()
    return render_template("history.html", history=history_list)

@app.route("/download/<filename>")
def download_file(filename):
    file_path = os.path.join(DOWNLOAD_DIR, filename)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    app.run()
