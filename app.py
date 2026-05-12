from flask import Flask
from flask_cors import CORS

from modules.converters.routes import converter_bp
from modules.todo.routes import todo_bp
from modules.games.housie.routes import housie_bp
from modules.games.tictactoe.routes import tic_tac_toe_bp
from modules.calculator.routes import calculator_bp

app = Flask(__name__)
CORS(app)

# register modules
app.register_blueprint(converter_bp)
app.register_blueprint(todo_bp)
app.register_blueprint(housie_bp)
app.register_blueprint(tic_tac_toe_bp)
app.register_blueprint(calculator_bp)


if __name__ == "__main__":
    app.run(debug=True)