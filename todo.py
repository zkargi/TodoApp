from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/zeynepkargi/Desktop/Todo App/todo.db"
db=SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add",methods=["POST"])
def TodoApp():
    title=request.form.get("title")
    newTodo=Todo(title=title,complete=False)
    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("index"))


class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80))
    complete=db.Column(db.Boolean)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)