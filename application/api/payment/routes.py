from flask import Blueprint,request,redirect,url_for,jsonify,render_template,flash
from ..authentication.routes import login_required
from ..database.model import update_list_item, update_prod_item,update_percentage,write_trans_item,get_transactions_receipt,update_invest_amount
mod = Blueprint('payment',__name__)


@mod.route('/execute',methods=['GET','POST'])
def execute_payment():
    payment=request.json['t_data']
    info = request.json['p_data']
    trans_id=payment[0]['related_resources'][0]['sale']['id']
    user_id=request.cookies.get('sub')
    try:
        update_list_item(user_id,payment)
        update_prod_item(payment)
        product_name = payment[0]['item_list']['items'][0]['name']
        write_trans_item(user_id,payment,info)
        update_percentage(product_name)
        update_invest_amount(user_id,payment)
    except:
        print("Wrong")
    return jsonify({"payment": payment,"user_info":info,"t_id":trans_id})


@mod.route('/receipt/<trans_id>',methods=['GET','POST'])
def receipt_post(trans_id):
    c=get_transactions_receipt(trans_id)
    return render_template("receipt.html",content=c)




