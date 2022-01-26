'''
app/__init__

Application Factory 역할을 담당하는 부분
'''
from flask import Flask
from app.view.test_index import test_index_template as test_index_bp
from app.view.test_CRUD import test_CRUD_bp 
from model import register_connection_pool

def create_app(config):
    # application factory 생성
    app = Flask(
        import_name=__name__,
        instance_relative_config=True,
        static_url_path='/',
        static_folder='asset/',
        template_folder='asset/')

    # app config 설정
    app.config.from_object(config)

    
    register_connection_pool(app)

    # 블루 프린트 등록
    app.register_blueprint(test_index_bp, url_prefix='/test/')
    app.register_blueprint(test_CRUD_bp, url_prefix='/test/CRUD/')

    return app