class Config(object):
    LOGGER = True

    API_KEY = "1732951299:AAH5y4W1CwYxGS5epURab3c3DZC5eAGhcvc"
    OWNER_ID = "989210292" 
    OWNER_USERNAME = "kaiyi"

    
    SQLALCHEMY_DATABASE_URI = 'postgres://joji:password@database-1.cuwoqmaijm80.us-east-2.rds.amazonaws.com:5432/jojibot'  # needed for any database modules
    MESSAGE_DUMP = None  
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    
    SUDO_USERS = []  
    SUPPORT_USERS = []  
    WHITELIST_USERS = []  
    DONATION_LINK = None  
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  
    STRICT_GBAN = False
    STRICT_GMUTE = False
    WORKERS = 8  
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
