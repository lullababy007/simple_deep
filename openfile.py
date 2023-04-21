import os
import subprocess

file_path = r"C:\Users\a\Desktop\쿨러LCD\6feFil.gif"  # 이미지 파일의 경로를 지정하세요

try:
    os.startfile(file_path)
except AttributeError:
    subprocess.run(["xdg-open", file_path])