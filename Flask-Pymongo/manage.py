"""
Application Main Manage Module

flask 웹 어플리케이션을 실행시키기 위한 메인 코드입니다. 
flask application 객체를 생성하고, 각종 shell context 설정 및 cli command 설정을 담당합니다.
"""

from config import config
from app import create_app
application = create_app(config)

# cli 명령어 등록
# flask_app 등록후 사용가능
@application.cli.command('cli-test')
def cli_test():
    print('cli test')

# # db를 초기화하는 명령어
# @application.cli.command('db-init')
# def db_init():
    
