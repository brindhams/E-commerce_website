from flask import render_template,session, request,redirect,url_for,flash
from shop import db, app, photos
from .models import Brand, Category, Addproduct
from .forms import Addproducts

import secrets




@app.route('/addbrand', methods=['GET','POST'])
def addbrand():
    # if 'email' not in session:
    #     flash(f'please login first', 'danger')
    #     return redirect(url_for('Login'))
    if request.method=="POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} was added to your database', 'success')
        db.session.commit()
        return redirect(url_for('addbrand'))

    
    return render_template('products/addbrand.html',brands='brands')


@app.route('/addcat', methods=['GET','POST'])
def addcat():
    if request.method=="POST":
        getbrand = request.form.get('category')
        cat = Category(name=getbrand)
        db.session.add(cat)
        flash(f'The Category {getbrand} was added to your database', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addbrand.html')

@app.route('/addproduct', methods=['GET','POST'])
def addproduct():
    brands=Brand.query.all()
    category = Category.query.all()
    form = Addproducts(request.form)
    if request.method == "POST":
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.color.data
        desc = form.description.data
        brand = request.form.get('brand')
        category = request.form.get('category')

        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        addpro = Addproduct(name=name,price=price,discount=discount,stock=stock,colors=colors,desc=desc,brand_id=brand, category_id=category,image_1=image_1,image_2=image_2,image_3=image_3)
        db.session.add(addpro)
        flash(f'The product {name} has been added to your database', 'success')
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('products/addproduct.html', form= form, title="Add Product Page", brands=brands, category= category)


