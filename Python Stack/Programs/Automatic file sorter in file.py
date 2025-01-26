import os
import shutil

path = r"C:/My space/exp/"
file_names = os.listdir(path)
folder_names = ["pdf", "image", "audio", "video", "text", "exe"]

# Create folders if they don't exist
for folder in folder_names:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        print(f"Creating folder: {folder_path}")
        os.makedirs(folder_path)

# Move files into respective folders
for file in file_names:
    source = os.path.join(path, file)

    if file.endswith(".pdf"):
        destination = os.path.join(path, 'pdf', file)
    elif file.endswith((".jpg", ".png")):
        destination = os.path.join(path, 'image', file)
    elif file.endswith(".mp3"):
        destination = os.path.join(path, 'audio', file)
    elif file.endswith(".mp4"):
        destination = os.path.join(path, 'video', file)
    elif file.endswith(".txt"):
        destination = os.path.join(path, 'text', file)
    elif file.endswith(".exe"):
        destination = os.path.join(path, 'exe', file)
    else:
        continue  # Skip files with unknown extensions

    # Move the file if it doesn't already exist at the destination
    if not os.path.exists(destination):
        shutil.move(source, destination)
        print(f"Moved: {source} -> {destination}")
