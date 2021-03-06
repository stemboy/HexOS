from configparser import ConfigParser as Cp


class ConfigParser(Cp):
    def get(self, *args, **kwargs):
        value = super(ConfigParser, self).get(*args, **kwargs)
        try:
            return int(value)

        except ValueError:
            try:
                return float(value)

            except ValueError:
                if value == "True":
                    return True
                if value == "False":
                    return False
                else:
                    return str(value)


baseSysConfig = ConfigParser()
baseSysConfig.read("HexOSBase/data/config_files/base_sys_config.ini")

baseSysPath = ""
HexOSPath = ""
userDataDir = ""

__all__ = ["baseSysPath", "baseSysConfig", "HexOSPath"]
