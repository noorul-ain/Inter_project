from django.shortcuts import render,redirect
from .forms import vechForm
from .models import Vech
# from django.http import HttpResponse

# Create your views here.
def home(request):
    form = vechForm()
    if request.method=='POST':
        form = vechForm(request.POST)
        form.save()
        form=vechForm()
    data=Vech.objects.all()
    context={'form':form,
             'data':data,
             }
    return render(request, 'index.html',  context)



def delete_data(request,id):
    if request.method=='POST':
        data=Vech.objects.get(pk=id)
        data.delete()
        return redirect('/')
    
    
    
def update_data(request,id):
    form = vechForm()
    if request.method=='POST':
        form = vechForm(request.POST, instance=data)
        data=Vech.objects.get(pk=id)
        if form.is_valid:
            form.save()
        else:
            data=Vech.objects.get(pk=id)
            form = vechForm(instance=data)
    context={'form':form,
        #  'data':data
            }
        
    return render(request, 'update.html', context)

            
   

    
    
