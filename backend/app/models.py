from app.database import db


class MateInOne(db.Model):
    __tablename__ = "base_exercise"

    id = db.Column(db.Integer, primary_key=True)

    white_pos = db.Column(db.String(100), nullable=False)
    black_pos = db.Column(db.String(100), nullable=False)

    is_white_to_move = db.Column(db.Boolean, nullable=False)

    answer = db.Column(db.String(100), nullable=False)
