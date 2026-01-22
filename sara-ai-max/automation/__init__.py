"""Automation - System control, file operations, and application management."""

from .app_controller import open_app, close_app, switch_app
from .file_ops import create_folder, create_file, delete_file, search_file
from .archives import create_zip, extract_zip, compress_folder, list_archive_contents
from .system import (
    get_system_info,
    control_volume,
    control_brightness,
    web_search,
    shutdown,
    restart,
    lock_screen
)

__all__ = [
    'open_app',
    'close_app',
    'switch_app',
    'create_folder',
    'create_file',
    'delete_file',
    'search_file',
    'create_zip',
    'extract_zip',
    'compress_folder',
    'list_archive_contents',
    'get_system_info',
    'control_volume',
    'control_brightness',
    'web_search',
    'shutdown',
    'restart',
    'lock_screen',
]
