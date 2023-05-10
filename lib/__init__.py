import os
import smtplib
import email.message
from email.mime import base, multipart
from credenciais import*
from datetime import datetime


def enviar_email(mensagem_erro):
    corpo_email = f"""
    <p>Website unavailable!!!</p>
    <p>Erro: {mensagem_erro}</p>
    <p>Logs attached for your analysis.</p>
    """

    msg = multipart.MIMEMultipart()
    msg['Subject'] = "Website Down"
    msg['From'] = credentials['user']
    msg['To'] = credentials['user']
    password = credentials['password']

    corpo = email.message.Message()
    corpo.add_header('Content-Type', 'text/html')
    corpo.set_payload(corpo_email)
    msg.attach(corpo)

    anx = open('logs.txt', 'rb')
    anexo = base.MIMEBase('application', 'octet-stream')
    anexo.set_payload(anx.read())
    anexo.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(anx.name)}"')
    msg.attach(anexo)

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
        text = 'Log Analysis: Identifying and Resolving Errors'
        a = open(arq, 'wt+')
        a.write('-' * 133)
        a.write(f'\n{text:>88}\n')
        a.write('-' * 133)
        a.write(f'\n\nConnection failure: Next attempt in 10 seconds... > | Error: {msg_erro} | {data_hora_atual}\n')
        a.write('-' * 133)
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
            a.write(f'\nConnection failure: Next attempt in 10 seconds... > | Error: {msg_erro} | {data_hora_atual}\n')
            a.write('-' * 133)
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro adicionado em {arq}')
            a.close()


def logs_email(arq, msg_erro=''):
    data_hora = datetime.now()
    data_hora_atual = data_hora.strftime('%d/%m/%Y %H:%M:%S')
    try:
        a = open(arq, 'at')
    except:
        print('Houve algum erro na abertura do arquivo')
    else:
        try:
            a. write(f'\nConnection failure: Alert sent by email > | Error: {msg_erro} | {data_hora_atual}\n')
            a.write('-' * 133)
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro adicionado em {arq}')
            a.close()
