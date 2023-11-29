# Generated from Algoritmia.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AlgoritmiaParser import AlgoritmiaParser
else:
    from AlgoritmiaParser import AlgoritmiaParser




# This class defines a complete generic visitor for a parse tree produced by AlgoritmiaParser.

class AlgoritmiaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AlgoritmiaParser#start.
    def visitStart(self, ctx:AlgoritmiaParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#bloque_principal.
    def visitBloque_principal(self, ctx:AlgoritmiaParser.Bloque_principalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#declaracion_procedimientos.
    def visitDeclaracion_procedimientos(self, ctx:AlgoritmiaParser.Declaracion_procedimientosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#parametro.
    def visitParametro(self, ctx:AlgoritmiaParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#bloque.
    def visitBloque(self, ctx:AlgoritmiaParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#bloque_instrucciones.
    def visitBloque_instrucciones(self, ctx:AlgoritmiaParser.Bloque_instruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#instruccion.
    def visitInstruccion(self, ctx:AlgoritmiaParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#asignacion.
    def visitAsignacion(self, ctx:AlgoritmiaParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#lectura.
    def visitLectura(self, ctx:AlgoritmiaParser.LecturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#escritura.
    def visitEscritura(self, ctx:AlgoritmiaParser.EscrituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#reproduccion.
    def visitReproduccion(self, ctx:AlgoritmiaParser.ReproduccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#llamada_procedimiento.
    def visitLlamada_procedimiento(self, ctx:AlgoritmiaParser.Llamada_procedimientoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#condicional.
    def visitCondicional(self, ctx:AlgoritmiaParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#repeticion.
    def visitRepeticion(self, ctx:AlgoritmiaParser.RepeticionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#anadir_lista.
    def visitAnadir_lista(self, ctx:AlgoritmiaParser.Anadir_listaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#cortar_lista.
    def visitCortar_lista(self, ctx:AlgoritmiaParser.Cortar_listaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#expresion.
    def visitExpresion(self, ctx:AlgoritmiaParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#crear_l.
    def visitCrear_l(self, ctx:AlgoritmiaParser.Crear_lContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#elemento.
    def visitElemento(self, ctx:AlgoritmiaParser.ElementoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AlgoritmiaParser#entero.
    def visitEntero(self, ctx:AlgoritmiaParser.EnteroContext):
        return self.visitChildren(ctx)



del AlgoritmiaParser
