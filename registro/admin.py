from django.contrib import admin
from registro.models import Usuario
from registro.models import Motorista
from registro.models import Veiculo
from registro.models import Rota
from registro.models import Reserva

class UsuarioAdmin(admin.ModelAdmin):
	model = Usuario
	list_display = ['user'] #list_display = ['Usuario_nome','Usuario_contato']
	search_fields = ['user'] #search_fields = ['Usuario_nome']
	save_on_top = True
admin.site.register(Usuario, UsuarioAdmin)

class MotoristaAdmin(admin.ModelAdmin):
	model = Motorista
	list_display = ['user'] #list_display = ['Motorista_nome','Motorista_contato']
	search_fields = ['user'] #search_fields = ['Motorista_nome']
	save_on_top = True
admin.site.register(Motorista, MotoristaAdmin)

class VeiculoAdmin(admin.ModelAdmin):
	model = Veiculo
	list_display = ['Veiculo_modelo','Veiculo_placa']
	search_fields = ['Veiculo_placa']
	save_on_top = True
admin.site.register(Veiculo, VeiculoAdmin)

class RotaAdmin(admin.ModelAdmin):
	model = Rota
	list_display = ['Rota_pontopartida','Rota_pontochegada','Rota_horario']
	search_fields = ['Rota_pontopartida']
	save_on_top = True
admin.site.register(Rota, RotaAdmin)

class ReservaAdmin(admin.ModelAdmin):
	model = Reserva
	list_display = ['Reserva_id']
	search_fields = ['Reserva_id']
	save_on_top = True
admin.site.register(Reserva, ReservaAdmin)