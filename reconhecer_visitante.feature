Feature: Reconhecer cliente pela foto

Scenario: Um cliente chega na loja e deve ser reconhecido por uma camera
    Given o ambiente seja preparado com sucesso
    When a foto C:\Users\Win10\Documents\GitHub\loja-inteligente-python-bdd\faces\elliot1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)
    When a foto C:\Users\Win10\Documents\GitHub\loja-inteligente-python-bdd\faces\darlene1.jpg de um visitante for capturada
    Then um(a) cliente deve ser reconhecido(a)

Scenario: Uma pessoa que nao e cliente chega na loja e nao deve ser reconhecida
    Given o ambiente seja preparado com sucesso
    When a foto C:\Users\Win10\Documents\GitHub\loja-inteligente-python-bdd\faces\angela1.jpeg de um visitante for capturada
    Then nenhum cliente deve ser reconhecido
