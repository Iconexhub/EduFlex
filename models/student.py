from models import db


class Student(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    full_name = db.Column(
        db.String(100),
        nullable=False
    )

    class_name = db.Column(
        db.String(50),
        nullable=False
    )

    parent_email = db.Column(
        db.String(120),
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    payment_plans = db.relationship(
        "PaymentPlan",
        backref="student",
        lazy=True
    )