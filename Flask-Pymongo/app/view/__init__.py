"""
API Request Handler and util
"""
from flask import Flask, g, current_app, request, Response

# app 초기화
def init_app(app: Flask):

    @app.before_first_request
    def before_first_request():
        '''맨 처음 리퀘스트가 오기 전에'''
        pass

    @app.before_request
    def before_request():
        '''HTTP 요청이 들어올때 마다'''
        pass

    @app.after_request
    def after_request():
        '''HTTP 요청이 끝나고 브라우저에 응답하기 전에'''
        pass
    @app.teardown_request
    def teardown_request():
        '''HTTP 요청이 끝나고 브라우저에 응답하기 전에'''
        pass

    @app.teardown_appcontext
    def teardown_appcontext():
        '''app context가 종료되기 전에'''
        pass