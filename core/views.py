from django.shortcuts import render

def login(request):	
	return render(request,'core/login.html')

def base(request):	
	return render(request,'core/base.html')	

def perfil(request):	
	return render(request,'core/perfil.html')		

def lista_user(request):
	return render(request, 'core/lista-usuarios.html')

def cadastrar_user(request):
	return render(request, 'core/cadastrar-usuarios.html')

def atualizar_perfil(request):
	return render(request, 'core/atualizar-perfil.html')	