import pyodbc as pyodbc
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render


server = 'gjndev.database.windows.net'
database = 'testing_excel_db'
username = 'gindev'
password = 'admin@123'
db = pyodbc.connect('DRIVER={SQL server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = db.cursor()



# Create your views here.
def userform(request):
    if request.method =='POST':
        hostid = request.POST.get('hostadd')
        username = request.POST.get('servername')
        sql = ("""insert into demo values('{}','{}')"""
               .format(hostid, username))
        cursor.execute(sql)
        cursor.commit()
        print("hello")




    return render(request, 'userform.html',{})


def validateno(request):
    if request.method =='POST':
        hostid = request.POST.get('hostadd')


    return render(request, 'validate.html',{})


def serverisexists(request):
    if request.method == 'POST':
        sname = request.POST.get('server_name')
        print("Hellp")

        rec = ("""select servername from demo where servername='{}' """.format(sname))
        record = cursor.execute(rec).fetchone()
        print(record)
        if record is None:
            print("If working now")
            return HttpResponse('OK')
        else:
            print('else working now')
            return HttpResponse("user already Exists")




def userisexists(request):
    if request.method == 'POST':
        uname = request.POST.get('user_name')
        print(uname)
        rec = ("""select username from demo where username='{}' """.format(uname))
        record = cursor.execute(rec).fetchone()
        print(record)
        if record is None:
            print(record)
            return HttpResponse('OK')
        else:
            print('else working')
            return HttpResponse( "user already Exists")

