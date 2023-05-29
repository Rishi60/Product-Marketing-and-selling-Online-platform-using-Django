from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf.urls import include
from django.template import loader
from .models import Student
from django.http import Http404
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
import pymysql.cursors
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')


def search(request):
    return render(request, 'home.html')

def cat(request):
    return render(request, 'home.html')

def signup_success(request):
    return render(request, 'signup_success.html')


def buy(request):
    connection = pymysql.connect(host='localhost',
                                 user='dodmise',
                                 password='dodmise123',
                                 db='shubham',
                                 )
    if request.method == 'POST':
            form = (request.POST)

            s2 = form['cnf_item']
            s3 = form['use_name']
            s4 = form['address']
            try:
                a1 = []
                b1 = []
                with connection.cursor() as cursor:
                    d={}
                    sql2 = "SELECT * from `stud_data` where `product_name`=(%s)"
                    cursor.execute(sql2, (s2))
                    result2 = cursor.fetchone()
                    if (result2 == None):
                        return render(request, "nomatch.html")
                    sql = "SELECT * from `sale` where `product_name`=(%s)"
                    cursor.execute(sql, (s2))
                    result = cursor.fetchone()
                    if (result == None):
                        return render(request, "nomatch.html")
                    pname=result[0]
                    cnt=result[2]
                    cnt2=cnt+1
                    sql1="UPDATE  `sale` SET count=%s where `product_name`=%s"
                    cursor.execute(sql1,(cnt2,pname))
                    sql2 = "INSERT INTO `order_details` (`username`, `item`,`address`) VALUES(%s,%s,%s)"
                    cursor.execute(sql2,(s3,s2,s4))
                    connection.commit()
                    d['a']=s3
                    d['b']=s2
                    d['c']=s4
                    return render(request, "buy.html", {"d":d})
            finally:
                connection.close()


def search(request):
    connection = pymysql.connect(host='localhost',
                                 user='dodmise',
                                 password='dodmise123',
                                 db='shubham',
                                 )
    if request.method == 'POST':
            form = (request.POST)

            s1 = form['search_item']
            try:
                a1 = []
                b1 = []
                with connection.cursor() as cursor:
                    sql = "SELECT * from `stud_data` where `product_name`=(%s)"
                    cursor.execute(sql, (s1))
                    a = cursor.fetchone()
                    if(a==None):
                        return render(request,"nomatch.html")
                    d = {}
                    d['product'] = a[0]
                    d['company'] = a[1]
                    d['description'] = a[2]
                    d['category'] = a[3]
                    d['price'] = a[4]
                    return render(request, "search.html", {"d": d, })
            finally:
                connection.close()


def home(request):
    connection = pymysql.connect(host='localhost',
                                 user='dodmise',
                                 password='dodmise123',
                                 db='shubham',
                                 )
    try:
        a = []
        b = []
        c = []
        d = []
        with connection.cursor() as cursor:
            sql = "SELECT * from stud_data"
            cursor.execute(sql)
            result = cursor.fetchall()
            j=0
            for i in result:
                d={}
                d['product']=i[0]
                d['company']=i[1]
                d['description'] = i[2]
                d['category']=i[3]
                d['price']=i[4]

                a.append(d)
            return render(request, "home.html", {"a": a, })
    finally:
        connection.close()

def cat(request):
    connection = pymysql.connect(host='localhost',
                                 user='dodmise',
                                 password='dodmise123',
                                 db='shubham',
                                 )
    if request.method == 'POST':
            form = (request.POST)

            s3 = form['cat_item']
            try:
                a = []
                b1 = []
                with connection.cursor() as cursor:
                    sql = "SELECT * from `stud_data` where `category`=(%s)"
                    cursor.execute(sql, (s3))
                    result = cursor.fetchall()
                    if(result==None):
                        return render(request,"nomatch.html")
                    for i in result:
                        d = {}
                        d['product'] = i[0]
                        d['company'] = i[1]
                        d['description'] = i[2]
                        d['category'] = i[3]
                        d['price'] = i[4]
                        categ=i[3]

                        a.append(d)
                    return render(request, "cat.html", {"a": a,"categ":categ, })
            finally:
                connection.close()
def test_matplotlib(request):
   
    connection = pymysql.connect(host='localhost',
                                 user='dodmise',
                                 password='dodmise123',
                                 db='shubham',
                                 )
    
    try:
     cnt=[]
     label=[]
     with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * from sale"
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
         label.append(i[0])
         cnt.append(i[2])
        
        
    finally:
    	connection.close()

    plt.pie(cnt,labels=label)
    #os.remove('/home/saurabh/Desktop/imart/student/static/student/chart.png')
    plt.savefig('/home/rushikesh/Desktop/dmart/student/static/student/images/chart.png')
    return render(request, "chart.html")
def bargraph(request):
	
	# Connect to the database
	connection = pymysql.connect(host='localhost',
		                     user='dodmise',
		                     password='dodmise123',
		                     db='shubham',
		                    )
	try:
	     a=[]
	     l = []
	     a1=[]
	     l1=[]
	     with connection.cursor() as cursor:
		# Read a single record
		sql = "SELECT sum(count) from `sale` group by category "
		cursor.execute(sql)
		result = cursor.fetchall()
		print(result)
		sql1 = "SELECT DISTINCT category from `sale`"
		cursor.execute(sql1)
		result1 = cursor.fetchall()
		print(result1)
		for j in result1:
		  num1=str(j[0])
		  a1.append(num1)
		  l1 = list(a1)
		for i in result:
		  num=int(i[0])
		  a.append(num)
		  l = list(a)
		l1.sort()

	finally:
	    connection.close()
	y_pos = np.arange(len(l1))

	 
	plt.bar(y_pos, l, align='center', alpha=0.5)
	plt.xticks(y_pos, l1)
	plt.ylabel('number of products')
	plt.title('category wise distribution')
	plt.savefig('/home/rushikesh/Desktop/dmart/student/static/student/bargraph.png')
  
        
        return render(request, "bargraph.html") 








