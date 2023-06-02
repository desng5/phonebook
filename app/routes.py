from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import Entry
from app.models import Person

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/entry', methods=["GET", "POST"])
def entry():

    form = Entry()

    if form.validate_on_submit():

        print('Your information has been submited!')

        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_num = form.phone_num.data
        address = form.address.data
        print(first_name, last_name, phone_num, address)

        add_info = Person(first_name=first_name, last_name=last_name,
                        phone_num=phone_num, address=address)

    
        db.session.add(add_info)
        db.session.commit()

        flash(f"{first_name}{last_name} has been added!", 'success')
        return redirect(url_for('index'))

    return render_template('info_entry.html', form=form)
