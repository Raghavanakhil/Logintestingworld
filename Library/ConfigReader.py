import configparser

def configRead(section,key):
    config = configparser.ConfigParser()
    config.read("./Configuration/Config.cfg")
    return config.get(section,key)

def Login(Login,key):
    config = configparser.ConfigParser()
    config.read("./Configuration/Config.cfg")
    return config.get(Login,key)
