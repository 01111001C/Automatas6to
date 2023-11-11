def clasificarNumero(self,tk,numero,row,col):    
    estado=AutomataReales(self,numero)
    self.down_text.config(state="normal")  
    self.right_text.config(state="normal")  
    datT=""
    #estados de aceptación
    if int(estado)<0:
        estado=str(int(estado)*-1)
    if estado=="1":
        datT= "INT"
        self.right_text.insert(tk.END, str(numero),"black_tag")    
        self.right_text.insert(tk.END, "["+str(datT)+"]","blue_tag")    
    elif estado=="2":
        datT= "INT"
        self.right_text.insert(tk.END, str(numero),"black_tag")    
        self.right_text.insert(tk.END, "["+str(datT)+"]","blue_tag")    
    elif estado=="3":
        self.down_text.insert(tk.END, "[line:"+str(row)+" col: "+str(col)+"][ Valor: "+numero+"]"+" ERROR\n")
        datT=  "DEC"
        self.right_text.insert(tk.END, str(numero)+"["+str(datT)+"]","red_tag")    
    elif estado=="4":
        datT=  "DEC"
        self.right_text.insert(tk.END, str(numero),"black_tag")    
        self.right_text.insert(tk.END, "["+str(datT)+"]","blue_tag")    
    elif estado=="5":
        self.down_text.insert(tk.END, "[line:"+str(row)+" col: "+str(col)+"][ Valor: "+numero+"]"+"Estado: "+" ERROR\n")
        datT=  "Real."
        self.right_text.insert(tk.END, str(numero)+"["+str(datT)+"]","red_tag")    
    elif estado=="6":
        self.down_text.insert(tk.END, "[line:"+str(row)+" col: "+str(col)+"][ Valor: "+numero+"]"+"Estado: "+" ERROR\n")
        datT=  "Real"
        self.right_text.insert(tk.END, str(numero)+"["+str(datT)+"]","red_tag")    
    elif estado=="7":
        datT=  "Real"
        self.right_text.insert(tk.END, str(numero),"black_tag")    
        self.right_text.insert(tk.END, "["+str(datT)+"]","blue_tag")    
    #errores
    self.down_text.config(state="disabled")
def AutomataReales(self,numero):
    estado="1"  
    for char in numero:
        if estado =="1":
            if char >="0" and char <="9":
                estado="2"
            elif char=="+" or char=="-":
                estado="2"
            else:
                return "-1"
        elif estado =="2":
            if char>="0" and char<="9":
                estado="2"
            elif char==".":
                estado="3"
            elif char=="E":
                estado="5"
            else:
                return "-2"
        elif estado == "3":
            if char>="0" and char<="9":
                estado="4"
            else:
                return "-3"
        elif estado=="4":
            if char>="0" and char<="9":
                estado="4"
            elif char=="E":
                estado="5"
            else:
                return "-4"
        elif estado=="5":              
            if char=="+" or char == "-":
                estado="6"
            elif char>="0" and char<="9":
                estado="7"
            else: return "-5"
        elif estado=="6":
            if char>="0" and char<="9":
                estado="7"
            else: return "-6"
        elif estado=="7":
            if char>="0" and char <="9":
                estado="7"
            else: return "-7"
    return estado

def validarID(self,tk,ID,row,col,funct):
    estado = AutomataIdentificadores(ID)
    if estado==2:
        self.down_text.insert(tk.END, "[line:"+str(row)+" col: "+str(col)+"][ Valor: "+ID+"]\n")
        return "ERR."
    elif estado==3 and funct!=True:
        return "ID"
    elif estado==3 and funct==True:
        return "Funct"

def AutomataIdentificadores(ID):
    estado =1
    for caracter in ID:
        if estado==1:
            if esNumero(caracter)==True: 
                estado=2 
                return estado
            elif esLetra(caracter)==True: 
                estado=3
        elif estado==3:
            if esLetra(caracter)==True or esNumero(caracter)==True: 
                estado=3
            else: 
                return "N/A"
    return estado

def esLetra(caracter):
    if caracter=="a": return True
    elif caracter=="b": return True
    elif caracter=="c": return True
    elif caracter=="d": return True
    elif caracter=="e": return True
    elif caracter=="f": return True
    elif caracter=="g": return True
    elif caracter=="h": return True
    elif caracter=="i": return True
    elif caracter=="j": return True
    elif caracter=="k": return True
    elif caracter=="l": return True
    elif caracter=="m": return True
    elif caracter=="n": return True
    elif caracter=="o": return True
    elif caracter=="p": return True
    elif caracter=="q": return True
    elif caracter=="r": return True
    elif caracter=="s": return True
    elif caracter=="t": return True
    elif caracter=="v": return True
    elif caracter=="w": return True
    elif caracter=="x": return True
    elif caracter=="y": return True
    elif caracter=="z": return True
    elif caracter=="(": return True
    elif caracter==")": return True
    elif caracter=="_": return True   
    else: return True

def ValidarHex(Num,self,tk,contLine,contChar):
    estado=AutomataHex(Num)
    if int(estado)<0:
        estado=int(estado)*-1
    if estado==4:
        self.right_text.insert(tk.END, "[HEX]","blue_tag")
    elif estado==5:
        self.right_text.insert(tk.END, "[INT]","blue_tag")
    elif estado==7:
        self.right_text.insert(tk.END, "[DEC]","blue_tag")
    elif estado==8:
        self.right_text.insert(tk.END, "[OCT]","blue_tag")
    
    elif estado==0:
        self.right_text.insert(tk.END, "[INT]","red_tag")
        self.down_text.insert(tk.END, str(contLine)+": "+str(contChar)+" Error: "+Num+"\n","red_tag")
    elif estado==1:
        self.right_text.insert(tk.END, "[INT]","red_tag")
        self.down_text.insert(tk.END, str(contLine)+": "+str(contChar)+" Error: "+Num+"\n","red_tag")
    elif estado==2:
        self.right_text.insert(tk.END, "[HEX]","red_tag")
        self.down_text.insert(tk.END, str(contLine)+": "+str(contChar)+" Error: "+Num+"\n","red_tag")
    elif estado==3:
        self.right_text.insert(tk.END, "[HEX]","red_tag")
        self.down_text.insert(tk.END, str(contLine)+": "+str(contChar)+" Error: "+Num+"\n","red_tag")
    elif estado==6:
        self.right_text.insert(tk.END, "[DEC]","red_tag")
        self.down_text.insert(tk.END, str(contLine)+": "+str(contChar)+" Error: "+Num+"\n","red_tag")
    elif estado==9:
        self.right_text.insert(tk.END, "[INV]","red_tag")
        self.down_text.insert(tk.END, str(contLine)+": "+str(contChar)+" Error: "+Num+"\n","red_tag")
    else:
        self.right_text.insert(tk.END, "[","Inv.","]","red_tag")
        self.down_text.insert(tk.END, str(contLine)+": "+str(contChar)+" Error: "+Num+"\n","red_tag")

def AutomataHex(Token):
    estado = 0
    for caracter in Token:
        if estado == 0:
            if caracter=='0':
                estado=1
            elif esMayor_0(caracter)==True:
                estado=5
            elif caracter=='.':
                estado=6
            else:
                return "-9"
        elif estado==1:
            if esOctal(caracter)==True:
                estado=8
            elif caracter=='x' or caracter=='X':
                estado=2
            elif estado=='.':
                estado=6
            else:
                return "-1"
        elif estado==2:
            if ValidarAF(caracter)==True or esNumero(caracter)==True:
                estado=3
            else:
                return "-2"
        elif estado==3:
            if ValidarAF(caracter)==True or esNumero(caracter)==True:
                estado=4
            else:
                return "-3"
        elif estado==4:
            if ValidarAF(caracter)==True or esNumero(caracter)==True:
                estado=3
            else:
                return "-4"
        elif estado==5:
            if esNumero(caracter)==True:
                estado=5
            elif caracter=='.':
                estado=6
            else:
                return "-5"
        elif estado==6:
            if esNumero(caracter)==True:
                estado=7
            else:
                return "-6"
        elif estado==7:
            if esNumero(caracter)==True:
                estado=7
            else:
                return "-7" 
        elif estado==8:
            if esOctal(caracter)==True:
                estado=8
            else:
                return "-8"
    return estado

def ValidarAF(num):
    #mins
    if num=='a':
        return True
    elif num=='b':
        return True
    elif num=='c':
        return True
    elif num=='d':
        return True
    elif num=='e':
        return True
    elif num=='f':
        return True
    #mayus
    if num=='A':
        return True
    elif num=='B':
        return True
    elif num=='C':
        return True
    elif num=='D':
        return True
    elif num=='E':
        return True
    elif num=='F':
        return True
    else:
        return False

def esNumero(caracter):
    if caracter=='0': return True
    elif caracter=='1': return True
    elif caracter=='2': return True
    elif caracter=='3': return True
    elif caracter=='4': return True
    elif caracter=='5': return True
    elif caracter=='6': return True
    elif caracter=='7': return True
    elif caracter=='8': return True
    elif caracter=='9': return True
    else: return False

def esMayor_0(caracter):
    if caracter=='1': return True
    elif caracter=='2': return True
    elif caracter=='3': return True
    elif caracter=='4': return True
    elif caracter=='5': return True
    elif caracter=='6': return True
    elif caracter=='7': return True
    elif caracter=='8': return True
    elif caracter=='9': return True
    else: return False

def esOctal(caracter):
    if caracter=='0': return True
    elif caracter=='1': return True
    elif caracter=='2': return True
    elif caracter=='3': return True
    elif caracter=='4': return True
    elif caracter=='5': return True
    elif caracter=='6': return True
    elif caracter=='7': return True
    else: return False


