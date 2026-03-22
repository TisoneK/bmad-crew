#!/usr/bin/env python
# /// script
# requires-python = ">=3.6"
# ///
"""
Platform detection bootstrap for BMAD Crew Advisor.
Run this once on first activation to detect OS and python binary.
Works with both `python` and `python3` — whichever resolves on this machine.

Usage:
  python detect-platform.py
  python3 detect-platform.py

Output (JSON):
  {"os": "Windows", "python_binary": "python", "python_version": "3.14.2"}
"""

import sys
import platform
import json

os_name = platform.system()          # Windows | Darwin | Linux
py_version = platform.python_version()

# Determine which binary was used to invoke this script
# sys.executable gives the full path; we just need the name
exe = sys.executable
if "python3" in exe.lower():
    binary = "python3"
else:
    binary = "python"

result = {
    "os": os_name,
    "python_binary": binary,
    "python_version": py_version,
}

print(json.dumps(result))
