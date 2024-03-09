#pip install flet

import flet as ft

def main(pagina):

    # 1 - crair titulo
    texto = ft.Text("Bem Vindo ao ALANZAP! =D")
    pagina.add(texto)

    def enviar_msg_tunel(mensagem):
#        texto_entrada = ft.Text(nome_usuario + "" + mensagem)
        texto_entrada = ft.Text(mensagem)
        chat.controls.append(texto_entrada)
        pagina.update()

    pagina.pubsub.subscribe(enviar_msg_tunel)

    def enviarmsg(evento):
        # add msg no chat
        pagina.pubsub.send_all(nome_usuario.value + ": " + campo_mensagem.value)

        # limpar campo msg
        campo_mensagem.value=""

        pagina.update()

    chat = ft.Column()
    campo_mensagem = ft.TextField(label="Mensagem...", on_submit=enviarmsg)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviarmsg)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])

    def entrarchat(evento):
        # fechar popup
        popup.open = False
        # tirar botao iniciar chat
        pagina.remove(botao)
        # tirar o titulo alanzap
        pagina.remove(texto)
        # crair o chat
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} Entrou no Chat")        
        # colocar campo digitar mensagem
        # criar botão enviar
        pagina.add(linha_enviar)
        
        
        #botao_enviar = ft.ElevatedButton("Enviar", on_click=enviarmsg)

        pagina.update()


    titulo_popup = ft.Text("Chat Iniciado!")
    nome_usuario = ft.TextField(label="Escreva Seu Nome")
    botao_chat = ft.ElevatedButton("Entrar no Chat", on_click=entrarchat)


    popup = ft.AlertDialog(
        open = False,
        modal = True,
        title = titulo_popup,
        content = nome_usuario,
        actions = [botao_chat]
    )

    # 2 - Criar botão "iniciar chat"
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(botao)
    # 3 - clicou no botão - Abre popup
        # titulo: bem vindo ao AlanZAP
        # campo: escreva seu nome
        # botão: entrar no chat

    # 4 - chat

    # 5 - embaixo do chat:
        # digite suamensagem
        # botão enviar

    # flet -> framework

ft.app(target=main, view=ft.WEB_BROWSER)
