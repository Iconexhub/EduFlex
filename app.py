from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user
from config import Config
from models import db
from models.user import User
from models.student import Student
from models.payment_plan import PaymentPlan
from routes.auth import auth
from routes.students import students
from routes.payments import payments
from routes.dashboard import dashboard

app = Flask(__name__)
login_manager = LoginManager()

# Load settings from config.py
app.config.from_object(Config)

# Connect SQLAlchemy to Flask
db.init_app(app)

login_manager.init_app(app)
login_manager.login_view = "auth.login"

app.register_blueprint(auth)
app.register_blueprint(students)
app.register_blueprint(payments)
app.register_blueprint(dashboard)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))    


@app.route("/")
def home():

    if current_user.is_authenticated:

        total_students = Student.query.filter_by(
            user_id=current_user.id
        ).count()

        total_plans = (
            PaymentPlan.query
            .join(Student)
            .filter(Student.user_id == current_user.id)
            .count()
        )

        return render_template(
            "home.html",
            total_students=total_students,
            total_plans=total_plans
        )

    return render_template("landing.html")


if __name__ == "__main__":
    app.run(debug=True)