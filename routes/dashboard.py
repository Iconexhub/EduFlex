from flask import Blueprint, render_template

from flask_login import login_required, current_user

from models.payment_plan import PaymentPlan
from models.student import Student


dashboard = Blueprint(
    "dashboard",
    __name__
)


@dashboard.route("/payment-plans")
@login_required
def payment_plans():

    plans = (
        PaymentPlan.query
        .join(Student)
        .filter(Student.user_id == current_user.id)
        .all()
    )

    return render_template(
        "payment_plans.html",
        plans=plans
    )