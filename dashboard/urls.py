from django.urls import path
from django.conf.urls import url
from dashboard import views

urlpatterns = [
    path('',views.index, name='index'),
    path('index/',views.index, name='index'),
    path('activity/', views.bill_record, name='bill_record'),
    path('activity/(\d+)',views.bill_page,name='bill_page'),
    path('edit_bill/', views.edit_bill, name='edit_bill'),
    #path('activity/',views.bill_list, name='bill_list'),
    path('edit_bill/', views.edit_bill, name='edit_bill'),
    #url(r'^bill/(?P<pk>\d+)/$', views.bill_detail, name='bill_detail'),
    #url(r'^bill/new/$', views.bill_new, name='bill_new'),
]
