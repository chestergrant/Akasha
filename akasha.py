import lex
import yacc

tokens = (
			'IF',
			'RBRACKET',
			'LBRACKET',
			'EQUAL',
			'EQUALEQUAL',
			'PRINT',
			'FOR',
			'IN',
			'FULLSTOP',
			'FUNCTION',
			'RETURN',
			'LSQUAREBRACKET',
			'RSQUAREBRACKET',
			'PLUS',
			'MINUS',
			'TIMES',
			'DIVIDE',
			'LT',
			'LE',
			'GT',
			'GE',
			'NE',
			'COMMA',
			'SEMICOLON',
			'INT',
			'FLOAT',
			'STRING',
			'LPAREN',
			'RPAREN',
			'ID',
			'HASH',
			'COMMENTBEGIN',
			'COMMENTEND',
			'ANDAND',
			'ELSE',
			'FALSE',
			'TRUE',
			'OROR',
			'OPEN',
			'TYPE',
			'NEWLINE',
			'IMPORT',
			'CODEGENERATIONBEGINS',
			'CODEGENERATIONENDS',
			'LIST',
			'APPENDFUNC',
			'DICT',
			'WHILE',
			'TUPLE',
			'TYPEFUNC',
			'SIZEFUNC',
			'PROGPARAMETER'
)
t_ignore = ' \t\v\r'

t_HASH = r'\#'
t_COMMENTBEGIN = r'/\*'
t_COMMENTEND = r'\*/'
t_ANDAND = r'&&'
t_NEWLINE = r'\n'

def t_PROGPARAMETER(t):
	r'_[a-z_]+'
	return t
	
def t_SIZEFUNC(t):
	r'size'
	return t
	
def t_TYPEFUNC(t):
	r'type'
	return t
	
def t_TUPLE(t):
	r'tuple'
	return t
	
def t_WHILE(t):
	r'while'
	return t
def t_DICT(t):
	r'dict'
	return t
	
def t_APPENDFUNC(t):
	r'append'
	return t
def t_LIST(t):
	r'list'
	return t
def t_CODEGENERATIONBEGINS(t):
	r'<codegeneration>'
	return t
def t_CODEGENERATIONENDS(t):
	r'</codegeneration>'
	return t
def t_IMPORT(t):
	r'import'
	return t
	
def t_ELSE (t):
	r'else'
	return t

def t_FALSE(t):
	r'false'
	return t

def t_TRUE(t):	
	r'true'
	return t
t_OROR = r'\|\|'
def t_OPEN(t):
	r'open'
	return t
def t_TYPE(t):
	r'(?:int)|(?:float)|(?:string)|(?:boolean)'
	return t
t_NE = r'!='
t_COMMA = r','
t_SEMICOLON = r';'
t_INT = r'[0-9]+'
t_FLOAT = r'[0-9]+\.[0-9]*'
def t_STRING(t):
	r'\".*?\"'
	t.value = t.value[1:-1]
	return t
t_LPAREN = '\('
t_RPAREN = '\)'
	
t_LSQUAREBRACKET = r'\['
t_RSQUAREBRACKET = r'\]'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\\'
t_LE = r'<='
t_LT = r'<'
t_GE = r'>='
t_GT = r'>'


def t_IF(t):
	r'if'
	return t

def t_RBRACKET(t):
	r'}'
	return t
def t_LBRACKET(t):
	r'{'
	return t
	
def t_EQUALEQUAL(t):
	r'=='
	return t
	
def t_EQUAL(t):
	r'='
	return t
	
def t_PRINT(t):
	r'print'
	return t
	
def t_FOR(t):
	r'for'
	return t
	
def t_IN(t):
	r'in'
	return t
	
def t_FULLSTOP(t):
	r'\.'
	return t
	
def t_FUNCTION(t):
	r'function'
	return t
	
def t_RETURN(t):
	r'return'
	return t

def t_error(t):
	t.lexer.skip(1)

t_ID = r'[a-zA-Z][a-zA-Z_]*'

prog = "!=,; 89 09 57 0. 1. 9.78 \"Hello My Name is \"() hello chester for # /* */  \n boolean && else false true || open int string float"
prog = "tuple type size list append dict while import <codegeneration> </codegeneration> _length _function_set"
akashalexer = lex.lex()
akashalexer.input(prog)
while True:
	tok = akashalexer.token()
	if not tok :break
	print tok