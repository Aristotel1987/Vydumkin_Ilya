from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm

def client_list(request):
       clients = Client.objects.all()
       return render(request, 'client/client_list.html', {'clients': clients})

def register_client(request):
       if request.method == 'POST':
           form = ClientForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('client_list')
       else:
           form = ClientForm()
       return render(request, 'client/register_client.html', {'form': form})

def delete_client(request, client_id):
       client = Client.objects.get(id=client_id)
       client.delete()
       return redirect('client_list')