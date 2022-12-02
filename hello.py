from flask import Flask, render_template, request, jsonify
import json
import logging
import os
import atexit
import animar

app = Flask(__name__, static_url_path='')

# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))


@app.route('/')
def root():
    temp = animar.animar()
    return temp


# @app.route('/agentes')
# def root2():
#    return jsonify([{"message": "Nacho"}])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
