from django.shortcuts import render

def home(request):
	var = 'Mundo'
	return render(request,'core/base.html', {'var':var})
