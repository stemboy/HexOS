import os
import sys

from appdirs import user_data_dir
from configparser import ConfigParser

import HexOSLibs

sysConfig = ConfigParser()
sysConfig.read("sysConfig.ini")

os.environ['KIVY_HOME'] = user_data_dir(sysConfig["main"]["name"])
os.environ['KIVY_CONFIG_FILE'] = user_data_dir(sysConfig["main"]["name"])
os.environ[str(sysConfig["main"]["name"]) + '_CONFIG'] = str(sysConfig.__dict__)
os.chdir(user_data_dir(sysConfig["main"]["name"]))

HexOSLibs.setup_app()
HexOSLibs.start_app()