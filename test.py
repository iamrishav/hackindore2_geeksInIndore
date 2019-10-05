from tkinter import *
import matplotlib.pyplot as plt 
import mysql.connector
from _cffi_backend import callback

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="agritech"
)

def agritech_year(cy, commod, yr ):

	mycursor = mydb.cursor()

	query = """SELECT avg(modal_price) from data where year=%s and commodity=%s and district_name=%s group by month"""
	query1 = """SELECT month from data where year=%s and commodity=%s and district_name=%s group by month"""
	mycursor.execute(query,(yr,commod,cy,))
	myresult = mycursor.fetchall()
	x=[]
	y=[]
	for i in myresult:
		x.append(i)
	mycursor.execute(query1,(yr,commod,cy,))
	myresult = mycursor.fetchall()
	for i in myresult:
		y.append(i)
	plt.title(commod)	
	plt.plot(y,x);
	plt.show();	

def agritech_month(cy, commod, yr, mo ):

	mycursor = mydb.cursor()

	query = """SELECT avg(modal_price), month from data where year=%s and commodity=%s and district_name=%s and month=%s group by month"""
	
	mycursor.execute(query,(yr,commod,cy,mo,))
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x);		
		

def agritech_month_day(cy, commod, yr, mo, dy ):

	mycursor = mydb.cursor()

	query = """SELECT modal_price, year, month, day from data where year=%s and commodity=%s and district_name=%s and month=%s and day = %s"""
	
	mycursor.execute(query,(yr,commod,cy,mo,dy,))
	myresult = mycursor.fetchall()
	for x in myresult:
		print(x);
def predict():
	mycursor = mydb.cursor()
	query = """SELECT avg(modal_price) from data where commodity=%s group by year"""
	query1 = """SELECT year from data where commodity=%s group by year"""
	mycursor.execute(query,('Wheat',))
	myresult = mycursor.fetchall()
	x1=[]
	y1=[]
	for i in myresult:
		x1.append(int(i[0]))
	mycursor.execute(query1,('Wheat',))
	myresult = mycursor.fetchall()
	for i in myresult:
		y1.append(str(i[0]))

	mycursor.execute(query,('Onion',))
	myresult = mycursor.fetchall()
	x2=[]
	y2=[]
	for i in myresult:
		x2.append(int(i[0]))
	mycursor.execute(query1,('Onion',))
	myresult = mycursor.fetchall()
	for i in myresult:
		y2.append(str(i[0]))

	mycursor.execute(query,('Ginger(Dry)',))
	myresult = mycursor.fetchall()
	x3=[]
	y3=[]
	for i in myresult:
		x3.append(int(i[0]))
	mycursor.execute(query1,('Ginger(Dry)',))
	myresult = mycursor.fetchall()
	for i in myresult:
		y3.append(str(i[0]))

	fig,  (plt1, plt2, plt3)= plt.subplots(3) 
	plt1.set_title('Wheat')
	plt1.plot(y1, x1)
	plt2.set_title('Onion')
	plt2.plot(y2, x2)
	plt3.set_title('Ginger(Dry)')
	plt3.plot(y3, x3)
	
	fig.subplots_adjust(hspace=1,wspace=1) 
	plt.show()
	
def future20mon():
	mycursor = mydb.cursor()
	q1 = "select avg(predicted) from future20 where commodity=%s group by month"
	q2 = "select month from future20 where commodity = %s group by month"
	mycursor.execute(q1,('Wheat',))
	res = mycursor.fetchall();
	x1=[]
	y1=[]
	for i in res:
		x1.append(int(i[0]))
	mycursor.execute(q2,('Wheat',))
	res = mycursor.fetchall();
	for i in res:
		y1.append(int(i[0]))
	
	mycursor.execute(q1,('Onion',))
	res = mycursor.fetchall();
	x2=[]
	y2=[]
	for i in res:
		x2.append(int(i[0]))
	mycursor.execute(q2,('Onion',))
	res = mycursor.fetchall();
	for i in res:
		y2.append(int(i[0]))

	
	mycursor.execute(q1,('Ginger(Dry)',))
	res = mycursor.fetchall();
	x3=[]
	y3=[]
	for i in res:
		x3.append(int(i[0]))
	mycursor.execute(q2,('Ginger(Dry)',))
	res = mycursor.fetchall();
	for i in res:
		y3.append(int(i[0]))

		 
	fig,  (plt1, plt2, plt3)= plt.subplots(3) 
	plt1.set_title('Wheat 2020')
	plt1.plot(y1, x1)
	plt2.set_title('Onion 2020')
	plt2.plot(y2, x2)
	plt3.set_title('Ginger(Dry) 2020')
	plt3.plot(y3, x3)
	fig.subplots_adjust(hspace=1,wspace=1) 
	plt.show()
def future20co():
	mycursor = mydb.cursor()
	q1 = "select avg(predicted) from future20 group by commodity"
	q2 = "select distinct commodity from future20 "
	mycursor.execute(q1)
	res = mycursor.fetchall();
	x1=[]
	y1=[]
	for i in res:
		x1.append(int(i[0]))
	mycursor.execute(q2)
	res = mycursor.fetchall();	
	for i in res:
		y1.append(str(i[0]))
	plt.title('2020')	
	plt.plot(y1,x1);
	plt.show();	
		
	
		 	
top = Tk() 
top.geometry('1000x1000')
city = Menubutton ( top, text = 'Select City') 
city.grid() 
city.menu = Menu ( city, tearoff = 0 ) 
city['menu'] = city.menu 
city.pack() 


a = Menubutton ( top, text = 'Select Commodity') 
a.pack() 
a.menu = Menu ( a, tearoff = 0 ) 
a['menu'] = a.menu 
a.pack() 



year = Menubutton ( top, text = 'Select Year') 
year.pack()
year.menu = Menu ( year, tearoff = 0 ) 
year['menu'] = year.menu 
year.pack() 

month = Menubutton ( top, text = 'Select Month') 
month.pack() 
month.menu = Menu ( month, tearoff = 0 ) 
month['menu'] = month.menu 
month.pack() 

B = Button(top, text="Predict Past Pattern", command = predict)
B.pack()

frame = Frame(top) 
frame.pack() 

L = Label(frame, text="Predict Future Pattern",)
L.pack()

f20m = Button(frame, text="Find Month Wise PAttern", command = future20mon)
f20m.pack()

f20co = Button(frame, text="Find Commodity Wise PAttern", command = future20co)
f20co.pack()


mycursor = mydb.cursor()
def callBackFunc1():
	agritech_year('Indore', 'Wheat', 2019);
def callBackFunc2():
	agritech_year('Indore', 'Wheat', 2018);
def callBackFunc3():
	agritech_year('Indore', 'Wheat', 2017);
def callBackFunc4():
	agritech_year('Indore', 'Wheat', 2016);
def callBackFunc5():
	mycursor.execute("SELECT distinct district_name from data")
	

	myresult = mycursor.fetchall()				
	v=[]
	i=0
	for x in myresult:
		v.insert(i,x);
		city.menu.add_checkbutton ( label = x, variable = v[i], command = callBackFunc6)
		i+=1
	
	
	
chkValue = BooleanVar() 
chkValue.set(False)

sixteen = year.menu.add_checkbutton(label=2016, variable=chkValue, command=callBackFunc4);
chkValue1 = BooleanVar() 
chkValue1.set(False)	
seventeen = year.menu.add_checkbutton(label=2017, variable=chkValue1, command=callBackFunc3);
chkValue3 = BooleanVar() 
chkValue3.set(False)	
eightyeen = year.menu.add_checkbutton(label=2018, variable=chkValue3, command=callBackFunc2);
chkValue4 = BooleanVar() 
chkValue4.set(False)	
ninteen = year.menu.add_checkbutton(label=2019, variable=chkValue4, command=callBackFunc1)

def callBackFunc6():
	mycursor.execute("SELECT distinct commodity from data")
	res = mycursor.fetchall()
	for x in res:
		a.menu.add_checkbutton(label=x)
def callBackFunc7():
	mycursor.execute("SELECT distinct month from data")
	res = mycursor.fetchall()
	for x in res:
		month.menu.add_checkbutton(label=x)		
	

chkValue5 = BooleanVar() 
chkValue5.set(False)
cy = city.menu.add_checkbutton ( label = "indore", variable = chkValue5, command=callBackFunc5)

chkValue6 = BooleanVar() 
chkValue6.set(False)
co = a.menu.add_checkbutton ( label = " Select Commodity", variable = chkValue6, command=callBackFunc6)

chkValue7 = BooleanVar() 
chkValue7.set(False)
mo = month.menu.add_checkbutton ( label = " Select Month", variable = chkValue7, command=callBackFunc7)


top.mainloop() 

