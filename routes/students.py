from flask import Blueprint, render_template, redirect, url_for, flash

from flask_login import login_required, current_user

from forms import StudentForm

from models import db
from models.student import Student


students = Blueprint("students", __name__)


@students.route("/students/add", methods=["GET", "POST"])
@login_required
def add_student():

    form = StudentForm()

    if form.validate_on_submit():

        student = Student(
            full_name=form.full_name.data,
            class_name=form.class_name.data,
            parent_email=form.parent_email.data,
            user_id=current_user.id
        )

        db.session.add(student)
        db.session.commit()

        flash("Student added successfully!")

        return redirect(url_for("students.list_students"))

    # DEBUG: Print validation errors if form submission fails
    if form.is_submitted():
        print("FORM ERRORS:", form.errors)

    return render_template(
        "add_student.html",
        form=form
    )


@students.route("/students")
@login_required
def list_students():

    student_list = Student.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "students.html",
        students=student_list
    )