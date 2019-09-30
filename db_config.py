from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = '<database-user>'
app.config['MYSQL_DATABASE_PASSWORD'] = '<database-password>'
app.config['MYSQL_DATABASE_DB'] = '<database-name>'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
