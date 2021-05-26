from tkinter import*

class Inicio(Toplevel):
  cor_fonte_botao = '#212529'
  cor_cinza_escuro ='#343A40'
  cor_cinza = '#495057'
  cor_cinza_claro = '#6cC757D'
  cor_cinza_bemclaro = '#ADB5BD'
  cor_fundo_tela ='#CED4DA'

  def __init__(self, original): 
    self.frame_original = original 

    Toplevel.frame__init__(self) #Importando Método Construtor 
    self.geometry('375x667+900+10')
    self.title('SEJA BEM VINDO(A) AO COINS!')
    self.configure(bg='#123456')

    self.btn = Button(
        self,
        text = 'ENTRAR',
        command=self.onClose)
   self.btn.pack(side = BOTTOM, fill=X)


  def onClose(self):
        self.destroy()
        self.frame_original.show() 

class App:
  #Cores
  cor_fonte_botao = '#212529'
  cor_cinza_escuro ='#343A40'
  cor_cinza = '#495057'
  cor_cinza_claro = '#6cC757D'
  cor_cinza_bemclaro = '#ADB5BD'
  cor_fundo_tela ='#CED4DA'

  def __init__(self): #Método construtor
        self.root = root 
        self.tela()
        self.frames()
        self.widgets_frame1()
        self.widgets_frame2()
        root.mainloop()

    def tela(self):
        self.root.title('COINS') #Título
        self.root.geometry('375x667+900+10') #Geometria
        self.root.configure(bg = self.cor_fundo_tela)


    def frames(self):
        self.frame1 = Frame(self.root, bg=self.cor_cinza)
        self.frame1.place(
            relx=0, 
            rely=0, 
            relwidth=1.00,
            relheight=1.00)
        
        self.frame2 = Frame(self.root, bg=self.cor_cinza_escuro)
        self.frame2.place(file='coins.png')
            relx=0,
            rely=0.90,
            relwidth=1.00,
            relheight=0.10) 
    
    def widgets_frame1(self):
        self.modelo = PhotoImage(
        self.img1 = Label(self.frame1, image=self.modelo, bd=0)
        self.img1.place(relx=0, rely=0, relwidth=1, relheight=1)
      
   def widgets_frame2(self):
        self.btn_entrar = Button(
            self.frame2, # Onde está localizado
            text='Entrar', # Texto do botão
            bg=self.cor_cinza, # Cor de fundo (background)
            activebackground=self.cor_cinza, # Cor clicado
            font=('helvetica', 20), # Fonte
            fg=self.cor_fonte_botao, # Cor da fonte
            activeforeground=self.cor_fonte_botao, # Cor fonte clicado
            command=self.clica_entrar
     
         self.btn_entrar.place(
            relx=0,
            rely=0,
            relwidth=0.50,
            relheight=1.00) 

         self.btn_login = Button(
            self.frame2,
            text='LOGIN',
            bg=self.cor_cinza,
            activebackground=self.cor_cinza,
            fg=self.cor_fonte_botao,
            activeforeground=self.cor_fonte_botao,
            font=('helvetica', 20),
            command=self.clica_entrar)
            
        self.btn_login.place(
            relx=0.50, 
            rely=0, 
            relwidth=0.50, 
            relheight=1.00)
            
  # Entrar em outra janela
    # Precisamos CLICA_ENTRAR (comando btn), HIDE, SHOW
    def clica_entrar(self): # Comando btn
        self.hide()
        self.subFrame = Anuncios(self)
    def clica_entrar(self):
        self.hide()
        self.subFrame = Entrar(self)
    def hide(self): # Esconde a root
        self.root.withdraw()
    def show(self): # Mostra o root novamente
        self.root.update()
        self.root.deiconify()






### PROGRAMA PRINCIPAL ### 
root = Tk()
App() 

