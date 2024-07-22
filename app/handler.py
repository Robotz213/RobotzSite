from flask import url_for, redirect
from app import app


@app.errorhandler(404)
def page_not_found(e):
    
    return redirect(url_for('index'))

@app.errorhandler(403)
def not_allowed(e):
    
    return redirect(url_for('index'))

@app.errorhandler(405)
def not_allowed(e):

    return redirect(url_for('index'))

@app.errorhandler(500)
def internal_error(e):
    
    return redirect(url_for('index'))

    
    