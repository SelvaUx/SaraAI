"""
Sara AI Browser Controller
Handles web browsing, search, and navigation using automation
"""

import os
import time
import logging
import pyautogui
import webbrowser
from typing import Optional
import subprocess

class BrowserController:
    def __init__(self):
        """Initialize browser controller"""
        self.logger = logging.getLogger('BrowserController')
        
        # Browser settings
        self.default_browser = "chrome"
        self.search_engines = {
            "google": "https://www.google.com/search?q={}",
            "bing": "https://www.bing.com/search?q={}",
            "duckduckgo": "https://duckduckgo.com/?q={}"
        }
        self.default_search_engine = "google"
        
        # Automation settings
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.5
        
        print("🌐 Browser Controller initialized")
        
    def open_browser_via_search(self, browser_name: str = None) -> bool:
        """Open browser using Windows search"""
        try:
            if not browser_name:
                browser_name = self.default_browser
                
            self.logger.info(f"Opening {browser_name} via Windows search")
            
            # Press Windows key to open search
            pyautogui.press('win')
            time.sleep(1)
            
            # Type browser name
            pyautogui.type(browser_name)
            time.sleep(1)
            
            # Press Enter to open
            pyautogui.press('enter')
            time.sleep(3)  # Wait for browser to load
            
            self.logger.info(f"{browser_name} opened successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening browser: {e}")
            return False
            
    def search_and_open(self, query: str, search_engine: str = None) -> bool:
        """Search for query and open browser"""
        try:
            if not search_engine:
                search_engine = self.default_search_engine
                
            self.logger.info(f"Searching for: {query}")
            
            # Open browser first
            if not self.open_browser_via_search():
                return False
                
            # Wait for browser to fully load
            time.sleep(2)
            
            # Click on address bar (Ctrl+L)
            pyautogui.hotkey('ctrl', 'l')
            time.sleep(0.5)
            
            # Type search query
            search_url = self.search_engines[search_engine].format(query.replace(' ', '+'))
            pyautogui.type(search_url)
            time.sleep(0.5)
            
            # Press Enter to search
            pyautogui.press('enter')
            time.sleep(2)
            
            self.logger.info(f"Search completed for: {query}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error searching: {e}")
            return False
            
    def quick_search(self, query: str) -> bool:
        """Quick search using default browser and search engine"""
        try:
            self.logger.info(f"Quick search for: {query}")
            
            # Open browser
            if not self.open_browser_via_search():
                return False
                
            time.sleep(2)
            
            # Use Ctrl+K for search (works in most browsers)
            pyautogui.hotkey('ctrl', 'k')
            time.sleep(0.5)
            
            # Type search query
            pyautogui.type(query)
            time.sleep(0.5)
            
            # Press Enter
            pyautogui.press('enter')
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error in quick search: {e}")
            return False
            
    def open_website(self, url: str) -> bool:
        """Open specific website"""
        try:
            self.logger.info(f"Opening website: {url}")
            
            # Add https:// if not present
            if not url.startswith(('http://', 'https://')):
                url = f"https://{url}"
                
            # Open browser
            if not self.open_browser_via_search():
                return False
                
            time.sleep(2)
            
            # Click address bar
            pyautogui.hotkey('ctrl', 'l')
            time.sleep(0.5)
            
            # Type URL
            pyautogui.type(url)
            time.sleep(0.5)
            
            # Press Enter
            pyautogui.press('enter')
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening website: {e}")
            return False
            
    def youtube_search(self, query: str) -> bool:
        """Search and play video on YouTube"""
        try:
            self.logger.info(f"YouTube search for: {query}")
            
            youtube_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            
            if not self.open_website(youtube_url):
                return False
                
            time.sleep(3)  # Wait for YouTube to load
            
            # Try to click the first video (this is approximate)
            # Look for the first video thumbnail
            try:
                # This is a basic attempt - may need adjustment based on YouTube layout
                pyautogui.click(400, 300)  # Approximate location of first video
                self.logger.info("Clicked on first video")
            except Exception:
                self.logger.warning("Could not auto-click first video")
                
            return True
            
        except Exception as e:
            self.logger.error(f"Error with YouTube search: {e}")
            return False
            
    def close_browser(self) -> bool:
        """Close the current browser window"""
        try:
            pyautogui.hotkey('alt', 'f4')
            self.logger.info("Browser closed")
            return True
            
        except Exception as e:
            self.logger.error(f"Error closing browser: {e}")
            return False
            
    def new_tab(self) -> bool:
        """Open new tab in browser"""
        try:
            pyautogui.hotkey('ctrl', 't')
            self.logger.info("New tab opened")
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening new tab: {e}")
            return False
            
    def go_back(self) -> bool:
        """Go back in browser history"""
        try:
            pyautogui.hotkey('alt', 'left')
            self.logger.info("Navigated back")
            return True
            
        except Exception as e:
            self.logger.error(f"Error navigating back: {e}")
            return False
            
    def go_forward(self) -> bool:
        """Go forward in browser history"""
        try:
            pyautogui.hotkey('alt', 'right')
            self.logger.info("Navigated forward")
            return True
            
        except Exception as e:
            self.logger.error(f"Error navigating forward: {e}")
            return False
            
    def refresh_page(self) -> bool:
        """Refresh current page"""
        try:
            pyautogui.press('f5')
            self.logger.info("Page refreshed")
            return True
            
        except Exception as e:
            self.logger.error(f"Error refreshing page: {e}")
            return False
            
    def scroll_down(self, scrolls: int = 3) -> bool:
        """Scroll down on the page"""
        try:
            for _ in range(scrolls):
                pyautogui.scroll(-3)  # Negative for down
                time.sleep(0.2)
            
            self.logger.info(f"Scrolled down {scrolls} times")
            return True
            
        except Exception as e:
            self.logger.error(f"Error scrolling: {e}")
            return False
            
    def scroll_up(self, scrolls: int = 3) -> bool:
        """Scroll up on the page"""
        try:
            for _ in range(scrolls):
                pyautogui.scroll(3)  # Positive for up
                time.sleep(0.2)
            
            self.logger.info(f"Scrolled up {scrolls} times")
            return True
            
        except Exception as e:
            self.logger.error(f"Error scrolling: {e}")
            return False

def main():
    """Test browser controller"""
    browser = BrowserController()
    
    # Test opening browser
    print("Testing browser opening...")
    browser.open_browser_via_search()
    
    time.sleep(3)
    
    # Test search
    print("Testing search...")
    browser.search_and_open("Python programming tutorials")

if __name__ == "__main__":
    main()
