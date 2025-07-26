import subprocess

def list_tasks():
    subprocess.run(["tasklist"])

def kill_task(image_name):
    subprocess.run(["taskkill", "/IM", image_name, "/F"])