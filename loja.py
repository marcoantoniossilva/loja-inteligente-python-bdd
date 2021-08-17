import face_recognition
import secrets
import random
import faker
import simpy
import json

FOTOS_CLIENTES = [
    "C:\\Users\\Win10\\Documents\\GitHub\\loja-inteligente-python\\faces\\angela1.jpeg",
    "C:\\Users\\Win10\\Documents\\GitHub\\loja-inteligente-python\\faces\\tyrell1.jpeg",
    "C:\\Users\\Win10\\Documents\\GitHub\\loja-inteligente-python\\faces\\price1.jpg",

    "C:\\Users\\Win10\\Documents\\GitHub\\loja-inteligente-python\\faces\\darlene1.jpg",
    "C:\\Users\\Win10\\Documents\\GitHub\\loja-inteligente-python\\faces\\darlene2.jpg",
    "C:\\Users\\Win10\\Documents\\GitHub\\loja-inteligente-python\\faces\\darlene3.jpg",

    "C:\\Users\\Win10\\Documents\\GitHub\\loja-inteligente-python\\faces\\elliot1.jpg",
    "C:\\Users\\Win10\\Documents\\GitHub\\loja-inteligente-python\\faces\\elliot2.jpg",
    "C:\\Users\\Win10\\Documents\\GitHub\\loja-inteligente-python\\faces\\elliot3.jpg"
]
ARQUIVO_CONFIGURACAO = "C:\\Users\\Win10\\Documents\\GitHub\\loja-inteligente-python\\configuracao.json"

def preparar():
    
    configuracao = None
    with open(ARQUIVO_CONFIGURACAO, "r") as arquivo_configuracao:
        configuracao = json.load(arquivo_configuracao)
        if configuracao:
            print("configuracao carregada. versao da simulacao:", configuracao["versao"])

    clientes_reconhecidos = {}
    clientes_inadimplentes = {}
    clientes_VIP = {}

    gerador_dados_falsos = faker.Faker(locale="pt_BR")
    
    return configuracao, clientes_reconhecidos, clientes_inadimplentes, clientes_VIP, gerador_dados_falsos

def simular_visita(foto_visitante):
    visitante = {
        "foto": foto_visitante,
        "dados": None
    }

    return visitante

def reconhecer_cliente(visitante,configuracao,gerador_dados_falsos):

    print("iniciando reconhecimento de cliente...")
    foto_visitante = face_recognition.load_image_file(visitante["foto"])
    encoding_foto_visitante = face_recognition.face_encodings(foto_visitante)[0]

    reconhecido = False
    for cadastro in configuracao["cadastros"]:
        fotos_banco = cadastro["fotos"]
        total_reconhecimentos = 0

        for foto in fotos_banco:
            foto_banco = face_recognition.load_image_file(foto)
            encoding_foto_banco = face_recognition.face_encodings(foto_banco)[0]

            foto_reconhecida = face_recognition.compare_faces([encoding_foto_visitante], encoding_foto_banco)[0]
            if foto_reconhecida:
                total_reconhecimentos += 1

        if total_reconhecimentos/len(fotos_banco) > 0.7:
            reconhecido = True

            visitante["dados"] = {}
            visitante["dados"]["nome"] = gerador_dados_falsos.name()
            visitante["dados"]["idade"] = random.randint(18, 100)
            visitante["dados"]["endereco"] = gerador_dados_falsos.address()
            visitante["dados"]["renda"] = random.randint(1100, 6000)

    return reconhecido, visitante

def imprimir_dados(cliente):
    print("nome:", cliente["dados"]["nome"])
    print("idade:", cliente["dados"]["idade"])
    print("endereco:", cliente["dados"]["endereco"])
    print("renda:", cliente["dados"]["renda"],"\n")

def reconhecer_visitante(clientes_reconhecidos):
    visitante = simular_visita()
    reconhecido, cliente = reconhecer_cliente(visitante)
    if reconhecido:
        id_atendimento = secrets.token_hex(nbytes=16).upper()
        clientes_reconhecidos[id_atendimento] = cliente

        print("um cliente foi reconhecido, imprimindo os dados...")
        imprimir_dados(cliente)
    else:
        print("nao foi reconhecido um cliente\n")


def identificar_inadimplencia(clientes_reconhecidos,clientes_inadimplentes,probabilidade_de_ser_inadimplente):
    total_clientes_em_inadimplencia = 0;
    if len(clientes_reconhecidos):
        for id_atendimento, cliente in list(clientes_reconhecidos.items()):
            inadimplencia_reconhecida = (random.randint(1, 100) <= probabilidade_de_ser_inadimplente)
            if inadimplencia_reconhecida:
                clientes_inadimplentes[id_atendimento] = cliente
                clientes_reconhecidos.pop(id_atendimento)
                total_clientes_em_inadimplencia += 1;

                print("ATENÇÃO! cliente", cliente["dados"]["nome"], "em situacao de inadimplencia!\n")
    return total_clientes_em_inadimplencia

def verificar_perfil(clientes_reconhecidos,probabilidade_de_ser_vip):
    total_clientes_VIP = 0
    if len(clientes_reconhecidos):
        for cliente in clientes_reconhecidos.values():
            cliente_vip = (random.randint(1, 100) <= probabilidade_de_ser_vip)
            if cliente_vip:
                print("cliente", cliente["dados"]["nome"], "e VIP.\n")
                total_clientes_VIP += 1
            else:
                print("cliente", cliente["dados"]["nome"], "nao e VIP.\n")
    return total_clientes_VIP

def atualizar_perfil(clientes,probabilidades):
    clientes_reconhecidos = clientes[0]
    clientes_inadimplentes = clientes[1]
    clientes_VIP = clientes[2]

    probabilidade_deixar_inadimplencia =  probabilidades[0]
    probabilidade_tornar_inadimplente = probabilidades[1]
    probabilidade_de_se_tornar_vip =  probabilidades[2]
    

    total_clientes_normais = 0
    total_novos_clientes_inadimplentes = 0
    total_novos_clientes_VIP = 0

    if len(clientes_reconhecidos) or len(clientes_inadimplentes):
        if len(clientes_reconhecidos):
            
            for id_atendimento, cliente in list(clientes_reconhecidos.items()):
                    tornou_inadimplente = (random.randint(1, 100) <= probabilidade_tornar_inadimplente)
                    if tornou_inadimplente:
                        clientes_inadimplentes[id_atendimento] = cliente
                        clientes_reconhecidos.pop(id_atendimento)
                        total_novos_clientes_inadimplentes +=1
                        print("cliente", cliente["dados"]["nome"], " tornou-se inadimplente\n")
                    else:
                        tornou_vip = (random.randint(1, 100) <= probabilidade_de_se_tornar_vip)
                        if tornou_vip:
                            clientes_VIP[id_atendimento] = cliente
                            clientes_reconhecidos.pop(id_atendimento)
                            total_novos_clientes_VIP +=1
                            print("cliente", cliente["dados"]["nome"], " tornou-se VIP\n")

        if len(clientes_inadimplentes):
            for id_atendimento, cliente in list(clientes_inadimplentes.items()):
                    deixou_inadimplencia = (random.randint(1, 100) <= probabilidade_deixar_inadimplencia)
                    if deixou_inadimplencia:
                        clientes_reconhecidos[id_atendimento] = cliente
                        clientes_inadimplentes.pop(id_atendimento)
                        total_clientes_normais +=1
                        print("cliente", cliente["dados"]["nome"], " deixou de ser inadimplente\n")
    return [total_clientes_normais,total_novos_clientes_inadimplentes,total_novos_clientes_VIP]