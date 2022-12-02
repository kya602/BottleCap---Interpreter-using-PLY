import ply.lex as lex
import ply.yacc as yacc
import sys


rkw = {
    'Print' : 'PRINT',
    'Add' : 'ADD',
    'with' : 'W',
    'Subtract' : 'SUB',
    'from' : 'FROM',
    'Multiply' : 'MUL',
    'Divide' : 'DIV',
    'by' : 'BY',
    'Assign' : 'ASSIGN',
    'to' : 'TO'

}



tokens = [
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'OBRACE',
    'CBRACE',
    'NEXT'
 ] + list(rkw.values())

literals = ['\t', '\n']

t_ignore = r' '

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_OBRACE  = r'\{'
t_CBRACE  = r'\}'
t_NEXT = r'\t+'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = rkw.get(t.value,'ID')    # Check for reserved words
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()















