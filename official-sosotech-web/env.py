import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "yz6{Teyyvejqfij{TQx;s,Z#O7g~")

# MYSQL Database
os.environ.setdefault("SQLALCHEMY_DATABASE_URI", "mysql+pymysql://root:Depay200$@localhost/sosotech")

# Gmail Configuration
os.environ.setdefault("MAIL_SERVER", "smtp.gmail.com")
os.environ.setdefault("MAIL_PORT", "587")
os.environ.setdefault("MAIL_USERNAME", "sosotechglobal@gmail.com")
os.environ.setdefault(
    "MAIL_PASSWORD", "tthtyfshxjvwacsm")

