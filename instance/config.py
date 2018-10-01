class BaseConfig:
    
    DATABASE_URL = 'postgresql://postgres:1460@localhost:5433/fast_food_db'
    DEBUG= True
    DB ='testing_db'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DB='fast_food_db'

class TestingConfig(BaseConfig):
    DATABASE_URL = 'postgresql://postgres:1460@localhost:5433/testing_db'
    DEBUG = False
    Testing =True
    DB = 'testing_db'

class ProductionConfig(BaseConfig):
    Debug =False

app_config={
    "development":DevelopmentConfig,
    "production":ProductionConfig,
    "testing":TestingConfig
    
}