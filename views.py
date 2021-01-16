from django.shortcuts import render,redirect
from account.models import User
from django.contrib import messages
def show_home(request):
    return render(request,"home.html")
# Create your views here.
def show_signup(request):
    if request.method=="POST":
        na = request.POST['name']
        m_no = request.POST['mno']
        e_mail = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        #print(na,m_no,e_mail,password1)
        if password1==password2:
            if User.objects.filter(email=e_mail).exists():
                print('email name taken')
                return redirect("home")
            else:
                us=User(name =str(na),mno=str(m_no),email=e_mail,password=str(password1))
                us.save()
                messages.success(request,"thanks for signup")
                print('signup succesfully')
                name=User.objects.get(name=na)
                return render(request,"signup.html",{'data':name})
        else:
            print('password not matching')
            return redirect("home")
    else:
        return render(request,"signup.html")
def show_login(request):
    print('Login')

    if request.method == "POST":
        email = request.POST['email']
        password1 = request.POST['password']
        user=User.objects.filter(email=email,password =password1).exists()
        if user:
            # auth.login(request,user)
            print('login successfull')
            return render(request,"welcome.html")
        else:
            print('unsuccessfull')
            return redirect("login")

    return render(request,"login.html")