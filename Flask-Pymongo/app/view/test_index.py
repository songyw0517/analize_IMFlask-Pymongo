"""
Template Example API
"""
from flask import Blueprint, render_template

test_index_template = Blueprint('test_index_template', __name__)

# route 설정
@test_index_template.route('/')
def index():
    return render_template('index.html')