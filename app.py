from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import traceback
import os
from dotenv import load_dotenv

try:
    # Load environment variables
    load_dotenv()

    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "your-secret-key-here")

    class ContactForm(FlaskForm):
        name = StringField("Name", validators=[DataRequired()])
        email = StringField("Email", validators=[DataRequired(), Email()])
        subject = StringField("Subject", validators=[DataRequired()])
        text = TextAreaField("Message", validators=[DataRequired()])
        timestamp = HiddenField("Timestamp")
        submit = SubmitField("Send Message")

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/experience/")
    def experience():
        return render_template("experience.html")

    @app.route("/projects/")
    def projects():
        return render_template("projects.html")

    @app.route("/education/")
    def education():
        return render_template("education.html")

    @app.route("/other/")
    def other():
        return render_template("other.html")

    @app.route("/contact/", methods=["GET", "POST"])
    def contact_form():
        form = ContactForm()
        if request.method == "POST" and form.validate_on_submit():
            # Set timestamp
            form.timestamp.data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                # Email configuration - using environment variables
                sender_email = os.getenv("SENDER_EMAIL")
                sender_password = os.getenv("SENDER_PASSWORD")
                receiver_email = os.getenv("SENDER_EMAIL")

                # Check if email credentials are configured
                if not sender_email or not sender_password:
                    flash(
                        "Email service not configured. Please contact the administrator.",
                        "error",
                    )
                    return redirect(url_for("contact_form"))

                # Create message
                msg = MIMEMultipart()
                msg["From"] = sender_email
                msg["To"] = receiver_email
                msg["Subject"] = f"Contact Form: {form.subject.data}"

                # Email body
                body = f"""
                New contact form submission:
                
                Name: {form.name.data}
                Email: {form.email.data}
                Subject: {form.subject.data}
                Timestamp: {form.timestamp.data}
                
                Message:
                {form.text.data}
                """

                msg.attach(MIMEText(body, "plain"))

                # Send email
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, sender_password)
                text = msg.as_string()
                server.sendmail(sender_email, receiver_email, text)
                server.quit()

                flash("Your message has been sent successfully!", "success")
                return redirect(url_for("contact_form"))

            except Exception as e:
                flash(
                    "There was an error sending your message. Please try again.",
                    "error",
                )
                print(f"Email error: {e}")

        return render_template("contact_form.html", form=form)

except Exception as e:
    print(e)
    print(traceback.format_exc())

if __name__ == "__main__":
    app.run()
