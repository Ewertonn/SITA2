from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator

class Usuario(models.Model):
	Usuario_id = models.AutoField(primary_key=True)
	Usuario_contato = models.CharField(max_length=15,validators=[
			RegexValidator(r'^[0-9]*$', 'Apenas números.')
		], null=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
	#Usuario_reserva = models.ManyToManyField('Reserva')
	
	def __str__(self):
		return self.user.first_name + " " + self.user.last_name

class Motorista(models.Model):
	Motorista_id = models.AutoField(primary_key=True)
	Motorista_contato = models.CharField(max_length=15,validators=[
			RegexValidator(r'^[0-9]*$', 'Apenas números.')
		], null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return self.user.first_name + " " + self.user.last_name

class Veiculo(models.Model):
	Veiculo_id = models.AutoField(primary_key=True)
	Veiculo_placa = models.CharField(null=True,max_length=7)
	Veiculo_modelo = models.CharField(max_length=50)
	Veiculo_cor = models.CharField(null=True,max_length=20)
	Motorista=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	Veiculo_rota = models.ManyToManyField('Rota',blank=True)

	def __str__(self):
		return self.Veiculo_placa

class Rota(models.Model):
	Rota_id = models.AutoField(primary_key=True)
	Rota_pontopartida = models.CharField(max_length=100)
	Rota_pontochegada = models.CharField(max_length=100)

	Rota_localpartida = models.CharField(max_length=50)

	Rota_horario = models.TimeField()
	Rota_data = models.DateField(null=True)
	Rota_veiculo = models.ManyToManyField('Veiculo', blank=True)
	Motorista=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	valor=models.FloatField(null=True)
	def __str__(self):
		return self.Rota_pontopartida + " - " + self.Rota_pontochegada + " - " + self.Motorista.username + "- " + str(self.Rota_horario)
	

class Reserva(models.Model):
	Reserva_id = models.AutoField(primary_key=True)
	Reserva_rota = models.ManyToManyField('Rota')
	Usuario=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	