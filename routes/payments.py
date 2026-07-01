from flask import Blueprint, render_template, redirect, url_for, flash

from flask_login import login_required, current_user

from forms import PaymentPlanForm

from models import db
from models.student import Student
from models.payment_plan import PaymentPlan


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