import os
import shutil
from datetime import datetime

# Source folder (change this)
source = r"C:\Users\Deepan\Documents\project_files"

# Destination folder (change this)
backup_root = r"C:\Users\Deepan\Documents\Backups"

# Create a backup folder with today’s date
today = datetime.now().strftime("%Y-%m-%d")
backup_folder = os.path.join(backup_root, f"backup_{today}")

# Create folder if not exists
os.makedirs(backup_folder, exist_ok=True)

# Copy all files and folders
for item in os.listdir(source):
    src_path = os.path.join(source, item)
    dst_path = os.path.join(backup_folder, item)
    if os.path.isdir(src_path):
        shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
    else:
        shutil.copy2(src_path, dst_path)

print(f"✅ Backup completed successfully: {backup_folder}")
