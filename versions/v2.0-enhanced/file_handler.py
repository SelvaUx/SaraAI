import os, shutil, pyautogui

def list_files(path="."):
    for f in os.listdir(path):
        print(f)

def delete_file(file_path):
    try:
        os.remove(file_path)
        print("Deleted", file_path)
    except Exception as e:
        print(e)

def move_file(src, dst):
    try:
        shutil.move(src, dst)
        print("Moved", src, "to", dst)
    except Exception as e:
        print(e)