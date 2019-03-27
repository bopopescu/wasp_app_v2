from flask import Blueprint,make_response,request,redirect,url_for,jsonify,render_template,flash
from random import sample
from math import exp
from math import log

mod = Blueprint('graph',__name__)


@mod.route('/graph_data',methods=['POST','GET'])
def graph_data():
    firstlist=[100]
    secondlist=[100]
    thirdlist = [100]
    thelist = []
    fourthlist = [100]
    for i in range(1,31):
        thelist.append("YEAR "+str(i))
    for i in range(1,30):
            theNewCR = (firstlist[i-1]) + (firstlist[i-1] * 0.06) + 100
            the2ndCR = (secondlist[i-1]) + (secondlist[i-1] * 0.03) + 100
            the3rdCR = (thirdlist[i-1] + (thirdlist[i-1] * 0.01) + 100)
            firstlist.append(round(theNewCR))
            secondlist.append(round(the2ndCR))
            thirdlist.append(round(the3rdCR))
            fourthlist.append(fourthlist[i-1]+100)
    return jsonify({'number':[firstlist,secondlist,thirdlist,thelist,fourthlist]})




