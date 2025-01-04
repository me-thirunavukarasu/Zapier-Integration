import os

class Config:
    DEBUG = False
    TESTING = False
    ZAPIER_URL = os.getenv("ZAPIER_URL", "https://hooks.zapier.com/hooks/catch/21200058/2zysb0x/")
