from django.shortcuts import render

from django.contrib import auth

# Create your views here.

import pyrebase
import datetime

config = {
    'apiKey': "AIzaSyASO2gO-Vt0I8nl6mtqI9r421L7wHkrgms",
    'authDomain': "smart-trolly-66fa2.firebaseapp.com",
    'databaseURL': "https://smart-trolly-66fa2.firebaseio.com",
    'projectId': "smart-trolly-66fa2",
    'storageBucket': "smart-trolly-66fa2.appspot.com",
    'messagingSenderId': "62868045977",
    'appId': "1:62868045977:web:3500825e53c7af9fe7f808",
    'measurementId': "G-189JB411MN"

}


firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
db = firebase.database()
def signIn(request):

    return render(request,"signIn.html")


def postSign(request):

    email = request.POST["email"]
    password = request.POST["password"]
    try:

        user = authe.sign_in_with_email_and_password(email, password)
    except:
        message = "Invalid Credentials"
        return render(request,"signIn.html",{"messg":message})
    print(user)
    session_id = user['idToken']

    request.session['uid'] = str(session_id)

    context ={
        'email' : email,
        'pass' :password
    }
    return render(request,"welcome.html",context)

def logout(request):
    auth.logout(request)
    return render(request,"signIn.html")



def check(request):
    print('Token is ')
    idtoken = request.session['uid']

    a = authe.get_account_info(idtoken)
    print('a is :')

    a = a['users']
    a = a[0]
    a = a['localId']
    print(a)
    itemId = db.child(a).child('item_id').shallow().get().val()
    print(itemId)

    return render(request,"check.html")

#

def shop(request):
    idtoken = request.session['uid']
    a= authe.get_account_info(idtoken)
    a= a['users']
    a=a[0]
    a= a['localId']
    print(a)
    trolly_id = db.child('Trolly_ID').shallow().get().val()
    print("Trolly ID : ")
    print(trolly_id)

    return render(request,"shop.html",{'trolly_id': trolly_id})

def product(request):
    now = datetime.date.today()
    print(now)
    idtoken = request.session['uid']
    a = authe.get_account_info(idtoken)
    a = a['users']
    a = a[0]
    a = a['localId']
    trolly_id = db.child('Trolly_ID').shallow().get().val()
    prod_id = db.child('Product_ID').shallow().get().val()
    prod_name =db.child('Product Name').shallow().get().val()
    price= db.child('Price').shallow().get().val()
    total = db.child('Total').shallow().get().val()
    context ={
        't_id': trolly_id,
        'pro_id' :prod_id,
        'p_name' : prod_name,
        'price' : price,
        'total' : total,
        'now' : now

    }
    product_name = db.child('Example').shallow().get().val()
    print(product_name)
    if request.method == 'POST':
        print('hai')
        db.child('Trolly_ID').shallow().remove()


    return render(request,"product.html",context)