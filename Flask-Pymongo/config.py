# 환경변수 처리
APP_NAME = "Scof"
FLASK_CONFIG="development" # develop, production
FLASK_ENV="development" # develop, production
FLASK_APP="manage:application"
MONGODB_URI = "mongodb://localhost:27017"
MONGODB_NAME = "scof"

class Config:
    MONGODB_URI = MONGODB_URI
    MONGODB_NAME = MONGODB_NAME

# FLASK_CONFIG 값에 따라 DEBUG, TESTING 값을 다르게 적용시킨다.
if FLASK_CONFIG == "development":
    class AppConfig(Config):
        DEBUG = True
        TESTING = False
elif FLASK_CONFIG == "production":
    class AappConifg(Config):
        DEBUG = False
        TESTING = False

config = AppConfig