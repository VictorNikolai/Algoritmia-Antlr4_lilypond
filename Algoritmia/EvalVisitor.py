from antlr4 import *
from AlgoritmiaLexer import AlgoritmiaLexer
from AlgoritmiaParser import AlgoritmiaParser
from antlr4.tree.Trees import Trees

class EvalVisitor(ParseTreeVisitor):

    def __init__(self):
        self.memory = {}

    def visitTerminal(self, node):
        return node.getText()

    def visitBloque_principal(self, ctx):
        return self.visit(ctx.bloque())
        
    def visitDeclaracion_procedimientos(self, ctx): 
        for declaracion in ctx.llamada_procedimiento():    
            self.visit(declaracion)

    #def visitDeclaracion_procedimiento(self, ctx):
        #print("si detecta declaracion procedimiento")
        #nombre = ctx.ID().getText()
        #parametros = []
        #if ctx.parametro():
            #for param in ctx.parametro():
                #parametros.append(param.getText())
        
        #self.memory[nombre] = {"params": parametros, "body": self.visit(ctx.bloque())}
        #print("bloque",self.visit(ctx.bloque())) ##borrar
        
        

    def visitParametro(self, ctx):
        return ctx.ID().getText() 

    def visitBloque(self, ctx):
        instrucciones = []
        for instr in ctx.bloque_instrucciones().instruccion(): 
            instrucciones.append(self.visit(instr))           
        return instrucciones

    def visitAsignacion(self, ctx): 
        id = ctx.ID().getText()  
        exp = self.visit(ctx.expresion())
        self.memory[id] = exp
                         
        
    
    def visitLectura(self, ctx):   
        id = ctx.ID().getText()   
        self.memory[id] = int(input()) #Debe ser valor entero    
        
        
        
    
    def visitEscritura(self, ctx):
        value = self.visit(ctx.getChild(1))
        
     
        if value in self.memory:
            print(self.memory[value])  
        else:
            print(value)
        
            

    def visitReproduccion(self, ctx):
        value = self.visit(ctx.expresion())
        print(value)

    def visitLlamada_procedimiento(self, ctx):
        
        #Declaracion procedimiento
        if ctx.ID() and ctx.parametro() and ctx.bloque(): ##Agregado
            #print("llamada declaracion procedimiento")
            nombre = ctx.ID().getText()
            parametros = []  ##borrar
            if ctx.parametro(): ##borrar
                for param in ctx.parametro(): ##borrar
                    parametros.append(param.getText())  ##borrar
                    #print("parametros",parametros)
            self.memory[nombre] = {"params": parametros, "body": self.visit(ctx.bloque())}  ##borrar
            #print(self.memory) ##agregado
            
        
        #Llamada procedimiento
        if ctx.ID() and ctx.expresion():
            #print("llamada a Llamada_Procedimiento")
            nombre = ctx.ID().getText()
            params = []
            if nombre in self.memory:           
                if ctx.expresion():
                    for exp in ctx.expresion():  ##for exp in ctx.expresion()
                        params.append(self.visit(exp))
                        #print("lista params",params) ##borrar  [a,b] COMENTARIO IMPORTANTE
                        #print("memory:",self.memory) ##borrar COMENTARIO IMPORTANTE
                #print("elemento valor de m:",self.memory['m']) ##borrar
                proc = self.memory[nombre]
                #print("proc",proc) ##COMENTARIO IMPORTANTE
                #print("proc:",proc) ##borrar
                #print("antes del for",self.memory) ##COMENTARIO IMPORTANTE
            
                #aca es donde se cambiaban los valores de asignacion, pero con este nuevo codigo ya no
                for i, param in enumerate(params):                      
                    self.memory[proc["params"][i]] = self.memory[params[i]]    #self.memory[proc["params"][i]] = param, con este comando anterior se cambian los valores de asignacion
                    #print("param",param)
                #print("despues del for",self.memory)
                #print("tamanio del diccionario",len(self.memory))
            ##aca termina el for
                
                #print("Param",self.memory[proc["params"][i]])
            #return self.visit(proc["body"])  ##colocar de nuevo
            
            #self.visit(proc["body"][i] for i in self.visit(ctx.expresion)) 
            
            #for exp in self.visit(ctx.expresion()):
            
            #print("memory[param]",self.memory[params[0]]) #IMPRIME EL VALOR COMO RESPUESTA  #ESTO SOLO SIRVE PARA EUCLIDES
            #return self.memory[params[0]] QUITAR EL COMENTARIO, AUNQUE ESTO SOLO SIRVE PARA EUCLIDES
            else:
                print("Nombre de procedimiento no encontrado :(")
        

    def visitCondicional(self, ctx):
        if self.visit(ctx.expresion()):
            return self.visit(ctx.bloque(0))
        elif ctx.bloque(1):
            return self.visit(ctx.bloque(1))
    
    def visitRepeticion(self, ctx):
        while self.visit(ctx.expresion()):
            self.visit(ctx.bloque())

    def visitAnadir_lista(self, ctx):
                       
        #AGREGAR_LISTA
        if ctx.ID() and ctx.expresion():
            id = ctx.ID().getText()
        
            exp = self.visit(ctx.expresion())
        
            if id not in self.memory: 
                self.memory[id] = []          
            self.memory[id].append(exp)
        
        
        ##TAMANIO_LISTA
        if ctx.TAM_L() and ctx.ID():                     
            id = ctx.ID().getText()                                
            if id in self.memory:
                tam = len(self.memory[id])                         
                print(tam)
            
                                                                                   
        
        
    #def visitTamano_lista(self,ctx):  
        #print("reconoce metodo")
        #id = ctx.ID().getText()
        #if id in self.memory:
            #tam = len(self.memory[id])         
        #return tam
        #return len(self.memory[id]) if id in self.memory else None
        
        

    def visitCortar_lista(self, ctx):       
        
        ##Cortar lista
        if ctx.ID() and ctx.expresion():
            id = ctx.ID().getText()
            index = self.visit(ctx.expresion())
            #Verificacion del valor que este dentro del rango
            if (index>=1 and index<=len(self.memory[id])):
                self.memory[id].pop(index-1) #Pues empieza desde 1 por enunciado del proyecto  
        
        #Obtener elemento de la lista
        if ctx.ID() and ctx.INT():
            id = ctx.ID().getText()
            index = int(ctx.INT().getText())
            if (index>=1 and index<=len(self.memory[id])): #Se verifica el rango, empieza desde 1
                print(self.memory[id][index-1]) 
            
        
        
        
        
    
        
    
    #def visitCrear_l(self, ctx):
        #print("Reconoce el metodo")
        #Se obtiene el nombre de la lista
        #id = ctx.ID.getText()
        
        
        #Se selecciona el unico valor permitido por defecto
        #e = self.visit(ctx.entero())
        
        #Como dicha lista recien se va a crear, entonces no va a estar en el diccionario 'memory', entonces        
        #self.memory[id] = [] #Clave-valor del diccionario 'memory' --> memory = {id:[]}
        #print("Memory de crear lista",self.memory)
        
        #Ahora, en la lista creada recientemente en el diccionario, debemos agregar el valor que esta en 'e'
        #self.memory[id].append(e) #Nos situamos en el valor de la clave 'id' en el diccionario memory, o sea memory = {id: -->'[]'}
        
        
        
        #Para probar si esta bien implementado el metodo, creare una lista y se mostrara el diccionario
        #print("Imprimiendo diccionario memory")
        #print(self.memory)
    
    
      

    def visitExpresion(self, ctx):
        if ctx.op:
            left = self.visit(ctx.expresion(0))
            right = self.visit(ctx.expresion(1))
            op = ctx.op.text    
            
            if op == '+':
                if (left in self.memory):        
                    if (right in self.memory):
                        left_val, right_val = self.memory[left], self.memory[right]
                        #print("Valores")
                        #print(left_val, right_val)
                        return left_val + right_val
                    else: #Si el valor de la derecha no esta en la memoria, entonces es un valor entero solo 
                        return self.memory[left] + right
                
                else: #Si left no esta en la memoria, entonces es un valor solo, pero pueden haber dos casos: x = 1 + x (e igual deberia funcionar)
                    if (right in self.memory):
                        right_val = self.memory[right]
                        return left + right_val
                    else: #Si no esta en la memoria el right, entonces es un valor entero solo
                        return left + right
                    
                    
                    
            elif op == '-':
                if (left in self.memory): # x - algo, x es una variable
                    if (right in self.memory): # x - a, a es una variable
                        left_val, right_val = self.memory[left], self.memory[right]
                        #print("Valores")
                        #print(left_val, right_val)
                        return left_val - right_val
                    else: #Si el valor de la derecha no esta en la memoria, entonces es un valor entero solo, x - numero 
                        return self.memory[left] - right
                
                else: #Si left no esta en la memoria, entonces es un valor solo, pero pueden haber dos casos: 1 - algo (e igual deberia funcionar)
                    if (right in self.memory): #1 - a, a es una variable
                        right_val = self.memory[right]
                        return left - right_val
                    else: #Si no esta en la memoria el right, entonces es un valor entero solo: 1 - 5
                        return left - right
                    
                    
                    
           
                    
            elif op == '*':
                if (left in self.memory): # x * algo, x es una variable
                    if (right in self.memory): # x * a, a es una variable
                        left_val, right_val = self.memory[left], self.memory[right]                       
                        return left_val * right_val
                    else: #Si el valor de la derecha no esta en la memoria, entonces es un valor entero solo, x * numero 
                        return self.memory[left] * right
                
                else: #Si left no esta en la memoria, entonces es un valor solo, pero pueden haber dos casos: 1 * algo (e igual deberia funcionar)
                    if (right in self.memory): #1 * a, a es una variable
                        right_val = self.memory[right]
                        return left * right_val
                    else: #Si no esta en la memoria el right, entonces es un valor entero solo: 1 * 5
                        return left * right
            
                          
                          
                                
         
                    
            elif op == '/':
                if (left in self.memory): # x / algo, x es una variable
                    if (right in self.memory): # x / a, a es una variable
                        left_val, right_val = self.memory[left], self.memory[right]                       
                        return left_val / right_val
                    else: #Si el valor de la derecha no esta en la memoria, entonces es un valor entero solo, x / numero 
                        return self.memory[left] / right
                
                else: #Si left no esta en la memoria, entonces es un valor solo, pero pueden haber dos casos: 1 / algo (e igual deberia funcionar)
                    if (right in self.memory): #1 / a, a es una variable
                        right_val = self.memory[right]
                        return left / right_val
                    else: #Si no esta en la memoria el right, entonces es un valor entero solo: 1 / 5
                        return left / right
                            
                    
            elif op =='%':
                if (left in self.memory): # x % algo, x es una variable
                    if (right in self.memory): # x % a, a es una variable
                        left_val, right_val = self.memory[left], self.memory[right]                       
                        return left_val % right_val
                    else: #Si el valor de la derecha no esta en la memoria, entonces es un valor entero solo, x % numero 
                        return self.memory[left] % right
                
                else: #Si left no esta en la memoria, entonces es un valor solo, pero pueden haber dos casos: 1 % algo (e igual deberia funcionar)
                    if (right in self.memory): #1 % a, a es una variable
                        right_val = self.memory[right]
                        return left % right_val
                    else: #Si no esta en la memoria el right, entonces es un valor entero solo: 1 % 5
                        return left % right
                        
                    
            
                
                
            elif op == '<':  
                if (left in self.memory): #Si el de la izquierda esta en memoria, es decir, x < (algo)
                    left_val = self.memory[left]
                    #Se verifica el de la derecha, pueden haber dos casos x < a, donde a es una variable ; o x < numero
                    if (right in self.memory): #Si es del caso x < a, 'a' es una variable
                        right_val = self.memory[right]
                        if left_val < right_val:
                            return 1
                        else:
                            return 0
                            
                    else: #Si no esta en memoria, o sea es un valor entero, tal que x < numero --> x < 4
                        if left_val < right:
                            return 1
                        else:
                            return 0
                            
                   
                else: #Si no esta en memoria el de la izquierda, es decir 4 < (algo)
                    if (right in self.memory): #Si el de la derecha esta en memoria, es decir 4 < x, x es una variable
                        right_val = self.memory[right]
                        if left < right_val:
                            return 1
                        else:
                            return 0
                    else: #Si el derecha no esta en memoria, teniendo en cuenta que en la condicional general 'else' el de la izquierda tampoco esta en memoria, entonces 4 < 2
                        if left < right:
                            return 1
                        else:
                            return 0
                            
                            
                
          
                        
            elif op == '>=':
                if (left in self.memory): #Si el de la izquierda esta en memoria, es decir, x >= (algo)
                    left_val = self.memory[left]
                    #Se verifica el de la derecha, pueden haber dos casos x >= a, donde a es una variable ; o x >= numero
                    if (right in self.memory): #Si es del caso x >= a, 'a' es una variable
                        right_val = self.memory[right]
                        if left_val >= right_val:
                            return 1
                        else:
                            return 0
                            
                    else: #Si no esta en memoria, o sea es un valor entero, tal que x < numero --> x >= 4
                        if left_val >= right:
                            return 1
                        else:
                            return 0
                            
                   
                else: #Si no esta en memoria el de la izquierda, es decir 4 >= (algo)
                    if (right in self.memory): #Si el de la derecha esta en memoria, es decir 4 >= x, >= es una variable
                        right_val = self.memory[right]
                        if left >= right_val:
                            return 1
                        else:
                            return 0
                    else: #Si el derecha no esta en memoria, teniendo en cuenta que en la condicional general 'else' el de la izquierda tampoco esta en memoria, entonces 4 >= 2
                        if left >= right:
                            return 1
                        else:
                            return 0
             
            
            ##
            elif op == '>':
                
                if (left in self.memory): #Si el de la izquierda esta en memoria, es decir, x >= (algo)
                    left_val = self.memory[left]
                    #Se verifica el de la derecha, pueden haber dos casos x >= a, donde a es una variable ; o x >= numero
                    if (right in self.memory): #Si es del caso x >= a, 'a' es una variable
                        right_val = self.memory[right]
                        if left_val > right_val:
                            return 1
                        else:
                            return 0
                            
                    else: #Si no esta en memoria, o sea es un valor entero, tal que x < numero --> x >= 4
                        if left_val > right:
                            return 1
                        else:
                            return 0
                            
                   
                else: #Si no esta en memoria el de la izquierda, es decir 4 >= (algo)
                    if (right in self.memory): #Si el de la derecha esta en memoria, es decir 4 >= x, >= es una variable
                        right_val = self.memory[right]
                        if left > right_val:
                            return 1
                        else:
                            return 0
                    else: #Si el derecha no esta en memoria, teniendo en cuenta que en la condicional general 'else' el de la izquierda tampoco esta en memoria, entonces 4 >= 2
                        if left > right:
                            return 1
                        else:
                            return 0
            
            
            elif op == '<=':
                if (left in self.memory): #Si el de la izquierda esta en memoria, es decir, x >= (algo)
                    left_val = self.memory[left]
                    #Se verifica el de la derecha, pueden haber dos casos x >= a, donde a es una variable ; o x >= numero
                    if (right in self.memory): #Si es del caso x >= a, 'a' es una variable
                        right_val = self.memory[right]
                        if left_val <= right_val:
                            return 1
                        else:
                            return 0
                            
                    else: #Si no esta en memoria, o sea es un valor entero, tal que x < numero --> x >= 4
                        if left_val <= right:
                            return 1
                        else:
                            return 0
                            
                   
                else: #Si no esta en memoria el de la izquierda, es decir 4 >= (algo)
                    if (right in self.memory): #Si el de la derecha esta en memoria, es decir 4 >= x, >= es una variable
                        right_val = self.memory[right]
                        if left <= right_val:
                            return 1
                        else:
                            return 0
                    else: #Si el derecha no esta en memoria, teniendo en cuenta que en la condicional general 'else' el de la izquierda tampoco esta en memoria, entonces 4 >= 2
                        if left <= right:
                            return 1
                        else:
                            return 0
             
            
                            
                
          
                        
                        
            elif op == '=':
                if (left in self.memory): #Si el de la izquierda esta en memoria, es decir, x == (algo)
                    left_val = self.memory[left]
                    #Se verifica el de la derecha
                    if (right in self.memory): 
                        right_val = self.memory[right]
                        if left_val == right_val:
                            return 1
                        else:
                            return 0
                            
                    else: #Si no esta en memoria, o sea es un valor entero
                        if left_val == right:
                            return 1
                        else:
                            return 0
                            
                   
                else: #Si no esta en memoria el de la izquierda
                    if (right in self.memory): #Si el de la derecha esta en memoria
                        right_val = self.memory[right]
                        if left == right_val:
                            return 1
                        else:
                            return 0
                    else: #Si el derecha no esta en memoria, teniendo en cuenta que en la condicional general 'else' el de la izquierda tampoco esta en memoria
                        if left == right:
                            return 1
                        else:
                            return 0
                
                
        
            
            elif op == '!=':
                if (left in self.memory): #Si el de la izquierda esta en memoria, es decir, x == (algo)
                    left_val = self.memory[left]
                    #Se verifica el de la derecha
                    if (right in self.memory): 
                        right_val = self.memory[right]
                        if left_val != right_val:
                            return 1
                        else:
                            return 0
                            
                    else: #Si no esta en memoria, o sea es un valor entero
                        if left_val != right:
                            return 1
                        else:
                            return 0
                            
                   
                else: #Si no esta en memoria el de la izquierda
                    if (right in self.memory): #Si el de la derecha esta en memoria
                        right_val = self.memory[right]
                        if left != right_val:
                            return 1
                        else:
                            return 0
                    else: #Si el derecha no esta en memoria, teniendo en cuenta que en la condicional general 'else' el de la izquierda tampoco esta en memoria
                        if left != right:
                            return 1
                        else:
                            return 0
           
           
                
                
        else:
            
            return self.visit(ctx.getChild(0))

    def visitEntero(self, ctx):
        return int(ctx.INT().getText())




