import os.path

from flask import Blueprint, request, render_template, current_app
from database.operations import select
from database.sql_provider import SQLProvider
from access import group_required


blueprint_query = Blueprint('bp_query', __name__, template_folder='templates')

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@blueprint_query.route('/test')
def provider_test():
    p = os.path
    print(p)
    p1 = os.path.dirname(__file__)
    print(p1)
    return 'None'



@blueprint_query.route('/menu_queries')
@group_required
def menu_queries():
    return render_template('menu_queries.html')

@blueprint_query.route('/query1')
@group_required
def query1():
    print(os.path.join(os.path.dirname(__file__)))
    _sql = provider.get('query1.sql')
    product_result, schema = select(current_app.config['db_config'], _sql)
    if len(product_result) == 0:
        return render_template('not_found.html')
    return render_template('db_result.html', schema=['Номер товара', 'Масса', 'Количество', 'Наименование', 'Цена'], result=product_result, query_numb="Query1")

@blueprint_query.route('/query2')
@group_required
def query2():
    print(os.path.join(os.path.dirname(__file__)))
    _sql = provider.get('query2.sql')
    product_result, schema = select(current_app.config['db_config'], _sql)
    if len(product_result) == 0:
        return render_template('not_found.html')
    return render_template('db_result.html', schema=['Номер заказа', 'Дата', 'Имя', 'Фамилия', 'Адрес', 'Номер телефона'], result=product_result, query_numb="Query2")

@blueprint_query.route('/query3', methods=['GET', 'POST'])
@group_required
def query3():
    print(os.path.join(os.path.dirname(__file__)))
    _sql = provider.get('query3.sql')
    product_result, schema = select(current_app.config['db_config'], _sql)
    if len(product_result) == 0:
        return render_template('not_found.html')
    return render_template('db_result.html', schema=['Номер заказа', 'Дата', 'Имя', 'Фамилия', 'Адрес', 'Номер телефона'], result=product_result, query_numb="Query3")

@blueprint_query.route('/query4', methods=['GET', 'POST'])
@group_required
def query4():
    print(os.path.join(os.path.dirname(__file__)))
    if request.method == 'POST':
        input_product = request.form.get('product_name')
        if input_product:
            _sql = provider.get('query4.sql', input_product=input_product)
            product_result, schema = select(current_app.config['db_config'], _sql)
            if len(product_result) == 0:
                return render_template('not_found.html')
            return render_template('db_result.html', schema=['Номер заказа', 'Дата', 'Клиент', 'Масса', 'Количество', 'Наименование'], result=product_result, query_numb="Query4")
        else:
            return render_template('not_found.html')
    elif request.method == 'GET':
        return render_template('query.html', ph_title="Введите номер заказа", title_name='Query4')

@blueprint_query.route('/query5', methods=['GET', 'POST'])
@group_required
def query5():
    print(os.path.join(os.path.dirname(__file__)))
    if request.method == 'POST':
        input_product = request.form.get('product_name')
        if input_product:
            _sql = provider.get('query5.sql', input_product=input_product)
            product_result, schema = select(current_app.config['db_config'], _sql)
            if len(product_result) == 0:
                return render_template('not_found.html')
            return render_template('db_result.html', schema=['№', 'Договор №', 'Имя', 'Фамилия', 'Телефон', 'Адресс', 'Скидка', 'Общая масса покупок', 'МКАД'], result=product_result, query_numb="Query5")
        else:
            return render_template('not_found.html')
    elif request.method == 'GET':
        return render_template('query.html', ph_title="Введите номер клиента", title_name='Query5')

@blueprint_query.route('/query6', methods=['GET', 'POST'])
@group_required
def query6():
    print(os.path.join(os.path.dirname(__file__)))
    _sql = provider.get('query6.sql')
    product_result, schema = select(current_app.config['db_config'], _sql)
    if len(product_result) == 0:
        return render_template('not_found.html')
    return render_template('db_result.html', schema=['№', 'Год', 'Марка', 'Гос.Номер', 'Объем'], result=product_result, query_numb="Query6")

