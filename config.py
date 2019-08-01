class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'some secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Owen2013@127.0.0.1:5432/payroll_system'
    environment = 'Development'
    DEBUG = True

class Development(Config):#(Config)inheriting config properties
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Owen2013@127.0.0.1:5432/payroll_system'
    environment = 'Development'
    DEBUG = True

class Testing(Config):
    DEBUG = False

class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Owen2013@127.0.0.1:5432/payroll_system'
    DEBUG = False
    environment = 'Production'