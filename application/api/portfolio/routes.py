from flask import Blueprint,render_template,request,jsonify#
from ..authentication.routes import login_required
from ..database.model import get_portfolio_item,get_transactions_receipt
from .model import make_portfolio

mod = Blueprint('portfolio',__name__)


@mod.route('/portfolio',methods=['GET','POST'])
@login_required
def load_portfolio():
    user = request.cookies['sub']
    purchases=get_portfolio_item(user)
    #purchases=get_portfolio_item("3a202b17-2af4-427f-abea-cea670fce242")
    products=make_portfolio(purchases['portfolio'])
    return render_template("dashboard_portfolio_section.html",products=products)
    #return jsonify({'data':render_template("dashboard_portfolio_section.html",product=products)})


@mod.route('/portfolio_load',methods=['GET','POST'])
@login_required
def load_bonds():
    user = request.cookies['sub']
    purchases = get_portfolio_item(user)
    # purchases=get_portfolio_item("3a202b17-2af4-427f-abea-cea670fce242")
    products = make_portfolio(purchases['portfolio'])
    print(purchases['portfolio'])
    return render_template('my_portfolio.html',p=zip(purchases['portfolio'],products))

@mod.route('/top_portfolio',methods=['GET','POST'])
@login_required
def top_section_portfolio():
    user = request.cookies['sub']
    the_user = get_portfolio_item(user)
    print(the_user)
    return render_template('top_portfolio_section.html',user=the_user)

@mod.route('/view_receipt/<the_id>',methods=['GET','POST'])
def view_receipt(the_id):
    the_list=get_transactions_receipt(the_id)
    return render_template('receipt.html',content=the_list)

@mod.route('/po',methods=['GET','POST'])
def po():
    return render_template("dashboard.html")



