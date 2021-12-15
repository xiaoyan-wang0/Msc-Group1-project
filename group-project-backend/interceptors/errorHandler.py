# -*- coding: utf-8 -*-
from application import app

#error process
@app.errorhandler( 404 )
def error_404( e ):
    return "404 not found"