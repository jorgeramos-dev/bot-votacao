## 💻 Curso: Bot de Votação Corrida das Blogueiras

- Código de Bot desenvolvido em Python para votação realite Corrida das Blogueiras.

## ▶️ Utilização
 - python robo.py

## 💻 Projeto

 - São 3 participantes na votação final, sendo 1 Elay, 2 Erick e 3 Jade.
 - A votação possui reCaptcha do Google "Não sou robô".
 - O envio da votação é feito por um POST, contendo um body com:
 - blogueira -> ID_BLOGUEIRA g-recaptcha-response -> NÃO SOU ROBÔ
 - O re-Captcha serve apenas para confirmar que não é um robo. No envio do voto, ele não validado.
 - Por fim conseguimos enviar o voto para o candito desejado, coletando o serial de um recaptcha.

☑️ O código tem com objetivo de se praticar Python e automação.