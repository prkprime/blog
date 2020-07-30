from app import app

'''
set debug=Falsee bellow when deploying to prod
'''
app.run(host='0.0.0.0', debug=True)