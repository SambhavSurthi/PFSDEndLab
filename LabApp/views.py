from django.shortcuts import render

# Create your views here.
def home(request):
    data={
        'Name':'Sambhav Surthi',
        'id':2300031622,
        'fname':'Anil Kumar',
        'mname':'Navyatha',
        'phone':6304749943
    }
    return render(request, 'index.html', data)
