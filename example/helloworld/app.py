# -*- coding: utf-8 -*-
"""Sample flask app."""
from random import randrange

from flask import Flask, render_template

from netCDF4 import Dataset

app = Flask(__name__)


@app.route('/')
def welcome():
    """Welcome page handler."""
    nc_file = './madis-maritime.nc'
    ds = Dataset(nc_file)
    variables = list(ds.variables.keys())
    varname = variables[randrange(0, len(variables))]
    v = ds.variables[varname]
    if v.shape[0] > 0:
        val = str(v[randrange(0, v.shape[0])])
    else:
        val = '[bad shape]'

    return render_template('welcome.html',
                           filename=nc_file,
                           variable=varname,
                           value=val)


if __name__ == "__main__":
    app.run()
