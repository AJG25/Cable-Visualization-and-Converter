# app.py
import os
import json
from dotenv import load_dotenv
from flask import Flask, render_template, request, g, jsonify
from flask_caching import Cache
from flask_login import LoginManager, login_required, current_user
from user import User
from db_utils import get_db

# Import the API Blueprint
from api_bp import api_bp  # Make sure this import is correct
from auth import auth_bp  # Existing Blueprint
from converter_bp import converter_bp  # Existing Blueprint
from profile_bp import profile_bp  # Existing Blueprint

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "fallback_development_key")
app.config["CACHE_TYPE"] = "simple"
app.config["CACHE_DEFAULT_TIMEOUT"] = 300

cache = Cache(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth_bp.login"  # Adjust if necessary

@login_manager.user_loader
def load_user(user_id):
    conn = get_db()
    user_row = conn.execute(
        'SELECT * FROM User WHERE user_id = ?',
        (int(user_id),)
    ).fetchone()
    if user_row:
        return User(
            user_id=user_row["user_id"],
            name=user_row["name"],
            email=user_row["email"],
            password=user_row["password"],
            role=user_row["role"]
        )
    return None

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db:
        db.close()

# Register your blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(converter_bp)
app.register_blueprint(profile_bp)

# Register the API Blueprint with the '/api' prefix
app.register_blueprint(api_bp)

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

if __name__ == "__main__":
    os.makedirs(os.path.join("static", "uploads"), exist_ok=True)
    app.run(debug=True)
