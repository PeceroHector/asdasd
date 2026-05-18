# Generated from SQL.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,169,15,2,0,7,0,2,1,7,1,1,0,5,0,6,8,0,10,0,12,0,9,9,0,1,0,1,0,
        1,1,1,1,1,1,0,0,2,0,2,0,0,13,0,7,1,0,0,0,2,12,1,0,0,0,4,6,3,2,1,
        0,5,4,1,0,0,0,6,9,1,0,0,0,7,5,1,0,0,0,7,8,1,0,0,0,8,10,1,0,0,0,9,
        7,1,0,0,0,10,11,5,0,0,1,11,1,1,0,0,0,12,13,9,0,0,0,13,3,1,0,0,0,
        1,7
    ]

class SQLParser ( Parser ):

    grammarFileName = "SQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'||'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'='", "<INVALID>", "'>'", 
                     "'<'", "'>='", "'<='", "';'", "','", "'.'", "'('", 
                     "')'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\n'" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "WHERE", "INSERT", 
                      "INTO", "VALUES", "UPDATE", "SET", "DELETE", "MERGE", 
                      "JOIN", "INNER", "LEFT", "RIGHT", "FULL", "OUTER", 
                      "CROSS", "ON", "GROUP", "BY", "ORDER", "HAVING", "LIMIT", 
                      "OFFSET", "DISTINCT", "ALL", "AS", "UNION", "INTERSECT", 
                      "EXCEPT", "SUBQUERY", "CREATE", "TABLE", "VIEW", "INDEX", 
                      "DATABASE", "SCHEMA", "ALTER", "DROP", "TRUNCATE", 
                      "RENAME", "ADD", "COLUMN", "CONSTRAINT", "PRIMARY", 
                      "FOREIGN", "KEY", "REFERENCES", "UNIQUE", "CHECK", 
                      "DEFAULT", "NOT", "NULL_KW", "AUTO_INCREMENT", "BEGIN", 
                      "COMMIT", "ROLLBACK", "SAVEPOINT", "TRANSACTION", 
                      "CASE", "WHEN", "THEN", "ELSE", "END_KW", "IF_KW", 
                      "EXISTS", "IN_KW", "BETWEEN", "LIKE", "ILIKE", "REGEXP", 
                      "IS", "AND_KW", "OR_KW", "T_INT", "T_BIGINT", "T_SMALLINT", 
                      "T_FLOAT", "T_DOUBLE", "T_NUMERIC", "T_CHAR", "T_VARCHAR", 
                      "T_TEXT", "T_BOOLEAN", "T_DATE", "T_TIME", "T_DATETIME", 
                      "T_TIMESTAMP", "T_JSON", "T_BLOB", "F_COUNT", "F_SUM", 
                      "F_AVG", "F_MAX", "F_MIN", "F_COALESCE", "F_NULLIF", 
                      "F_CAST", "F_UPPER", "F_LOWER", "F_LENGTH", "F_TRIM", 
                      "F_CONCAT", "F_SUBSTR", "F_NOW", "F_ROUND", "F_ABS", 
                      "F_FLOOR", "F_CEIL", "SUMA", "RESTA", "MULT", "DIV", 
                      "MODULO", "CONCAT_OP", "WITH", "FETCH", "NEXT", "ROWS", 
                      "ONLY", "TOP", "OVER", "PARTITION", "ASC", "DESC", 
                      "PROCEDURE", "FUNCTION", "TRIGGER", "SEQUENCE", "TYPE", 
                      "CASCADE", "RESTRICT", "TO", "GRANT", "REVOKE", "DENY", 
                      "ANY", "SOME", "NULLS", "FIRST", "LAST", "DECLARE", 
                      "EXEC", "T_NVARCHAR", "T_XML", "T_UUID", "T_MONEY", 
                      "T_DECIMAL", "IGUAL", "DIFERENTE", "MAYOR", "MENOR", 
                      "MAYOR_IGUAL", "MENOR_IGUAL", "PUNTO_COMA", "COMA", 
                      "PUNTO", "PAREN_IZQ", "PAREN_DER", "NUMERO_ENTERO", 
                      "NUMERO_DECIMAL", "CADENA_TEXTO", "IDENTIFICADOR_QUOTED", 
                      "IDENTIFICADOR", "COMENTARIO_LINEA", "COMENTARIO_BLOQUE", 
                      "ESPACIO", "NUEVA_LINEA", "ERROR_LEXICO" ]

    RULE_programa = 0
    RULE_sentencia = 1

    ruleNames =  [ "programa", "sentencia" ]

    EOF = Token.EOF
    SELECT=1
    FROM=2
    WHERE=3
    INSERT=4
    INTO=5
    VALUES=6
    UPDATE=7
    SET=8
    DELETE=9
    MERGE=10
    JOIN=11
    INNER=12
    LEFT=13
    RIGHT=14
    FULL=15
    OUTER=16
    CROSS=17
    ON=18
    GROUP=19
    BY=20
    ORDER=21
    HAVING=22
    LIMIT=23
    OFFSET=24
    DISTINCT=25
    ALL=26
    AS=27
    UNION=28
    INTERSECT=29
    EXCEPT=30
    SUBQUERY=31
    CREATE=32
    TABLE=33
    VIEW=34
    INDEX=35
    DATABASE=36
    SCHEMA=37
    ALTER=38
    DROP=39
    TRUNCATE=40
    RENAME=41
    ADD=42
    COLUMN=43
    CONSTRAINT=44
    PRIMARY=45
    FOREIGN=46
    KEY=47
    REFERENCES=48
    UNIQUE=49
    CHECK=50
    DEFAULT=51
    NOT=52
    NULL_KW=53
    AUTO_INCREMENT=54
    BEGIN=55
    COMMIT=56
    ROLLBACK=57
    SAVEPOINT=58
    TRANSACTION=59
    CASE=60
    WHEN=61
    THEN=62
    ELSE=63
    END_KW=64
    IF_KW=65
    EXISTS=66
    IN_KW=67
    BETWEEN=68
    LIKE=69
    ILIKE=70
    REGEXP=71
    IS=72
    AND_KW=73
    OR_KW=74
    T_INT=75
    T_BIGINT=76
    T_SMALLINT=77
    T_FLOAT=78
    T_DOUBLE=79
    T_NUMERIC=80
    T_CHAR=81
    T_VARCHAR=82
    T_TEXT=83
    T_BOOLEAN=84
    T_DATE=85
    T_TIME=86
    T_DATETIME=87
    T_TIMESTAMP=88
    T_JSON=89
    T_BLOB=90
    F_COUNT=91
    F_SUM=92
    F_AVG=93
    F_MAX=94
    F_MIN=95
    F_COALESCE=96
    F_NULLIF=97
    F_CAST=98
    F_UPPER=99
    F_LOWER=100
    F_LENGTH=101
    F_TRIM=102
    F_CONCAT=103
    F_SUBSTR=104
    F_NOW=105
    F_ROUND=106
    F_ABS=107
    F_FLOOR=108
    F_CEIL=109
    SUMA=110
    RESTA=111
    MULT=112
    DIV=113
    MODULO=114
    CONCAT_OP=115
    WITH=116
    FETCH=117
    NEXT=118
    ROWS=119
    ONLY=120
    TOP=121
    OVER=122
    PARTITION=123
    ASC=124
    DESC=125
    PROCEDURE=126
    FUNCTION=127
    TRIGGER=128
    SEQUENCE=129
    TYPE=130
    CASCADE=131
    RESTRICT=132
    TO=133
    GRANT=134
    REVOKE=135
    DENY=136
    ANY=137
    SOME=138
    NULLS=139
    FIRST=140
    LAST=141
    DECLARE=142
    EXEC=143
    T_NVARCHAR=144
    T_XML=145
    T_UUID=146
    T_MONEY=147
    T_DECIMAL=148
    IGUAL=149
    DIFERENTE=150
    MAYOR=151
    MENOR=152
    MAYOR_IGUAL=153
    MENOR_IGUAL=154
    PUNTO_COMA=155
    COMA=156
    PUNTO=157
    PAREN_IZQ=158
    PAREN_DER=159
    NUMERO_ENTERO=160
    NUMERO_DECIMAL=161
    CADENA_TEXTO=162
    IDENTIFICADOR_QUOTED=163
    IDENTIFICADOR=164
    COMENTARIO_LINEA=165
    COMENTARIO_BLOQUE=166
    ESPACIO=167
    NUEVA_LINEA=168
    ERROR_LEXICO=169

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SQLParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(SQLParser.SentenciaContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = SQLParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -2) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & -1) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & 4398046511103) != 0):
                self.state = 4
                self.sentencia()
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 10
            self.match(SQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SQLParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = SQLParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





