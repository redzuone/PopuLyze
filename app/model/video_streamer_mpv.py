import os

from PySide6 import QtCore

from app.utils.paths import get_libmpv_path

libmpv_path = get_libmpv_path()
if libmpv_path is not None:
    os.environ['PATH'] = libmpv_path + os.pathsep + os.environ['PATH']
# ruff: noqa: E402
import locale

import mpv

from app.logger import logger

# This is necessary since PyQT stomps over the locale settings needed by libmpv.
# This needs to happen after importing PyQT before creating the first mpv.MPV instance.
locale.setlocale(locale.LC_NUMERIC, 'C')


class VideoStreamerMPV(QtCore.QObject):
    def __init__(self, id: str, source: str) -> None:
        super().__init__()
        self.source = source
        self.is_playing = False
        self.player = None
        self.window_id = ''

    def start(self) -> None:
        if self.window_id == '':
            logger.debug('no window id to embed mpv')
            return
        logger.debug('init mpv')
        self.player = mpv.MPV(
            wid=self.window_id,
            profile='low-latency',
            untimed=True,
            speed=1.005,
            log_handler=print,
            rtsp_transport='udp',
        )

        @self.player.property_observer('video-params')
        def vid_observer(_name, value: dict | None):
            if value:
                logger.debug(value)
                self.is_playing = True

        self.player.play(self.source)

    def stop(self) -> None:
        if self.player is not None:
            self.player.terminate()
