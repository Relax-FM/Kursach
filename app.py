import json

from flask import Flask, render_template, session
from auth.routes import blueprint_auth
from report.route import blueprint_report
from query.routes import blueprint_query
from access import login_required
from edit.route import blueprint_edit
from market.route import blueprint_market
from orders.route import blueprint_orders


app = Flask(__name__)
app.secret_key = 'SuperKey'

app.register_blueprint(blueprint_query, url_prefix='/zaproses')
app.register_blueprint(blueprint_auth, url_prefix='/auth')
app.register_blueprint(blueprint_report, url_prefix='/report')
app.register_blueprint(blueprint_edit, url_prefix='/edit')
app.register_blueprint(blueprint_market, url_prefix='/market')
app.register_blueprint(blueprint_orders, url_prefix='/orders')

app.config['db_config'] = json.load(open('configs/db.json'))
app.config['access_config'] = json.load(open('configs/access.json'))
app.config['cache_config'] = json.load(open('configs/cache.json'))

@app.route('/')
@login_required
def menu_choice():
    if session.get('user_group', None):
        return render_template('internal_user_menu.html')
    return render_template('external_user_menu.html')


@app.route('/exit')
@login_required
def exit_func():
    session.clear()
    return render_template('exit.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002)
