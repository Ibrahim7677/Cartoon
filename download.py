# download.py
import os
import requests

url = "https://github.com/TencentARC/GFPGAN/releases/download/v1.3.8/GFPGANv1.3.pth"
os.makedirs("gfpgan/weights", exist_ok=True)
r = requests.get(url, allow_redirects=True)
with open("gfpgan/weights/GFPGANv1.3.pth", "wb") as f:
    f.write(r.content)
