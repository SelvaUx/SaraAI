<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/90cc662e-4d05-4f0b-8e5f-62c074b0f54b" />


# **Sara AI**

Sara AI is an intelligent virtual assistant built with Python. It allows you to control applications, search for information, interact with various utilities, and provides a **Jarvis-like** speaking experience. This AI can also perform actions such as opening applications, taking screenshots, and answering questions using **Wikipedia**.

### **Features**:

* **Search Commands**: Search for queries in Google.
* **Open Application Commands**: Open applications via **Windows Search**.
* **Utility Commands**: Get the current **time**, **date**, or hear a **random joke**.
* **Screenshot Command**: Takes a screenshot and saves it in the **Pictures** folder.
* **Wikipedia Command**: Search Wikipedia and give a brief summary.
* **Text-to-Speech (TTS)**: Sara AI speaks commands in a professional **Jarvis-like** style.

### **Commands**:

1. **Search Commands**:

   * **"search \[query]"**: Searches for the query on **Google** in the default browser.

     * **Example**: `"search AI"`
   * **"open \[website]"**: Opens the specified website (e.g., **YouTube**) in the default browser.

     * **Example**: `"open youtube.com"`

2. **Open Application Commands**:

   * **"open \[application]"**: Opens the specified application via **Windows Search**.

     * **Example**: `"open notepad"`, `"open telegram"`, `"open chrome"`

3. **Utility Commands**:

   * **"time"**: Tells the current **time**.
   * **"date"**: Tells the current **date**.
   * **"joke"**: Tells a **random joke**.

4. **Screenshot Command**:

   * **"screenshot"**: Takes a **screenshot** and saves it in your **Pictures** folder.

5. **Wikipedia Command**:

   * **"wikipedia \[query]"**: Searches **Wikipedia** for the query and provides a summary.

     * **Example**: `"wikipedia Python programming"`

### **Installation**:

To get started with **Sara AI**, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/YourUsername/SaraAI.git
   cd SaraAI
   ```

2. **Install Dependencies**:
   Install the required dependencies using **pip**:

   ```bash
   pip install -r requirements.txt
   ```

   Dependencies include:

   * **`wikipedia`**: For Wikipedia search functionality.
   * **`pyttsx3`**: For Text-to-Speech (TTS).
   * **`pyautogui`**: For automating the opening of applications.
   * **`pyjokes`**: For telling random jokes.

3. **Ensure Python is Installed**:
   Ensure you have **Python 3.x** installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

4. **Run the Application**:
   Run **`main.py`** to start the AI:

   ```bash
   python main.py
   ```

5. **Interacting with the AI**:

   * You will be prompted to enter commands.
   * The AI will respond to your commands with **text-to-speech** feedback.

### **Commands Example**:

Here are some example commands you can try:

* **"search AI"**:

  * **Sara AI** will speak: **"Searching for AI in Google."** and perform a Google search for **AI**.

* **"open youtube"**:

  * **Sara AI** will speak: **"Opening youtube using Windows search."** and open **YouTube**.

* **"wikipedia Python programming"**:

  * **Sara AI** will search **Wikipedia** for **Python programming** and read a summary aloud.

* **"time"**:

  * **Sara AI** will speak: **"The current time is 12:30 PM."**

* **"date"**:

  * **Sara AI** will speak: **"The current date is 14th September 2025."**

* **"joke"**:

  * **Sara AI** will tell a **random joke**.

### **Key Features**:

* **Dynamic Speech**: **Sara AI** speaks in a **Jarvis-like** voice, making the interaction more engaging.
* **Application Control**: Opens any installed application using **Windows Search**.
* **Wikipedia Integration**: Search for information directly on **Wikipedia** and hear the summary.
* **Screenshot Functionality**: Easily take and save screenshots with a simple command.

### **How Sara AI Works**:

1. **Speech-to-Text**: The assistant listens to your commands using **speech recognition** and processes them.
2. **Application and Web Control**: It can open websites, search Google, open applications via Windows Search, and more.
3. **Text-to-Speech**: Once a command is executed, **Sara AI** speaks the action or result, providing real-time verbal feedback.

### **Troubleshooting**:

* If Sara AI is unable to find or open an application, make sure it’s correctly installed and appears in the **Windows Start Menu**.
* If speech is not working, make sure your audio device is properly configured and your **Python** environment has the required libraries installed.

---

### **Contributing**:

Feel free to fork the repository, make changes, and create pull requests. Contributions are always welcome!

### **License**:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
