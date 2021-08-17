Feature: Atualizando o perfil do cliente

Scenario: Um cliente reconhecido pode ter seu perfil atualizado
    Given o ambiente seja preparado com sucesso
    When a foto C:\Users\Win10\Documents\GitHub\loja-inteligente-python-bdd\faces\elliot1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When a probabilidade de se tornar vip for 100 porcento
    Then todos os clientes devem ser movidos para a lista de vips
    When a foto C:\Users\Win10\Documents\GitHub\loja-inteligente-python-bdd\faces\darlene1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When a probabilidade de se tornar vip for 0 porcento
    Then nenhum cliente deve ser movido para a lista de vips

    When a foto C:\Users\Win10\Documents\GitHub\loja-inteligente-python-bdd\faces\elliot2.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When a probabilidade de ser tornar inadimplente for 100 porcento
    Then todos os clientes devem ser movidos para a lista de inadimplentes
    When a foto C:\Users\Win10\Documents\GitHub\loja-inteligente-python-bdd\faces\darlene2.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When a probabilidade de ser tornar inadimplente for 0 porcento
    Then nenhum cliente deve ser movido para a lista de inadimplentes

    When a foto C:\Users\Win10\Documents\GitHub\loja-inteligente-python-bdd\faces\elliot3.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When a probabilidade de deixar de ser vip for 100 porcento
    Then todos os clientes devem ser movidos para a lista de reconhecidos (normais)
    When a foto C:\Users\Win10\Documents\GitHub\loja-inteligente-python-bdd\faces\darlene3.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When a probabilidade de deixar de ser vip for 0 porcento
    Then nenhum cliente deve ser retirado da lista de vips