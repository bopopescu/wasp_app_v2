from application import app
app.jinja_env.cache = {}
app.run(threaded=True)