from flask import Blueprint, render_template, request, session, current_app, url_for
from database.sql_provider import SQLProvider
import os
from access import group_required
from database.operations import select, select_dict, insert, update

blueprint_orders = Blueprint('bp_orders', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@blueprint_orders.route('/', methods=['GET', 'POST'])
@group_required
def start_page():
    db_config = current_app.config['db_config']

    if request.method == 'GET':
        sql = provider.get('orders_list.sql')
        orders = select_dict(db_config, sql)
        print(orders)
        return render_template('orders_list.html', orders=orders)
    else:
        action = request.form.get('action')
        print('action:', action)
        order_id = request.form['order_id']
        print("order_id : ", order_id)
        user_id = session.get('user_id')
        sql1 = provider.get('get_car.sql', user_id=user_id)
        car_id = select_dict(db_config, sql1)
        car_id = car_id[0]
        car_id = car_id['car_id']
        print("car_id : ", car_id)
        if int(action) == 1:
            sql = provider.get('orders_list_accept.sql', order_id=order_id, user_id=user_id, car_id=car_id)
            items = update(db_config, sql)
            return render_template('orders_accept.html', order_id=order_id)
        else:
            return "Упс...Что-то пошло не так"

# def get_some_info(order_id:str, items:dict):
#     item_description = [item for item in items if str(item['id_N']) == str(order_id)]
#     print("Item_description before = ", item_description)
#     item_description = item_description[0]
#     print("Item description after : ", item_description)
#     curr_basket = session.get('info_items', {})
#     print("curr_basket : ", curr_basket)
#
#     if order_id in curr_basket:
#         print('zhopa')
#         curr_basket.pop(order_id, 4000)
#     else:
#         print('good')
#         curr_basket[order_id] = {
#             'id_N': order_id,
#             'Adress': item_description['Adress'],
#             'amount': 1
#         }
#         session['info_items'] = curr_basket
#         print(session['info_items'])
#         session.permanent = True
#
#     return True