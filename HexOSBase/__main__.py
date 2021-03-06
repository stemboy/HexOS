import os

from kivy.app import App
from kivy.core.window import Window as CoreWindow

from HexOSBase.tmpdir import clear_tmp_dir
from HexOSBase.window import Window
from HexOSBase import globals


class HexOSBase(App):
    title = globals.baseSysConfig.get("main", "name")

    def build(self):
        CoreWindow.bind(on_request_close=self.on_close)

        return Window()


    def on_close(self, *args):
        clear_tmp_dir()
        globals.baseSysConfig.write(open(os.path.join(globals.baseSysPath, "HexOSBase/data/config_files/base_sys_config.ini"), "w"))


__all__ = ["HexOSBase"]
