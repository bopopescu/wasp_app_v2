from flask import Flask,request,redirect,url_for,make_response,render_template,jsonify
from flask_cors import CORS
from flask_compress import Compress
from flask_assets import Environment,Bundle
from flask_mail import Mail,Message
from .api.authentication.routes import login_manager
from .api.authentication.model import check_refresh_token,check_valid_token,refresh_token
from .api.database.model import dynamodb_user_upload,get_all_items
from application import api
from application import site
from zappa.async import task
from .api.database.model import get_table_item,add_subscriber_list

js_comingsoon=Bundle('js/parallax.min.js','js/plugins.js','js/owl.carousel.min.js','js/scrollax.js','js/main.js',output='gen/mainJSComingSoon.js', filters="jsmin")

js=Bundle('js/functions/form.js','js/functions/facebook_login.js','js/plugins.js','js/isotope.pkgd.min.js',
          'js/jquery.easing.1.3.js','js/jquery.countdown.min.js','js/jquery.magnific-popup.min.js','js/owl.carousel.min.js','js/jquery.easypiechart.min.js','js/spectragram.min.js',
          'js/jquery.waypoints.min.js','js/scrollax.js','js/functions/load_campaign.js','js/main.js','js/functions/newsletter.js',output='gen/main.js', filters="jsmin")

css_comingsoon = Bundle('css/comingsoon/comingsoonpage.css','css/font-awesome.min.css','css/bootstrap.min.css','css/owl.carousel.min.css',
           'css/owl.theme.default.min.css','css/woocommerce.css','css/plugins.css','css/style.css','css/responsive.css',output='gen/mainCSSComingSoon.css',filters="cssmin")
css_comingsoon2 = Bundle('css/comingsoon/theCSSCM.css',output='gen/testCSS.css',filters="cssmin")

css=Bundle('css/iconfont.css','css/font-awesome.min.css','css/bootstrap.min.css','css/isotope.css','css/magnific-popup.css','css/owl.carousel.min.css',
           'css/owl.theme.default.min.css','css/woocommerce.css','css/plugins.css','css/style.css','css/responsive.css',output='gen/main.css',filters="cssmin")
#not in used js_dash causing error
js_dash=Bundle('css/dashboard/jquery/jquery.js','css/dashboard/popper.js/popper.js','css/dashboard/bootstrap/bootstrap.js','css/dashboard/perfect-scrollbar/js/perfect-scrollbar.jquery.js',
               'css/dashboard/moment/moment.js','css/dashboard/jquery-ui/jquery-ui.js','css/dashboard/jquery-switchbutton/jquery.switchButton.js','css/dashboard/peity/jquery.peity.js','css/dashboard/chartist/chartist.js',
               'css/dashboard/jquery.sparkline.bower/jquery.sparkline.min.js','css/dashboard/d3/d3.js','js/dashboard/bracket.js','js/dashboard/ResizeSensor.js','js/dashboard/dashboard.js'
               ,'css/dashboard/rickshaw/rickshaw.min.js',output='gen/main_dashboard.js',filters='jsmin')
css_dash=Bundle('css/dashboard/select2/css/select2.min.css','css/dashboard/datatables/jquery.dataTables.css','css/dashboard/font-awesome/css/font-awesome.css','css/dashboard/perfect-scrollbar/css/perfect-scrollbar.css','css/dashboard/jquery-switchbutton/jquery.switchButton.css',
                'css/dashboard/rickshaw/rickshaw.min.css','css/dashboard/chartist/chartist.css','css/dashboard/bracket.css',output='gen/main_dashboard.css',filters='cssmin')
js_secondary_market=Bundle('css/dashboard/jquery/jquery.js','css/dashboard/popper.js/popper.js','css/dashboard/bootstrap/bootstrap.js','css/dashboard/perfect-scrollbar/js/perfect-scrollbar.jquery.js',
                           'css/dashboard/moment/moment.js','css/dashboard/jquery-ui/jquery-ui.js','css/dashboard/jquery-switchbutton/jquery.switchButton.js','css/dashboard/peity/jquery.peity.js'
                           ,'css/dashboard/highlightjs/highlight.pack.js','css/dashboard/datatables/jquery.dataTables.js','css/dashboard/datatables-responsive/dataTables.responsive.js'
                           ,'css/dashboard/select2/js/select2.min.js','js/dashboard/bracket.js','js/functions/bond_caculator.js','js/functions/dashboard.js',output='gen/market_dashboard.js',filters='jsmin')
app = Flask(__name__)
app.config.update(
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'admin@wasp.finance',
    DEFAULT_MAIL_SENDER = 'admin@wasp.finance',
	MAIL_PASSWORD = 'Yennhan1*'
	)
login_manager.init_app(app)
assets = Environment(app)

assets.register('main_css',css)
assets.register('main_js',js)
assets.register('coming_soonJS',js_comingsoon)
assets.register('coming_soonCSS',css_comingsoon)
assets.register('dash_css',css_dash)
assets.register('dash_js',js_dash)
assets.register('secondary_js',js_secondary_market)

CORS(app)
Compress(app)
mail = Mail(app)
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
from application.api.calculator.routes import mod
from application.api.Graph.routes import mod
from application.api.email_send.routes import send_email
app.register_blueprint(api.authentication.routes.mod)
app.register_blueprint(site.routes.mod)
app.register_blueprint(api.about_us.routes.mod)
app.register_blueprint(api.portfolio.routes.mod)
app.register_blueprint(api.campaign.routes.mod)
app.register_blueprint(api.payment.routes.mod)
app.register_blueprint(api.calculator.routes.mod)
app.register_blueprint(api.Graph.routes.mod)

thelist=['leowyennhan@gmail.com','jeffreyhwc23@gmail.com']
"""
import boto3
def get_all_items():
    client   = boto3.resource('dynamodb', region_name="ap-southeast-1")
    table    = client.Table('newsletter')
    response = table.scan()
    list=[]
    for item in response['Items']:
        if item['status'] == 'new':
            list.append(item)
    return list
"""
@task
def send_mail(email):
    with app.app_context():
        msg = Message("Welcome to WASP",sender="admin@wasp.finance",recipients=[email])
        msg.html = render_template('early_signup.html')
        mail.send(msg)
    #return "Yeah"


@app.route("/subscribe", methods=['POST','GET'])
def subscribe():
    list = request.get_json()
    for item in list:
        if item['value'] != "":
            add_subscriber_list(item['value'])
            send_mail(item['value'])
            #run_the_email(item['value'])
            #add_item(item['value'])
    return jsonify({"success":"Thank You for Subscribing with Us, we will send you updates and early user privilege through your email soon."})




@app.route('/privacypolicy')
def get_privacy_policy():
    return render_template('privacypolicy.html')

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










