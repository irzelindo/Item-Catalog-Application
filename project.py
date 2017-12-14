from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, get_flashed_messages
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

# Connect to Database and create database session
engine = create_engine('sqlite:///itemcatalogs.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/catalog/')
def showCatalogs():
    catalogs = session.query(Catalog).all()
    items = session.query(Item, Catalog).join(Catalog).filter(
        Catalog.id == Item.catalog_id).order_by(Item.date.desc()).limit(10)
    return render_template('catalogs.html', catalogs=catalogs, items=items)


@app.route('/catalog/new/', methods=['GET', 'POST'])
def newCatalog():
    if request.method == 'POST':
        if request.form['catalog']:
            newCatalog = Catalog(name=request.form['catalog'])
            session.add(newCatalog)
            session.commit()
            flash("{} added to Catalogs".format(request.form['catalog']))
            return redirect(url_for('showCatalogs'))
        else:
            flash("Cannot create empty catalog")
            return render_template('newCatalog.html')
    else:
        return render_template('newCatalog.html')


@app.route('/catalog/<int:catalog_id>/edit/', methods=['GET', 'POST'])
def editCatalog(catalog_id):
    catalog = session.query(
        Catalog).filter_by(id=catalog_id).one()
    catalogBefore = catalog.name
    if request.method == 'POST':
        if request.form['catalog']:
            catalog.name = request.form['catalog']
            flash("Catalog {} successfully edited to {}".format(
                catalogBefore, catalog.name))
            return redirect(url_for('showCatalogs'))
        else:
            flash("Nothing Changed")
            return redirect(url_for('showItems', catalog_id=catalog.id))
    else:
        return render_template('editCatalog.html', catalog=catalog)


@app.route('/catalog/<int:catalog_id>/delete/')
def deleteCatalog(catalog_id):
    catalog = session.query(
        Catalog).filter_by(id=catalog_id).one()
    session.delete(catalog)
    flash("Catalog {} successfully deleted".format(catalog.name))
    session.commit()
    return redirect(url_for('showCatalogs'))


@app.route('/catalog/<int:catalog_id>/items/')
def showItems(catalog_id):
    catalog = session.query(Catalog).filter_by(id=catalog_id).one()
    items_catalog = session.query(Item).filter_by(
        catalog_id=catalog_id).all()
    return render_template('showItems.html', catalog=catalog, items=items_catalog)


@app.route('/catalog/newItem/', methods=['GET', 'POST'])
def newItem():
    catalogs = session.query(Catalog).all()
    if request.method == 'POST':
        catalog = session.query(Catalog).filter_by(
            name=request.form['category']).one()
        if request.form['title'] and request.form['category'] and request.form['description']:
            newItem = Item(title=request.form['title'],
                           description=request.form['description'], catalog_id=catalog.id)
            session.add(newItem)
            session.commit()
            flash("New Item added to {} Catalog".format(catalog.name))
            return redirect(url_for('showItems', catalog_id=catalog.id))
        else:
            flash("Couldn't create new Item")
            return render_template('newItem.html', catalog=catalog)
    else:
        return render_template('newItem.html', catalogs=catalogs)


@app.route('/catalog/<int:catalog_id>/items/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(catalog_id, item_id):
    catalogs = session.query(Catalog).all()
    catalog = session.query(
        Catalog).filter_by(id=catalog_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    itemBefore = item.title
    if request.method == 'POST':
        if request.form['title'] and request.form['category'] and request.form['description']:
            item.title = request.form['title']
            item.description = request.form['description']
            item.catalog_id = catalog.id
            flash("{} successfully edited".format(
                itemBefore))
            return redirect(url_for('showItems', catalog_id=catalog.id))
        else:
            flash("Nothing Changed")
            return redirect(url_for('showItems', catalog_id=catalog.id))
    else:
        return render_template('editItem.html', item=item, catalogs=catalogs, catalog=catalog)


@app.route('/catalog/<int:catalog_id>/items/<int:item_id>/')
def itemDescription(catalog_id, item_id):
    catalog = session.query(Catalog).filter_by(id=catalog_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('itemDescription.html', item=item, catalog=catalog)


@app.route('/catalog/<int:catalog_id>/items/<int:item_id>/delete/')
def deleteItem(catalog_id, item_id):
    item = session.query(
        Item).filter_by(id=item_id).one()
    session.delete(item)
    flash("{} successfully deleted".format(item.title))
    session.commit()
    return redirect(url_for('showItems', catalog_id=catalog_id))


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
