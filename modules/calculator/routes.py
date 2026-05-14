from flask import (
    Blueprint,
    request,
    jsonify
)

from modules.calculator.financial.simple_interest import (
    calculate_simple_interest
)

from modules.calculator.financial.compound_interest import (
    calculate_compound_interest
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

@calculator_bp.route(
    "/calculate/compound-interest",
    methods=["POST"]
)
def compound_interest():
    data = request.get_json()

    result = (
        calculate_compound_interest(
            data
        )
    )

    return jsonify(result)