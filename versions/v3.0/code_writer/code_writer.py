#!/usr/bin/env python3
"""
Sara AI Code Writer
Generates code templates and writes code to files using automation
"""

import os
import time
import logging
import pyautogui
from typing import Dict, Optional

class CodeWriter:
    def __init__(self):
        """Initialize code writer"""
        self.logger = logging.getLogger('CodeWriter')
        
        # Code templates
        self.code_templates = self.load_code_templates()
        
        # Automation settings
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.3
        
        print("💻 Code Writer initialized")
        
    def load_code_templates(self) -> Dict:
        """Load code templates for different languages"""
        return {
            "html": {
                "login": '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .login-container {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        .form-group {
            margin-bottom: 1rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-sizing: border-box;
        }
        .login-btn {
            width: 100%;
            padding: 0.75rem;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
        }
        .login-btn:hover {
            background: #5a6fd8;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2 style="text-align: center; margin-bottom: 1.5rem;">Login</h2>
        <form>
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit" class="login-btn">Login</button>
        </form>
    </div>
</body>
</html>''',
                "signup": '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .signup-container {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 350px;
        }
        .form-group {
            margin-bottom: 1rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
        }
        input {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-sizing: border-box;
        }
        .signup-btn {
            width: 100%;
            padding: 0.75rem;
            background: #764ba2;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
        }
    </style>
</head>
<body>
    <div class="signup-container">
        <h2 style="text-align: center;">Sign Up</h2>
        <form>
            <div class="form-group">
                <label for="fullname">Full Name:</label>
                <input type="text" id="fullname" name="fullname" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit" class="signup-btn">Sign Up</button>
        </form>
    </div>
</body>
</html>'''
            },
            "python": {
                "hello_world": '''#!/usr/bin/env python3
"""
Hello World Program
"""

def main():
    print("Hello, World!")
    print("Welcome to Python programming!")
    
    # Get user input
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")

if __name__ == "__main__":
    main()''',
                "calculator": '''#!/usr/bin/env python3
"""
Simple Calculator Program
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()'''
            },
            "cpp": {
                "hello_world": '''#include <iostream>
#include <string>

int main() {
    std::cout << "Hello, World!" << std::endl;
    std::cout << "Welcome to C++ programming!" << std::endl;
    
    std::string name;
    std::cout << "What's your name? ";
    std::getline(std::cin, name);
    
    std::cout << "Nice to meet you, " << name << "!" << std::endl;
    
    return 0;
}''',
                "calculator": '''#include <iostream>

double add(double x, double y) {
    return x + y;
}

double subtract(double x, double y) {
    return x - y;
}

double multiply(double x, double y) {
    return x * y;
}

double divide(double x, double y) {
    if (y != 0) {
        return x / y;
    } else {
        std::cout << "Error: Division by zero!" << std::endl;
        return 0;
    }
}

int main() {
    std::cout << "Simple Calculator" << std::endl;
    std::cout << "Select operation:" << std::endl;
    std::cout << "1. Add" << std::endl;
    std::cout << "2. Subtract" << std::endl;
    std::cout << "3. Multiply" << std::endl;
    std::cout << "4. Divide" << std::endl;
    
    int choice;
    double num1, num2;
    
    std::cout << "Enter choice (1/2/3/4): ";
    std::cin >> choice;
    
    std::cout << "Enter first number: ";
    std::cin >> num1;
    
    std::cout << "Enter second number: ";
    std::cin >> num2;
    
    switch(choice) {
        case 1:
            std::cout << "Result: " << add(num1, num2) << std::endl;
            break;
        case 2:
            std::cout << "Result: " << subtract(num1, num2) << std::endl;
            break;
        case 3:
            std::cout << "Result: " << multiply(num1, num2) << std::endl;
            break;
        case 4:
            std::cout << "Result: " << divide(num1, num2) << std::endl;
            break;
        default:
            std::cout << "Invalid choice!" << std::endl;
    }
    
    return 0;
}'''
            },
            "java": {
                "hello_world": '''import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
        System.out.println("Welcome to Java programming!");
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("What's your name? ");
        String name = scanner.nextLine();
        
        System.out.println("Nice to meet you, " + name + "!");
        
        scanner.close();
    }
}'''
            }
        }
        
    def open_notepad(self) -> bool:
        """Open Notepad via Windows search"""
        try:
            self.logger.info("Opening Notepad")
            
            # Press Windows key
            pyautogui.press('win')
            time.sleep(1)
            
            # Type notepad
            pyautogui.type('notepad')
            time.sleep(1)
            
            # Press Enter
            pyautogui.press('enter')
            time.sleep(2)  # Wait for Notepad to open
            
            self.logger.info("Notepad opened successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening Notepad: {e}")
            return False
            
    def type_code(self, code: str) -> bool:
        """Type code into the active window"""
        try:
            self.logger.info("Typing code...")
            
            # Type the code with appropriate pauses
            lines = code.split('\n')
            
            for line in lines:
                pyautogui.type(line)
                pyautogui.press('enter')
                time.sleep(0.1)  # Small delay between lines
                
            self.logger.info("Code typed successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error typing code: {e}")
            return False
            
    def create_code_template(self, code_type: str, template_name: str = None) -> bool:
        """Create code template in Notepad"""
        try:
            self.logger.info(f"Creating {code_type} code template")
            
            # Determine language and template
            language = code_type.lower()
            if not template_name:
                # Default templates
                if language in ['html', 'web']:
                    template_name = 'login'
                    language = 'html'
                elif language in ['python', 'py']:
                    template_name = 'hello_world'
                    language = 'python'
                elif language in ['cpp', 'c++']:
                    template_name = 'hello_world'
                    language = 'cpp'
                elif language in ['java']:
                    template_name = 'hello_world'
                    language = 'java'
                else:
                    language = 'python'
                    template_name = 'hello_world'
                    
            # Get template code
            if language in self.code_templates and template_name in self.code_templates[language]:
                code = self.code_templates[language][template_name]
            else:
                self.logger.warning(f"Template not found: {language}/{template_name}")
                return False
                
            # Open Notepad
            if not self.open_notepad():
                return False
                
            # Type the code
            return self.type_code(code)
            
        except Exception as e:
            self.logger.error(f"Error creating code template: {e}")
            return False
            
    def write_custom_code(self, code_text: str) -> bool:
        """Write custom code to Notepad"""
        try:
            self.logger.info("Writing custom code")
            
            # Open Notepad
            if not self.open_notepad():
                return False
                
            # Type the custom code
            return self.type_code(code_text)
            
        except Exception as e:
            self.logger.error(f"Error writing custom code: {e}")
            return False
            
    def save_file(self, filename: str = None) -> bool:
        """Save the current file"""
        try:
            # Ctrl+S to save
            pyautogui.hotkey('ctrl', 's')
            time.sleep(1)
            
            if filename:
                # Type filename
                pyautogui.type(filename)
                time.sleep(0.5)
                
            # Press Enter to save
            pyautogui.press('enter')
            time.sleep(1)
            
            self.logger.info(f"File saved: {filename or 'default'}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error saving file: {e}")
            return False
            
    def create_and_save_code(self, code_type: str, filename: str = None, template_name: str = None) -> bool:
        """Create code template and save it"""
        try:
            # Create the code template
            if not self.create_code_template(code_type, template_name):
                return False
                
            time.sleep(1)
            
            # Save the file
            if not filename:
                extension_map = {
                    'html': '.html',
                    'python': '.py',
                    'cpp': '.cpp',
                    'java': '.java'
                }
                ext = extension_map.get(code_type.lower(), '.txt')
                filename = f"sara_generated_code{ext}"
                
            return self.save_file(filename)
            
        except Exception as e:
            self.logger.error(f"Error creating and saving code: {e}")
            return False
            
    def open_vs_code(self) -> bool:
        """Open Visual Studio Code"""
        try:
            self.logger.info("Opening Visual Studio Code")
            
            # Press Windows key
            pyautogui.press('win')
            time.sleep(1)
            
            # Type VS Code
            pyautogui.type('visual studio code')
            time.sleep(1)
            
            # Press Enter
            pyautogui.press('enter')
            time.sleep(3)  # Wait for VS Code to load
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening VS Code: {e}")
            return False

def main():
    """Test code writer"""
    writer = CodeWriter()
    
    # Test creating HTML login page
    print("Creating HTML login page...")
    writer.create_code_template('html', 'login')
    
    time.sleep(5)
    
    # Test saving
    print("Saving file...")
    writer.save_file('login_page.html')

if __name__ == "__main__":
    main()
