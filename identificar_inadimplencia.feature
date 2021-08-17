Feature: Verificando se o cliente está inadimplente

Scenario: Um cliente reconhecido pode estar inadimplente
    Given o ambiente seja preparado com sucesso
    When a foto C:\Users\Win10\Documents\GitHub\loja-inteligente-python-bdd\faces\elliot1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When a probabilidade de inadimplencia for 100 porcento
    Then 1 cliente deve ser movido para a lista de inadimplentes
    When a foto C:\Users\Win10\Documents\GitHub\loja-inteligente-python-bdd\faces\darlene1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When a probabilidade de inadimplencia for 0 porcento
    Then 0 cliente deve ser movido para a lista de inadimplentes