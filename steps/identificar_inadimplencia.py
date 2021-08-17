from behave import when, then
from loja import *

@when("a probabilidade de inadimplencia for {probabilidade_de_ser_inadimplente} porcento")
def when_tiver_probabilidade_de_ser_inadimplente(context, probabilidade_de_ser_inadimplente):
    context.total_clientes_em_inadimplencia = identificar_inadimplencia(context.clientes_reconhecidos, context.clientes_inadimplentes, int(probabilidade_de_ser_inadimplente))

@then("{numero_de_clientes_em_inadimplencia} cliente deve ser movido para a lista de inadimplentes")
def then_verificar_cliente_em_inadimplencia(context, numero_de_clientes_em_inadimplencia):
    assert context.total_clientes_em_inadimplencia == int(numero_de_clientes_em_inadimplencia)

