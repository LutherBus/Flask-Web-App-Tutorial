from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import time
from flask import redirect, url_for, current_app
from unlock import move_servo

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
    return render_template("home.html", user=current_user)

@views.route('/button_clicked', methods=['POST'])
def button_clicked():
    move_servo(90)
    time.sleep(3)
    return redirect(url_for('auth.login'))