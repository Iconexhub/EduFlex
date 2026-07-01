from models import db


class PaymentPlan(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    total_fee = db.Column(
        db.Integer,
        nullable=False
    )

    amount_paid = db.Column(
        db.Integer,
        default=0
    )

    due_date = db.Column(
        db.String(50),
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    nomba_order_reference = db.Column(
        db.String(100),
        nullable=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("student.id"),
        nullable=False
    )