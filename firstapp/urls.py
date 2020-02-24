from django.urls import path

from. import views

urlpatterns =[
    path('',views.signIn,name ='signIn'),
    path('postSign/',views.postSign,name="postSign"),
    path('check/',views.check,name="check"),
    path('logout',views.logout,name='logout')
]
