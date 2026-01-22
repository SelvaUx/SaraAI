"""Connectors - External application integrations."""

from .browser import BrowserController
from .messaging import MessagingConnector
from .email import EmailConnector
from .office import OfficeAutomation

__all__ = [
    'BrowserController',
    'MessagingConnector',
    'EmailConnector',
    'OfficeAutomation',
]
