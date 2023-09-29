##importando bibliotecas##

import smtplib
from email.message import EmailMessage

mail = '<EMAIL AQUI>' #Variavel do email

msg = EmailMessage()

##componentes do mail##

msg.set_content('<MENSAGEM AQUI>')
#mensagem
msg['Subject'] = '<ASSUNTO AQUI>' #Assunto
msg['From'] = mail #Remetente
msg['To'] = mail #Destinatário

##Mandando o email pelo smtp gmail.##

def send():    
                            #server = smtplib.SMTP_SSL('smtp.gmail.com', 465) 
    server = smtplib.SMTP_SSL('<HOST AQUI:>!^recomendo^codigo^acima^!', PORTA AQUI) #Protocolo
    server.login(meio, open('senha.txt').read().strip()) #Login
    server.send_message(msg) #Servidor envia mensagem com todos os componentes dela
    server.quit() #Sai do servidor
    print("Sucesso ao enviar o email") #Só pra confirmar

send() #Executa função acima