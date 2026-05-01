from SMS import SMS
from Email import Email
from PushNotification import PushNotification

def alertar_usuario(canal, mensagem):
    canal.enviar(mensagem)


canal_sms = SMS()
canal_emil = Email()
canal_push_notification = PushNotification()

alertar_usuario(canal_sms, "ESTOU ENVIANDO UM SMS")
alertar_usuario(canal_emil, "ESTOU ENVIANDO UM E-mail")
alertar_usuario(canal_push_notification, "ESTOU ENVIANDO UM PushNotification")