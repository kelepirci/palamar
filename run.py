#!../venv/bin/python
# -*- coding: utf-8 -*-

from dash import dash

# run the dash application
if __name__ == '__main__':
    dash.run(debug=True, host='0.0.0.0', port=8000)