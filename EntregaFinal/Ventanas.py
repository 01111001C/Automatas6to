def create_Frames(self,tk):
        self.root.title("Automas y Lenguajes Formales")
        self.left_frame = tk.Frame(self.root, width=600, height=800, bg="white")
        self.right_frame = tk.Frame(self.root, width=600, height=800, bg="white")
        self.down_frame = tk.Frame(self.root, width=1200, height=50, bg="black")

        self.left_frame.grid(row=0 , column=0, sticky="nsew")
        self.right_frame.grid(row=0 , column=1, sticky="nsew")
        self.down_frame.grid(row= 1, column=0, columnspan=2, sticky="nsew")

        self.left_frame.columnconfigure(0,weight=1)
        self.right_frame.columnconfigure(0,weight=1)
        self.down_frame.columnconfigure(0,weight=1)

        self.left_frame.rowconfigure(0,weight=1)
        self.right_frame.rowconfigure(0,weight=1)
        self.down_frame.rowconfigure(0,weight=1)


        self.left_text_changed = False
        self.current_file_path = ""

def create_navigation_menu(self,tk):
        navigation_menu = tk.Menu(self.root)
        self.root.config(menu=navigation_menu)
        
        file_menu = tk.Menu(navigation_menu, tearoff=0)
        Token_menu = tk.Menu(navigation_menu, tearoff=0)
        Automatas_menu =tk.Menu(navigation_menu, tearoff=0)
        
        navigation_menu.add_cascade(label="Archivo", menu=file_menu)
        navigation_menu.add_cascade(label="Tokens", menu=Token_menu)
        navigation_menu.add_cascade(label="Automatas", menu=Automatas_menu)

        Token_menu.add_command(label="Tokenizar", command=self.tokenizar)
        Token_menu.add_command(label="Clasificar", command=self.clasificacion)

        file_menu.add_separator() 
        file_menu.add_command(label="Abrir Documento (Vista Izquierda)", command=self.open_document_left)
        file_menu.add_command(label="Guardar Panel Izquierdo", command=self.save_panel_izquierdo)
        file_menu.add_command(label="Guardar como... (vista derecha)", command=self.save_document_as)
        file_menu.add_separator()
        
        file_menu.add_command(label="Cerrar", command=self.close_windows)

        Automatas_menu.add_command(label="Hexadecimales", command=self.AutomataHexas)

def create_initial_text_widgets(self,tk):   
        tg_PlR = "blue_tag"
        self.left_text = tk.Text(self.left_frame, wrap=tk.NONE, bg="white", fg="black",)
        self.right_text = tk.Text(self.right_frame, wrap=tk.NONE, bg="white", fg="black")
        self.down_text = tk.Text(self.down_frame, wrap=tk.NONE, bg="black", fg="red")

        self.left_text.grid(row=0, column=0, columnspan=1, sticky="nsew")
        self.right_text.grid(row=0, column=1, columnspan=1, sticky="nsew")
        self.down_text.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.left_text.columnconfigure(0,weight=1)
        self.right_text.columnconfigure(0,weight=1)
        self.down_text.columnconfigure(0,weight=1)

        self.left_text.rowconfigure(0,weight=1)
        self.right_text.rowconfigure(0,weight=1)
        self.down_text.rowconfigure(0,weight=0)

        self.left_text.config(width=100)
        self.right_text.config(width=100)
        self.down_text.config(height=10, insertbackground="red")

        self.left_text.insert(tk.END, "(Abre un archivo en [archivo/abrir documento(vista izquierda) o escribe aquí el texto)")

        self.left_text.bind("<Key>", self.mark_left_text_as_changed)

        self.right_text.config(state="normal")
        self.right_text.insert(tk.END, "Aquí verás el resultado despues de ejecutar las funciones")
        self.right_text.config(state="disabled")

        self.down_text.config(state="normal")
        self.down_text.insert(tk.END, "Errores Detectados:\n")
        self.down_text.config(state="disabled")

        self.down_text.tag_configure(tg_PlR, foreground="blue")
        self.down_text.tag_configure("black_tag", foreground="black")
        self.right_text.tag_configure("blue_tag", foreground="blue")
        self.right_text.tag_configure("black_tag", foreground="black")
        self.right_text.tag_configure("red_tag", foreground="red")
        self.right_text.tag_configure("brown_tag", foreground="Brown")
        self.right_text.tag_configure("purple_tag", foreground="Purple")
        self.right_text.tag_configure("green_tag", foreground="green")