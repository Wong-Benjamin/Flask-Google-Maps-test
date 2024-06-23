"""
Simple server primarily derived from Google's own guides.
"""
import os

from flask import Flask, render_template

# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')

# renders the map displaying portion of this mini project.
def renderMap():

    # holdovers from tutorial that I'll just keep around for future learning...
    # Get Cloud Run environment variables.
    # service = os.environ.get('K_SERVICE', 'Unknown service')
    # revision = os.environ.get('K_REVISION', 'Unknown revision')

    # ...just render the new html site I've written.
    return render_template('map.html')

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')