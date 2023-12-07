from django.shortcuts import render
from django.shortcuts import render, redirect  
from employee.form import EmployeeForm  
from employee.models import Employee 
from employee.models import plant
from employee.form import plantForm  
from django.contrib import messages
from django.shortcuts import render
import mysql.connector as sql
from django.contrib.auth import logout
#from django.contrib.auth import logout as auth_logout
from tensorflow import keras
from tensorflow import keras
import numpy as np
import tensorflow as tf
import numpy as np
from django.shortcuts import reverse



#main page
def main(request):  # create function name:main 
    return render(request,'SystemHomePage.html') #when call this function, go to main page




# sign up and sign in user 
def signup(request):
    # define 4 variables
    fn=''
    em=''
    pwd=''
    ty='user'
    
    #if click on signin:
    if request.method=="POST" and 'signin' in request.POST:
              
              m=sql.connect(host="localhost",user="root",password="root",database='websites') #connect with database
              
              cursor=m.cursor() #Allows Python code to execute SQL command in a database session
              
              d=request.POST #puts data in request.POST when a user submits a form with the attribute method="post" and store it in d
              
              for key,value in d.items():
                if key=="email":  # the key=name in html file
                    em=value #store the value of email entered from user in em variable
                if key=="password": 
                  pwd=value #store the value of email entered from user in pwd variable

                c="select * from user where  email='{}' and password='{}'".format(em,pwd) #get the row in database that have same email & password that entered from user
               
                cursor.execute(c) #execute sql command
                
                t=tuple(cursor.fetchall()) #used to store multiple items(email,password) in a single variable (t)
               
                if t==(): #if t is empty tell the user to check his information 
                   messages.success(request, "Please check your information") 
                
                else: #if t is not empty, allow the user to enter his page
                      
                      return redirect('/showresult')
                
    #if click on signup:           
    elif request.method=="POST" and 'signup' in request.POST:
              
              m=sql.connect(host="localhost",user="root",password="root",database='websites')

              cursor=m.cursor()

              d=request.POST

              for key,value in d.items():
                if key=="name":
                    fn=value
                if key=="email":
                 em=value
                if key=="password":
                  pwd=value

              a="select * from user where email='{}' ".format(em)
              
              cursor.execute(a)

              t=tuple(cursor.fetchall())

              if t==(): #if t is empty insert the user data in database
                 c="insert into user (name,email, password, type)values('{}','{}','{}','{}')".format(fn,em,pwd,ty)
                 cursor.execute(c)
                 m.commit() #allow the database to create new row(block) and store all data in it

                 messages.success(request, "Success sign up, now you can sign in")
                 
              else: #if t is not empty tell the user that the account they are trying to register was exist
                 messages.success(request, "This user is already exist")
                  

    return render(request,'SignUpUser.html')


#reset password of user
def reset_password(request):

    em=''
    pas=''
    pas2=''

    if request.method=="POST" :
       
              m=sql.connect(host="localhost",user="root",password="root",database='websites') #connect to database
              
              cursor=m.cursor() 
              
              d=request.POST 
              
              for key,value in d.items():
                if key=="email":
                 em=value
                if key=="password":
                 pas=value
                if key=="password2":
                 pas2=value
                

              a="select * from user where email='{}' ".format(em)  

              cursor.execute(a) 
              
              t=tuple(cursor.fetchall()) 
              
              if t==(): 
                messages.success(request, "The email not in database") 
              
              else:   
              
               if pas==pas2: 
              
                s="update user set password='{}' where email='{}' ".format(pas,em)
              
                cursor.execute(s)
              
                m.commit() 

                messages.success(request, "The password change")
              
               else: 
                   messages.success(request, "The password not match")
                   
               
               return render(request,"reset_password_user.html")
                

                
    return render(request,"reset_password_user.html")


#show result for user
def showresult(request): 
    if request.method == "POST" and 'submit' in request.POST and 'image' in request.FILES:
        image = request.FILES['image']
        
        # Save the uploaded image
        with open('uploaded_image.jpg', 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)

        # Load the saved model
        model = tf.keras.models.load_model(r"C:\Users\DELL\Downloads\model.h5")

        # Preprocess the input data into the correct format for the model
        input_data = preprocess('uploaded_image.jpg')

        # Use the model to make predictions on the input data
        predictions = model.predict(input_data)
        if round(predictions[0][0]) > 0.5:
            prediction = 'healthy'
        else:
            prediction = 'non-healthy'

        # Render the output in a template
        context = {'predictions': prediction}
        
        return render(request, 'UserPage.html', context)

    return render(request, 'UserPage.html')
        










# To show all requests when click on the button in main admin page
def requests(request):
                if request.method == "POST": 
     
                 return redirect('/show')  
                 
                return render(request,'MainAdminPage.html')

# sign up super admin and sent all data to the request && login main admin and super admin
def emp(request): 
      email=''
      pasword=''
      mainadmin='fatima@gmail.com' #this is the email of main admin

      if request.method=="POST" and 'signin' in request.POST: # If this is a POST request then process the Form data
            
            form = EmployeeForm(request.POST) # Create a form instance and populate it with data from the request (binding):
           
            m=sql.connect(host="localhost",user="root",password="root",database='websites')
           
            cursor=m.cursor()
           
            d=request.POST
           
            email = request.POST.get('eemail') #get hte entered email and store it

            password = request.POST.get('econtact') #get hte entered password and store it

            c="select * from  plantadmin where  email='{}' and password='{}'".format(email,password)

            cursor.execute(c)

            t=tuple(cursor.fetchall())

            if t==(): #if the admin not exist in database 
                   messages.success(request, "You are not admin") 

            else:
                  if email==mainadmin: #if the entered email = email of main admin return to main admin page
                      return redirect('/showresultformainadmin')
                  
                  else: #if the entered email not equle email of main admin return to admin page
                    
                    return redirect('/showresultforsuperadmin')
                    
                  
          
      else:
          form = EmployeeForm(request.POST) #create instanse from form 
         
          if form.is_valid():  
                
            try:  
                
                 pasword = request.POST.get('econtact') #get the password entered by user
                 pasword2 = request.POST.get('eid') #get the repassword entered by user


                 if pasword==pasword2: # if the passwords matching save the information 
                  
                    form.save() 

                    messages.success(request, "Please wait until admin accept you")

                    return redirect('/emp')  #return user to signup admin page
                 
                 else: # if the passwords not matching show to user that Password not match
                     messages.success(request, "Password not match")
                     
            except:  
                 pass  
          else: 
            
             form = EmployeeForm()  
      return render(request,'SignUpAdmin.html',{'form':form}) 
     

# show all requests for main admin
def show(request):  
    employees = Employee.objects.all()  #get all object  
    return render(request,"AdminRequest.html",{'employees':employees}) 


# to show accept form
def accept(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'CheckAccept.html', {'employee':employee})


# Accept the main admin the super Admin
def signup2(request,id): 

    fn=''
    em=''
    pwd=''
    ty='admin' 
    code=''
    start=''
    end=''
         
    if request.method=="POST": 
                
              m=sql.connect(host="localhost",user="root",password="root",database='websites')
              
              cursor=m.cursor()
              
              d=request.POST

              for key,value in d.items():
                if key=="ename":
                    fn=value
                if key=="eemail":
                 em=value
                if key=="econtact":
                  pwd=value
                if key=="code":
                  code=value
                if key=="start":
                  start=value
                if key=="end":
                  end=value 

              a="select * from  admin where name='{}' and email='{}' and password='{}'".format(fn,em,pwd)
              
              cursor.execute(a)
              
              t=tuple(cursor.fetchall())
              
              if t==(): #if t is empty (no admin in database have the admin information entered) add admin in data base
                 #c="insert into  admin(Name,Email,Password,Type) values('{}','{}','{}','{}')".format(fn,em,pwd,ty)
                 c="insert into admin(Name,Email,Password,Type,code,SubscriptionStartTime,SubscriptionEndTime) values('{}','{}','{}','{}','{}','{}','{}')".format(fn,em,pwd,ty,code,start,end)

                 cursor.execute(c)

                 m.commit() 

                 employee = Employee.objects.get(id=id)  #get the object that the id=id of select request

                 employee.delete() #delete the request after accept admin
                            
              else: #if t is not empty (the admin exist in database) tell the user that the admin exist in data base
                  messages.success(request, "this admin is already exist")  

    return redirect("/show")
# Delete request
def destroy(request, id): 

    employee = Employee.objects.get(id=id)  #get the object that from employee table where id=id of select request

    employee.delete()  #delete the request from table
    
    return redirect("/show") #return to show request page
 

#reset password of main/super admin
def reset_password_admin(request):
    em=''
    pas=''
    pas2=''

    if request.method=="POST" :
       
              m=sql.connect(host="localhost",user="root",password="root",database='websites')
              
              cursor=m.cursor()
              
              d=request.POST
              
              for key,value in d.items():
                
                if key=="email":
                 em=value
                if key=="password":
                 pas=value
                if key=="password2":
                 pas2=value
                

              a="select * from plantadmin where email='{}' ".format(em)
              
              cursor.execute(a)
              
              t=tuple(cursor.fetchall())
              
              if t==():
                messages.success(request, "The email not in database") 
              
              else: 
                
               if pas==pas2:
                s="update plantadmin set password='{}' where email='{}' ".format(pas,em)
                
                cursor.execute(s)
                
                m.commit()

                messages.success(request, "The password change")
               
               else:
                   messages.success(request, "The password not match")
                   
               
               return render(request,"reset_password_admin.html")
                

                
    return render(request,"reset_password_admin.html")

#logout user/main admin/super admin
def logoutpage(request):
    request.session.flush()
    response =redirect('main')
    response.delete_cookie('sessionid')
    return response


#show history for main admin                
def showhistory(request): 
        m=sql.connect(host="localhost",user="root",password="root",database='websites')
        cursor=m.cursor()
        d=1
        cursor.execute("select * from HistoryMainAdmin where state='{}' ".format(d))
        result=cursor.fetchall()
        return render(request,"History4Admin.html",{'result':result})

#delete one item from history
def destroy2(request,id):
    m=sql.connect(host="localhost",user="root",password="root",database='websites')
    cursor=m.cursor()
    d=id
    s=0
    c="update HistoryMainAdmin set state='{}' where Number='{}' ".format(s,d)
    cursor.execute(c)
    m.commit()
    return redirect("/showhistory")

#delete all item from history
def deleteall(request):
    m=sql.connect(host="localhost",user="root",password="root",database='websites')
    cursor=m.cursor()
    s=0
    c="update HistoryMainAdmin set state='{}' ".format(s)
    cursor.execute(c)
    m.commit()

    return redirect("/showhistory")

#for main admin
def showresultformainadmin(request): 
    if request.method == "POST" and 'submit' in request.POST and 'image' in request.FILES:
        image = request.FILES['image']
        
        # Save the uploaded image
        with open('uploaded_image.jpg', 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)

        # Load the saved model
        model = tf.keras.models.load_model(r"C:\Users\DELL\Downloads\model.h5")

        # Preprocess the input data into the correct format for the model
        input_data = preprocess('uploaded_image.jpg')

        # Use the model to make predictions on the input data
        predictions = model.predict(input_data)
        if round(predictions[0][0]) > 0.5:
            prediction = 'healthy'
        else:
            prediction = 'non-healthy'

        # Render the output in a template
        context = {'predictions': prediction}
        m=sql.connect(host="localhost",user="root",password="root",database='websites') #connect to database
              
        cursor=m.cursor() 
              
        d=request.POST 
              
        for key,value in d.items():
                if key=="Plant":
                 plan=value
                

        c="insert into  HistoryMainAdmin(plantType,photo,path,result) values('{}','{}','{}','{}')".format(plan,image,image,prediction)
        cursor.execute(c)
        m.commit()
        return render(request, 'MainAdminPage.html', context)

    return render(request, 'MainAdminPage.html')
        
    
   



#for sub admin
email=''
def showhistoryadmin(request):
    if request.method=="POST" and 'submit' in request.POST: 
        code = request.POST.get('code', '')  # get the value of the 'code' field from the form
        if not code:
            messages.success(request, "Please enter a code.")
        else:
            m = sql.connect(host="localhost", user="root", password="root", database='websites')
            cursor = m.cursor()
            cursor.execute("SELECT * FROM admin WHERE code = %s", (code,))
            result = cursor.fetchall()
            if not result:
                messages.success(request, "Invalid code.")
            else:
                cursor.execute("SELECT * FROM HistoryForSubAdmin WHERE state = 1 AND code = %s", (code,))
                result = cursor.fetchall()
                return render(request, "History4SubAdmin.html", {'result': result})
            
    elif request.method=="POST" and 'submit1' in request.POST:
        m = sql.connect(host="localhost", user="root", password="root", database='websites')
        cursor = m.cursor()
        
        code = ''  
        d = request.POST 
        for key, value in d.items():
            if key == "code":
                code = value
        c = "UPDATE HistoryForSubAdmin SET state = 0 WHERE code = %s"
        cursor.execute(c, (code,))
        m.commit()

    return redirect("/showhistoryadmin")
       #return render(request, "History4SubAdmin.html")



e=''
def showresultforsuperadmin(request): 
    if request.method == "POST" and 'submit' in request.POST and 'image' in request.FILES:
        image = request.FILES['image']
        
        # Save the uploaded image
        with open('uploaded_image.jpg', 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)

        # Load the saved model
        model = tf.keras.models.load_model(r"C:\Users\DELL\Downloads\model.h5")

        # Preprocess the input data into the correct format for the model
        input_data = preprocess('uploaded_image.jpg')

        # Use the model to make predictions on the input data
        predictions = model.predict(input_data)
        if round(predictions[0][0]) > 0.5:
            prediction = 'healthy'
        else:
            prediction = 'non-healthy'

        # Render the output in a template
        context = {'predictions': prediction}
        
        m=sql.connect(host="localhost",user="root",password="root",database='websites') #connect to database
              
        cursor=m.cursor() 
              
        d=request.POST 
        code=''  
        plan=''   
        for key,value in d.items():
                if key=="Plant":
                 plan=value
                if key=="code":
                 code=value
                c="select * from admin where  code='{}' ".format(code) #get the row in database that have same email & password that entered from user
               
                cursor.execute(c) #execute sql command
                
                t=tuple(cursor.fetchall()) #used to store multiple items(email,password) in a single variable (t)
               
                if t==(): #if t is empty tell the user to check his information 
                   
                    messages.error(request, "Invalid code.")
                
                else: #if t is not empty, allow the user to enter his page
                      c="insert into  HistoryForSubAdmin(plantType,photo,path,result,code) values('{}','{}','{}','{}','{}')".format(plan,image,image,prediction,code)
                      cursor.execute(c)
                      
         
        
        return render(request, 'SubAdminPage.html', context)

    return render(request, 'SubAdminPage.html')



 

    
def destroy3(request,id):
    m=sql.connect(host="localhost",user="root",password="root",database='websites')
    cursor=m.cursor()
    d=id
    s=0
    c="update  HistoryForSubAdmin set state='{}' where Number='{}' ".format(s,d)
    cursor.execute(c)
    m.commit()
    return redirect("/showhistoryadmin")

#delete all item from history
def deleteall1(request):
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", password="root", database='websites')
        cursor = m.cursor()
        
        code = ''  
        d = request.POST 
        for key, value in d.items():
            if key == "code":
                code = value
        c = "UPDATE HistoryForSubAdmin SET state = 0 WHERE code = %s"
        cursor.execute(c, (code,))
        m.commit()

    return redirect("/showhistoryadmin")

def preprocess(image):
    img = tf.keras.preprocessing.image.load_img(image, target_size=(512, 512))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = img / 255.0
    img = img.reshape(1, 512, 512, 3)
    return img
