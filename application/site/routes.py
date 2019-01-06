from flask import Blueprint

mod = Blueprint('site',__name__)

@mod.route('/getstuff')
def get_stuff():
    return "{'you are in the api':'hello world'}"