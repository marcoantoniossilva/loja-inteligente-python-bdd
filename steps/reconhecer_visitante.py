from behave import given, when, then
from loja import *

@given("o ambiente seja preparado com sucesso")
def given_ambiente_preparado(context):
    context.configuracao, context.clientes_reconhecidos, context.clientes_inadimplentes, context.clientes_VIP, context.gerador_dados_falsos = preparar()
    # por alguma razao, esses abaixo nao funcionam se forem inicializados no script ENVIRONMENT
    context.clientes_reconhecidos = {}
    context.clientes_inadimplentes = {}
    context.clientes_VIP = {}
    
    assert context.configuracao != None

@when("a foto {foto} de um visitante for capturada")
def when_foto_capturada(context, foto):
    visitante = simular_visita(foto)
    context.reconhecido, context.cliente = reconhecer_cliente(visitante, context.configuracao, context.gerador_dados_falsos)

    assert True

@then("um(a) cliente deve ser reconhecido(a)")
def then_cliente_reconhecido(context):
    id_atendimento = secrets.token_hex(nbytes=16).upper()
    context.clientes_reconhecidos[id_atendimento] = context.cliente

    assert context.reconhecido is True

@then("nenhum cliente deve ser reconhecido")
def then_cliente_nao_reconhecido(context):
    assert context.reconhecido is False