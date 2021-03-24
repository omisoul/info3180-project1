"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db

from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename

from .forms import PropertyForm
from .models import Property

def get_uploaded_images():
    # image_list = []
    file_list = []
    rootdir = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            # image_list.append(os.path.join(subdir,file))
            file_list.append(file)
    return file_list
            


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Info Project 1")

@app.route('/property', methods=['GET', 'POST'])
def add_property():
    propertyForm = PropertyForm()

    if request.method == 'POST':
        if propertyForm.validate_on_submit():
            title = propertyForm.title.data
            noBedrooms = propertyForm.noBedrooms.data
            noBathrooms = propertyForm.noBathrooms.data
            location = propertyForm.location.data
            description = propertyForm.description.data
            price = propertyForm.price.data
            propertyType = propertyForm.propertyType.data

            photo = propertyForm.photoFileName.data
            photoFileName = secure_filename(photo.filename)
            photo.save(os.path.join(
            app.config['UPLOAD_FOLDER'], photoFileName
            ))

            propertyInfo = Property(title,description,noBedrooms,noBathrooms,price,propertyType,location,photoFileName)
            db.session.add(propertyInfo)
            db.session.commit()
            flash('File Saved', 'success')
            return redirect(url_for('properties'))

    flash_errors(propertyForm)
    return render_template('add_property.html', propertyForm=propertyForm)

@app.route('/properties')
def properties():
    propertiesList = Property.query.all()
    return render_template('properties.html', propertiesList=propertiesList)

@app.route('/properties/<propertyid>')
def get_property_info(propertyid):
    propertyInfo = db.session.query(Property).get(propertyid)
    return render_template('view_property.html', propertyInfo=propertyInfo)

@app.route("/uploads/<filename>")
def get_image(filename):
    root_dir = os.getcwd()
    path = os.path.join(root_dir, app.config['UPLOAD_FOLDER'])
    return send_from_directory(path, filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
