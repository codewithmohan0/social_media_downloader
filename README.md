# 📥 Social Media Video Downloader Bot (Flask + Ngrok)

A full-featured web app to download videos or photos from **YouTube, TikTok, Instagram, Facebook** via public URLs. Mobile-friendly, fast, and tracks download history.

## 🚀 Features

- ✅ Supports YouTube, Instagram, TikTok, Facebook
- ✅ Flask web app with Ngrok integration for mobile
- ✅ Clean responsive UI with CSS
- ✅ Tracks download history
- ✅ Works on Android via Termux

## 📦 Requirements

```
pip install flask flask-ngrok yt-dlp
```

## 🖥️ Run on Desktop

```bash
python app.py
```

## 📱 Run on Android (Termux)

```bash
pkg update && pkg install python
pip install flask flask-ngrok yt-dlp
cd social_media_downloader
python app.py
```

Ngrok will give you a public link to open in your browser.

## 🗂️ Project Structure

- `app.py` - Flask app runner
- `download.py` - Download logic using yt-dlp
- `templates/` - HTML pages
- `static/style.css` - Styling
- `history.json` - Download history
