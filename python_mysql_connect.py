import mysql.connector
from tabulate import tabulate 
from prettytable import PrettyTable

mydb = mysql.connector.connect(
                host="localhost",
                user="admin",
                passwd="Admin",
                database="timesheetDB"
              )

mycursor = mydb.cursor()
mycursor.execute("SELECT date1,week FROM timesheet")
#mycursor.execute("SELECT date1,week,name, project, hours,build,test,activity,count1,jira FROM timesheet")
myresult = mycursor.fetchall()

#print(PrettyTable(myresult))

#print(tabulate(myresult, headers=['date1', 'week_number', 'emp_name', 'project', 'hours', 'build_type', 'test_type', 'activity', 'count', 'jira'], tablefmt='psql'))

print(tabulate(myresult, headers=['EmpName', 'EmpSalary'], tablefmt='psql'))
