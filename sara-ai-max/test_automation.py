"""
Test the new step-by-step automation.

This script demonstrates the detailed, visible automation approach.
"""

import time
from automation import app_controller

print("="*60)
print("SARA AI MAX - STEP-BY-STEP AUTOMATION TEST")
print("="*60)
print("\nThis will demonstrate detailed automation with visible steps.\n")

# Test 1: Open Notepad
print("\n🧪 TEST 1: Opening Notepad with Windows Search")
print("-"*60)
input("Press Enter to start...")

success = app_controller.open_app("notepad")
if success:
    print("✅ Notepad opened successfully!\n")
    time.sleep(2)
else:
    print("❌ Failed to open Notepad\n")

# Test 2: Minimize all
print("\n🧪 TEST 2: Minimizing all windows")
print("-"*60)
input("Press Enter to start...")

success = app_controller.minimize_all_windows()
if success:
    print("✅ All windows minimized!\n")
    time.sleep(2)
else:
    print("❌ Failed to minimize\n")

# Test 3: Open Calculator
print("\n🧪 TEST 3: Opening Calculator")
print("-"*60)
input("Press Enter to start...")

success = app_controller.open_app("calculator")
if success:
    print("✅ Calculator opened successfully!\n")
    time.sleep(2)
else:
    print("❌ Failed to open Calculator\n")

# Test 4: Close Notepad
print("\n🧪 TEST 4: Closing Notepad")
print("-"*60)
input("Press Enter to start...")

success = app_controller.close_app("notepad")
if success:
    print("✅ Notepad closed successfully!\n")
else:
    print("❌ Failed to close Notepad\n")

print("\n" + "="*60)
print("ALL TESTS COMPLETE!")
print("="*60)
print("\n✨ Sara AI Max now uses detailed step-by-step automation!")
print("   Every action is visible and traceable.\n")
