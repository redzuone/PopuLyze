import os
import sys


def is_bundled() -> bool:
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return True
    else:
        return False


def resource_path(relative_path: str) -> str:
    """Get absolute path to resource, works in dev and PyInstaller builds."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, 'resources', relative_path)
    return os.path.join(os.path.dirname(__file__), '..', 'resources', relative_path)


def get_libmpv_path() -> str | None:
    bundled = is_bundled()
    if bundled:
        meipass = getattr(sys, '_MEIPASS', None)
        if meipass is None:
            return None
        # check in app directory
        base_path = os.path.dirname(meipass)
        libmpv_path = os.path.join(base_path, 'libmpv-2.dll')
        if os.path.exists(libmpv_path):
            return base_path
        # check in _meipass/lib directory
        lib_dir_path = os.path.join(meipass, 'lib')
        libmpv_dll_path = os.path.join(lib_dir_path, 'libmpv-2.dll')
        if os.path.exists(libmpv_dll_path):
            return lib_dir_path
    else:
        # dev env: lib directory
        base_path = os.path.join(os.path.dirname(__file__), '..', '..')
        libmpv_path = os.path.join(os.path.abspath(base_path), 'lib')
        return libmpv_path
    return None
