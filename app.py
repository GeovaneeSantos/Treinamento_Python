#Antes de rodar esse código, certifique-se de ter o customtkinter instalado. Você pode instalar usando o comando: pip install customtkinter
import customtkinter as ctk #importando o tkinter e atribuindo um "apelido" para chamá-lo

#1 Configuração da aparência
ctk.set_appearance_mode("dark") #aqui você pode escolher o modo "dark" ou "light"

#2 Criação das funções de funcionalidade
def validar_login(): #função que valida o login
    usuario = campo_usuario.get() #get() pega o valor digitado no campo de usuário e guarda na variavel usuario
    senha = campo_senha.get() #get() pega o valor digitado no campo de senha e guarda na variavel senha
    
    #aqui você pode colocar a lógica de validação, como verificar em um banco de dados ou uma lista de usuários
    if usuario == "admin" and senha == "1234": #exemplo simples de validação
        resultado_login.configure(text = "Login feito com Sucesso !", text_color="green") #se o login for válido, mostra a mensagem de sucesso em verde
    else:
        resultado_login.configure(text = "Usuário ou senha incorretos.", text_color="red")

#3 Criação da janela principal
app = ctk.CTk() #criando a janela principal e guardando ela na variavel app
app.title("Sistema de Login") #definindo o título da janela "Aquele texto que aparece na barra superior"
app.geometry("300x300") #definindo o tamanho da janela (largura x altura) 

#4 Criação dos campos
#Para criar os campos, precisamos usar os elementos do tkinter que são:

#Label (Etiqueta/titulo que fica acima do campo)
#Entry (Campo de entrada de dados)
#Button (Elemento clicável que executa uma ação "Botao")

#Label
label_usuario = ctk.CTkLabel(app, text="Usuário:") #Aqui estou criando um elemento label que recebe como primeiro argumento a janela principal (app) e o segundo argumento é o texto que aparecerá na tela e guardando ele na variavel label_usuario

label_usuario.pack(pady=10) #O pack() serve para "empacotar" o elemento na janela, ou seja, para que ele apareça na tela pady é o espaçamento vertical (em pixels) entre o elemento e os outros elementos ou bordas da janela

#Entry
campo_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário") #aqui estou criando um elemento entry que recebe como primeiro argumento a janela principal (app) e o segundo argumento é o texto que aparecerá dentro do campo como dica e guardando ele na variavel campo_usuario

campo_usuario.pack(pady=10) #Empacotando o campo de usuário na janela com um espaçamento vertical de 10 pixels

#Label
label_senha = ctk.CTkLabel(app, text="Senha:") #Label do campo de senha
label_senha.pack(pady=10) #Empacotando o label de senha na janela com um espaçamento vertical de 10 pixels

#Entry
campo_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha", show="*") #Entry do campo de senha, o argumento show="*" faz com que os caracteres digitados apareçam como asteriscos

campo_senha.pack(pady=10) #Empacotando o campo de senha na janela com um espaçamento vertical de 10 pixels

#Button
botao_login = ctk.CTkButton(app, text = "Login", command = validar_login) #aqui estou criando um botão que recebe como primeiro argumento a janela principal (app), o segundo argumento é o texto que aparecerá no botão e o terceiro argumento é a função que será executada quando o botão for clicado 

botao_login.pack(pady=10) #Empacotando o botão de login na janela com um espaçamento vertical de 10 pixels

#campo de feedback de login
resultado_login = ctk.CTkLabel(app, text="") #Label vazio que será usado para mostrar mensagens de feedback de login
resultado_login.pack(pady=10) #Empacotando o label de resultado de login na janela com um espaçamento vertical de 10 pixels

#5 Iniciar a aplicação
app.mainloop() #mantém a janela aberta, aguardando interações do usuário