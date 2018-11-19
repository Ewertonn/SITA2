from .models import Usuario, Motorista, Reserva, Rota, Veiculo
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserModelForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username',  'password',  'email']

	def save(self,commit=True):
		user = super(UserModelForm,self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user

class usuarioformulario(forms.ModelForm):
	#Usuario_senha = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Usuario
		fields = ['Usuario_contato'] #'Usuario_contato','Usuario_senha','Usuario_email','Usuario_imagem', Usuario_contato]


class motoristaformulario(forms.ModelForm):
	#Motorista_senha = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Motorista
		fields = ['Motorista_contato']#'Motorista_contato','Motorista_senha','Motorista_nome','Motorista_imagem']

class reservaformulario(forms.ModelForm):
	class Meta:
		model = Reserva
		fields = ['Reserva_rota']

class rotaformulario(forms.ModelForm):
	class Meta:
		model = Rota
		fields = ['Rota_id','Rota_pontopartida','Rota_pontochegada', 'Rota_localpartida', 'Rota_horario', 'Rota_data', 'Rota_veiculo', 'valor']	

class veiculoformulario(forms.ModelForm):
	class Meta:
		model = Veiculo
		fields = ['Veiculo_placa','Veiculo_modelo','Veiculo_cor']