import os
import sys


def resource_path(relative_path: str) -> str:
    """Get absolute path to resource, works in dev and PyInstaller builds."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, 'resources', relative_path)
    return os.path.join(os.path.dirname(__file__), '..', 'resources', relative_path)
