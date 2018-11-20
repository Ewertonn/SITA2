from django.shortcuts import render , redirect
from django.views.generic import View, CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from .forms import usuarioformulario, motoristaformulario, UserModelForm, reservaformulario, rotaformulario, veiculoformulario
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import Usuario, Reserva, Rota, Motorista, Veiculo
from django.http import HttpResponse
from django.utils.decorators import method_decorator
import datetime
from django.contrib import messages



aux = False

@csrf_protect
def home(request):
	global aux 
	rotas=[]
	date_format = '%d/%m/%Y'
	valor = aux
	aux = False
	try:
		origem = request.GET.get('o')
		destino = request.GET.get('d')
		data = datetime.datetime.strptime(request.GET.get('dt'), date_format)
		rotas = Rota.objects.filter(Rota_pontopartida=origem, Rota_pontochegada=destino, Rota_data=data)
		print(rotas)
		return render(request, 'home/index.html', {'rotas':rotas, 'valor': valor})
	except:
		print(rotas)
		return render(request, 'home/index.html', {'rotas':rotas, 'valor': valor})
	

def dologin(request):
	return render(request, 'login/login.html')

def motoristaregistro(request):
	return render(request, 'motoristaregistro/index.html')

def usuarioregistro(request):
	return render(request, 'usuarioregistro/index.html')

@login_required	
@csrf_protect
def telamotorista(request):
	rotas = Rota.objects.filter(Motorista=request.user)
	reservas = Reserva.objects.filter(Reserva_rota__Motorista=request.user)
	form_class2 = veiculoformulario
	template_name = 'telamotorista/index.html'

	veiculos = Veiculo.objects.filter(Motorista=request.user)
	
	@method_decorator(login_required)
	def get(self, request):
		form2 = self.form_class2(None)
		veiculos = Veiculo.objects.all()
		rotas = Rota.objects.filter(Motorista=request.user)
		return render(request, self.template_name, {'form2':form2, 'veiculos':veiculos, 'rotas' : rotas})
	
	if request.method == 'POST':
		form = rotaformulario(request.POST)
		form2 = veiculoformulario(request.POST)
		if form.is_valid():
			f = form.save(commit=False)
			f.Motorista = request.user
			f.save()
			return redirect('/sita/telamotorista')
		
		elif form2.is_valid():
			veiculo = form2.save(commit=False) 
			veiculo.save()
			veiculo.Veiculo_placa = form2.cleaned_data['Veiculo_placa']
			veiculo.Veiculo_modelo = form2.cleaned_data['Veiculo_modelo']
			veiculo.Veiculo_cor = form2.cleaned_data['Veiculo_cor']
			f = form2.save(commit=False)
			f.Motorista = request.user
			f.save()
			veiculo.save()
			messages.error(request, 'Veiculo cadastrado com sucesso!')
			return redirect('/sita/telamotorista')
			

			return redirect('/sita/telamotorista')
		else:
			messages.error(request, 'Corrija os dados')
			
			return redirect('telamotorista')

	else:
		form = rotaformulario()
		form.fields['Rota_veiculo'].queryset=Veiculo.objects.filter(Motorista=request.user)
		form2 = veiculoformulario
		rotas = Rota.objects.filter(Motorista=request.user)
		return render(request, 'telamotorista/index.html', {'veiculos':veiculos, 'form3' : form, 'rotas' : rotas, 'reservas':reservas, 'form2':form2})
			

@login_required
def telausuario(request):
	return render(request, 'telausuario/index.html')

@login_required
def telausuario(request):
	return render(request, 'telausuario/index.html')


@login_required	
def deletar_rota(request, id):
	u = Rota.objects.get(Rota_id=id)
	u.delete()
	return redirect('telamotorista')
	

@require_POST
def entraar(request):
		if request.method == 'POST':
			user = authenticate(username=request.POST['username'], password=request.POST['senha'])
			if user is None:
				return redirect('dologin')
			elif user is not None:
				login(request, user)
			u = User.objects.get(username=user)
			if u.groups.filter(name='Usuário').exists():
				return redirect ('/telausuario')
			if u.groups.filter(name='Motorista').exists():
				return redirect ('/telamotorista')			
		return redirect('dologin')
				

class usuarioformulario(View):
	form1_class = UserModelForm
	form2_class = usuarioformulario
	template_name = 'usuarioregistro/index.html'
	
	def get(self, request):
		form1 = self.form1_class(None)
		form2 = self.form2_class(None)
		return render(request, self.template_name, {'form1':form1, 'form2':form2})

	#colocando no banco de dados
	def post(self, request):
		form1 = self.form1_class(request.POST)
		form2 = self.form2_class(request.POST)

		if form1.is_valid() and form2.is_valid():
			user = form1.save(commit=False)
			usuario = form2.save(commit=False)
			u_name = user.username
			user.save()
			usuario.save()
			u = User.objects.get(username=u_name)
			usuario.user = u
			group = Group.objects.get(name='Usuário')
			u.groups.add(group)
			u.save()
			usuario.save()

			global aux 
			aux = True
			return redirect('home')

		return render(request, self.template_name, {'form1':form1, 'form2':form2})
		
class motoristaformulario(View):
	form1_class = UserModelForm
	form2_class = motoristaformulario
	template_name = 'motoristaregistro/index.html'
	

	def get(self, request):
		form1 = self.form1_class(None)
		form2 = self.form2_class(None)
		return render(request, self.template_name, {'form1':form1, 'form2':form2})

	#colocando no banco de dados
	def post(self, request):
		form1 = self.form1_class(request.POST)
		form2 = self.form2_class(request.POST)

		if form1.is_valid() and form2.is_valid():
			user = form1.save(commit=False)
			motorista = form2.save(commit=False)
			u_name = user.username
			user.save()
			u = User.objects.get(username=u_name)
			motorista.user = u
			group = Group.objects.get(name='Motorista')
			u.groups.add(group)
			u.save()
			motorista.save()
			
			global aux 
			aux = True
			return redirect('home')
					
		return render(request, self.template_name, {'form1':form1, 'form2':form2})

def dologout(request):
	logout(request)
	return redirect('/home')


def criar_user(request):
	
	if request.method == 'POST':
		form = UserModelForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('ok')
		else:
			return HttpResponse('errado')
	else:
		form = UserModelForm()
	return render(request, 'motoristaregistro/oi.html', {'form' : form})



class reservaformulario(View): 
	form_class = reservaformulario
	template_name = 'telausuario/index.html'

	@method_decorator(login_required)
	def get(self, request):
		form = self.form_class(None)
		reservas = Reserva.objects.filter(Usuario=request.user)
		return render(request, self.template_name, {'form':form, 'reservas':reservas})

	#colocando no banco de dados
	def post(self, request):
		
		form = self.form_class(request.POST)

		if form.is_valid():
			reserva = form.save(commit=False)
			reserva.save()
			reserva.Reserva_rota.set(form.cleaned_data['Reserva_rota'])
			reserva.Usuario = request.user
			reserva.save()

			return redirect('/sita/telausuario')
		
		return render(request, self.template_name, {'form':form})

#Continuação dos homes para quando o usuario clicar em inicio
@csrf_protect
def home2(request):
	rotas=[]
	date_format = '%d/%m/%Y'
	try:
		origem = request.GET.get('o')
		destino = request.GET.get('d')
		data = datetime.datetime.strptime(request.GET.get('dt'), date_format)
		rotas = Rota.objects.filter(Rota_pontopartida=origem, Rota_pontochegada=destino, Rota_data=data)
		print(rotas)
		return render(request, 'home2/home2.html', {'rotas':rotas})
	except:
		print(rotas)
		return render(request, 'home2/home2.html', {'rotas':rotas})

@csrf_protect
def home3(request):
	rotas=[]
	date_format = '%d/%m/%Y'
	try:
		origem = request.GET.get('o')
		destino = request.GET.get('d')
		horario = request.GET.get('h')
		data = datetime.datetime.strptime(request.GET.get('dt'), date_format)
		rotas = Rota.objects.filter(Rota_pontopartida=origem, Rota_pontochegada=destino, Rota_data=data)
		print(rotas)
		return render(request, 'home3/home3.html', {'rotas':rotas})
	except:
		print(rotas)
		return render(request, 'home3/home3.html', {'rotas':rotas})