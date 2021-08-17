from behave import when, then
from loja import *

@when("a probabilidade de ser vip for {probabilidade_de_ser_vip} porcento")
def when_tiver_probabilidade_de_ser_vip(context, probabilidade_de_ser_vip):
    context.total_clientes_VIP = verificar_perfil(context.clientes_reconhecidos, int(probabilidade_de_ser_vip))

@then("{numero_de_clientes_VIP} cliente deve ser movido para a lista de vips")
def then_verificar_cliente_VIP(context, numero_de_clientes_VIP):
    assert context.total_clientes_VIP == int(numero_de_clientes_VIP)

