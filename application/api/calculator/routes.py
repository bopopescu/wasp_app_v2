from flask import Blueprint,jsonify,request
from .model import bond_price

mod = Blueprint('calculation',__name__)


@mod.route("/calculate_bond_price",methods=['POST'])
def route_bp():
    par_val           = request.form['parv']
    time_period       = request.form['timeperiod']
    yield_to_maturity = request.form['ytm']
    coupon            = request.form['coupon']
    freq              = request.form['freq']
    the_yield         = int(yield_to_maturity)/100
    b_pr              = bond_price(int(par_val),int(time_period),the_yield,int(coupon),int(freq))
    b_pr = round(b_pr,2)
    return jsonify({'price':b_pr})

