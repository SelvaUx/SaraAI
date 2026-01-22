"""
Sara AI Max - Web GUI

A modern web-based interface that's guaranteed to work.
Uses Flask for the backend and HTML/CSS/JS for the frontend.
"""

from flask import Flask, render_template, request, jsonify
import asyncio
from threading import Thread
import webbrowser
from pathlib import Path

from sara_core.nlu import NLUEngine
from sara_core.planner import Planner
from sara_core.executor import Executor
from sara_core.security import SecurityManager
from sara_core.context import ContextManager

app = Flask(__name__)

# Initialize Sara components
context = ContextManager()
security = SecurityManager()
nlu = NLUEngine()
planner = Planner(security)
executor = Executor(security, context)


@app.route('/')
def index():
    """Serve the main page."""
    return render_template('index.html')


@app.route('/api/process', methods=['POST'])
def process_command():
    """Process a command."""
    try:
        data = request.json
        command = data.get('command', '')
        
        if not command:
            return jsonify({'success': False, 'error': 'No command provided'})
        
        # Create new event loop for this thread
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            # Parse intent
            intent = nlu.parse(command)
            
            # Create plan
            plan = planner.create_plan(intent)
            
            # Execute
            result = loop.run_until_complete(executor.execute(plan))
            
            return jsonify({
                'success': result.success,
                'message': result.message or ('Done!' if result.success else 'Error occurred'),
                'error': result.error
            })
        finally:
            loop.close()
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


def open_browser():
    """Open browser after a short delay."""
    import time
    time.sleep(1.5)
    webbrowser.open('http://127.0.0.1:5000')


if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    templates_dir = Path(__file__).parent / 'templates'
    templates_dir.mkdir(exist_ok=True)
    
    # Open browser in background
    Thread(target=open_browser, daemon=True).start()
    
    # Run Flask app
    print("🤖 Sara AI Max Web GUI starting...")
    print("🌐 Opening browser at http://127.0.0.1:5000")
    print("Press Ctrl+C to stop")
    
    app.run(debug=False, port=5000)
