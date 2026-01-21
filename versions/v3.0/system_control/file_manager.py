#!/usr/bin/env python3
"""
Sara AI File Manager
Handles file and folder operations, file management tasks
"""

import os
import shutil
import time
import logging
import subprocess
from typing import List, Optional, Dict
from pathlib import Path
from datetime import datetime

class FileManager:
    def __init__(self):
        """Initialize file manager"""
        self.logger = logging.getLogger('FileManager')
        
        # Current working directory
        self.current_dir = os.getcwd()
        
        # File operation history
        self.operation_history = []
        
        print("📁 File Manager initialized")
        
    def create_file(self, filename: str, content: str = "", directory: str = None) -> bool:
        """Create a new file with optional content"""
        try:
            if directory:
                filepath = os.path.join(directory, filename)
            else:
                filepath = os.path.join(self.current_dir, filename)
                
            # Ensure directory exists
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            # Create file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
            self.logger.info(f"File created: {filepath}")
            self.operation_history.append({
                'operation': 'create_file',
                'path': filepath,
                'timestamp': datetime.now()
            })
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error creating file {filename}: {e}")
            return False
            
    def create_folder(self, foldername: str, directory: str = None) -> bool:
        """Create a new folder"""
        try:
            if directory:
                folderpath = os.path.join(directory, foldername)
            else:
                folderpath = os.path.join(self.current_dir, foldername)
                
            os.makedirs(folderpath, exist_ok=True)
            
            self.logger.info(f"Folder created: {folderpath}")
            self.operation_history.append({
                'operation': 'create_folder',
                'path': folderpath,
                'timestamp': datetime.now()
            })
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error creating folder {foldername}: {e}")
            return False
            
    def delete_file(self, filepath: str) -> bool:
        """Delete a file"""
        try:
            if not os.path.exists(filepath):
                self.logger.warning(f"File not found: {filepath}")
                return False
                
            if os.path.isfile(filepath):
                os.remove(filepath)
                self.logger.info(f"File deleted: {filepath}")
                
                self.operation_history.append({
                    'operation': 'delete_file',
                    'path': filepath,
                    'timestamp': datetime.now()
                })
                
                return True
            else:
                self.logger.error(f"Path is not a file: {filepath}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error deleting file {filepath}: {e}")
            return False
            
    def delete_folder(self, folderpath: str) -> bool:
        """Delete a folder and its contents"""
        try:
            if not os.path.exists(folderpath):
                self.logger.warning(f"Folder not found: {folderpath}")
                return False
                
            if os.path.isdir(folderpath):
                shutil.rmtree(folderpath)
                self.logger.info(f"Folder deleted: {folderpath}")
                
                self.operation_history.append({
                    'operation': 'delete_folder',
                    'path': folderpath,
                    'timestamp': datetime.now()
                })
                
                return True
            else:
                self.logger.error(f"Path is not a folder: {folderpath}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error deleting folder {folderpath}: {e}")
            return False
            
    def copy_file(self, source: str, destination: str) -> bool:
        """Copy a file from source to destination"""
        try:
            if not os.path.exists(source):
                self.logger.error(f"Source file not found: {source}")
                return False
                
            # Ensure destination directory exists
            dest_dir = os.path.dirname(destination)
            if dest_dir:
                os.makedirs(dest_dir, exist_ok=True)
                
            shutil.copy2(source, destination)
            
            self.logger.info(f"File copied: {source} -> {destination}")
            self.operation_history.append({
                'operation': 'copy_file',
                'source': source,
                'destination': destination,
                'timestamp': datetime.now()
            })
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error copying file {source} to {destination}: {e}")
            return False
            
    def move_file(self, source: str, destination: str) -> bool:
        """Move a file from source to destination"""
        try:
            if not os.path.exists(source):
                self.logger.error(f"Source file not found: {source}")
                return False
                
            # Ensure destination directory exists
            dest_dir = os.path.dirname(destination)
            if dest_dir:
                os.makedirs(dest_dir, exist_ok=True)
                
            shutil.move(source, destination)
            
            self.logger.info(f"File moved: {source} -> {destination}")
            self.operation_history.append({
                'operation': 'move_file',
                'source': source,
                'destination': destination,
                'timestamp': datetime.now()
            })
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error moving file {source} to {destination}: {e}")
            return False
            
    def rename_file(self, old_path: str, new_name: str) -> bool:
        """Rename a file or folder"""
        try:
            if not os.path.exists(old_path):
                self.logger.error(f"File/folder not found: {old_path}")
                return False
                
            directory = os.path.dirname(old_path)
            new_path = os.path.join(directory, new_name)
            
            os.rename(old_path, new_path)
            
            self.logger.info(f"Renamed: {old_path} -> {new_path}")
            self.operation_history.append({
                'operation': 'rename',
                'old_path': old_path,
                'new_path': new_path,
                'timestamp': datetime.now()
            })
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error renaming {old_path} to {new_name}: {e}")
            return False
            
    def list_directory(self, directory: str = None) -> List[Dict]:
        """List contents of a directory"""
        try:
            if not directory:
                directory = self.current_dir
                
            if not os.path.exists(directory):
                self.logger.error(f"Directory not found: {directory}")
                return []
                
            items = []
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                stat = os.stat(item_path)
                
                items.append({
                    'name': item,
                    'path': item_path,
                    'type': 'directory' if os.path.isdir(item_path) else 'file',
                    'size': stat.st_size if os.path.isfile(item_path) else 0,
                    'modified': datetime.fromtimestamp(stat.st_mtime),
                    'created': datetime.fromtimestamp(stat.st_ctime)
                })
                
            self.logger.info(f"Listed {len(items)} items in {directory}")
            return items
            
        except Exception as e:
            self.logger.error(f"Error listing directory {directory}: {e}")
            return []
            
    def search_files(self, pattern: str, directory: str = None, recursive: bool = True) -> List[str]:
        """Search for files matching a pattern"""
        try:
            if not directory:
                directory = self.current_dir
                
            import glob
            
            if recursive:
                search_pattern = os.path.join(directory, '**', pattern)
                files = glob.glob(search_pattern, recursive=True)
            else:
                search_pattern = os.path.join(directory, pattern)
                files = glob.glob(search_pattern)
                
            self.logger.info(f"Found {len(files)} files matching '{pattern}'")
            return files
            
        except Exception as e:
            self.logger.error(f"Error searching for files: {e}")
            return []
            
    def get_file_info(self, filepath: str) -> Dict:
        """Get detailed information about a file"""
        try:
            if not os.path.exists(filepath):
                return {'error': 'File not found'}
                
            stat = os.stat(filepath)
            path_obj = Path(filepath)
            
            info = {
                'name': path_obj.name,
                'path': str(path_obj.absolute()),
                'directory': str(path_obj.parent),
                'extension': path_obj.suffix,
                'type': 'directory' if os.path.isdir(filepath) else 'file',
                'size': stat.st_size,
                'size_human': self.format_size(stat.st_size),
                'created': datetime.fromtimestamp(stat.st_ctime),
                'modified': datetime.fromtimestamp(stat.st_mtime),
                'accessed': datetime.fromtimestamp(stat.st_atime),
                'permissions': oct(stat.st_mode)[-3:]
            }
            
            return info
            
        except Exception as e:
            self.logger.error(f"Error getting file info for {filepath}: {e}")
            return {'error': str(e)}
            
    def format_size(self, size_bytes: int) -> str:
        """Format file size in human readable format"""
        if size_bytes == 0:
            return "0 B"
            
        size_names = ["B", "KB", "MB", "GB", "TB"]
        import math
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return f"{s} {size_names[i]}"
        
    def open_file_explorer(self, directory: str = None) -> bool:
        """Open Windows File Explorer"""
        try:
            if not directory:
                directory = self.current_dir
                
            if not os.path.exists(directory):
                directory = self.current_dir
                
            subprocess.run(['explorer', directory], check=True)
            self.logger.info(f"Opened File Explorer at: {directory}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening File Explorer: {e}")
            return False
            
    def open_file_with_default(self, filepath: str) -> bool:
        """Open file with default application"""
        try:
            if not os.path.exists(filepath):
                self.logger.error(f"File not found: {filepath}")
                return False
                
            os.startfile(filepath)
            self.logger.info(f"Opened file with default application: {filepath}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error opening file {filepath}: {e}")
            return False
            
    def get_disk_usage(self, directory: str = None) -> Dict:
        """Get disk usage information"""
        try:
            if not directory:
                directory = self.current_dir
                
            usage = shutil.disk_usage(directory)
            
            return {
                'total': usage.total,
                'used': usage.used,
                'free': usage.free,
                'total_human': self.format_size(usage.total),
                'used_human': self.format_size(usage.used),
                'free_human': self.format_size(usage.free),
                'used_percent': round((usage.used / usage.total) * 100, 2)
            }
            
        except Exception as e:
            self.logger.error(f"Error getting disk usage: {e}")
            return {}
            
    def create_backup(self, source: str, backup_dir: str = None) -> bool:
        """Create backup of file or folder"""
        try:
            if not os.path.exists(source):
                self.logger.error(f"Source not found: {source}")
                return False
                
            if not backup_dir:
                backup_dir = os.path.join(self.current_dir, 'backups')
                
            os.makedirs(backup_dir, exist_ok=True)
            
            # Create backup filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            source_name = os.path.basename(source)
            backup_name = f"{source_name}_backup_{timestamp}"
            backup_path = os.path.join(backup_dir, backup_name)
            
            if os.path.isfile(source):
                shutil.copy2(source, backup_path)
            else:
                shutil.copytree(source, backup_path)
                
            self.logger.info(f"Backup created: {source} -> {backup_path}")
            self.operation_history.append({
                'operation': 'backup',
                'source': source,
                'backup': backup_path,
                'timestamp': datetime.now()
            })
            
            return True
            
        except Exception as e:
            self.logger.error(f"Error creating backup: {e}")
            return False
            
    def change_directory(self, directory: str) -> bool:
        """Change current working directory"""
        try:
            if os.path.exists(directory) and os.path.isdir(directory):
                self.current_dir = os.path.abspath(directory)
                os.chdir(self.current_dir)
                self.logger.info(f"Changed directory to: {self.current_dir}")
                return True
            else:
                self.logger.error(f"Directory not found: {directory}")
                return False
                
        except Exception as e:
            self.logger.error(f"Error changing directory: {e}")
            return False
            
    def get_recent_files(self, directory: str = None, days: int = 7) -> List[Dict]:
        """Get recently modified files"""
        try:
            if not directory:
                directory = self.current_dir
                
            cutoff_time = time.time() - (days * 24 * 60 * 60)
            recent_files = []
            
            for root, dirs, files in os.walk(directory):
                for file in files:
                    filepath = os.path.join(root, file)
                    try:
                        mtime = os.path.getmtime(filepath)
                        if mtime > cutoff_time:
                            recent_files.append({
                                'path': filepath,
                                'name': file,
                                'modified': datetime.fromtimestamp(mtime)
                            })
                    except OSError:
                        continue
                        
            # Sort by modification time (newest first)
            recent_files.sort(key=lambda x: x['modified'], reverse=True)
            
            self.logger.info(f"Found {len(recent_files)} recent files")
            return recent_files
            
        except Exception as e:
            self.logger.error(f"Error getting recent files: {e}")
            return []
            
    def get_operation_history(self) -> List[Dict]:
        """Get file operation history"""
        return self.operation_history.copy()
        
    def clear_history(self) -> bool:
        """Clear operation history"""
        self.operation_history.clear()
        self.logger.info("Operation history cleared")
        return True

def main():
    """Test file manager"""
    manager = FileManager()
    
    # Test creating files and folders
    print("Testing file operations...")
    
    # Create test folder
    manager.create_folder("test_folder")
    
    # Create test file
    manager.create_file("test_file.txt", "Hello from Sara AI!")
    
    # List directory
    items = manager.list_directory()
    print(f"Directory contains {len(items)} items")
    
    # Get file info
    info = manager.get_file_info("test_file.txt")
    print(f"File info: {info}")
    
    # Test disk usage
    usage = manager.get_disk_usage()
    print(f"Disk usage: {usage['used_human']}/{usage['total_human']} ({usage['used_percent']}%)")

if __name__ == "__main__":
    main()
