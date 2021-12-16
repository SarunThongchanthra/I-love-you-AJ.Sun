import sys
from PyQt5.uic import loadUi 
from PyQt5 import QtWidgets, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QTimer, QTime

count_for_user = 0
setuser1 = False
setuser2 = False
setuser3 = False
setadduser = True
setremoveuser = False
username_login = str
addproduct_accept = False
namex = ''
productcodex = ''
costbuyx = ''
costsellx = ''
quantityx = ''
daterecivex = ''
dateexpirex = ''
checkboxx = False
idtext_list = []
product_X = [[],[],[]]
which_one = str
userid = 0

class User(QDialog):
    def __init__(self):
        super(User, self).__init__()
        loadUi("user.ui",self)
        self.pushbutton_adduser.clicked.connect(self.adduser)
        self.pushbutton_removeuser.clicked.connect(self.removeuser)
        self.pushbutton_user1.setVisible(setuser1)
        self.pushbutton_user2.setVisible(setuser2)
        self.pushbutton_user3.setVisible(setuser3)
        self.pushbutton_adduser.setVisible(setadduser)
        self.pushbutton_removeuser.setVisible(setremoveuser)
        self.lable_usernumber.setText(str(count_for_user)+'/'+'3')
        self.pushbutton_user1.clicked.connect(self.user)
        self.pushbutton_user2.clicked.connect(self.user)
        self.pushbutton_user3.clicked.connect(self.user)
            
    def removeuser(self):
        global count_for_user, setuser1, setuser2, setuser3, setadduser, setremoveuser
        count_for_user = count_for_user - 1 
        if count_for_user == 2:
            setuser1 = True
            setuser2 = True
            setuser3 = False
            setadduser = True
            setremoveuser = True
        elif count_for_user == 1:
            setuser1 = True
            setuser2 = False
            setuser3 = False
            setadduser = True
            setremoveuser = True
        elif count_for_user == 0:
            setuser1 = False
            setuser2 = False
            setuser3 = False
            setadduser = True
            setremoveuser = False
        login = User()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
            
    def adduser(self):
        global count_for_user, setuser1, setuser2, setuser3, setadduser, setremoveuser
        count_for_user = count_for_user + 1
        if count_for_user == 1:
            setuser1 = True
            setuser2 = False
            setuser3 = False
            setadduser = True
            setremoveuser = True
        elif count_for_user == 2:
            setuser1 = True
            setuser2 = True
            setuser3 = False
            setadduser = True
            setremoveuser = True
        elif count_for_user == 3:
            setuser1 = True
            setuser2 = True
            setuser3 = True
            setadduser = False
            setremoveuser = True
        login = User()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def user(self):
        global username_login, userid
        if self.sender() == self.pushbutton_user1:
            username_login = "User 1"
            userid = 0
        elif self.sender() == self.pushbutton_user2:
            username_login = "User 2"
            userid = 1
        else:
            username_login = "User 3"
            userid = 2
        login = Main()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("main.ui",self)
        save()
        self.pushbutton_changeuser.clicked.connect(self.change_user)
        self.lable_username.setText(str(username_login))
        self.pushbutton_addproduct.clicked.connect(self.addproduct)
        self.lable_productcount.setText('Product:'+' '+ str(len(product_X[userid])))
        self.combobox_sort.activated.connect(self.sort)
        for i in range(0,len(product_X[userid])):
            self.generateGroupbox(i)
            self.pushbutton_list.clicked.connect(self.listt)
            self.comboBox_options.activated.connect(self.option)
        timer = QTimer(self)
        timer.timeout.connect(self.clock)
        timer.start(1000)
        self.clock()
    
    def listt(self):
        global which_one
        which_one = self.sender().objectName()
        which_one = int(which_one[15:])
        login = Listt()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def option(self, x):
        global which_one
        which_one = self.sender().objectName()
        which_one = int(which_one[16:])
        if x == 1:
            login = Infoo()
        elif x == 2:
            login = Edit()
        elif x == 3:
            del product_X[userid][which_one]
            login = Main()
        if x != 0:
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)
            
    def generateGroupbox(self,i):
        _translate = QtCore.QCoreApplication.translate
        self.groupbox_product = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupbox_product.setMinimumSize(QtCore.QSize(635, 91))
        self.groupbox_product.setMaximumSize(QtCore.QSize(635, 91))
        self.groupbox_product.setTitle("")
        self.groupbox_product.setObjectName("groupbox_product")
        self.lable_productname = QtWidgets.QLabel(self.groupbox_product)
        self.lable_productname.setGeometry(QtCore.QRect(10, 10, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.lable_productname.setFont(font)
        self.lable_productname.setStyleSheet("")
        self.lable_productname.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lable_productname.setObjectName("lable_productname")
        self.lable_id = QtWidgets.QLabel(self.groupbox_product)
        self.lable_id.setGeometry(QtCore.QRect(10, 60, 201, 21))
        self.lable_id.setMaximumSize(QtCore.QSize(201, 21))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.lable_id.setFont(font)
        self.lable_id.setStyleSheet("")
        self.lable_id.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lable_id.setObjectName("lable_id")
        self.lable_productremain = QtWidgets.QLabel(self.groupbox_product)
        self.lable_productremain.setGeometry(QtCore.QRect(230, 10, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(10)
        self.lable_productremain.setFont(font)
        self.lable_productremain.setStyleSheet("")
        self.lable_productremain.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lable_productremain.setObjectName("lable_productremain")
        self.lable_price = QtWidgets.QLabel(self.groupbox_product)
        self.lable_price.setGeometry(QtCore.QRect(450, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.lable_price.setFont(font)
        self.lable_price.setStyleSheet("")
        self.lable_price.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lable_price.setObjectName("lable_price")
        self.comboBox_options = QtWidgets.QComboBox(self.groupbox_product)
        self.comboBox_options.setGeometry(QtCore.QRect(450, 60, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.comboBox_options.setFont(font)
        self.comboBox_options.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-color: rgb(0, 0, 0);\n"
        "border-width : 0.5px;\n"
        "border-style:inset;")
        self.comboBox_options.setObjectName("comboBox_options"+str(i))
        self.comboBox_options.addItem("")
        self.comboBox_options.addItem("")
        self.comboBox_options.addItem("")
        self.comboBox_options.addItem("")
        self.pushbutton_list = QtWidgets.QPushButton(self.groupbox_product)
        self.pushbutton_list.setGeometry(QtCore.QRect(230, 60, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.pushbutton_list.setFont(font)
        self.pushbutton_list.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-color: rgb(0, 0, 0);\n"
        "border-width : 0.5px;\n"
        "border-style:inset;")
        self.pushbutton_list.setObjectName("pushbutton_list" + str(i))
        self.verticalLayout_2.addWidget(self.groupbox_product)
        self.lable_productname.setText(_translate("Dialog", "Name:" + str(product_X[userid][i].name)))
        self.lable_id.setText(_translate("Dialog", "Product ID:" + str(product_X[userid][i].productcode)))
        self.lable_productremain.setText("Product Remain:" +str(product_X[userid][i].quantity - product_X[userid][i].quantitysold))
        self.lable_price.setText(_translate("Dialog", "Price:"+ str(product_X[userid][i].costsell)))
        self.comboBox_options.setItemText(0, _translate("Dialog", "Options"))
        self.comboBox_options.setItemText(1, _translate("Dialog", "Info"))
        self.comboBox_options.setItemText(2, _translate("Dialog", "Edit"))
        self.comboBox_options.setItemText(3, _translate("Dialog", "Delete"))
        self.pushbutton_list.setText(_translate("Dialog", "List"))
             
    def sort(self,sortby):
        if sortby == 0:
            pass
        else:
            global product_X
            product_Y = []
            if sortby == 1:
                product_Y = sorted(product_X[userid], key=lambda x: x.name)
            elif sortby == 2:
                product_Y = sorted(product_X[userid], key=lambda x: x.productcode)
            elif sortby == 3:
                product_Y = sorted(product_X[userid], key=lambda x: x.quantity)
            elif sortby == 4:
                product_Y = sorted(product_X[userid], key=lambda x: x.costsell)
            product_X[userid] = product_Y
            login = Main()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)  
   
    def clock(self):
        currentime = QTime.currentTime()
        displaytext = currentime.toString('hh:mm')
        self.lable_clock.setText(displaytext)
        
    def change_user(self):
        login = User()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def addproduct(self):
        login = Addproduct()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Addproduct(QDialog):
    def __init__(self):
        super(Addproduct, self).__init__()
        loadUi("addproduct.ui",self)
        self.pushbutton_accept.setVisible(addproduct_accept)
        self.lable_warningbuy.setVisible(False)
        self.lable_warningsell.setVisible(False)
        self.lable_warningquantity.setVisible(False)
        self.pushbutton_back.clicked.connect(self.back)
        self.pushbutton_accept.clicked.connect(self.accept)
        self.lineEdit_name.textChanged.connect(self.check)
        self.lineEdit_costbuy.textChanged.connect(self.check)
        self.lineEdit_costsell.textChanged.connect(self.check)
        self.lineEdit_quantity.textChanged.connect(self.check)
        self.lineEdit_name.setText(str(namex))
        self.lineEdit_code.setText(str(productcodex))
        self.lineEdit_costbuy.setText(str(costbuyx))
        self.lineEdit_costsell.setText(str(costsellx))
        self.lineEdit_quantity.setText(str(quantityx))
        self.lineEdit_daterecive.setText(str(daterecivex))
        self.lineEdit_dateexpire.setText(str(dateexpirex))
        self.checkBox_id.setChecked(bool(checkboxx))
        
    def check(self):
        global addproduct_accept
        LEname = len(self.lineEdit_name.text())
        LEcostbuy = len(self.lineEdit_costbuy.text())
        LEcostsell = len(self.lineEdit_costsell.text())
        LEquantity = len(self.lineEdit_quantity.text())
        textcostbuy = self.lineEdit_costbuy.text()
        textcostsell = self.lineEdit_costsell.text()
        textquantity = self.lineEdit_quantity.text()
        if LEname != 0 and LEcostbuy != 0 and LEcostsell != 0 and LEquantity != 0:
            addproduct_accept = True
            self.pushbutton_accept.setVisible(addproduct_accept)
        if LEname == 0 or LEcostbuy == 0 or LEcostsell == 0 or LEquantity == 0:
            addproduct_accept = False
            self.pushbutton_accept.setVisible(addproduct_accept)
        if not textcostbuy.isdigit() and LEcostbuy != 0:
            self.lable_warningbuy.setVisible(True)
            addproduct_accept = False
            self.pushbutton_accept.setVisible(addproduct_accept)
        if not textcostsell.isdigit() and LEcostsell != 0:
            self.lable_warningsell.setVisible(True)
            addproduct_accept = False
            self.pushbutton_accept.setVisible(addproduct_accept)
        if not textquantity.isdigit() and LEquantity != 0:
            self.lable_warningquantity.setVisible(True)
            addproduct_accept = False
            self.pushbutton_accept.setVisible(addproduct_accept)
        if LEcostbuy == 0 or textcostbuy.isdigit():
            self.lable_warningbuy.setVisible(False)
        if LEcostsell == 0 or textcostsell.isdigit():
            self.lable_warningsell.setVisible(False)
        if LEquantity == 0 or textquantity.isdigit():
            self.lable_warningquantity.setVisible(False)

    def back(self):
        resettext()
        login = Main()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)    

    def accept(self):
        global namex,productcodex,costbuyx,costsellx,quantityx,daterecivex,dateexpirex,checkboxx,product_X
        namex = str(self.lineEdit_name.text())
        productcodex =  str(self.lineEdit_code.text())
        costbuyx = int(self.lineEdit_costbuy.text())
        costsellx = int(self.lineEdit_costsell.text())
        quantityx = int(self.lineEdit_quantity.text())
        daterecivex = str(self.lineEdit_daterecive.text())
        dateexpirex = str(self.lineEdit_dateexpire.text())
        checkboxx = bool(self.checkBox_id.isChecked())
        allproductidx = []
        if len(daterecivex) == 0:
            daterecivex = '-'
        if len(productcodex) == 0:
            productcodex = '-'
        if len(dateexpirex) == 0:
            dateexpirex = '-'
        if self.checkBox_id.isChecked() == True:
            login = Addproductid()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            list_sellx = []
            for allid in range(1,quantityx+1):
                allproductidx.append(namex +'-'+ str(allid))
                list_sellx.append(True)
            x = TheProduct(namex, productcodex, costbuyx, costsellx, quantityx, daterecivex, dateexpirex, allproductidx, list_sellx)
            product_X[userid].append(x)
            resettext()
            login = Main()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)
            
class Addproductid(QDialog):
    def __init__(self):
        global idtext_list
        super(Addproductid, self).__init__()
        loadUi("addproductid.ui",self)
        self.lable_quantitiy_addproductid.setText('Quantity:' + str(quantityx))
        self.pushbutton_back.clicked.connect(self.back)
        self.pushbutton_accept.clicked.connect(self.accept)
        idtext_list = []
        for i in range(1,int(quantityx)+1):
            self.generate_groupbox(i)
    
    def generate_groupbox(self,i):
        global idtext_list
        _translate = QtCore.QCoreApplication.translate
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setMinimumSize(QtCore.QSize(631, 41))
        self.groupBox.setMaximumSize(QtCore.QSize(631, 41))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lable_id = QtWidgets.QLabel(self.groupBox)
        self.lable_id.setGeometry(QtCore.QRect(10, 10, 41, 21))
        self.lable_id.setMaximumSize(QtCore.QSize(41, 21))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(16)
        self.lable_id.setFont(font)
        self.lable_id.setStyleSheet("")
        self.lable_id.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lable_id.setObjectName("lable_id")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(50, 10, 571, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.lable_id.setText(_translate("Dialog", (str(i)+")ID:")))
        idtext_list.append(self.lineEdit)
                
    def back(self):
        login = Addproduct()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def accept(self):
        global product_X
        allproductidx = []
        list_sellx = []
        for i in range(0,quantityx):
            list_sellx.append(True)
            allproductidx.append(idtext_list[i].text())
        x = TheProduct(namex, productcodex, costbuyx, costsellx, quantityx, daterecivex, dateexpirex, allproductidx, list_sellx)
        product_X[userid].append(x)
        resettext()
        login = Main()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Infoo(QDialog):
    def __init__(self):
        super(Infoo, self).__init__()
        loadUi("Info.ui",self)
        self.pushbutton_back.clicked.connect(self.back)
        self.lable_costbuy.setText('Cost(buy):'+str(product_X[userid][which_one].costbuy))
        self.lable_costsell.setText('Cost(sell):'+str(product_X[userid][which_one].costsell))
        self.lable_daterecive.setText('Date(recive):'+str(product_X[userid][which_one].daterecive))
        self.lable_dateexpire.setText('Date(expire):'+str(product_X[userid][which_one].dateexpire))
        self.lable_quantitysold.setText('Quantity Sold:'+str(product_X[userid][which_one].quantitysold))
        self.lable_revenue.setText('Revenue:'+str(product_X[userid][which_one].quantitysold * product_X[userid][which_one].costsell))
        self.lable_spend.setText('Money Spend:'+ str(product_X[userid][which_one].quantity * product_X[userid][which_one].costbuy))
        self.lable_profit.setText('Profit:'+str((product_X[userid][which_one].quantitysold * product_X[userid][which_one].costsell)-(product_X[userid][which_one].quantity * product_X[userid][which_one].costbuy)))
        self.lable_quantityremain.setText('Quantity Remain:'+str(product_X[userid][which_one].quantity - product_X[userid][which_one].quantitysold))
        
    def back(self):
        login = Main()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Edit(QDialog):
    def __init__(self):
        super(Edit, self).__init__()
        loadUi("edit.ui",self)
        self.pushbutton_accept.setVisible(addproduct_accept)
        self.lable_warningbuy.setVisible(False)
        self.lable_warningsell.setVisible(False)
        self.pushbutton_back.clicked.connect(self.back)
        self.pushbutton_accept.clicked.connect(self.accept)
        self.lineEdit_name.textChanged.connect(self.check)
        self.lineEdit_costbuy.textChanged.connect(self.check)
        self.lineEdit_costsell.textChanged.connect(self.check)
        self.lineEdit_name.setText(product_X[userid][which_one].name)
        self.lineEdit_code.setText(product_X[userid][which_one].productcode)
        self.lineEdit_costbuy.setText(str(product_X[userid][which_one].costbuy))
        self.lineEdit_costsell.setText(str(product_X[userid][which_one].costsell))
        self.lineEdit_daterecive.setText(str(product_X[userid][which_one].daterecive))
        self.lineEdit_dateexpire.setText(str(product_X[userid][which_one].dateexpire))
    
    def check(self):
        global addproduct_accept
        LEname = len(self.lineEdit_name.text())
        LEcostbuy = len(self.lineEdit_costbuy.text())
        LEcostsell = len(self.lineEdit_costsell.text())
        textcostbuy = self.lineEdit_costbuy.text()
        textcostsell = self.lineEdit_costsell.text()
        if LEname != 0 and LEcostbuy != 0 and LEcostsell != 0:
            addproduct_accept = True
            self.pushbutton_accept.setVisible(addproduct_accept)
        if LEname == 0 or LEcostbuy == 0 or LEcostsell == 0:
            addproduct_accept = False
            self.pushbutton_accept.setVisible(addproduct_accept)
        if not textcostbuy.isdigit() and LEcostbuy != 0:
            self.lable_warningbuy.setVisible(True)
            addproduct_accept = False
            self.pushbutton_accept.setVisible(addproduct_accept)
        if not textcostsell.isdigit() and LEcostsell != 0:
            self.lable_warningsell.setVisible(True)
            addproduct_accept = False
            self.pushbutton_accept.setVisible(addproduct_accept)
        if LEcostbuy == 0 or textcostbuy.isdigit():
            self.lable_warningbuy.setVisible(False)
        if LEcostsell == 0 or textcostsell.isdigit():
            self.lable_warningsell.setVisible(False)
    
    def back(self):
        login = Main()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)    
    
    def accept(self):
        global product_X
        product_X[userid][which_one].name = str(self.lineEdit_name.text())
        product_X[userid][which_one].productcode = str(self.lineEdit_code.text())
        product_X[userid][which_one].costbuy = int(self.lineEdit_costbuy.text())
        product_X[userid][which_one].costsell = int(self.lineEdit_costsell.text())
        product_X[userid][which_one].daterecive = str(self.lineEdit_daterecive.text())
        product_X[userid][which_one].dateexpire = str(self.lineEdit_dateexpire.text())
        login = Main()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
       
class Listt(QDialog):
    def __init__(self):
        super(Listt, self).__init__()
        loadUi("list.ui",self)
        self.pushbutton_back.clicked.connect(self.back)
        for i in range(len(product_X[userid][which_one].allproductid)):
            self.generate_groupbox(i)
            self.pushbutton_sell.clicked.connect(self.sell)
            self.pushbutton_remove.clicked.connect(self.remove)
    
    def generate_groupbox(self,i):
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setMinimumSize(QtCore.QSize(631, 80))
        self.groupBox.setMaximumSize(QtCore.QSize(631, 80))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lable_id = QtWidgets.QLabel(self.groupBox)
        self.lable_id.setGeometry(QtCore.QRect(0, 30, 491, 20))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(20)
        self.lable_id.setFont(font)
        self.lable_id.setObjectName("lable_id")
        self.pushbutton_sell = QtWidgets.QPushButton(self.groupBox)
        self.pushbutton_sell.setGeometry(QtCore.QRect(550, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushbutton_sell.setFont(font)
        self.pushbutton_sell.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-color: rgb(0, 0, 0);\n"
        "border-width : 0.5px;\n"
        "border-style:inset;")
        self.pushbutton_sell.setObjectName("pushbotton_sell" + str(i))
        self.pushbutton_sell.setText("Sell")
        self.pushbutton_sell.setVisible(bool(product_X[userid][which_one].listsell[i]))
        self.pushbutton_remove = QtWidgets.QPushButton(self.groupBox)
        self.pushbutton_remove.setGeometry(QtCore.QRect(550, 50, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushbutton_remove.setFont(font)
        self.pushbutton_remove.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-color: rgb(0, 0, 0);\n"
        "border-width : 0.5px;\n"
        "border-style:inset;")
        self.pushbutton_remove.setObjectName("pushbotton_remove" + str(i))
        self.pushbutton_remove.setText("Remove")
        self.verticalLayout.addWidget(self.groupBox)
        self.lable_id.setText(str(i+1)+')ID:' + str(product_X[userid][which_one].allproductid[i]))
    
    def sell(self):
        which_id = self.sender().objectName()
        which_id = int(which_id[15:])
        product_X[userid][which_one].quantitysold = product_X[userid][which_one].quantitysold + 1
        product_X[userid][which_one].listsell[which_id] = False
        login = Listt()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def remove(self):
        which_id = self.sender().objectName()
        which_id = int(which_id[17:])
        if product_X[userid][which_one].listsell[which_id] == True:
            del product_X[userid][which_one].allproductid[which_id]
            product_X[userid][which_one].quantity = product_X[userid][which_one].quantity - 1
            del product_X[userid][which_one].listsell[which_id]
        else:
            del product_X[userid][which_one].listsell[which_id]
            del product_X[userid][which_one].allproductid[which_id]
        login = Listt()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def back(self):
        login = Main()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
          
class TheProduct:
    def __init__(self, name, productcode, costbuy, costsell, quantity, daterecive, dateexpire, allproductid, list_sell, quantitysold = 0):
        self.name = str(name)
        self.productcode = str(productcode)
        self.costbuy = int(costbuy)
        self.costsell = int(costsell)
        self.quantity = int(quantity)
        self.daterecive = str(daterecive)
        self.dateexpire = str(dateexpire)
        self.allproductid = list(allproductid)
        self.quantitysold = int(quantitysold)
        self.listsell = list(list_sell)

def resettext():
    global namex,productcodex,costbuyx,costsellx,quantityx,daterecivex,dateexpirex,checkboxx
    namex = ''
    productcodex = ''
    costbuyx = ''
    costsellx = ''
    quantityx = ''
    daterecivex = ''
    dateexpirex = ''
    checkboxx = False
    
def save():
    savefile = open("save.txt", "w")
    for user in range(0,3):
        write = str(len(product_X[user])) + '\n'
        savefile.write(write)
    for product in range(0,3):
        for i in range(0,len(product_X[product])):
            write = product_X[product][i].name + ' ' + product_X[product][i].productcode + ' ' + str(product_X[product][i].costbuy) + ' ' + str(product_X[product][i].costsell) + ' ' + str(product_X[product][i].quantity) + ' ' + product_X[product][i].daterecive + ' ' + product_X[product][i].dateexpire + ' ' +  str(product_X[product][i].quantitysold) + '\n'
            savefile.write(write)
            for ii in range(0, len(product_X[product][i].allproductid)):
                if ii != product_X[product][i].quantity - 1:
                    write = str(product_X[product][i].allproductid[ii]) + ' '
                else:
                    write = str(product_X[product][i].allproductid[ii]) + '\n'
                savefile.write(write)
            for iii in range(0, len(product_X[product][i].listsell)):
                if iii != product_X[product][i].quantity - 1:
                    write = str(product_X[product][i].listsell[iii]) + ' '
                else:
                    write = str(product_X[product][i].listsell[iii]) + '\n'
                savefile.write(write)
    savefile.write(str(setuser1)+'\n')
    savefile.write(str(setuser2)+'\n')
    savefile.write(str(setuser3)+'\n')
    savefile.write(str(setadduser)+'\n')
    savefile.write(str(setremoveuser)+'\n')
    savefile.write(str(count_for_user))

def load():
    global product_X, setuser1, setuser2, setuser3, setadduser, setremoveuser, count_for_user
    try:
        loadfile = open("save.txt", "r")
        user1 = int(loadfile.readline())
        user2 = int(loadfile.readline())
        user3 = int(loadfile.readline())
        for i in range(user1):
            D1 = loadfile.readline().split()
            namex = str(D1[0])
            productcodex = str(D1[1])
            costbuyx = int(D1[2])
            costsellx = int(D1[3])
            quantityx = int(D1[4])
            daterecivex = str(D1[5])
            dateexpirex = str(D1[6])
            quantitysoldx = int(D1[7])
            allproductidx = loadfile.readline().split()
            list_sellx = loadfile.readline().split()
            x = TheProduct(namex, productcodex, costbuyx, costsellx, quantityx, daterecivex, dateexpirex, allproductidx, list_sellx, quantitysoldx)
            product_X[0].append(x)
        for j in range(user2):
            D1 = loadfile.readline().split()
            namex = str(D1[0])
            productcodex = str(D1[1])
            costbuyx = int(D1[2])
            costsellx = int(D1[3])
            quantityx = int(D1[4])
            daterecivex = str(D1[5])
            dateexpirex = str(D1[6])
            quantitysoldx = int(D1[7])
            allproductidx = loadfile.readline().split()
            list_sellx = loadfile.readline().split()
            x = TheProduct(namex, productcodex, costbuyx, costsellx, quantityx, daterecivex, dateexpirex, allproductidx, list_sellx, quantitysoldx)
            product_X[1].append(x)
        for k in range(user3):
            D1 = loadfile.readline().split()
            namex = str(D1[0])
            productcodex = str(D1[1])
            costbuyx = int(D1[2])
            costsellx = int(D1[3])
            quantityx = int(D1[4])
            daterecivex = str(D1[5])
            dateexpirex = str(D1[6])
            quantitysoldx = int(D1[7])
            allproductidx = loadfile.readline().split()
            list_sellx = loadfile.readline().split()
            x = TheProduct(namex, productcodex, costbuyx, costsellx, quantityx, daterecivex, dateexpirex, allproductidx, list_sellx, quantitysoldx)
            product_X[2].append(x)    
        if loadfile.readline()[:4] == 'True':
            setuser1 = True
        else:
            setuser1 = False
        if loadfile.readline()[:4] == 'True':
            setuser2 = True
        else:
            setuser2 = False
        if loadfile.readline()[:4] == 'True':
            setuser3 = True
        else:
            setuser3 = False
        if loadfile.readline()[:4] == 'True':
            setadduser = True
        else:
            setadduser = False    
        if loadfile.readline()[:4] == 'True':
            setremoveuser = True
        else:
            setremoveuser = False
        count_for_user = int(loadfile.readline())
    except:
        pass

load()
app = QApplication(sys.argv)
first = User()
widget = QtWidgets.QStackedWidget()
widget.addWidget(first)
widget.setFixedHeight(422)
widget.setFixedWidth(671)
widget.show()
sys.exit(app.exec_())