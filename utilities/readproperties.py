import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseUrl')
        return url

    @staticmethod
    def getUserEmail():
        usrname = config.get('common info','username')
        return usrname

    @staticmethod
    def getPassword():
        pasword = config.get('common info', 'password')
        return pasword