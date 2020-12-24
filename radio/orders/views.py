from django.shortcuts import render
from stations.models import Track
from .forms import OrderCreateForm

# Create your views here.

def order_create(request):
    track = Track()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid:
            track = form.save()

        return render(request, 'orders/created.html',
                            {'track': track})
    else:
        form = OrderCreateForm
    return render(request,'orders/create.html', {'form': form})