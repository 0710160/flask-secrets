from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators


class MyForm(FlaskForm):
    email = StringField(label="Email", validators=[validators.InputRequired(),
                                                   validators.Email()])
    password = PasswordField(label="Password", validators=[validators.InputRequired(),
                                                           validators.Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "some-secret-key"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = MyForm()
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug=True)