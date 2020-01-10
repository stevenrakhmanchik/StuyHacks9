from flask import Flask, request, render_template, abort, jsonify, session, redirect, url_for
import dbm
import json
from backend import write, models, takephoto, steven
from backend import takephoto
Users = {}
# app = Flask(__name__, static_folder='.', root_path='
app = Flask(__name__, static_folder='./static', template_folder='./templates')
app.config.update(TEMPLATES_AUTO_RELOAD=True)

@app.route('/about', methods=['GET'])
def about():
  return render_template(
    'about.html'
  )

@app.route('/map', methods=['GET'])
def map():
  return render_template('map.html')

@app.route('/', methods=['GET', 'POST'])
def root():

    #cities = newModels.get_cities_sparse()
    #print('cities', cities)
    #cities_names = [c['name'] for c in cities]

    return render_template(
        'index.html'
    )  # main page

@app.route('/test')
def test():
  print(Users)
@app.route('/leaderboard', methods=['GET'])
def leaderboard():
  #code that gives top ten ppl and their scores

  return render_template('leaderboard.html', user=Users)

#def send_cities_sparse():
#    cities = newModels.get_cities_sparse()
#    return jsonify(cities)


## post new products to track  wait wrong route i think -> we need autocompleted cities in the root function

def send_city_info(city_name):
    cities = newModels.get_cities_sparse()
    for city in cities:
        if city['name'].lower() != city_name.lower():
            print(f"{city['name']} is not {city_name}")
            continue

        info = newModels.get_products_in_city_with_average_prices(
            city['id'])
        print('sendingnjson')
        return jsonify(info)
    print('not found')
    return 'city not found'

@app.route('/cities/<city>/products/<product>', methods=['GET', 'POST'])
def show_product(city, product):
    #check if product exists /we need to do this anyways we gotta do this

    #get information about product
    return render_template(
        'product.html',
        title1=city,
        title2="The average price of" + product + "in this city is:",
        toinput='yes')

    if request.method == 'POST':
        pass

# it'll probably fix itself soon

from tkinter import filedialog
from tkinter import *

## just for testing a scriptyikes ye ig we can go off the call
game = 0
@app.route('/login', methods=['GET', 'POST'])
def login():
  good = "yes"
  print('login start')
  if request.method == 'POST':
    submit = request.form.get('submit')
    print('mode:')
    print(submit)
    if submit == 1:
      filein = request.form.get('name')
      holding = steven.count(filein)
      print('start')
      print(holding)
      Users[user][1] = Users[user][0] , Users[user][1] + 24
      return render_template('leaderbo.html', user="+24")
    print('start post')
    user = request.form.get('username')
    passward = request.form.get('password')
    if user == None or passward == None:
      print("form not filled")
      good = "no"
      return render_template('login.html', good=good)
    print('user: ' + user)
    print('pass: ' + passward)
    
    temppp = write.get_user(user)
    print(temppp)#false if temp is false 
    if user not in Users:
      # ru
      Users[user]= [passward, 0]
      print("runtime list:")
      #print(temp)
      #allusers.append(temp)
      #print(allusers)
      #write.generic_write(tempuserinfo)
      good = "success"
      #print("saved file:")
      print(good)
      return render_template('play.html', good=good, user=user)
    elif Users[user][0] == passward:
      good = "success"
      print(good)
      return render_template('play.html', good=good, user=user)
    else:
      print(temppp)
      good = "wrong"
    return render_template('login.html', good=good)
  game = 0
  return render_template('login.html', good=good)
  





@app.route('/test')
def test_route():
    UPC = "UPC"
    print('test route')
    return render_template('test.html', UPC=UPC)

# upc = request.args.get('upc')
# x = backend.write.read(upc) #test if its in dictionary
# if x != "N/A":
#   #x = item info
#   print('post decode:' + x)

#   pass

# else:
#   #give error
#   return render_template('./not_found.html')

# if request.method == 'POST':


# params for post: price
# @app.route('/products/<upc>', methods=['GET', 'POST'])
# def show_product(upc): #, methods=['GET', 'POST']
#     # if 'location'not in session.keys():
#     #     print("redirecting to getLocation")
#     #     print(request.path)
#     #     return redirect('https://fairprices.petevdp.repl.co/getLocation') #redirect
#     # location = session['location']
#     print("upc: ", int(upc))
#     x = backend.write.read(str(upc))
#     print(x)
#     product = products.get_product(int(upc))# product details
#     # if product == None:
#         #-----> send seach webpage
#     if product is None:
#         abort(404, description="Product not found!")

#     print(f"product: {product}")
#     if request.method == 'POST':
#         submitted_price = request.args.get('price')
#         try:
#             test = submitted_price + 1 #testing if its a number
#         except TypeError:
#             return { render_template('./products.html', product="N/A")}
#         if submitted_price != None and submitted_price > 0:
#             product.submit_price("user_id", submitted_price)

#     return render_template('product.html', location=location)
#     # return render_template('./products.htu0s), average_price=product.get_average_price()) #product search

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000')
    app.run(host='0.0.0.0', port='3000')
