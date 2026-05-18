import sys
import os
from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from SQLLexer import SQLLexer


class LexerErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errores.append({
            'linea':   line,
            'columna': column + 1,
            'mensaje': msg
        })

NOMBRES = {
    # DML
    SQLLexer.SELECT:        'SELECT',
    SQLLexer.FROM:          'FROM',
    SQLLexer.WHERE:         'WHERE',
    SQLLexer.INSERT:        'INSERT',
    SQLLexer.INTO:          'INTO',
    SQLLexer.VALUES:        'VALUES',
    SQLLexer.UPDATE:        'UPDATE',
    SQLLexer.SET:           'SET',
    SQLLexer.DELETE:        'DELETE',
    SQLLexer.MERGE:         'MERGE',
    SQLLexer.TO:            'TO',

    # Cláusulas de consulta
    SQLLexer.JOIN:          'JOIN',
    SQLLexer.INNER:         'INNER',
    SQLLexer.LEFT:          'LEFT',
    SQLLexer.RIGHT:         'RIGHT',
    SQLLexer.FULL:          'FULL',
    SQLLexer.OUTER:         'OUTER',
    SQLLexer.CROSS:         'CROSS',
    SQLLexer.ON:            'ON',
    SQLLexer.GROUP:         'GROUP',
    SQLLexer.BY:            'BY',
    SQLLexer.ORDER:         'ORDER',
    SQLLexer.HAVING:        'HAVING',
    SQLLexer.LIMIT:         'LIMIT',
    SQLLexer.OFFSET:        'OFFSET',
    SQLLexer.DISTINCT:      'DISTINCT',
    SQLLexer.ALL:           'ALL',
    SQLLexer.AS:            'AS',
    SQLLexer.UNION:         'UNION',
    SQLLexer.INTERSECT:     'INTERSECT',
    SQLLexer.EXCEPT:        'EXCEPT',
    SQLLexer.SUBQUERY:      'SUBQUERY',

    # Consultas avanzadas y Window Functions
    SQLLexer.WITH:          'WITH',
    SQLLexer.FETCH:         'FETCH',
    SQLLexer.NEXT:          'NEXT',
    SQLLexer.ROWS:          'ROWS',
    SQLLexer.ONLY:          'ONLY',
    SQLLexer.TOP:           'TOP',
    SQLLexer.OVER:          'OVER',
    SQLLexer.PARTITION:     'PARTITION',
    SQLLexer.ASC:           'ASC',
    SQLLexer.DESC:          'DESC',
    
    # DDL Extendido y DCL
    SQLLexer.PROCEDURE:     'PROCEDURE',
    SQLLexer.FUNCTION:      'FUNCTION',
    SQLLexer.TRIGGER:       'TRIGGER',
    SQLLexer.SEQUENCE:      'SEQUENCE',
    SQLLexer.TYPE:          'TYPE',
    SQLLexer.CASCADE:       'CASCADE',
    SQLLexer.RESTRICT:      'RESTRICT',
    SQLLexer.GRANT:         'GRANT',
    SQLLexer.REVOKE:        'REVOKE',
    SQLLexer.DENY:          'DENY',

    # Conjuntos, lógica y variables
    SQLLexer.ANY:           'ANY',
    SQLLexer.SOME:          'SOME',
    SQLLexer.NULLS:         'NULLS',
    SQLLexer.FIRST:         'FIRST',
    SQLLexer.LAST:          'LAST',
    SQLLexer.DECLARE:       'DECLARE',
    SQLLexer.EXEC:          'EXEC',

    # Nuevos Tipos de Dato
    SQLLexer.T_NVARCHAR:    'T_NVARCHAR',
    SQLLexer.T_XML:         'T_XML',
    SQLLexer.T_UUID:        'T_UUID',
    SQLLexer.T_MONEY:       'T_MONEY',
    SQLLexer.T_DECIMAL:     'T_DECIMAL',

    # DDL
    SQLLexer.CREATE:        'CREATE',
    SQLLexer.TABLE:         'TABLE',
    SQLLexer.VIEW:          'VIEW',
    SQLLexer.INDEX:         'INDEX',
    SQLLexer.DATABASE:      'DATABASE',
    SQLLexer.SCHEMA:        'SCHEMA',
    SQLLexer.ALTER:         'ALTER',
    SQLLexer.DROP:          'DROP',
    SQLLexer.TRUNCATE:      'TRUNCATE',
    SQLLexer.RENAME:        'RENAME',
    SQLLexer.ADD:           'ADD',
    SQLLexer.COLUMN:        'COLUMN',
    SQLLexer.CONSTRAINT:    'CONSTRAINT',
    SQLLexer.PRIMARY:       'PRIMARY',
    SQLLexer.FOREIGN:       'FOREIGN',
    SQLLexer.KEY:           'KEY',
    SQLLexer.REFERENCES:    'REFERENCES',
    SQLLexer.UNIQUE:        'UNIQUE',
    SQLLexer.CHECK:         'CHECK',
    SQLLexer.DEFAULT:       'DEFAULT',
    SQLLexer.NOT:           'NOT',
    SQLLexer.NULL_KW:       'NULL',
    SQLLexer.AUTO_INCREMENT:'AUTO_INCREMENT',
    # TCL
    SQLLexer.BEGIN:         'BEGIN',
    SQLLexer.COMMIT:        'COMMIT',
    SQLLexer.ROLLBACK:      'ROLLBACK',
    SQLLexer.SAVEPOINT:     'SAVEPOINT',
    SQLLexer.TRANSACTION:   'TRANSACTION',
    # Condicional / lógica
    SQLLexer.CASE:          'CASE',
    SQLLexer.WHEN:          'WHEN',
    SQLLexer.THEN:          'THEN',
    SQLLexer.ELSE:          'ELSE',
    SQLLexer.END_KW:        'END',
    SQLLexer.IF_KW:         'IF',
    SQLLexer.EXISTS:        'EXISTS',
    SQLLexer.IN_KW:         'IN',
    SQLLexer.BETWEEN:       'BETWEEN',
    SQLLexer.LIKE:          'LIKE',
    SQLLexer.ILIKE:         'ILIKE',
    SQLLexer.REGEXP:        'REGEXP',
    SQLLexer.IS:            'IS',
    SQLLexer.AND_KW:        'AND',
    SQLLexer.OR_KW:         'OR',
    # Tipos de dato
    SQLLexer.T_INT:         'T_INT',
    SQLLexer.T_BIGINT:      'T_BIGINT',
    SQLLexer.T_SMALLINT:    'T_SMALLINT',
    SQLLexer.T_FLOAT:       'T_FLOAT',
    SQLLexer.T_DOUBLE:      'T_DOUBLE',
    SQLLexer.T_NUMERIC:     'T_NUMERIC',
    SQLLexer.T_CHAR:        'T_CHAR',
    SQLLexer.T_VARCHAR:     'T_VARCHAR',
    SQLLexer.T_TEXT:        'T_TEXT',
    SQLLexer.T_BOOLEAN:     'T_BOOLEAN',
    SQLLexer.T_DATE:        'T_DATE',
    SQLLexer.T_TIME:        'T_TIME',
    SQLLexer.T_DATETIME:    'T_DATETIME',
    SQLLexer.T_TIMESTAMP:   'T_TIMESTAMP',
    SQLLexer.T_JSON:        'T_JSON',
    SQLLexer.T_BLOB:        'T_BLOB',
    # Funciones
    SQLLexer.F_COUNT:       'COUNT',
    SQLLexer.F_SUM:         'SUM',
    SQLLexer.F_AVG:         'AVG',
    SQLLexer.F_MAX:         'MAX',
    SQLLexer.F_MIN:         'MIN',
    SQLLexer.F_COALESCE:    'COALESCE',
    SQLLexer.F_NULLIF:      'NULLIF',
    SQLLexer.F_CAST:        'CAST',
    SQLLexer.F_UPPER:       'UPPER',
    SQLLexer.F_LOWER:       'LOWER',
    SQLLexer.F_LENGTH:      'LENGTH',
    SQLLexer.F_TRIM:        'TRIM',
    SQLLexer.F_CONCAT:      'CONCAT',
    SQLLexer.F_SUBSTR:      'SUBSTR',
    SQLLexer.F_NOW:         'NOW',
    SQLLexer.F_ROUND:       'ROUND',
    SQLLexer.F_ABS:         'ABS',
    SQLLexer.F_FLOOR:       'FLOOR',
    SQLLexer.F_CEIL:        'CEIL',
    # Operadores aritméticos
    SQLLexer.SUMA:          'SUMA',
    SQLLexer.RESTA:         'RESTA',
    SQLLexer.MULT:          'MULT',
    SQLLexer.DIV:           'DIV',
    SQLLexer.MODULO:        'MODULO',
    SQLLexer.CONCAT_OP:     'CONCAT_OP',
    # Operadores relacionales
    SQLLexer.IGUAL:         'IGUAL',
    SQLLexer.DIFERENTE:     'DIFERENTE',
    SQLLexer.MAYOR:         'MAYOR',
    SQLLexer.MENOR:         'MENOR',
    SQLLexer.MAYOR_IGUAL:   'MAYOR_IGUAL',
    SQLLexer.MENOR_IGUAL:   'MENOR_IGUAL',
    # Delimitadores
    SQLLexer.PUNTO_COMA:    'PUNTO_COMA',
    SQLLexer.COMA:          'COMA',
    SQLLexer.PUNTO:         'PUNTO',
    SQLLexer.PAREN_IZQ:     'PAREN_IZQ',
    SQLLexer.PAREN_DER:     'PAREN_DER',
    # Literales
    SQLLexer.NUMERO_ENTERO:       'NUMERO_ENTERO',
    SQLLexer.NUMERO_DECIMAL:      'NUMERO_DECIMAL',
    SQLLexer.CADENA_TEXTO:        'CADENA_TEXTO',
    SQLLexer.IDENTIFICADOR_QUOTED:'IDENTIFICADOR_QUOTED',
    SQLLexer.IDENTIFICADOR:       'IDENTIFICADOR',
    # Ignorados / auxiliares
    SQLLexer.COMENTARIO_LINEA:    'COMENTARIO_LINEA',
    SQLLexer.COMENTARIO_BLOQUE:   'COMENTARIO_BLOQUE',
    SQLLexer.ESPACIO:             'ESPACIO',
    SQLLexer.NUEVA_LINEA:         'NUEVA_LINEA',
    SQLLexer.ERROR_LEXICO:        'ERROR_LEXICO',
    -1: 'EOF',
}

# Tokens que se omiten en la salida
OMITIR = {'COMENTARIO_LINEA', 'COMENTARIO_BLOQUE', 'ESPACIO', 'NUEVA_LINEA', 'EOF'}


#análisis


def analizar(fuente: str, nombre_archivo: str = "<fuente>"):
    print("=" * 50)
    print(f"  Analizador Lexico SQL")
    print(f"  Archivo: {nombre_archivo}")
    print("=" * 50)

    input_stream = InputStream(fuente)
    lexer = SQLLexer(input_stream)

    error_listener = LexerErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    stream = CommonTokenStream(lexer)
    stream.fill()
    tokens = stream.tokens

    print("\nToken List:")

    contador = 1
    for tok in tokens:
        nombre = NOMBRES.get(tok.type, f'TIPO_{tok.type}')
        if nombre in OMITIR:
            continue

        valor = f'"{tok.text}"'

        print(f"  {contador}: ({nombre}, {valor})")
        contador += 1

    print(f"\nTotal de tokens: {contador - 1}")

    # Recolectar tokens ERROR_LEXICO
    for tok in tokens:
        if NOMBRES.get(tok.type, '') == 'ERROR_LEXICO':
            error_listener.errores.append({
                'linea':   tok.line,
                'columna': tok.column + 1,
                'mensaje': f"Símbolo desconocido '{tok.text}'"
            })

    if error_listener.errores:
        print("\nError List:")
        for i, err in enumerate(error_listener.errores, 1):
            print(
                f"  Line {err['linea']}, Column {err['columna']}:  "
                f"{err['mensaje']}"
            )
        print(f"\nTotal de errores: {len(error_listener.errores)}")
    else:
        print("\nAnalisis lexico completado sin errores.")

    print()
    return tokens, error_listener.errores


#inicio
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <archivo.sql>")
        sys.exit(1)

    argumento = sys.argv[1]

    if not os.path.exists(argumento):
        print(f"Error: no se encontró el archivo '{argumento}'")
        sys.exit(1)

    with open(argumento, encoding="utf-8") as f:
        codigo = f.read()

    analizar(codigo, argumento)
