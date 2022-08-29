from cgitb import text
from operator import truediv
from typing import Text
#from colorama import Cursor
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from PyQt5 import uic,QtWidgets
import sqlite3

from pyparsing import str_type

valor_selec = 0
#import mysql.connector

banco = sqlite3.connect('banco_programa.db')
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (id INTEGER PRIMARY KEY AUTOINCREMENT, nome_cad_funcionario text, login_cad_funcionario text NOT NULL UNIQUE, senha_cad_funcionario text)") 
cursor.execute("CREATE TABLE IF NOT EXISTS cadastro_clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome text, apelido text, sexo text, cpf text, email text, telefone text, identidade int, oemissor text, nascimento text, nacionalidade text, estadoc text, naturalidade text, notas text)")
cursor.execute("INSERT OR IGNORE INTO cadastro (nome_cad_funcionario, login_cad_funcionario, senha_cad_funcionario) VALUES ('Administrador','admin',123)")
banco.commit()
banco.close()

def faz_login():

    tela_login.label_5.setText("")
    nome_usuario = tela_login.lineEdit.text()
    senha = tela_login.lineEdit_3.text()
    banco = sqlite3.connect('banco_programa.db')
    cursor = banco.cursor()
    try:
        
        cursor.execute(("SELECT senha_cad_funcionario FROM cadastro WHERE login_cad_funcionario = '{}'".format(nome_usuario)))
        senha_bd = cursor.fetchall()
        #Verifica se a senha está vazia e caso esteja é atribuído o valor 0
        if len(senha_bd) > 0:
            senha_bd2 = senha_bd[0][0]
        else:
            senha_bd2 = 0
        banco.close()
    
    except:
        print("Erro ao validar login!")
        
    if senha == senha_bd2:

        print("Passou!")
        tela_login.close()
        s_menu.show()

    else:

        tela_login.label_5.setText("Dados de login incorretos!")
        print("Erro")

# Cadastra cliente no banco

def cadastrar_dados_cliente():
    # banco = mysql.connector.connect(
    #     host="localhost",
    #     database="fender",
    #     user="root",
    #     password=""
    # )

    nome2 = usuario_cad.nome.text()
    apelido2 = usuario_cad.apelido.text()

    if usuario_cad.radioMasculino.isChecked():
        sexo = "m"
    if usuario_cad.radioFeminino.isChecked():
        sexo = "f"

    cpf2 = usuario_cad.cpf.text()
    email2 = usuario_cad.email.text()
    telefone2 = usuario_cad.telefone.text()
    identidade2 = usuario_cad.identidade.text()
    oemissor2 = usuario_cad.oEmissor.text()
    nascimento2 = usuario_cad.dateEdit.text()
    nacionalidade2 = usuario_cad.nacionalidade.text()

    if usuario_cad.radioSolteiro.isChecked():
        estadoC = "solteiro"
        value=1
    if usuario_cad.radioCasado.isChecked():
        estadoC = "casado"
    if usuario_cad.radioDivorciado.isChecked():
        estadoC = "divorciado"
    if usuario_cad.radioViuvo.isChecked():
        estadoC = "viuvo"

    naturalidade2 = usuario_cad.naturalidade.text()
    notas2 = usuario_cad.notas.text()
    banco = sqlite3.connect('banco_programa.db')
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS cadastro_clientes (id inter, nome text, apelido text, sexo text, cpf text, email text, telefone text, identidade int, oemissor text, nascimento text, nacionalidade text, estadoc text, naturalidade text, notas text)")
    cursor.execute("INSERT INTO cadastro_clientes (nome, apelido, sexo, cpf, email, telefone, identidade, oemissor, nascimento, nacionalidade, estadoc, naturalidade, notas)  VALUES ('" +nome2 + "','" + apelido2 + "','" + sexo + "','" + cpf2 + "','" + email2 + "','" + telefone2 + "','" + identidade2 + "','" + oemissor2 + "','" + nascimento2 +"','" + nacionalidade2 + "','" + estadoC + "','" + naturalidade2 + "','" + notas2 + "')")
    banco.commit()
    banco.close()

    #
    # Limpa formulárlio
    #

    usuario_cad.nome.setText("")
    usuario_cad.apelido.setText("")
    usuario_cad.cpf.setText("")
    usuario_cad.email.setText("")
    usuario_cad.telefone.setText("")
    usuario_cad.identidade.setText("")
    usuario_cad.oEmissor.setText("")
    usuario_cad.nacionalidade.setText("")
    usuario_cad.naturalidade.setText("")
    usuario_cad.notas.setText("")
    usuario_cad.label_2.setText("Cliente cadastrado com sucesso!")

    # cursor = banco.cursor()
    # comando = " INSERT INTO cadastro (nome, apelido, sexo, cpf, email, tel, identidade, oEmissor, nascimento, nacionalidade, estadocivil, naturalidade, notas) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # val = (str(nome2), str(apelido2), sexo, cpf2, email2, telefone2, identidade2, oEmissor2, nascimento2, nacionalidade2,
    # estadoC, naturalidade2, notas2)
    # cursor.execute(comando, val)
    # banco.commit()

# Cadastra funcionário no banco

def cad_funcionario():
    nome_cad_funcionario = tela_cad_login.lineEdit.text()
    login_cad_funcionario = tela_cad_login.lineEdit_2.text()
    senha_cad_funcionario = tela_cad_login.lineEdit_3.text()
    c_senha_cad_funcionario = tela_cad_login.lineEdit_4.text()

    if (senha_cad_funcionario == c_senha_cad_funcionario):
        try:
            banco = sqlite3.connect('banco_programa.db')
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome_cad_funcionario text, login_cad_funcionario text, senha_cad_funcionario text)")
            cursor.execute("INSERT INTO cadastro (nome_cad_funcionario, login_cad_funcionario, senha_cad_funcionario) VALUES ('"+nome_cad_funcionario+"','"+login_cad_funcionario+"','"+senha_cad_funcionario+"')")

            banco.commit()
            banco.close()
            tela_cad_login.label_2.setText("Usuário cadastrado com sucesso!")
            tela_cad_login.label_3.setText("")

            #
            #Limpa Formulário
            #

            nome_cad_funcionario = tela_cad_login.lineEdit.setText("")
            login_cad_funcionario = tela_cad_login.lineEdit_2.setText("")
            senha_cad_funcionario = tela_cad_login.lineEdit_3.setText("")
            c_senha_cad_funcionario = tela_cad_login.lineEdit_4.setText("")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        tela_cad_login.label_3.setText("As senhas digitadas estão diferentes!")
        tela_cad_login.label_2.setText(" ")

# Exclui clientes

def excluir_cliente():
    linha = t_consulta.tableWidget.currentRow()
    t_consulta.tableWidget.removeRow(linha)
    banco = sqlite3.connect('banco_programa.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cadastro_clientes")
    dados_lidos = cursor.fetchall()
    
    ex_cli_valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM cadastro_clientes WHERE id="+ str(ex_cli_valor_id))

    banco.commit()
    banco.close()

# Exclui funcionário

def excluir_funcionario():

    linha = t_consulta_f.tableWidget.currentRow()
    banco = sqlite3.connect('banco_programa.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cadastro")
    dados_lidos = cursor.fetchall()
    t_consulta_f.label_2.setText("")

    ex_fun_valor_id = dados_lidos[linha][0]

    if ex_fun_valor_id == 1:
        t_consulta_f.label_2.setText("Esse funcionário não pode ser excluído.")

    else:

        cursor.execute("DELETE FROM cadastro WHERE id="+ str(ex_fun_valor_id))
        t_consulta_f.tableWidget.removeRow(linha)

    banco.commit()
    banco.close()

# localiza cliente

def consulta_cliente():

    r_cpf = t_consulta.cpf.text()
    banco = sqlite3.connect('banco_programa.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cadastro_clientes where cpf = '{}'".format(r_cpf))
    dados_lidos = cursor.fetchall()
    t_consulta.label_2.setText("")
        
    t_consulta.tableWidget.setRowCount(len(dados_lidos))
    t_consulta.tableWidget.setColumnCount(13)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 13):
           t_consulta.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    banco.close()

# localiza funcionário

def consulta_funcionario():

    r_login = t_consulta_f.login.text()
    banco = sqlite3.connect('banco_programa.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cadastro where login_cad_funcionario = '{}'".format(r_login))
    dados_lidos = cursor.fetchall()
        
    t_consulta_f.tableWidget.setRowCount(len(dados_lidos))
    t_consulta_f.tableWidget.setColumnCount(3)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
           t_consulta_f.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    banco.close()

# Lista todos os clientes

def l_todos_clientes():
    
    banco = sqlite3.connect('banco_programa.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cadastro_clientes")
    dados_lidos = cursor.fetchall()

           
    t_consulta.tableWidget.setRowCount(len(dados_lidos))
    t_consulta.tableWidget.setColumnCount(14)
    
    for i in range(0, len(dados_lidos)):
        for j in range(0, 14):
           t_consulta.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
           t_consulta.label_2.setText("")

    
    if len(dados_lidos) > 0:
            dados_lidos2 = dados_lidos[i][j]
    else:
            t_consulta.label_2.setText("Nenhum cliente cadastrado!")
    
    banco.close()

# Lista todos os funcionários

def l_todos_funcionarios():
    
    t_consulta_f.label_2.setText("")
    banco = sqlite3.connect('banco_programa.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cadastro")
    dados_lidos = cursor.fetchall()
    print(dados_lidos)
    t_consulta_f.tableWidget.setRowCount(len(dados_lidos))
    t_consulta_f.tableWidget.setColumnCount(3)
    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
           t_consulta_f.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    banco.close()

# Gera arquivo clientes pdf

def gerar_clientes_pdf():
    print("gerar_pdf")
    banco = sqlite3.connect('banco_programa.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cadastro_clientes")
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("Clientes Cadastrados.pdf", pagesize=landscape(letter))
    pdf.setFont("Times-Bold", 18)
    pdf.drawString(300,550, "Clientes Cadastrados")
    pdf.setFont("Times-Bold", 10)

    #pdf.drawString(10, 750, "ID")
    pdf.drawString(10, 500, "NOME")
    pdf.drawString(130, 500, "APELIDO")
    pdf.drawString(230, 500, "SEXO")
    pdf.drawString(260, 500, "CPF")
    pdf.drawString(330, 500, "E-MAIL")
    pdf.drawString(480, 500, "TELEFONE")
    pdf.drawString(550, 500, "IDENTIDADE")
    pdf.drawString(630, 500, "ÓRGÃO EMISSOR")


    for i in range(0, len(dados_lidos)):
        y = y + 20
        #arpdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(10,500 - y, str(dados_lidos[i][1]))
        pdf.drawString(130,500 - y, str(dados_lidos[i][2]))
        pdf.drawString(230,500 - y, str(dados_lidos[i][3]))
        pdf.drawString(260,500 - y, str(dados_lidos[i][4]))
        pdf.drawString(330,500 - y, str(dados_lidos[i][5]))
        pdf.drawString(480,500 - y, str(dados_lidos[i][6]))
        pdf.drawString(550,500 - y, str(dados_lidos[i][7]))
        pdf.drawString(630,500 - y, str(dados_lidos[i][8]))
    
    pdf.save()
    print("O pdf foi gerado")

# Gera arquivo funcionarios pdf

def gerar_funcionarios_pdf ():
    print("gerar_pdf")
    banco = sqlite3.connect('banco_programa.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cadastro")
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("Funcionários Cadastrados.pdf", pagesize=landscape(letter))
    pdf.setFont("Times-Bold", 18)
    pdf.drawString(300,550, "Funcionários Cadastrados")
    pdf.setFont("Times-Bold", 10)

    #pdf.drawString(10, 750, "ID")
    pdf.drawString(10, 500, "NOME")
    pdf.drawString(130, 500, "LOGIN")
    
    for i in range(0, len(dados_lidos)):
        y = y + 20

        pdf.drawString(10,500 - y, str(dados_lidos[i][1]))
        pdf.drawString(130,500 - y, str(dados_lidos[i][2]))
            
    pdf.save()
    print("O pdf foi gerado")

# carrega os dados do cliente para alteração na tela

def editar_cliente():
   
    global valor_selec

    linha = t_consulta.tableWidget.currentRow()

    banco = sqlite3.connect('banco_programa.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cadastro_clientes")
    dados_lidos = cursor.fetchall()   
    valor_id = dados_lidos[linha][0]
    valor_selec = valor_id
    cursor.execute("SELECT * FROM cadastro_clientes WHERE id ="+ str(valor_id))
    c_cliente = cursor.fetchall()
    print(c_cliente)
    t_consulta.close()
    ed_cliente.show()

    ed_cliente.nome.setText(str(c_cliente[0][1]))
    ed_cliente.apelido.setText(str(c_cliente[0][2]))
    
    s = str(c_cliente[0][3])
    if s == "m":
        ed_cliente.radioMasculino.setChecked(True)
    else:
        ed_cliente.radioFeminino.setChecked(True)
    
    ed_cliente.cpf.setText(str(c_cliente[0][4]))
    ed_cliente.email.setText(str(c_cliente[0][5]))
    ed_cliente.telefone.setText(str(c_cliente[0][6]))
    ed_cliente.identidade.setText(str(c_cliente[0][7]))
    ed_cliente.oEmissor.setText(str(c_cliente[0][8]))

    # d = str(c_cliente[0][9])
    # print(d)
    # ed_cliente.dateEdit.setDate(d)

    ed_cliente.nacionalidade.setText(str(c_cliente[0][10]))

    r = str(c_cliente[0][11])
    if r == "casado":
        ed_cliente.radioCasado.setChecked(True)
    elif r == "solteiro":
        ed_cliente.radioSolteiro.setChecked(True)
    elif r == "divorciado":
        ed_cliente.radio.Divorciado.setChecked(True)
    else: ed_cliente.radioViuvo.setChecked(True)

    ed_cliente.naturalidade.setText(str(c_cliente[0][12]))
    ed_cliente.notas.setText(str(c_cliente[0][13]))
   
    ed_cliente.label_2.setText("")

 # edita cliente

def editar_cliente2():
    
    #pega o número do id
    global valor_selec

    nome2 = ed_cliente.nome.text()
    apelido2 = ed_cliente.apelido.text()

    if ed_cliente.radioMasculino.isChecked():
        sexo = "m"
    if ed_cliente.radioFeminino.isChecked():
        sexo = "f"

    cpf2 = ed_cliente.cpf.text()
    email2 = ed_cliente.email.text()
    telefone2 = ed_cliente.telefone.text()
    identidade2 = ed_cliente.identidade.text()
    oemissor2 = ed_cliente.oEmissor.text()
    nascimento2 = ed_cliente.dateEdit.text()
    nacionalidade2 = ed_cliente.nacionalidade.text()

    if ed_cliente.radioSolteiro.isChecked():
        estadoC = "solteiro"
        value=1
    if ed_cliente.radioCasado.isChecked():
        estadoC = "casado"
    if ed_cliente.radioDivorciado.isChecked():
        estadoC = "divorciado"
    if ed_cliente.radioViuvo.isChecked():
        estadoC = "viuvo"

    naturalidade2 = ed_cliente.naturalidade.text()
    notas2 = ed_cliente.notas.text()

    banco = sqlite3.connect('banco_programa.db')
    cursor = banco.cursor()
    cursor.execute("UPDATE cadastro_clientes SET nome = '{}', apelido = '{}', sexo = '{}', cpf = '{}', email = '{}', telefone = '{}', identidade = '{}', oemissor = '{}', nascimento = '{}', nacionalidade = '{}', estadoc = '{}', naturalidade = '{}', notas = '{}' WHERE id = {}".format(nome2, apelido2, sexo, cpf2, email2, telefone2, identidade2, oemissor2, nascimento2, nacionalidade2, estadoC, naturalidade2, notas2, valor_selec))
    banco.commit()
    banco.close()

     #
    # Limpa formulárlio
    #

    ed_cliente.nome.setText("")
    ed_cliente.apelido.setText("")
    ed_cliente.cpf.setText("")
    ed_cliente.email.setText("")
    ed_cliente.telefone.setText("")
    ed_cliente.identidade.setText("")
    ed_cliente.oEmissor.setText("")
    ed_cliente.nacionalidade.setText("")
    ed_cliente.naturalidade.setText("")
    ed_cliente.notas.setText("")
    ed_cliente.label_2.setText("Cliente alterado com sucesso!")

def troca_senha():
    
    t_consulta_f.close()
    ed_funcionario.show()

    ed_funcionario.label_2.setText("")

def troca_senha_fun():

    senha_cad_funcionario = ed_funcionario.lineEdit_3.text()
    c_senha_cad_funcionario = ed_funcionario.lineEdit_4.text()

    linha = t_consulta_f.tableWidget.currentRow()
    banco = sqlite3.connect('banco_programa.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cadastro")
    dados_lidos = cursor.fetchall()
    
    fun_valor_id = dados_lidos[linha][0]

    if (senha_cad_funcionario == c_senha_cad_funcionario):

        try:
           
            cursor.execute("UPDATE cadastro SET senha_cad_funcionario = '{}' WHERE id = {}".format(senha_cad_funcionario, fun_valor_id))
            banco.commit()
            banco.close()
            ed_funcionario.label_2.setText("Senha alterada!")
            ed_funcionario.label_3.setText("")

            #
            #Limpa Formulário
            #

            senha_cad_funcionario = ed_funcionario.lineEdit_3.setText("")
            c_senha_cad_funcionario = ed_funcionario.lineEdit_4.setText("")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        ed_funcionario.label_3.setText("As senhas digitadas estão diferentes!")
        ed_funcionario.label_2.setText("")   

def chama_tela_menu3():
    usuario_cad.close()
    s_menu.show()

def chama_tela_localiza_cliente():
    ed_cliente.close()
    t_consulta.show()

def chama_localiza_cliente():

    t_consulta.show()
    t_consulta.cpf.setText("")
    t_consulta.label_2.setText("")
    s_menu.close()

def chama_tela_menu():
    t_consulta.close()
    t_consulta_f.close()
    s_menu.show()

def chama_tela_consulta_cliente():
    s_menu.close()
    t_consulta.show()

def chama_tela_consulta_funcionario():
    s_menu.close()
    ed_funcionario.close()
    t_consulta_f.show()
    t_consulta_f.label_2.setText("")

def logout():
    s_menu.close()
    tela_login.show()
    nome_usuario = tela_login.lineEdit.setText("")
    senha = tela_login.lineEdit_3.setText("")

def chama_tela_cad_login():
    s_menu.close()
    tela_cad_login.show()

def chama_tela_menu2():
    tela_cad_login.close()
    s_menu.show()

def chama_tela_cad_cliente():

    tela_cad_login.label_2.setText("")
    s_menu.close()
    usuario_cad.show()

       
app=QtWidgets.QApplication([])
tela_login=uic.loadUi("login.ui")
usuario_cad=uic.loadUi("cadastro.ui")
ed_cliente=uic.loadUi("ed_cliente.ui")
tela_cad_login=uic.loadUi("cad_user_programa.ui")
s_menu=uic.loadUi("menu.ui")
t_consulta=uic.loadUi("tela_consulta_cliente.ui")
t_consulta_f=uic.loadUi("tela_consulta_funcionario.ui")
ed_funcionario=uic.loadUi("ed_funcionario.ui")
ed_funcionario.pushButton.clicked.connect(troca_senha_fun)
ed_funcionario.pushButton_2.clicked.connect(chama_tela_consulta_funcionario)
t_consulta.pushButton_7.clicked.connect(consulta_cliente)
t_consulta_f.pushButton_7.clicked.connect(consulta_funcionario)
t_consulta.pushButton_8.clicked.connect(l_todos_clientes)
t_consulta.pushButton_4.clicked.connect(editar_cliente)
t_consulta_f.pushButton_8.clicked.connect(l_todos_funcionarios)
t_consulta.pushButton_6.clicked.connect(chama_tela_menu)
t_consulta_f.pushButton_6.clicked.connect(chama_tela_menu)
t_consulta.pushButton.clicked.connect(gerar_clientes_pdf)
t_consulta_f.pushButton.clicked.connect(gerar_funcionarios_pdf)
t_consulta.pushButton_5.clicked.connect(excluir_cliente)
t_consulta_f.pushButton_5.clicked.connect(excluir_funcionario)
t_consulta_f.pushButton_4.clicked.connect(troca_senha)
tela_cad_login.pushButton_2.clicked.connect(chama_tela_menu2)
tela_cad_login.pushButton.clicked.connect(cad_funcionario)
s_menu.pushButton.clicked.connect(chama_tela_cad_cliente)
s_menu.pushButton_2.clicked.connect(chama_tela_cad_login)
s_menu.pushButton_4.clicked.connect(logout)
s_menu.pushButton_5.clicked.connect(chama_localiza_cliente)
s_menu.pushButton_3.clicked.connect(chama_tela_consulta_funcionario)
usuario_cad.cadastrar.clicked.connect(cadastrar_dados_cliente)
usuario_cad.pushButton_3.clicked.connect(chama_tela_menu3)
ed_cliente.cadastrar.clicked.connect(editar_cliente2)
ed_cliente.pushButton_3.clicked.connect(chama_tela_localiza_cliente)
tela_login.pushButton.clicked.connect(faz_login)
tela_login.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
tela_login.show()
app.exec()
