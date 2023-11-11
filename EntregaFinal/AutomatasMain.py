import tkinter as tk
from tkinter import filedialog, messagebox

import Automata
import Ventanas
import Diccionarios

class CursoAutomatas:
    def __init__(self, root):
        self.root = root
        self.ClassType="None"
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        Ventanas.create_Frames(self,tk)
        Ventanas.create_navigation_menu(self,tk)
        Ventanas.create_initial_text_widgets(self,tk)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)    

    def tokenizar(self):
        self.ClassType="tokenizar"
        self.Tokens()

    def clasificacion(self):
        self.ClassType="clasificar"
        contLine=0 #contador de lineas
        contChar=0 # contador de caracteres / columnas
        bandera="inicio"#bandera de posiciones
        isnnum=False#bandera numerica
        signo="Pos"
        numInit=0 #posicion en que inicia el numero
        token = ""#variable para validar
        comentario=False
        openParentesis=0
        closeParentesis=0
        isFunct=False

        self.right_text.config(state="normal")#desbloqueo de texto derecho
        left_text = self.left_text.get("1.0", tk.END)#Obtencion del texto a validar
        self.right_text.delete("1.0", tk.END)        #Limpiar texto Derecho
        
        if not left_text.strip():
            self.show_error_message("No se ha ingresado ningún número.")
            return
        for caracter in left_text:
            #caso de caracter especial
            if(caracter=="\n" or caracter=="\t" or caracter==" "):
                if caracter=="\n": 
                    contLine+=1
                    if comentario==True: comentario=False
                #en la primera posicion
                if bandera=="comentario" and caracter!="\n":
                    self.right_text.insert(tk.END, token,"green_tag")
                elif bandera=="inicio":
                    if caracter>="0" and caracter<="9" or caracter=="-" or caracter=="+" or caracter==".":
                        signo="Pos"
                        if caracter=="-":
                            signo="Neg."                         
                        isnnum=True
                        numInit=contChar
                    elif caracter=="'": comentario=True
                    token=caracter
                    
                    #impresion de caracteres especiales directos
                    self.right_text.insert(tk.END, token,"red_tag")
                #Caso de segunda posicion
                elif bandera=="primerBandera":
                    if caracter>="0" and caracter<="9" or caracter=="-" or caracter=="+" or caracter==".":
                        signo="Pos"
                        if caracter=="-":
                            signo="Neg."
                        isnnum=True
                        numInit=contChar
                    token=caracter
                    
                    self.right_text.insert(tk.END, token,"red_tag")
                #caso de secuencia [token]
                elif bandera=="secuencia" and isnnum==False:
                        self.right_text.insert(tk.END, token,"black_tag")
                        token=token.lower()
                        if token in Diccionarios.asignacion:
                            self.right_text.insert(tk.END, "[Asg] ","blue_tag")
                        elif token in Diccionarios.OperadoresDeComparación:
                            self.right_text.insert(tk.END, "[OpC] ","blue_tag")
                        elif token in Diccionarios.operadoresMatematicos:
                            self.right_text.insert(tk.END, "[OpM] ","blue_tag")
                        elif token in Diccionarios.OperadoresLogicos:
                            self.right_text.insert(tk.END, "[OpL] ","blue_tag")
                        elif token in Diccionarios.PalabrasReservadas:
                            self.right_text.insert(tk.END, "[PR] ","blue_tag")
                        else: #identificadores
                            if isFunct==False:
                                ID=Automata.validarID(self,tk,token,contLine,contChar,False)
                                self.right_text.insert(tk.END, "["+str(ID)+"]","purple_tag")
                        token=caracter
                        self.right_text.insert(tk.END, token,"black_tag")
                #Caso numerico
                elif bandera=="secuencia" and isnnum==True:
                    Automata.clasificarNumero(self,tk,token,contLine,numInit)
                    isnnum=False
                    numInit=contChar
                    token=caracter
                    self.right_text.insert(tk.END, token,"red_tag")   
                    #caso funcion
                elif bandera=="function":
                    token=caracter
                    self.right_text.insert(tk.END, token,"red_tag")   
                token=""
                bandera="primerBandera"  
                if caracter=="\n":
                    contChar=0
                else:contChar=contChar+1
            elif caracter=="'" and bandera=="inicio":
                bandera="comentario"
                contChar=contChar+1
            else:   
                contChar=contChar+1
                if bandera=="inicio":
                    if caracter>="0" and caracter<="9" or caracter=="-" or caracter=="+" or caracter==".":
                        signo="Pos"
                        if caracter=="-":
                            signo="Neg."
                        isnnum=True
                        numInit=contChar
                    elif caracter=="'": bandera="comentario"
                elif bandera=="primerBandera":
                    if caracter>="0" and caracter<="9" or caracter=="-" or caracter=="+" or caracter==".":
                        signo="Pos"
                        if caracter=="-":
                            signo="Neg."
                        isnnum=True
                        numInit=contChar
                    elif caracter=="'": bandera="comentario"
                token=token+caracter
                bandera="secuencia"
                
                if caracter=="(" and self.ClassType=="clasificar":
                    openParentesis+=1
                    self.right_text.insert(tk.END,token,"black_tag")
                    self.right_text.insert(tk.END,"["+str(Automata.validarID(self,tk,token,contLine,contChar,True))+":Name]","red_tag")
                    token=""
                    isFunct=True
                    bandera="function"
                elif caracter==")" and self.ClassType=="clasificar":
                    closeParentesis+=1
                    self.right_text.insert(tk.END,token,"black_tag")
                    self.right_text.insert(tk.END,"["+str(Automata.validarID(self,tk,token,contLine,contChar,True))+":Param.]","red_tag")
                    token=""
                    isFunct=False
                    bandera="function"
                
                
        self.right_text.config(state="disabled")      

    def AutomataHexas(self):
        contLine=0 #contador de lineas
        contChar=0 # contador de caracteres / columnas
        token = ""#variable para validar
        
        self.right_text.config(state="normal")#desbloqueo de texto derecho
        self.down_text.config(state="normal")#desbloqueo de texto derecho
        left_text = self.left_text.get("1.0", tk.END)#Obtencion del texto a validar
        self.right_text.delete("1.0", tk.END)        #Limpiar texto Derecho
        
        if not left_text.strip():
            self.show_error_message("No se ha ingresado ningún número.")
            return
        for caracter in left_text:
            #caso de caracter especial
            if(caracter=="\n" or caracter=="\t" or caracter==" "):
                if caracter=="\n" and token=="": 
                    contLine+=1
                    contChar=0
                    self.right_text.insert(tk.END, caracter,"red_tag")
                    token=""
                elif caracter=="\t":
                    self.right_text.insert(tk.END, caracter,"red_tag")
                    token=""
                #caso de secuencia [token]
                elif (caracter==" " or caracter=="\n") and token!="":
                    if caracter=="\n":
                        contLine+=1
                        contChar=0
                    self.right_text.insert(tk.END, token,"black_tag")
                    Automata.ValidarHex(token,self,tk,contLine,contChar)
                    self.right_text.insert(tk.END, caracter,"red_tag")
                token=""    
            else:   
                contChar=contChar+1
                token=token+caracter
        self.right_text.config(state="disabled")
        self.down_text.config(state="disabled")

    def Tokens(self):
        contLine=0 #contador de lineas
        contChar=0 # contador de caracteres / columnas
        bandera="inicio"#bandera de posiciones
        isnnum=False#bandera numerica
        signo="Pos"
        numInit=0 #posicion en que inicia el numero
        token = ""#variable para validar
        comentario=False
        openParentesis=0
        closeParentesis=0
        isFunct=False

        self.right_text.config(state="normal")#desbloqueo de texto derecho
        left_text = self.left_text.get("1.0", tk.END)#Obtencion del texto a validar
        self.right_text.delete("1.0", tk.END)        #Limpiar texto Derecho
        
        if not left_text.strip():
            self.show_error_message("No se ha ingresado ningún número.")
            return
        for caracter in left_text:
            #caso de caracter especial
            if(caracter=="\n" or caracter=="\t" or caracter==" "):
                if caracter=="\n": 
                    contLine+=1
                    if comentario==True: comentario=False
                #en la primera posicion
                if bandera=="comentario" and caracter!="\n":
                    self.right_text.insert(tk.END, token,"green_tag")
                elif bandera=="inicio":
                    if caracter>="0" and caracter<="9" or caracter=="-" or caracter=="+" or caracter==".":
                        signo="Pos"
                        if caracter=="-":
                            signo="Neg."                         
                        isnnum=True
                        numInit=contChar
                    elif caracter=="'": comentario=True
                    token=caracter
                    
                    #impresion de caracteres especiales directos
                    self.right_text.insert(tk.END, token,"red_tag")
                #Caso de segunda posicion
                elif bandera=="primerBandera":
                    if caracter>="0" and caracter<="9" or caracter=="-" or caracter=="+" or caracter==".":
                        signo="Pos"
                        if caracter=="-":
                            signo="Neg."
                        isnnum=True
                        numInit=contChar
                    token=caracter
                    
                    self.right_text.insert(tk.END, token,"red_tag")
                #caso de secuencia [token]
                elif bandera=="secuencia" and isnnum==False:
                    if self.ClassType=="clasificar":
                        self.right_text.insert(tk.END, token,"black_tag")
                        token=token.lower()
                        if token in Diccionarios.asignacion:
                            self.right_text.insert(tk.END, "[Asg] ","blue_tag")
                        elif token in Diccionarios.OperadoresDeComparación:
                            self.right_text.insert(tk.END, "[OpC] ","blue_tag")
                        elif token in Diccionarios.operadoresMatematicos:
                            self.right_text.insert(tk.END, "[OpM] ","blue_tag")
                        elif token in Diccionarios.OperadoresLogicos:
                            self.right_text.insert(tk.END, "[OpL] ","blue_tag")
                        elif token in Diccionarios.PalabrasReservadas:
                            self.right_text.insert(tk.END, "[PR] ","blue_tag")
                        else: #identificadores
                            if isFunct==False:
                                ID=Automata.validarID(self,tk,token,contLine,contChar,False)
                                self.right_text.insert(tk.END, "["+str(ID)+"]","purple_tag")
                        token=caracter
                        self.right_text.insert(tk.END, token,"black_tag")
                    elif self.ClassType=="tokenizar":
                        self.right_text.insert(tk.END, token,"black_tag")
                        self.right_text.insert(tk.END, ",","red_tag")
                        token=caracter
                        self.right_text.insert(tk.END, token,"black_tag")
                #Caso numerico
                elif bandera=="secuencia" and isnnum==True:
                    if self.ClassType=="clasificar":
                        AutoReal=Automata.clasificarNumero(self,tk,token,contLine,numInit)
                        if AutoReal=="ERR.":
                            self.right_text.insert(tk.END, token,"red_tag")    
                            self.right_text.insert(tk.END,"["+AutoReal+"]","red_tag")
                        else:
                            self.right_text.insert(tk.END, token,"balck_tag")    
                            if signo=="Pos":#positivos
                                self.right_text.insert(tk.END,"["+AutoReal+"]","blue_tag")
                            elif signo=="Neg.":#negativos
                                self.right_text.insert(tk.END,"["+AutoReal+"]","brown_tag")
                    elif self.ClassType=="tokenizar":
                        self.right_text.insert(tk.END, token,"black_tag")
                        self.right_text.insert(tk.END, ",","red_tag")
                    isnnum=False
                    numInit=contChar
                    token=caracter
                    self.right_text.insert(tk.END, token,"red_tag")   
                    #caso funcion
                elif bandera=="function":
                    token=caracter
                    self.right_text.insert(tk.END, token,"red_tag")   
                token=""
                bandera="primerBandera"  
                if caracter=="\n":
                    contChar=0
                else:contChar=contChar+1
            elif caracter=="'" and bandera=="inicio":
                bandera="comentario"
                contChar=contChar+1
            else:   
                contChar=contChar+1
                if bandera=="inicio":
                    if caracter>="0" and caracter<="9" or caracter=="-" or caracter=="+" or caracter==".":
                        signo="Pos"
                        if caracter=="-":
                            signo="Neg."
                        isnnum=True
                        numInit=contChar
                    elif caracter=="'": bandera="comentario"
                elif bandera=="primerBandera":
                    if caracter>="0" and caracter<="9" or caracter=="-" or caracter=="+" or caracter==".":
                        signo="Pos"
                        if caracter=="-":
                            signo="Neg."
                        isnnum=True
                        numInit=contChar
                    elif caracter=="'": bandera="comentario"
                token=token+caracter
                bandera="secuencia"
                
                if caracter=="(" and self.ClassType=="clasificar":
                    openParentesis+=1
                    self.right_text.insert(tk.END,token,"black_tag")
                    self.right_text.insert(tk.END,"["+str(Automata.validarID(self,tk,token,contLine,contChar,True))+":Name]","red_tag")
                    token=""
                    isFunct=True
                    bandera="function"
                elif caracter==")" and self.ClassType=="clasificar":
                    closeParentesis+=1
                    self.right_text.insert(tk.END,token,"black_tag")
                    self.right_text.insert(tk.END,"["+str(Automata.validarID(self,tk,token,contLine,contChar,True))+":Param.]","red_tag")
                    token=""
                    isFunct=False
                    bandera="function"
                
                
        self.right_text.config(state="disabled")      
    def AutomataNumerosReales():
        return 0
    
    def open_document_left(self):
        if self.left_text_changed:
            result = self.ask_for_save()
            if result == "cancel":
                return
            elif result == "save":
                self.save_panel_izquierdo()
        
        file_path = filedialog.askopenfilename(filetypes=[("Archivos Visual Basic", "*.vb")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.left_text.delete("1.0", tk.END)
                self.left_text.insert(tk.END, content)
                self.current_file_path = file_path
                self.left_text_changed = False

    def save_panel_izquierdo(self):
        content = self.left_text.get("1.0", tk.END)
        if self.current_file_path:
            with open(self.current_file_path, "w") as file:
                file.write(content)
            self.left_text_changed = False
            messagebox.showinfo("Guardado", "Archivo del panel izquierdo guardado exitosamente.")
        else:
            self.save_document_as()

    def save_document_right(self):
        if self.current_file_path:
            content = self.right_text.get("1.0", tk.END)
            with open(self.current_file_path, "w") as file:
                file.write(content)
            messagebox.showinfo("Guardado", "Archivo del panel derecho guardado exitosamente.")
        else:
            self.save_document_as()

    def save_document_as(self):
        content = self.right_text.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".vb", filetypes=[("Archivos Visual Basic", "*.vb")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)
            self.current_file_path = file_path
            messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")

    def ask_for_save(self):
        result = messagebox.askyesnocancel("Guardar Cambios", "¿Desea guardar los cambios?")
        if result:
            return "save"
        elif result is None:
            return "cancel"
        return "discard"

    def mark_left_text_as_changed(self, event=None):
        self.left_text_changed = True

    def mark_left_text_as_not_changed(self, event=None):
        self.left_text_changed = True

    def show_error_message(self, message):
        messagebox.showerror("Error", message)

    def close_windows(self):
        if self.left_text_changed:
            result = self.ask_for_save()
            if result == "cancel":
                return
            elif result == "save":
                self.save_panel_izquierdo()
        self.root.destroy()

    def on_closing(self):
        if self.left_text_changed:
            result = self.ask_for_save()
            if result == "cancel":
                return
            elif result == "save":
                self.save_panel_izquierdo()
        self.root.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CursoAutomatas(root)
    app.run()