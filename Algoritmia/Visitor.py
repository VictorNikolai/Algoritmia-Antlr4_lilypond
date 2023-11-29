import operator
ops = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.truediv, '^' : operator.pow}

if __name__ is not None and "." in __name__:
    from .AlgoritmiaParser import AlgoritmiaParser
    from .AlgoritmiaVisitor import AlgoritmiaVisitor
else:
    from AlgoritmiaParser import AlgoritmiaParser
    from AlgoritmiaVisitor import AlgoritmiaVisitor

class Visitor(AlgoritmiaVisitor):
    def __init__(self):
        self.myvars = {}
    
    def visitStart(self,ctx):
        l = list(ctx.getChildren())
        for i in range(0, len(l)-1):  
            print(self.visit(l[i]))

    def visitExpresion(self,ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            return int(l[0].getText())
        else:
            return (ops[l[1].getText()](self.visit(l[0]),self.visit(l[2])))
            
   
