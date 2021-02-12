from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from controllers.web_controller import get_user_by_email


class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    file = FileField()
    submit = SubmitField("Sign up")

    def validate_email(self, email):
        user = get_user_by_email(email.data)
        if user:
            raise ValidationError('The email is already taken.')


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")


class PostForm(FlaskForm):
    description = StringField("Description")
    file = FileField(validators=[DataRequired(), FileAllowed(['jpg', 'png', 'gif'], 'Filetype not allowed!')]) #test
    submit = SubmitField("Submit")


class CommentForm(FlaskForm):
    comment = StringField("Comment")
    submit = SubmitField("Submit")


class UpdateProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Update')



