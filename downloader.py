import os
from yt_dlp import YoutubeDL

def get_platform(url: str) -> str:
    if "youtube.com" in url or "youtu.be" in url:
        return "youtube"
    elif "instagram.com" in url:
        return "instagram"
    elif "facebook.com" in url:
        return "facebook"
    elif "tiktok.com" in url:
        return "tiktok"
    else:
        return "unknown"

def download_media(url: str, output_dir: str = "downloads"):
    platform = get_platform(url)
    if platform == "unknown":
        return {"status": "error", "msg": "Unsupported platform"}

    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'quiet': True,
        'noplaylist': True,
        'format': 'best',
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url)
            return {
                "status": "success",
                "title": info.get("title"),
                "filepath": ydl.prepare_filename(info),
                "filename": os.path.basename(ydl.prepare_filename(info)),
                "platform": platform
            }
    except Exception as e:
        return {"status": "error", "msg": str(e)}
