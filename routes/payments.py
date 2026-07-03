from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify

from flask_login import login_required, current_user

from forms import PaymentPlanForm

from models import db
from models.student import Student
from models.payment_plan import PaymentPlan
from services.nomba_service import create_checkout_order


payments = Blueprint("payments", __name__)


@payments.route("/students/<int:student_id>/payment-plan", methods=["GET", "POST"])
@login_required
def create_payment_plan(student_id):

    student = Student.query.filter_by(
        id=student_id,
        user_id=current_user.id
    ).first_or_404()

    form = PaymentPlanForm()

    if form.validate_on_submit():

        payment_plan = PaymentPlan(
            total_fee=form.total_fee.data,
            due_date=form.due_date.data,
            student_id=student.id
        )

        db.session.add(payment_plan)
        db.session.commit()

        flash("Payment plan created successfully!")

        return redirect(url_for("students.list_students"))

    return render_template(
        "create_payment_plan.html",
        form=form,
        student=student
    )

@payments.route("/payment/<int:plan_id>/generate-link")
@login_required
def generate_payment_link(plan_id):

    plan = (
        PaymentPlan.query
        .join(Student)
        .filter(
            PaymentPlan.id == plan_id,
            Student.user_id == current_user.id
        )
        .first_or_404()
    )

    result = create_checkout_order(
        amount=plan.total_fee,
        customer_email=plan.student.parent_email,
        callback_url="https://google.com"
    )

    if result.get("code") != "00":

        flash("Failed to generate payment link.")

        return redirect(
            url_for("dashboard.payment_dashboard")
        )

    plan.nomba_order_reference = (
        result["data"]["orderReference"]
    )

    db.session.commit()

    return redirect(
        result["data"]["checkoutLink"]
    )

@payments.route("/webhook/nomba", methods=["POST"])
def nomba_webhook():

    signature = request.headers.get("nomba-signature")

    print("\n========== NOMBA WEBHOOK ==========")
    print("Signature:", signature)
    print("Data:", request.json)
    print("===================================\n")

    return jsonify({
        "success": True
    }), 200