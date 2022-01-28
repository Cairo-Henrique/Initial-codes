from random import choice
lacração = ['Essas palavras são inadequadas, não devem ser usadas comigo e com mais ninguém.', 'Pra você pode ter sido uma brincadeira, pra mim foi violento.', 'Essas palavras são inadequadas para a nossa conversa. Além disso, sou um bando de if else que fala sobre assuntos financeiros.']
lr = lacração
while True:
    msg = input()
    if ('oi' in msg) or ('olá' in msg):
        print('Olá! Mande foto do cartão do papai e mamãe!')
    elif ('depositar' in msg) or ('deposito' in msg) or ('transferir' in msg) or ('saque' in msg) or ('retirar' in msg):
        print('https://banco.bradesco/html/classic/produtos-servicos/mais-produtos-servicos/transferencias-saques-e-depositos.shtm')
    elif ('puta' in msg) or ('gorda' in msg) or ('comer' in msg) or ('gostosa' in msg):
        lacração = choice(lacração)
        print(lacração)
        lacração = lr
    elif ('foto' or 'fotografia') in msg:
        print('Foto? Apesar de falar como humana, sou um bando de if else')
    elif 'pedro' in msg:
        print('Lindão pode me estuprar')
    elif ('obrigado' in msg) or ('agradeço' in msg):
        print('Nada, cobro pix de 100 reais')
    else:
        print('Não entendi, poderia repetir?')