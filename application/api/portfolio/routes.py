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
    #print(products)
    return render_template("dashboard_portfolio_section.html",products=products)
    #return jsonify({'data':render_template("dashboard_portfolio_section.html",product=products)})

@mod.route('/view_receipt/<the_id>',methods=['GET','POST'])
def view_receipt(the_id):
    the_list=get_transactions_receipt(the_id)
    print(the_list)
    return render_template('receipt.html',content=the_list)

@mod.route('/po',methods=['GET','POST'])
def po():
    return render_template("dashboard.html")



