from flask import (
    Blueprint,
    request,
    jsonify
)

from modules.calculator.financial.simple_interest import (calculate_simple_interest)
from modules.calculator.financial.compound_interest import (calculate_compound_interest)
from modules.calculator.financial.emi import (calculate_emi)
from modules.calculator.general.discount import (calculate_discount)

calculator_bp = Blueprint(
    "calculator",
    __name__,
)

# Simple Interest API
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

#Compound Interest API
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

#EMI API
@calculator_bp.route(
    "/calculate/emi",
    methods=["POST"]
)
def emi():
    data = request.get_json()

    result = calculate_emi(data)

    return jsonify(result)

# Discount API
@calculator_bp.route(
    "/calculate/discount",
    methods=["POST"]
)
def discount():
    data = request.get_json()

    result = calculate_discount(data)

    return jsonify(result)