# Generated from SQL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

# This class defines a complete listener for a parse tree produced by SQLParser.
class SQLListener(ParseTreeListener):

    # Enter a parse tree produced by SQLParser#programa.
    def enterPrograma(self, ctx:SQLParser.ProgramaContext):
        pass

    # Exit a parse tree produced by SQLParser#programa.
    def exitPrograma(self, ctx:SQLParser.ProgramaContext):
        pass


    # Enter a parse tree produced by SQLParser#sentencia.
    def enterSentencia(self, ctx:SQLParser.SentenciaContext):
        pass

    # Exit a parse tree produced by SQLParser#sentencia.
    def exitSentencia(self, ctx:SQLParser.SentenciaContext):
        pass



del SQLParser