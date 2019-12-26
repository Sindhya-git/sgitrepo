from flask import Flask, render_template, json, request, session, redirect
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
from functools import wraps
import os

#Initialize flask
application = Flask(__name__)
# Config MySQL
mysql = MySQL()
application.config['MYSQL_HOST']  = "custom-mysql.gamification.svc.cluster.local"
application.config['MYSQL_USER']  = "xxuser"
application.config['MYSQL_PASSWORD'] = "welcome1"
application.config['MYSQL_DB']    = "sampledb"
application.config['MYSQL_PORT']  = int('3306')
application.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize the app for use with this MySQL class
mysql.init_app(application)


@application.route("/")
def home_page():
  if 'view' in request.args:
    item_number= request.args['view']
    print ("item number is :", item_number)
    cur2 = mysql.connection.cursor()
    cur2.execute("SELECT s.ITEM_NUMBER, s.DESCRIPTION,s.LONG_DESCRIPTION, s.SKU_ATTRIBUTE_VALUE1,s.SKU_ATTRIBUTE_VALUE2,p.LIST_PRICE,p.DISCOUNT FROM XXIBM_PRODUCT_SKU s INNER JOIN XXIBM_PRODUCT_PRICING p WHERE s.ITEM_NUMBER=p.ITEM_NUMBER and s.ITEM_NUMBER=%s LIMIT 1", (item_number,))
    product1 = cur2.fetchall()
    print("product1 is :",product1)
    return render_template('product_detail.html', prdtdetail=product1)
  else:
    print("inside home page",)  
    cur1 = mysql.connection.cursor()
    cur1.execute("SELECT s.ITEM_NUMBER, s.DESCRIPTION,s.LONG_DESCRIPTION, s.SKU_ATTRIBUTE_VALUE1,s.SKU_ATTRIBUTE_VALUE2,p.LIST_PRICE,p.DISCOUNT FROM XXIBM_PRODUCT_SKU s INNER JOIN XXIBM_PRODUCT_PRICING p WHERE s.ITEM_NUMBER=p.ITEM_NUMBER LIMIT 25")
    shirts = cur1.fetchall()
 # Close Connection
    cur1.close()
    return render_template('home.html', shirts=shirts)
  
@application.route("/women")
def womens_page():
  print ("in womens page",)
  if 'view' in request.args:
    bname = request.args['view']
    print ("brand name is :", bname)
    if bname == 'Reflex':
      bname = 'Reflex Women'
    curbw = mysql.connection.cursor()
    query1 = "SELECT s.ITEM_NUMBER, s.DESCRIPTION,s.LONG_DESCRIPTION, s.SKU_ATTRIBUTE_VALUE1,s.SKU_ATTRIBUTE_VALUE2,p.LIST_PRICE,p.DISCOUNT"
    query2 = " FROM XXIBM_PRODUCT_SKU s INNER JOIN XXIBM_PRODUCT_PRICING p WHERE s.ITEM_NUMBER=p.ITEM_NUMBER"
    query3 = " AND s.DESCRIPTION LIKE %s"
    curbwquery = query1 + query2 + query3 
    print("curbwquery is:",curbwquery)
    curbm.execute(curbwquery,('%' + bname + '%',)) 
    bwcollection = curbm.fetchall()
    print("bmcollection is :",bwcollection)
 # Close Connection
    curbw.close()
    return render_template('Bmens.html', bmomencol=bwcollection)
  else:
    curw = mysql.connection.cursor()
    query1 = "SELECT s.ITEM_NUMBER, s.DESCRIPTION,s.LONG_DESCRIPTION, s.SKU_ATTRIBUTE_VALUE1,s.SKU_ATTRIBUTE_VALUE2,p.LIST_PRICE,p.DISCOUNT"
    query2 = " FROM XXIBM_PRODUCT_SKU s INNER JOIN XXIBM_PRODUCT_PRICING p WHERE s.ITEM_NUMBER=p.ITEM_NUMBER"
    query3 = " AND s.DESCRIPTION LIKE '%Women%'"
    curwquery = query1 + query2 + query3 
    print("curwquery is:",curwquery)
    curw.execute(curwquery) 
    wcollection = curw.fetchall()
 # Close Connection
    curw.close()
    return render_template('Womens.html', womcol=wcollection)
                 
@application.route("/men")
def mens_page():
  print ("in mens page",)
  if 'view' in request.args:
    bname = request.args['view']
    print ("brand name is :", bname)
    if bname == 'Reflex':
      bname = 'Reflex Men'
    curbm = mysql.connection.cursor()
    query1 = "SELECT s.ITEM_NUMBER, s.DESCRIPTION,s.LONG_DESCRIPTION, s.SKU_ATTRIBUTE_VALUE1,s.SKU_ATTRIBUTE_VALUE2,p.LIST_PRICE,p.DISCOUNT"
    query2 = " FROM XXIBM_PRODUCT_SKU s INNER JOIN XXIBM_PRODUCT_PRICING p WHERE s.ITEM_NUMBER=p.ITEM_NUMBER"
    query3 = " AND s.DESCRIPTION LIKE %s"
    curbmquery = query1 + query2 + query3 
    print("curbmquery is:",curbmquery)
    curbm.execute(curbmquery,('%' + bname + '%',)) 
    bmcollection = curbm.fetchall()
    print("bmcollection is :",bmcollection)
 # Close Connection
    curbm.close()
    return render_template('Bmens.html', bmencol=bmcollection)
  else:
    curm = mysql.connection.cursor()
    query1 = "SELECT s.ITEM_NUMBER, s.DESCRIPTION,s.LONG_DESCRIPTION, s.SKU_ATTRIBUTE_VALUE1,s.SKU_ATTRIBUTE_VALUE2,p.LIST_PRICE,p.DISCOUNT"
    query2 = " FROM XXIBM_PRODUCT_SKU s INNER JOIN XXIBM_PRODUCT_PRICING p WHERE s.ITEM_NUMBER=p.ITEM_NUMBER"
    query3 = " AND s.DESCRIPTION not LIKE '%Women%'"
    curmquery = query1 + query2 + query3 
    print("curmquery is:",curmquery)
    curm.execute(curmquery) 
    mcollection = curm.fetchall()
    print("mcollection is :",mcollection)
 # Close Connection
    curm.close()
    return render_template('Mens.html', mencol=mcollection)


@application.route("/boys")
def boys_page():
  print ("in boys page",)
  curb = mysql.connection.cursor()
  curbquery = "SELECT FAMILY_NAME,CLASS_NAME,COMMODITY,COMMODITY_NAME FROM XXIBM_PRODUCT_CATALOGUE WHERE COMMODITY_NAME LIKE '%Boys%' "
  curb.execute(curbquery) 
  bcollection = curb.fetchall()
  print("bcollection is :",bcollection)
 # Close Connection
  curb.close()
  return render_template('Boys.html', boyscol=bcollection)

@application.route("/girls")
def girls_page():
  print ("in girls page",)
  curg = mysql.connection.cursor()
  curgquery = "SELECT FAMILY_NAME,CLASS_NAME,COMMODITY,COMMODITY_NAME FROM XXIBM_PRODUCT_CATALOGUE WHERE COMMODITY_NAME LIKE '%girl%' "
  curg.execute(curgquery) 
  gcollection = curg.fetchall()
  print("gcollection is :",gcollection)
 # Close Connection
  curg.close()
  return render_template('Girls.html', girlscol=gcollection)
  

@application.route('/search', methods=['POST', 'GET'])
def search():
    if 'q' in request.args:
        q = request.args['q']
        print ("q is :",q)
        productsrch = ' '
        # Create cursor
        cur3 = mysql.connection.cursor()
   # Get the row count in cur3.rowcount
        query_string = "SELECT * FROM XXIBM_PRODUCT_CATALOGUE WHERE COMMODITY_NAME LIKE %s ORDER BY COMMODITY ASC"
        cur3.execute(query_string, ('%' + q + '%',))
        commosrch1 = cur3.fetchall()
        print("cur3 is :",cur3.rowcount)
        cur3.execute(query_string, ('%' + q + '%',))
        commosrch = cur3.fetchone()
          
   # Collect all the commodity in dict by looping thru the cursor    
        commo_id = []
        for i in range(0,cur3.rowcount):
          print ("commo1 is:", commosrch['COMMODITY'])
          commo_id.append(commosrch['COMMODITY'])          
          commosrch = cur3.fetchone()
          
        print("commo_id is :", str(commo_id))
        cur3.close()
        
        if commo_id:
          cur4 = mysql.connection.cursor()
          productsrch = ' '
          commo_dict = ','.join((str(n) for n in commo_id))
          print ("commo2 is:", commo_dict)
          query = "SELECT s.ITEM_NUMBER, s.DESCRIPTION,s.LONG_DESCRIPTION, s.SKU_ATTRIBUTE_VALUE1,s.SKU_ATTRIBUTE_VALUE2,p.LIST_PRICE,p.DISCOUNT FROM XXIBM_PRODUCT_SKU s INNER JOIN XXIBM_PRODUCT_PRICING p WHERE s.ITEM_NUMBER=p.ITEM_NUMBER and s.CATALOGUE_CATEGORY IN (%s)" % commo_dict
          cur4.execute(query)
          productsrch = cur4.fetchall()
          print("productsrch is :",productsrch)
          cur4.close()
        
          return render_template('search.html', product_srch=productsrch)
        else:
          return render_template('search.html')  

    
if __name__ == "__main__":
    application.run()
