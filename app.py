from flask import Flask, jsonify, render_template
from utils import auth, db, ma


app = Flask(__name__, static_folder="statics")
app.json.ensure_ascii = False


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///structure.db"
db.init_app(app)
ma.init_app(app)


from structures.views import views
from structures.aggregations import views as agregations

app.register_blueprint(views, url_prefix="/api/v1/cities")
app.register_blueprint(agregations, url_prefix="/api/v1/products")


@app.route("/")
def index():
    html = render_template("index.html")
    return html


@auth.get_password
def get_password(username):
    if username == "student":
        return "dvfu"
    return None


@auth.error_handler
def unauthorized():
    return jsonify({"error": "Unauthorized access"}), 401


if __name__ == "__main__":
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000)
