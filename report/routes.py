from flask import Blueprint, render_template

from access import group_required

blueprint_report = Blueprint('blueprint_report', __name__, template_folder='templates')


@blueprint_report.route('/first_report')
@group_required
def first_report():
    return render_template('first_report.html')

@blueprint_report.route('/menu_report')
@group_required
def menu_report():
    return render_template('menu_report.html')