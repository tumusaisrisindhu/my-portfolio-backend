from flask import (
    Blueprint,
    request,
    jsonify
)

from modules.calculator.financial.simple_interest import (
    calculate_simple_interest
)

calculator_bp = Blueprint(
    "calculator",
    __name__,
)


@calculator_bp.route(
    "/calculate/simple-interest",
    methods=["POST"]
)
def simple_interest():
    data = request.get_json()

    result = (
        calculate_simple_interest(data)
    )

    return jsonify(result)