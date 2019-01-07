from flask import Flask,request,redirect,url_for,make_response
from flask_cors import CORS
from flask_compress import Compress
from flask_assets import Environment,Bundle
from .api.authentication.routes import login_manager
from .api.authentication.model import check_refresh_token,check_valid_token,refresh_token
from .api.database.model import dynamodb_user_upload,get_all_items
from flask_paranoid import Paranoid
import datetime
from application import api
from application import site


js=Bundle('js/functions/form.js','js/functions/facebook_login.js','js/plugins.js','js/isotope.pkgd.min.js',
          'js/jquery.easing.1.3.js','js/jquery.countdown.min.js','js/jquery.magnific-popup.min.js','js/owl.carousel.min.js','js/parallax.min.js','js/jquery.easypiechart.min.js','js/spectragram.min.js',
          'js/jquery.waypoints.min.js','js/scrollax.js','js/functions/load_campaign.js','js/main.js',output='gen/main.js', filters="jsmin")

css=Bundle('css/iconfont.css','css/font-awesome.min.css','css/bootstrap.min.css','css/isotope.css','css/magnific-popup.css','css/owl.carousel.min.css',
           'css/owl.theme.default.min.css','css/woocommerce.css','css/plugins.css','css/plugins.css','css/style.css','css/responsive.css',output='gen/main.css',filters="cssmin")
app = Flask(__name__)
login_manager.init_app(app)
assets = Environment(app)

assets.register('main_css',css)
assets.register('main_js',js)

CORS(app)
Compress(app)
app.secret_key = 'TheSecretSecretKey'
app.config['SESSION_TYPE'] = 'filesystem'
app.config["USE_CLIENT_SECRET"]= 'True'
#app.config['COGNITO_APP_WITH_SECRET_ID']='2jc7148a2h54itqn97qatrjg91'
#paranoid = Paranoid(app)
#paranoid.redirect_view = '/'

from application.api.authentication.routes import mod
from application.api.about_us.routes import mod
from application.site.routes import mod
from application.api.portfolio.routes import mod
from application.api.campaign.routes import mod
from application.api.payment.routes import mod
app.register_blueprint(api.authentication.routes.mod)
app.register_blueprint(site.routes.mod)
app.register_blueprint(api.about_us.routes.mod)
app.register_blueprint(api.portfolio.routes.mod)
app.register_blueprint(api.campaign.routes.mod)
app.register_blueprint(api.payment.routes.mod)



@app.before_request
def reset_token():
    if "the_token" in request.cookies:
        r_token=request.cookies['refresh_token']
        a_token=request.cookies['the_token']
        outcome=check_valid_token(a_token)
        if outcome is True:
            token1=refresh_token(r_token)
            token1=token1['AuthenticationResult']['AccessToken']
            resp = make_response(redirect(url_for('authentication.homepage')))
            resp.set_cookie("the_token", token1)
            return resp
        else:
            pass
    else:
        pass











