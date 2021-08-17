from behave import when, then
from loja import *

@when("a probabilidade de deixar de ser vip for {probabilidade_de_deixar_de_ser_vip} porcento")
def when_tiver_probabilidade_de_deixar_de_ser_vip(context, probabilidade_de_deixar_de_ser_vip):
    clientes = [context.clientes_reconhecidos, context.clientes_inadimplentes, context.clientes_VIP]
    context.perfis = atualizar_perfil(clientes, [int(probabilidade_de_deixar_de_ser_vip),0,0])

@then("todos os clientes devem ser movidos para a lista de reconhecidos (normais)")
def then_verificar_todos_os_clientes_VIP(context):
    assert context.perfis[0] == context.perfis[0]+context.perfis[1]+context.perfis[2] # considero teste como acertivo quando só existem perfis normais
    context.lista_vips_estava_vazia = True # sinalizo que a lista de vips ja esta vazia

@then("nenhum cliente deve ser retirado da lista de vips")
def then_verificar_nenhum_cliente_VIP(context):
    assert context.perfis[2] > 0 or context.lista_vips_estava_vazia==True# considero teste como acertivo quando existe perfil vip ou se a lista já estava vazia antes

@when("a probabilidade de ser tornar inadimplente for {probabilidade_de_se_tornar_inadimplente} porcento")
def when_tiver_probabilidade_de_se_tornar_inadimplente(context, probabilidade_de_se_tornar_inadimplente):
    clientes = [context.clientes_reconhecidos, context.clientes_inadimplentes, context.clientes_VIP]
    context.perfis = atualizar_perfil(clientes, [0,int(probabilidade_de_se_tornar_inadimplente),0])

@then("todos os clientes devem ser movidos para a lista de inadimplentes")
def then_verificar_todos_os_clientes_inadimplente(context):
    assert context.perfis[1] == context.perfis[0]+context.perfis[1]+context.perfis[2] # considero teste como acertivo quando só existem perfis inadimplentes

@then("nenhum cliente deve ser movido para a lista de inadimplentes")
def then_verificar_nenhum_cliente_inadimplente(context):
    assert context.perfis[1] == 0 # considero teste como acertivo quando não existe perfis inadimplentes

@when("a probabilidade de se tornar vip for {probabilidade_de_se_tornar_vip} porcento")
def when_tiver_probabilidade_de_se_tornar_vip(context, probabilidade_de_se_tornar_vip):
    clientes = [context.clientes_reconhecidos, context.clientes_inadimplentes, context.clientes_VIP]
    context.perfis = atualizar_perfil(clientes, [0,0,int(probabilidade_de_se_tornar_vip)])

@then("todos os clientes devem ser movidos para a lista de vips")
def then_verificar_todos_os_clientes_VIPs(context):
    assert context.perfis[2] == context.perfis[0]+context.perfis[1]+context.perfis[2] # considero teste como acertivo quando só existem perfis vips
@then("nenhum cliente deve ser movido para a lista de vips")
def then_verificar_nenhum_cliente_inadimplente(context):
    assert context.perfis[2] == 0 # considero teste como acertivo quando não existe perfis vips