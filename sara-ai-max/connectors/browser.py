"""
Browser Controller - Playwright-based browser automation.

This module provides comprehensive browser control for Chrome, Firefox, and Edge.
"""

import logging
from typing import Optional, List
from contextlib import asynccontextmanager

logger = logging.getLogger(__name__)

try:
    from playwright.async_api import async_playwright, Browser, Page
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    logger.warning("Playwright not installed. Browser automation unavailable.")


class BrowserController:
    """Control web browsers using Playwright."""
    
    def __init__(self):
        """Initialize browser controller."""
        self.browser: Optional[Browser] = None
        self.page: Optional[Page] = None
        self.playwright = None
        
        if not PLAYWRIGHT_AVAILABLE:
            logger.error("Playwright not available. Install with: pip install playwright")
    
    async def start(self, browser_type: str = "chromium", headless: bool = False):
        """
        Start a browser instance.
        
        Args:
            browser_type: chromium, firefox, or webkit
            headless: Whether to run in headless mode
        """
        if not PLAYWRIGHT_AVAILABLE:
            raise ImportError("Playwright not installed")
        
        try:
            self.playwright = await async_playwright().start()
            
            if browser_type == "chromium":
                self.browser = await self.playwright.chromium.launch(headless=headless)
            elif browser_type == "firefox":
                self.browser = await self.playwright.firefox.launch(headless=headless)
            elif browser_type == "webkit":
                self.browser = await self.playwright.webkit.launch(headless=headless)
            else:
                raise ValueError(f"Unknown browser type: {browser_type}")
            
            self.page = await self.browser.new_page()
            logger.info(f"Started {browser_type} browser")
            
        except Exception as e:
            logger.error(f"Error starting browser: {e}")
            raise
    
    async def navigate(self, url: str):
        """Navigate to a URL."""
        if not self.page:
            raise RuntimeError("Browser not started")
        
        try:
            await self.page.goto(url)
            logger.info(f"Navigated to: {url}")
        except Exception as e:
            logger.error(f"Error navigating to {url}: {e}")
            raise
    
    async def click(self, selector: str):
        """Click an element by selector."""
        if not self.page:
            raise RuntimeError("Browser not started")
        
        try:
            await self.page.click(selector)
            logger.info(f"Clicked: {selector}")
        except Exception as e:
            logger.error(f"Error clicking {selector}: {e}")
            raise
    
    async def type_text(self, selector: str, text: str):
        """Type text into an element."""
        if not self.page:
            raise RuntimeError("Browser not started")
        
        try:
            await self.page.fill(selector, text)
            logger.info(f"Typed text into: {selector}")
        except Exception as e:
            logger.error(f"Error typing into {selector}: {e}")
            raise
    
    async def get_text(self, selector: str) -> str:
        """Get text from an element."""
        if not self.page:
            raise RuntimeError("Browser not started")
        
        try:
            element = await self.page.query_selector(selector)
            if element:
                text = await element.inner_text()
                return text
            return ""
        except Exception as e:
            logger.error(f"Error getting text from {selector}: {e}")
            return ""
    
    async def screenshot(self, path: str):
        """Take a screenshot."""
        if not self.page:
            raise RuntimeError("Browser not started")
        
        try:
            await self.page.screenshot(path=path)
            logger.info(f"Screenshot saved to: {path}")
        except Exception as e:
            logger.error(f"Error taking screenshot: {e}")
            raise
    
    async def close(self):
        """Close the browser."""
        try:
            if self.browser:
                await self.browser.close()
            if self.playwright:
                await self.playwright.stop()
            logger.info("Browser closed")
        except Exception as e:
            logger.error(f"Error closing browser: {e}")


# Convenience function for one-off browser tasks
@asynccontextmanager
async def browser_session(browser_type: str = "chromium", headless: bool = False):
    """
    Context manager for browser sessions.
    
    Usage:
        async with browser_session() as browser:
            await browser.navigate("https://example.com")
            text = await browser.get_text("h1")
    """
    controller = BrowserController()
    await controller.start(browser_type, headless)
    try:
        yield controller
    finally:
        await controller.close()
