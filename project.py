from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Catalog, Item
from flask import session as login_session

import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

# Show all Catalogs


@app.route('/')
@app.route('/catalog/')
def showCatalogs():
    return 'All catalogs'


@app.route('/catalog/new/')
def newcatalog():
    return 'New catalog'


@app.route('/catalog/<int:catalog_id>/edit/')
def editCatalog(catalog_id):
    return 'Edit {}'.format(catalog_id)


@app.route('/catalog/<int:catalog_id>/delete/')
def deleteCatalog(catalog_id):
    return 'Delete Catalog {}'.format(catalog_id)


@app.route('/catalog/<int:catalog_id>/items/')
def showItems(catalog_id):
    return 'Items from catalog {}'.format(catalog_id)


@app.route('/catalog/<int:catalog_id>/items/new/')
def newItem(catalog_id):
    return 'New Item for catalog {}'.format(catalog_id)


@app.route('/catalog/<int:catalog_id>/items/<int:item_id>/edit/')
def editItem(catalog_id, item_id):
    return 'Edit Item {} from catalog {}'.format(item_id, catalog_id)


@app.route('/catalog/<int:catalog_id>/items/<int:item_id>/delete/')
def deleteItem(catalog_id, item_id):
    return 'Delete Item {} from catalog {}'.format(item_id, catalog_id)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
