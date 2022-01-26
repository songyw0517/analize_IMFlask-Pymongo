from flask import Blueprint, current_app, redirect, render_template, request, url_for
from model.mongodb import Testdb
test_CRUD_bp = Blueprint('testBp', __name__)

@test_CRUD_bp.route('/')
def index():
    return render_template('mongoCRUD.html')

# insert
@test_CRUD_bp.route('/insert/', methods=['POST', 'GET'])
def testInsert():
    if request.method == 'POST':
        # request를 통해 html로 부터 데이터를 받아옴
        id, pw = request.form['id'], request.form['pw']
        info = {'id':id, 'pw':pw}
        '''
        id 검증 단계
        '''
        
        # db에 id, pw 삽입
        Testdb(current_app.db).insert_userInfo(info)

        # document 가져오기
        data_list=Testdb(current_app.db).get_document()
        
        return render_template('mongoCRUD.html', msg = info, data_list = data_list)
    else:
        # error note
        # url_for('index') 사용시 어떤 index()인지 판단불가
        # url_for('test_CRUD.index')로 지정해줘야한다.
        print("else")
        return redirect(url_for('testBp.index'))

# read
@test_CRUD_bp.route('/read/', methods=['POST', 'GET'])
def testRead():
    if request.method == 'POST':
        data=Testdb(current_app.db).get_document()
    return render_template('mongoCRUD.html', data_list = data)

# clear
@test_CRUD_bp.route('/clear/', methods=['POST', 'GET'])
def testClear():
    if request.method == 'POST':
        Testdb(current_app.db).drop_collection()
    return redirect(url_for('testBp.index'))

# update
@test_CRUD_bp.route('/update/', methods=['POST', 'GET'])
def testUpdate():
    if request.method == 'POST':
        # form으로부터 데이터 가져오기
        id, ch_pw = request.form['id'], request.form['ch_pw']
        info = {'id':id, 'ch_pw':ch_pw}
        
        # db 업데이트 
        Testdb(current_app.db).update_userInfo(info)


    return render_template('mongoCRUD.html', data_list = Testdb(current_app.db).get_document())

# delete
@test_CRUD_bp.route('/delete/', methods=['POST', 'GET'])
def testDelete():
    if request.method == 'POST':
        # id가져오기
        id = request.form['id']

        Testdb(current_app.db).delete_id(id)

    return render_template('mongoCRUD.html', data_list = Testdb(current_app.db).get_document())