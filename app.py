from flask import Flask
from models import db  # import db from your models file

app = Flask(__name__)

# ===========================
# 🧠 MySQL Configuration
# ===========================
# Format: mysql+<driver>://<username>:<password>@<host>/<database_name>
user = "csv_user"
password = "CsvUser@1234"
database = "csv_db"
sql_file = "csv_db.sql"  # This file should exist in the same folder

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root@localhost/travel_db?unix_socket=/var/run/mysqld/mysqld.sock"

# Disable tracking modifications (not needed)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Import models to register them with SQLAlchemy
from models import User, Destinations, Accommodation, Transport, Booking


with app.app_context():
    db.create_all()
    print("✅ MySQL database and tables created successfully!")
