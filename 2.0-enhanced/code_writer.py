import os, pyautogui, time

TEMPLATES = {
    "login": '''<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
  <h2>Login Page</h2>
  <form>
    <input type="text" placeholder="Username"><br>
    <input type="password" placeholder="Password"><br>
    <button>Login</button>
  </form>
</body>
</html>''',
    "hello python": "print('Hello, world!')",
    "cpp main": '''#include <iostream>
int main() {
    std::cout << "Hello from C++";
    return 0;
}'''
}

def write_code(snippet_key="hello python"):
    """Opens Notepad and types the chosen snippet."""
    pyautogui.hotkey('win')
    time.sleep(0.5)
    pyautogui.write("notepad")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1.5)
    template = TEMPLATES.get(snippet_key.lower(), snippet_key)
    pyautogui.write(template, interval=0.02)

def create_project(name):
    path = os.path.join(os.path.expanduser("~\\Desktop"), name)
    os.makedirs(path, exist_ok=True)
    os.startfile(path)