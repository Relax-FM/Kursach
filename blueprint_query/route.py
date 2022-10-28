import os.path

from flask import Blueprint, request, render_template, current_app
from db_work import select
from sql_provider import SQLProvider


blueprint_query = Blueprint('bp_query', __name__, template_folder='templates')

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_query.route('/test')
def provider_test():
    p = os.path
    print(p)
    p1 = os.path.dirname(__file__)
    print(p1)
    p2 = os.path.join(os.path.dirname(__file__), 'sql')
    print(p2)
    return 'None'


@blueprint_query.route('/queries', methods=['GET', 'POST'])
def queries():
    if request.method == 'POST':
        input_product = request.form.get('product_name')
        if input_product:
            _sql = provider.get('delivery.sql', input_product=input_product)
            product_result, schema = select(current_app.config['dbconfig'], _sql)
            return render_template('db_result.html', schema=schema, result=product_result, title='Items in order')
        else:
            return "Repeat input"
    return render_template('queries.html', placeholder='Entry delivery ID')

@blueprint_query.route('/menu')
def menu():
    return render_template('main_menu.html')

@blueprint_query.route('/NotDelivery', methods=['GET', 'POST'])
def check_not_delivery():
        _sql = provider.get('NotDelivered.sql')
        product_result, schema = select(current_app.config['dbconfig'], _sql)
        return render_template('db_result.html', schema=schema, result=product_result, title='Not delivered')

@blueprint_query.route('/delivery', methods=['GET', 'POST'])
def check_delivery():
        _sql = provider.get('Delivered.sql')
        product_result, schema = select(current_app.config['dbconfig'], _sql)
        return render_template('db_result.html', schema=schema, result=product_result, title='Delivered')

@blueprint_query.route('/stock', methods=['GET', 'POST'])
def check_stock():
        _sql = provider.get('Stock.sql')
        product_result, schema = select(current_app.config['dbconfig'], _sql)
        return render_template('db_result.html', schema=schema, result=product_result, title='Stock')

@blueprint_query.route('/automobile', methods=['GET', 'POST'])
def check_automobile():
        _sql = provider.get('Automobile.sql')
        product_result, schema = select(current_app.config['dbconfig'], _sql)
        return render_template('db_result.html', schema=schema, result=product_result, title='Automobile')

@blueprint_query.route('/client_queries', methods=['GET', 'POST'])
def cl_queries():
    if request.method == 'POST':
        input_product = request.form.get('product_name')
        if input_product:
            _sql = provider.get('Client.sql', input_product=input_product)
            product_result, schema = select(current_app.config['dbconfig'], _sql)
            return render_template('db_result.html', schema=schema, result=product_result, title='Client info')
        else:
            return "Repeat input"
    return render_template('queries.html', placeholder='Entry client ID')
