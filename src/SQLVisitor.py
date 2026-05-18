# Generated from SQL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

# This class defines a complete generic visitor for a parse tree produced by SQLParser.

class SQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SQLParser#programa.
    def visitPrograma(self, ctx:SQLParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQLParser#sentencia.
    def visitSentencia(self, ctx:SQLParser.SentenciaContext):
        return self.visitChildren(ctx)



del SQLParser