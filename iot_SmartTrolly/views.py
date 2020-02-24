# from django.shortcuts import render
#
# import pyrebase
#
# config = {
#     'apiKey': "AIzaSyASO2gO-Vt0I8nl6mtqI9r421L7wHkrgms",
#     'authDomain': "smart-trolly-66fa2.firebaseapp.com",
#     'databaseURL': "https://smart-trolly-66fa2.firebaseio.com",
#     'projectId': "smart-trolly-66fa2",
#     'storageBucket': "smart-trolly-66fa2.appspot.com",
#     'messagingSenderId': "62868045977",
#     'appId': "1:62868045977:web:3500825e53c7af9fe7f808",
#     'measurementId': "G-189JB411MN"
#
# }
#
#
# firebase = pyrebase.initialize_app(config)
#
# auth = firebase.auth()
#
# def signIn(request):
#
#     return render(request,"signIn.html")