from flask import Blueprint, render_template

from .data import MODEL_PREDICTIONS

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html", model_predictions=MODEL_PREDICTIONS)
