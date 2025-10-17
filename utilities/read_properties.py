import configparser
config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class Read_config :
    @staticmethod
    def get_admin_page_url():
        url= config.get('admin login info','login_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('admin login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password