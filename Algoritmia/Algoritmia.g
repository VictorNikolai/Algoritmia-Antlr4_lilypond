grammar Algoritmia;

@header {
import InterpreteAlgoritmia
}

start
  : bloque EOF
  ;

bloque_principal
  : 'Main' ':' bloque
  ;  

declaracion_procedimientos
  : (llamada_procedimiento)+
  ;



parametro
  : ID
  ;
  
bloque
  : ':' bloque_instrucciones ':'
  ;
  
bloque_instrucciones
  : (instruccion)*
  ;
  
instruccion
  : asignacion
  | lectura
  | escritura
  | reproduccion
  | llamada_procedimiento
  | condicional
  | repeticion
  | anadir_lista
  | cortar_lista
  ;

asignacion
  : '<' ID '=' expresion '>'
  ;

lectura
  : '<?' ID '>'
  ;

escritura
  : '<w>' (expresion | CADENA) '>'
  ;
  
reproduccion
  : '(' expresion ')'
  ;
  
llamada_procedimiento
  : ID '(' (parametro (',' parametro)*)? ')' ':' bloque
  | ID '(' (expresion (',' expresion)*)? ')' 
  ;
  
condicional
  : 'if' expresion bloque ('else' bloque)?
  ;
  
repeticion 
  : 'while' expresion bloque
  ;
  
anadir_lista
  : '<' ID '<<' expresion '>' | TAM_L ID
  ;

cortar_lista
  : '<' ID '8<' expresion '>' | ID '[' INT ']' 
  ;
  

TAM_L
  : '#'
  ;
  

  
PUNTO
  : '.'
  ;

LLAVE
  : ('{' | '}')     
  ;    


expresion
  : expresion op=('*'|'/'| '%') expresion
  | expresion op=('+'|'-') expresion
  | expresion op=('<'|'>='|'='|'!='|'>'|'<=') expresion
  | entero
  | ID
  | llamada_procedimiento
  ;


crear_l
  : '<' ID '=' '{' entero '}' '>'
  ;

elemento
: entero
;

entero
  : INT
  ;

INT
  : [0-9]+
  ;

CADENA
  : '"' (~["\r\n] | '""')* '"'
  ;

ID
  : [a-zA-Z] [a-zA-Z0-9]*
  ;

COMENTARIO
  : '###' .*? '###' -> skip
  ;

WS
  : [ \t\r\n] -> skip
  ;


