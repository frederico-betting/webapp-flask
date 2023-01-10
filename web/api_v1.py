from flask import Blueprint, render_template, session,abort
import config

api_v1 = Blueprint('api_v1',__name__)

ENDPOINT = '/api/v1'

@api_v1.route(f'{ENDPOINT}/health')
def health():
    response = {
        "name": "webapp-flask",
        "apiVersion": 'v1',
        "version": config.VERSION
    }
    return response
