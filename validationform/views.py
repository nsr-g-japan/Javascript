import pyodbc as pyodbc
from django.shortcuts import render
db = pyodbc.connect('Driver={SQL server};' 'server=Nisarbasha;' 'Database=dwproject;' 'Trusted_connection=yes;')
cursor = db.cursor()
# Create your views here.
def userform(request):
    if request.method =='POST':
        hostid = request.POST.get('hostadd')
        username = request.POST.get('username')
        print(hostid,username)
        sql = ("""insert into demo values('{}','{}')"""
               .format(hostid, username))
        cursor.execute(sql)
        cursor.commit()


    return render(request, 'userform.html',{})