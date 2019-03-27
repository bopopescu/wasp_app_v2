from flask import Blueprint,render_template,request,jsonify
from ..database.model import get_table_item,add_subscriber_list

mod = Blueprint('campaign',__name__)


@mod.route("/campaign_page/<the_id>",methods=['GET','POST'])
def view_campaign(the_id):
    prod=get_table_item(the_id)
    return render_template('product_detail.html',products=prod)




