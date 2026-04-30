from flask import Flask
from flask_cors import CORS

from modules.converters.routes import converter_bp

app = Flask(__name__)
CORS(app)

# register modules
app.register_blueprint(converter_bp)


if __name__ == "__main__":
    app.run(debug=True)