import os

class Config:
    SECRET_KEY = 'b9a02b0c6d1d076ac2f644b43acb64a38b5124fb8dce339dc00804bfb9af1eca'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'testingpurpose.flask@gmail.com'
    MAIL_PASSWORD = 'qzdgsuvmvblugqwf'
