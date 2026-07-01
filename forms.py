from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(FlaskForm):
    full_name = StringField(
        "Full Name",
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=6)
        ]
    )

    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Login")

class StudentForm(FlaskForm):

    full_name = StringField(
        "Student Full Name",
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

    class_name = StringField(
        "Class",
        validators=[
            DataRequired()
        ]
    )

    parent_email = StringField(
        "Parent Email",
        validators=[
            DataRequired(),
            Email()
        ]
    )

    submit = SubmitField("Add Student")


class PaymentPlanForm(FlaskForm):

    total_fee = IntegerField(
        "Total School Fee (₦)",
        validators=[
            DataRequired()
        ]
    )

    due_date = StringField(
        "Due Date (Example: 31 August 2026)",
        validators=[
            DataRequired()
        ]
    )

    submit = SubmitField("Create Payment Plan")