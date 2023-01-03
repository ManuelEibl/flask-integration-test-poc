class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Testing(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class Development(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"


class Production(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///some-prod-db.db"
