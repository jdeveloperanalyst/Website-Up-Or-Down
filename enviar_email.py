def env_email():
    import smtplib
    remetente = ''
    senha = ''
    destinatario = ''
    assunto = ''
    corpo = ''
    mensagem = f'Subject: {assunto}\n\n{corpo}'
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
            servidor.starttls()
            servidor.login(remetente, senha)
            servidor.sendmail(remetente, destinatario, mensagem)
            print('E-mail enviado com sucesso!')
    except Exception as e:
        print(f'Erro ao enviar o e-mail: {e}')
