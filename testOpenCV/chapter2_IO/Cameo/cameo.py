import cv2
from managers import WindowManager, CaptureManager


class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

    def run(self):
        """
        执行循环
        """
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            #  过滤帧
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """
        处理键盘输入：
        1、空格截屏
        2、tab开始停止录像
        3、esc退出
        """
        if keycode == 32:  #space
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9:  #tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:  #escape
            self._windowManager.destroyWindow()


if __name__ == "__main__":
    Cameo().run()
