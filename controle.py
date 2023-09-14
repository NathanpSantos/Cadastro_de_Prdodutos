from PyQt5 import  uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="projeto_cadastro"
)

def editar_dados():
    global numero_id

    linha = segunda_tela.tableWidget.currentRow()
    
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM produtos WHERE id="+ str(valor_id))
    produto = cursor.fetchall()
    tela_editar.show()

    tela_editar.lineEdit.setText(str(produto[0][0])) # id
    tela_editar.lineEdit_2.setText(str(produto[0][1])) # código
    tela_editar.lineEdit_3.setText(str(produto[0][2])) # tipo
    tela_editar.lineEdit_4.setText(str(produto[0][3])) # setor
    tela_editar.lineEdit_5.setText(str(produto[0][4])) # fornecedor
    tela_editar.lineEdit_6.setText(str(produto[0][5])) # categoria

    numero_id = valor_id


def salvar_valor_editado():
    global numero_id

    # ler dados do lineEdit
    codigo = tela_editar.lineEdit_2.text()
    tipo = tela_editar.lineEdit_3.text()
    setor = tela_editar.lineEdit_4.text()
    fornecedor = tela_editar.lineEdit_5.text()
    categoria = tela_editar.lineEdit_6.text()

    # atualizar os dados no banco
    cursor = banco.cursor()
    comando_SQL = "UPDATE produtos SET codigo = %s, tipo = %s, setor = %s, fornecedor = %s, categoria = %s WHERE id = %s"
    dados = (codigo, tipo, setor, fornecedor, categoria, numero_id)
    cursor.execute(comando_SQL, dados)
    banco.commit()
    #atualizar as janelas
    tela_editar.close()
    segunda_tela.close()
    chama_segunda_tela()

    

    
    
    
def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id="+ str(valor_id))


def gerar_pdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    y = 0
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10,750, "ID")
    pdf.drawString(110,750, "CODIGO")
    pdf.drawString(210,750, "TIPO")
    pdf.drawString(310,750, "SETOR")
    pdf.drawString(410,750, "FORNECEDOR")
    pdf.drawString(510,750, "CATEGORIA")


    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))
        pdf.drawString(510,750 - y, str(dados_lidos[i][5]))
    pdf.save()
    print("PDF FOI GERADO COM SUCESSO!")

def funcao_principal():
    linha1 = tela.lineEdit.text() # código
    linha2 = tela.lineEdit_5.text() # tipo
    linha3 = tela.lineEdit_6.text() # setor
    linha4 = tela.lineEdit_7.text() # fornecedor
    
    categoria = ""
    
    if tela.radioButton.isChecked():
        print("Categoria Sacaria foi selecionada")
        categoria = "Sacarias"
    elif tela.radioButton_2.isChecked():
        print("Categoria Telhas foi selecionada")
        categoria = "Telhas"
    elif tela.radioButton_3.isChecked():
        print("Categoria Madeiras foi selecionada")
        categoria = "Madeiras"
    elif tela.radioButton_4.isChecked():
        print("Categoria Metalão foi selecionada")
        categoria = "Metalão"
    elif tela.radioButton_5.isChecked():
        print("Categoria Fitas foi selecionada")
        categoria = "Fitas"
    elif tela.radioButton_6.isChecked():
        print("Categoria Drywall foi selecionada")
        categoria = "Drywall"
    elif tela.radioButton_7.isChecked():
        print("Categoria Caixa d'água foi selecionada")
        categoria = "Caixa d'água"
    elif tela.radioButton_8.isChecked():
        print("Categoria Ferro foi selecionada")
        categoria = "Ferro"
    elif tela.radioButton_9.isChecked():
        print("Categoria Blocos foi selecionada")
        categoria = "Blocos"
    elif tela.radioButton_10.isChecked():
        print("Categoria Caixa d'água foi selecionada")
        categoria = "Caixa d'água"
    elif tela.radioButton_11.isChecked():
        print("Categoria Tubos foi selecionada")
        categoria = "Tubos"
    elif tela.radioButton_12.isChecked():
        print("Categoria Argamassa foi selecionada")
        categoria = "Argamassa"
    elif tela.radioButton_7.isChecked():
        print("Categoria Compensados foi selecionada")
        categoria = "CCompensados"
    else:
        print("Nenhuma categoria foi selecionada")
        categoria = "Nenhuma"

    print("Código:", linha1)
    print("Tipo:", linha2)
    print("Setor:", linha3)
    print("Fornecedor:", linha4)
    print("Categoria:", categoria)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo,tipo,setor,fornecedor,categoria) VALUES (%s,%s,%s,%s,%s)"
    dados = (str(linha2), str(linha3), str(linha4), str(linha4), categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()
    tela.lineEdit.setText("")
    tela.lineEdit_5.setText("")
    tela.lineEdit_6.setText("")
    tela.lineEdit_7.setText("")


def chama_segunda_tela():
    segunda_tela.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(7)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 6):
           segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j]))) 
   
    
app=QtWidgets.QApplication([])
tela=uic.loadUi("tela.ui")
segunda_tela=uic.loadUi("listar_dados.ui")
tela_editar=uic.loadUi("menu_editar.ui")
tela.pushButton.clicked.connect(funcao_principal)
tela.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton_1.clicked.connect(gerar_pdf)
segunda_tela.pushButton_2.clicked.connect(excluir_dados)
segunda_tela.pushButton_3.clicked.connect(editar_dados)
tela_editar.pushButton.clicked.connect(salvar_valor_editado)

tela.show()
app.exec()