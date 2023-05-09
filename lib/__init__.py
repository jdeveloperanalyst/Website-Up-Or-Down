import smtplib
import email.message
from credenciais import*
from datetime import datetime


def enviar_email(mensagem_erro=''):
    corpo_email = f"""
    <p>\033[0;31mWebsite fora do ar!!!\033[m</p>
    <p>Erro: {mensagem_erro}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Website Down"
    msg['From'] = credentials['user']
    msg['To'] = credentials['user']
    password = credentials['password']
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


def criar_arquivo(arq, msg_erro=''):
    data_hora = datetime.now()
    data_hora_atual = data_hora.strftime('%d/%m/%Y %H:%M:%S')
    try:
        a = open(arq, 'wt+')
        a.write(f'FALHA DE CONEXÃO: Próxima tentativa em 5 segundos... > | ERRO: <{msg_erro}> | {data_hora_atual}\n')
        a.close()
    except:
        print('Houve algum erro na criação do arquivo')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def atualizar_arquivo(arq, msg_erro=''):
    data_hora = datetime.now()
    data_hora_atual = data_hora.strftime('%d/%m/%Y %H:%M:%S')
    try:
        a = open(arq, 'at')
    except:
        print('Houve algum erro na abertura do arquivo')
    else:
        try:
            a.write(f'FALHA DE CONEXÃO: Próxima tentativa em 5 segundos... > | ERRO: <{msg_erro}> | {data_hora_atual}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {arq} adicionado.')
            a.close()
