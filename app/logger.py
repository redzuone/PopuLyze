import os
import pathlib
import sys
from datetime import datetime
from typing import Any, TextIO

from loguru import logger
from platformdirs import user_data_dir

console_sink_id = None
file_sink_id = None


def _get_log_dir(app_name: str, app_author: str) -> str:
    if getattr(sys, 'frozen', False):
        base_dir = user_data_dir(app_name, app_author)
        log_dir = os.path.join(base_dir, 'logs')
    else:
        log_dir = os.path.join(pathlib.Path(__file__).parent, 'logs')
    os.makedirs(log_dir, exist_ok=True)
    return log_dir


def rotate_by_day_and_size(message: Any, file: TextIO) -> bool:
    # Rotate if file size > 100 MB
    if os.stat(file.name).st_size > 100 * 1024 * 1024:
        return True
    # Rotate if it's a new day
    file_date = datetime.fromtimestamp(os.stat(file.name).st_mtime).date()
    now_date = datetime.now().date()
    if now_date > file_date:
        return True
    return False


def setup_logger(app_name: str, app_author: str, log_file_suffix: str = '') -> None:
    global console_sink_id, file_sink_id
    log_dir = _get_log_dir(app_name, app_author)
    # Remove default handler
    logger.remove()

    # Logging to console - debug
    if sys.stdout:
        console_sink_id = logger.add(sys.stderr, level='DEBUG')

    # Logging to file - trace
    filename = f'{datetime.now().strftime("%Y-%m-%d")}'
    if log_file_suffix:
        filename += f'_{log_file_suffix}'
    filename += '.log'

    file_sink_id = logger.add(
        os.path.join(log_dir, filename), rotation=rotate_by_day_and_size, encoding='utf-8', level='TRACE'
    )


def get_last_logfile_location() -> str | None:
    """Return the current log file name and full path."""
    # Access sink from logger._core.handlers (not public API, but works)
    handler_id = next(reversed(logger._core.handlers))  # type: ignore[attr-defined]
    sink = logger._core.handlers[handler_id]  # type: ignore[attr-defined]
    if hasattr(sink, '_name') and sink._name is not None:
        file_path: str = sink._name
        return file_path
    return None


__all__ = ['setup_logger', 'logger']
