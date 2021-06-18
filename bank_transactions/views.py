from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib import messages
from .models import *
from django.db import transaction

def about(request):
    return render(request,'about-us.html')

def homepage(request):
    return render(request,'index.html')




def transact(request):
    all_data=Payments.objects.all().order_by("amount")
    if request.method== 'POST':
        try: 
            user_one_obj=Payments.objects.get(name= 'You') 
            user_two=request.POST.get('recepient_name')
            amount=request.POST.get('amount')

            with transaction.atomic():

                user_one_obj.amount -= int(amount)
                
                if user_one_obj.amount<0:
                    messages.error(request, 'Not Enough Balance!')
                    return redirect('http://127.0.0.1:8000/transact/')

                user_one_obj.save()

                user_two_obj = Payments.objects.get(name=user_two)
                user_two_obj.amount += int(amount)
                user_two_obj.save()
                messages.success(request, 'Your amount has been transferred successfully')

        except Exception as e:
            print(e)
            messages.success(request, 'Something went wrong.Please check your entry and try again')

        return redirect('http://127.0.0.1:8000/transact/')   

    return render(request, "transact.html",{"data":all_data})


