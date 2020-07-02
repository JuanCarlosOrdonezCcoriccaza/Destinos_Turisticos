from django.shortcuts import render

# Create your views here.

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user =auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('/')