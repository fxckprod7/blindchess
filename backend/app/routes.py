from flask import Blueprint, request, jsonify

from app.database import db
from app.models import MateInOne

bp = Blueprint("api", __name__)

@bp.route("/mate-in-one")
def mate_in_one():
    exercise = MateInOne.query.get(1)

    return jsonify(
        {
            "status": "success",
            "data": {
                "white_pos": exercise.white_pos,
                "black_pos": exercise.black_pos,
                "is_white_to_move": exercise.is_white_to_move,
                "answer": exercise.answer
            }
        }
    ), 200

@bp.route("/create")
def create() -> dict:
    exercise = MateInOne(
        white_pos="Kg1Ph2Pg2Pf2Re1",
        black_pos="Kg8Ph7Pg7Pf7Qh5",
        is_white_to_move=True,
        answer="Re8"
    )

    db.session.add(exercise)
    db.session.commit()

    return {"status": "success"}
