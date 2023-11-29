# test.py

from antlr4 import *
from AlgoritmiaLexer import AlgoritmiaLexer
from AlgoritmiaParser import AlgoritmiaParser
from EvalVisitor import EvalVisitor

def main():

    input= """
Main:
 <w> "Ingrese dos numeros">   
<? a>
<? b>



  Euclides (a,b):
  :
  while a != b:
  
  if a > b:
  <a = a - b>
  :
  
  else:
  <b = b - a> 
  :
  
  :
  
  <w> "Su MCD es">
  <w> a>
  :
  
  <w> "Fin">
  
  <q = 4>
  <r= 6>
  <w> q>
  <w> r>
  
  if q > r:
  <w> "True">
  :
  else:
  <w> "False">
  :
  
  <w> "Escribe dos numeros para aplicar el operador mod:">
  <? d>
  <? u>
  <j = d % u>
  <w> j>
  
  
  
  
  < l << a >
  
  < l << b >
  
  < l << c >
  
  
  <w> "Lista completa">
  <w> l>
  
  
  <w> "Tamanio de la lista">
  # l
 
  
  <w> "Eliminacion del elemento 2">
  < l 8< 2 >
  
  <w> l>
  
  <w> "Agregamos el elemento u">
  < l << u >
  <w> "ListaFinal">
  <w> l>
  
  <w> "Elemento de la posicion 1"
  l [ 1 ]
  
  
  <m = 3>
  <w> m>
  
  <w> "Tamanio de la lista">
  # l
  
  <w> "Agregamos el elemento r">
  < l << r >
  <w> "Tamanio lista">
  # l
  
  <w> "Eliminacion de elemento 1">
  < l 8< 1 >
  <w> l>
  <w> "Tamanio final">
  # l
  
  < f = 3 + 5 * 3 >
  <w> f>
  
:
  
"""

    lexer = AlgoritmiaLexer(InputStream(input))
    stream = CommonTokenStream(lexer)
    parser = AlgoritmiaParser(stream)
    tree = parser.start()

    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
