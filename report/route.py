from flask import *
from database.operations import select, call_proc, select1
from access import login_required, group_required
from database.sql_provider import SQLProvider
import os
from database.connection import UseDatabase as DBConnection

blueprint_report = Blueprint('bp_report', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))



report_list = [
    {'rep_name':'Отчёт 1 ', 'rep_id':'1'},
    {'rep_name':'Отчёт 2 ', 'rep_id':'2'}
]


report_url = {
    '1': {'create_rep':'bp_report.create_rep1', 'view_rep':'bp_report.view_rep1'},
    '2': {'create_rep':'bp_report.create_rep2', 'view_rep':'bp_report.view_rep2'}
}


@blueprint_report.route('/', methods=['GET', 'POST'])
def start_report():
    if request.method == 'GET':
        return render_template('menu_report.html', report_list=report_list)
    else:
        rep_id = request.form.get('rep_id')
        print('rep_id = ', rep_id)
        if request.form.get('create_rep'):
            url_rep = report_url[rep_id]['create_rep']
        else:
            url_rep = report_url[rep_id]['view_rep']
        print('url_rep = ', url_rep)
        return redirect(url_for(url_rep))
    # из формы получает номер отчета и какую кнопку

@blueprint_report.route('/create_rep1', methods=['GET', 'POST'])
@group_required
def create_rep1():
    if request.method == 'GET':
        print("GET_create")
        return render_template('report_create.html', name_rep="продаже товаров")
    else:
        print(current_app.config['db_config'])
        print("POST_create")
        rep_month = request.form.get('input_month')
        rep_year = request.form.get('input_year')
        print("Loading...")
        if rep_year and rep_month:
            _sql = provider.get('check_rep1.sql', in_year=rep_year, in_month=rep_month)
            product_result, schema = select1(current_app.config['db_config'], _sql)
            print(product_result)
            if (product_result[0][0] > 0):
                return "Такой отчёт уже существует"
            else:
                res = call_proc(current_app.config['db_config'], 'product_report', rep_month, rep_year)
                print('res=', res)
                return render_template('report_created.html', rep_month=rep_month, rep_year=rep_year, name_rep="продаже товаров")
        else:
            return "Repeat input"


@blueprint_report.route('/view_rep1', methods=['GET', 'POST'])
@group_required
def view_rep1():
    if request.method == 'GET':
        return render_template('view_rep.html', name_rep='продаже товаров')
    else:
        rep_month = request.form.get('input_month')
        rep_year = request.form.get('input_year')
        print(rep_month)
        print(rep_year)
        if rep_year and rep_month:
            _sql = provider.get('rep1.sql', in_year=rep_year, in_month=rep_month)
            product_result, schema = select(current_app.config['db_config'], _sql)
            if product_result:
                return render_template('result_rep1.html', schema=["№", "Продукт №", "Название", "Кол-во", "Месяц", "Год"], result=product_result, rep_month=rep_month, rep_year=rep_year)
            else:
                return "Такой отчёт не был создан"
        else:
            return "Repeat input"

@blueprint_report.route('/create_rep2', methods=['GET', 'POST'])
@group_required
def create_rep2():
    if request.method == 'GET':
        print("GET_create")
        return render_template('report_create.html', name_rep="кол-ве доставок")
    else:
        print(current_app.config['db_config'])
        print("POST_create")
        rep_month = request.form.get('input_month')
        rep_year = request.form.get('input_year')
        print("Loading...")
        if rep_year and rep_month:
            _sql = provider.get('check_rep2.sql', in_year=rep_year, in_month=rep_month)
            product_result, schema = select1(current_app.config['db_config'], _sql)
            print(product_result)
            if (product_result[0][0] > 0):
                return "Такой отчёт уже существует"
            else:
                res = call_proc(current_app.config['db_config'], 'delivery_report', rep_month, rep_year)
                print('res=', res)
                return render_template('report_created.html', rep_month=rep_month, rep_year=rep_year, name_rep="кол-ве доставок")
        else:
            return "Repeat input"

@blueprint_report.route('/view_rep2', methods=['GET', 'POST'])
@group_required
def view_rep2():
    if request.method == 'GET':
        return render_template('view_rep.html', name_rep="кол-ве доставок")
    else:
        rep_month = request.form.get('input_month')
        rep_year = request.form.get('input_year')
        print(rep_month)
        print(rep_year)
        if rep_year and rep_month:
            _sql = provider.get('rep2.sql', in_year=rep_year, in_month=rep_month)
            product_result, schema = select(current_app.config['db_config'], _sql)
            if product_result:
                return render_template('result_rep1.html', schema=["№", "Кол-во", "Месяц", "Год"], result=product_result, rep_month=rep_month, rep_year=rep_year)
            else:
                return "Такой отчёт не был создан"
        else:
            return "Repeat input"
