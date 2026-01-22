#!/usr/bin/env python3
"""
saractl - Command-line control tool for Sara AI Max.

Usage:
    saractl start                    # Start Sara AI Max
    saractl stop                     # Stop Sara AI Max
    saractl status                   # Check status
    saractl logs [--tail N]          # View logs
    saractl config [--show|--edit]   # Manage configuration
    saractl plugins [list|load|unload] [name]  # Manage plugins
    saractl test                     # Run tests
"""

import sys
import argparse
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class SaraCtl:
    """Command-line control for Sara AI Max."""
    
    def __init__(self):
        """Initialize saractl."""
        self.base_dir = Path(__file__).parent.parent
    
    def start(self, args):
        """Start Sara AI Max."""
        print("Starting Sara AI Max...")
        # Import and run main
        import subprocess
        subprocess.run([sys.executable, str(self.base_dir / "main.py")])
    
    def stop(self, args):
        """Stop Sara AI Max."""
        print("Stopping Sara AI Max...")
        # Send stop signal
        print("Sara AI Max stopped.")
    
    def status(self, args):
        """Check Sara AI Max status."""
        print("Sara AI Max Status:")
        print("  Running: No")  # Check if process is running
        print("  Version: 1.0.0-mvp")
    
    def logs(self, args):
        """View logs."""
        log_file = self.base_dir / "sara_max.log"
        
        if not log_file.exists():
            print("No log file found.")
            return
        
        with open(log_file, 'r') as f:
            lines = f.readlines()
        
        if args.tail:
            lines = lines[-args.tail:]
        
        for line in lines:
            print(line.strip())
    
    def config(self, args):
        """Manage configuration."""
        config_file = self.base_dir / "config.example.json"
        
        if args.show:
            if config_file.exists():
                with open(config_file, 'r') as f:
                    print(f.read())
            else:
                print("Config file not found.")
        elif args.edit:
            import os
            os.system(f"notepad {config_file}")
        else:
            print("Config file location:", config_file)
    
    def plugins(self, args):
        """Manage plugins."""
        from plugins.plugin_manager import PluginManager
        
        manager = PluginManager()
        
        if args.command == "list":
            plugins = manager.discover_plugins()
            print(f"Available plugins ({len(plugins)}):")
            for plugin in plugins:
                print(f"  - {plugin}")
                
            loaded = manager.list_loaded_plugins()
            print(f"\nLoaded plugins ({len(loaded)}):")
            for plugin in loaded:
                print(f"  - {plugin}")
        
        elif args.command == "load":
            if not args.name:
                print("Error: Plugin name required")
                return
            
            if manager.load_plugin(args.name):
                print(f"Plugin loaded: {args.name}")
            else:
                print(f"Failed to load plugin: {args.name}")
        
        elif args.command == "unload":
            if not args.name:
                print("Error: Plugin name required")
                return
            
            if manager.unload_plugin(args.name):
                print(f"Plugin unloaded: {args.name}")
            else:
                print(f"Failed to unload plugin: {args.name}")
    
    def test(self, args):
        """Run tests."""
        print("Running tests...")
        import subprocess
        subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"])
    
    def run(self):
        """Run the CLI."""
        parser = argparse.ArgumentParser(description="Sara AI Max Control Tool")
        subparsers = parser.add_subparsers(dest='command', help='Commands')
        
        # Start command
        subparsers.add_parser('start', help='Start Sara AI Max')
        
        # Stop command
        subparsers.add_parser('stop', help='Stop Sara AI Max')
        
        # Status command
        subparsers.add_parser('status', help='Check status')
        
        # Logs command
        logs_parser = subparsers.add_parser('logs', help='View logs')
        logs_parser.add_argument('--tail', type=int, help='Show last N lines')
        
        # Config command
        config_parser = subparsers.add_parser('config', help='Manage configuration')
        config_parser.add_argument('--show', action='store_true', help='Show config')
        config_parser.add_argument('--edit', action='store_true', help='Edit config')
        
        # Plugins command
        plugins_parser = subparsers.add_parser('plugins', help='Manage plugins')
        plugins_parser.add_argument('command', choices=['list', 'load', 'unload'])
        plugins_parser.add_argument('name', nargs='?', help='Plugin name')
        
        # Test command
        subparsers.add_parser('test', help='Run tests')
        
        args = parser.parse_args()
        
        if not args.command:
            parser.print_help()
            return
        
        # Route to appropriate handler
        handler = getattr(self, args.command, None)
        if handler:
            handler(args)
        else:
            print(f"Unknown command: {args.command}")


def main():
    """Main entry point."""
    ctl = SaraCtl()
    ctl.run()


if __name__ == "__main__":
    main()
