import lex
import yacc
start  = 'program'

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
			'LENFUNC',
			'PROGPARAMETER',
			'COMMENT',
			'COLON',
			'RANGEFUNC'
)
t_ignore = ' \t\v\r'

def t_HASH(t):
	r'\#'
	return t
def t_COMMENTBEGIN(t):
	r'/\*'
	return t
def t_COMMENTEND(t):
	r'\*/'
	return t
def t_ANDAND(t):
	r'&&'
	return t

def t_PROGPARAMETER(t):
	r'_[a-z_]+'
	return t
def t_RANGEFUNC(t):
	r'range'
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
def t_LENFUNC(t):
	r'len'
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
def t_OROR(t):
	r'\|\|'
	return t
def t_OPEN(t):
	r'open'
	return t
def t_TYPE(t):
	r'(?:int)|(?:float)|(?:string)|(?:boolean)'
	return t
def t_NE(t):
	r'!='
	return t
def t_COMMA(t):
	r','
	return t
def t_SEMICOLON (t):
	r';'
	return t
def t_COLON(t):
	r':'
	return t
	
def t_FLOAT(t):
	r'-?[0-9]+\.[0-9]*'
	return t
	
def t_INT(t):
	r'-?[0-9]+'
	return t

def t_STRING(t):
	r'\"(?:(?:\W)|(?:\w))*\"'
	t.value = t.value[1:-1]
	return t

def t_NEWLINE(t):
	r'\n'
	return t
	
def t_LPAREN(t):
	'\('
	return t
def t_RPAREN(t):
	'\)'
	return t
def t_LSQUAREBRACKET(t):
	r'\['
	return t
def t_RSQUAREBRACKET(t):
	r'\]'
	return t
def t_PLUS(t):
	r'\+'
	return t
def t_MINUS(t):
	r'\-'
	return t
def t_TIMES(t):
	r'\*'
	return t
def t_DIVIDE(t):
	r'\\'
	return t
def t_LE(t):
	r'<='
	return t
def t_LT(t):
	r'<'
	return t
def t_GE(t):
	r'>='
	return t
def t_GT(t):
	r'>'
	return t
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
def t_ID(t):
	r'[a-zA-Z][a-zA-Z_]*'
	return t
def t_COMMENT(t):
	r'[^a-zA-Z0-9 \t\n]+'	
	return t
	
def t_error(t):
	t.lexer.skip(1)
def p_program(p):
	'program : programstatements'
	p[0] = ("program",p[1])
def p_program_empty(p):
	'program : '
	p[0] = ("program","No Code")
def p_programstatements_one(p):
	'programstatements : codeblock'
	p[0] = ("programstatements",p[1])
def p_programstatements_multi(p):
	'programstatements : codeblock programstatements'
	p[0] = ("programstatement",p[1],p[2])
def p_codeblock_fileopen(p):
	'codeblock : fileopen'
	p[0] =("codeblock",p[1])

def p_fileopen(p):
	'fileopen : FILE ID OPEN LPAREN stringdata RPAREN SEMICOLON'
	p[0] = ("fileopen",p[2],p[5])
def p_stringdata_string(p):
	'stringdata : STRING'
	p[0] = ("stringdata",p[1])
def p_stringdata_variable(p):
	'stringdata : ID'
	p[0] = ("stringdata", p[1])
def p_stringdata_strfunc(p):
	'stringdata : strfunccall'
	p[0] = ("stringdata",p[1])
def p_strfunccall(p):
	'strfunccall : STRFUNC LPAREN datalist RPAREN' #need to define othernonstring
	p[0] = ("strfunccall",p[3])
	
def p_stringdata_concat(p):
	'stringdata : stringdata PLUS stringdata'
	p[0] = ("stringdata",p[1],p[2])
def p_stringdata_empty(p):
	'stringdata : '
	p[0] =("stringdata","")

def p_codeblock_printing(p):
	'codeblock : printing'
	p[0] = ("codeblock",p[1])

def p_printing(p):
	'printing : PRINT LPAREN printlocation COMMA stringdata RPAREN SEMICOLON'
	p[0] = ("printing",p[3],p[5])
def p_printlocation(p):
	'''printlocation : ID 
					 | funccall'''
	p[0] = p[1]
def p_printing_screen(p):
	'printing : PRINT LPAREN stringdata RPAREN SEMICOLON'
	p[0] = ("printing",p[3])
def p_commenting(p):
	'commenting : HASH comments NEWLINE'
	p[0] = ("commenting",p[2])
def p_comments(p):
	'comments : '
	p[0] = ""
def p_comments_everybody(p):
	'''comments :  commentoptions comments'''
	p[0] = p[1] + p[2]
def p_commentoptions(p):
	'''commentoptions : IF
					  | RBRACKET
					  | LBRACKET
					  | EQUAL
					  | EQUALEQUAL
					  | PRINT
					  | FOR
					  | IN
					  | FULLSTOP
					  | FUNCTION
					  | RETURN
					  | LSQUAREBRACKET
					  | RSQUAREBRACKET
					  | PLUS
					  | MINUS
					  | TIMES
					  | DIVIDE
					  | COLON
					  | LT
					  | LE
					  | GT
					  | GE
					  | NE
					  | COMMA
					  | SEMICOLON
					  | INT
					  | FLOAT
					  | STRING
					  | LPAREN
					  | RPAREN
					  | ID
					  | HASH
					  | COMMENTBEGIN
					  | COMMENTEND
					  | ANDAND
					  | ELSE
					  | FALSE
					  | TRUE
					  | OROR
					  | OPEN
					  | TYPE
					  | IMPORT
					  | CODEGENERATIONBEGINS
					  | CODEGENERATIONENDS
					  | LIST
					  | APPENDFUNC
					  | DICT
					  | WHILE
					  | TUPLE
					  | TYPEFUNC
					  | SIZEFUNC
					  | PROGPARAMETER
					  | COMMENT
					  | RANGEFUNC'''
	p[0] = p[1]
def p_commenting(p):
	'commenting : COMMENTBEGIN multilinecomment COMMENTEND'
	p[0] = ("commenting",p[2])
def p_multilinecomment(p):
	'multilinecomment : comments'
	p[0] = p[1]
def p_multilinecomment_multi(p):
	'multilinecomment : comments NEWLINE comments'
	p[0] = p[1]+p[3]

def p_codeblock_commenting(p):
	'codeblock : commenting'
	p[0] = ("codeblock",p[1])
def p_codeblock_variabledeclaration(p):
	'codeblock : variabledeclaration'
	p[0] = ("codeblock",p[1])

def p_variabledeclaration(p):
	'variabledeclaration : typeoptions ID SEMICOLON'
	p[0] = ("variabledeclaration", p[1],p[2])
def p_variabledeclaration_assignment(p):
	'variabledeclaration : typeoptions ID EQUAL value SEMICOLON'
	p[0] =("variabledeclaration",p[1],p[2],p[4])
def p_value(p):
	'''value : stringdata
			 | INT
			 | FLOAT
			 | BOOLEAN
			 | ID
			 | funccall
			 | sizefunccall
			 | lenfunccall'''
	p[0] = ("value",p[1])
def p_variabledeclaration_tuple(p):
	'variabledeclaration : tupledeclaration'
	p[0] = ("variabledeclaration",p[1])
def p_variabledeclaration_list(p):
	'variabledeclaration : listdeclaration'
	p[0] = ("variabledeclaration",p[1])
def p_variabledeclaration_dict(p):
	'variabledeclaration : dictdeclaration'
	p[0] = ("variabledeclaration", p[1])
def p_tupledeclaration(p):
	'tupledeclaration : tupletype ID EQUAL tuplevalue SEMICOLON'
	p[0] = ("tupledeclaration",p[1],p[2],p[4])
def p_tupletype(p):
	'tupletype : TUPLE LPAREN complexlist RPAREN'
	p[0] = ("tupletype",p[3])
def p_complexlist(p):
	'complexlist : differenttype'
	p[0] = ("complexlist",p[1])
def p_complexlist(p):
	'complexlist : differenttype COMMA complexlist'
	p[0] = ("complexlist",p[1],p[2])
def p_differenttype(p):
	'''differenttype : TYPE
					 | tupletype
					 | listtype
					 | dicttype
					 | typefunccall'''
	p[0] = ("differenttype",p[1])
def p_listdeclaration(p):
	'listdeclaration : listtype ID SEMICOLON'
	p[0] = ("listdeclaration", p[1],p[2])
def p_listdeclaration_assignment(p):
	'listdeclaration : listtype ID EQUAL listvalue SEMICOLON'
	p[0] = ("listdeclaration",p[1],p[2],p[4])
def p_listtype(p):
	'listtype : LIST LPAREN complexlist RPAREN'
	p[0] = ("listtype",p[3])
def p_dictdeclaration(p):
	'dictdeclaration : dicttype ID EQUAL LBRACKET RBRACKET SEMICOLON'
	p[0] = ("dictdeclaration", p[1],p[2])
def p_dictdeclaration_assignment(p):
	'dictdeclaration : dicttype ID EQUAL dictvalue SEMICOLON'
	p[0] = ("dictdeclaration", p[1],p[2],p[4])
def p_dicttype(p):
	'dicttype : DICT LPAREN dictlist RPAREN'
	p[0] = ("dicttype",p[3])
def p_dictlist(p):
	'dictlist : key COMMA differenttype'
	p[0] = ("dictlist",p[1],p[3])
def p_key(p):
	'''key : TYPE
		   | tupletype
		   | typefunccall'''
	p[0] = ("key",p[1])
def p_tuplevalue(p):
	'tuplevalue : LPAREN tupledatalist RPAREN'
	p[0] = ("tuplevalue", p[2])
def p_tuplevalue_id(p):
	'tuplevalue : ID'
	p[0] = ("tuplevalue", p[1])
	
def p_tupledatalist(p):
	'tupledatalist : datalist'
	p[0] = ("tupledatalist",p[1])
def p_tupledatalist_multi(p):
	'tupledatalist : datalist COMMA tupledatalist'
	p[0] = ("tupledatalist",p[1],p[3])
def p_datalist(p):
	'''datalist : listvalue
			    | tuplevalue
				| INT
				| FLOAT
				| stringdata
				| BOOLEAN
				| dictvalue
				| ID
				| arithmetic
				| funccall
				| sizefunccall
				| rangefunccall
				| lenfunccall'''
	p[0] = ("datalist",p[1])
def p_typeoptions(p):
	'''typeoptions : TYPE 
				   | typefunccall'''
	p[0] = ("type",p[1])
def p_listvalue(p):
	'listvalue : LSQUAREBRACKET RSQUAREBRACKET'
	p[0] = ("listvalue","")
def p_listvalue_id(p):
	'listvalue : ID'
	p[0] =("listvalue",p[1])
def p_listvalue_multi(p):
	'listvalue : LSQUAREBRACKET listdatalist RSQUAREBRACKET'
	p[0] = ("listvalue", p[2])
def p_listdatalist(p):
	'listdatalist : datalist'
	p[0] = ("listdatalist",p[1])
def p_listdatalist_multi(p):
	'listdatalist : datalist COMMA listdatalist'
	p[0] = ("listdatalist",p[1],p[3])
def p_dictvalue_id(p):
	'dictvalue : ID'
	p[0] = ("dictvalue",p[1])
def p_dictvalue(p):
	'dictvalue: LBRACKET dictdatalist RBRACKET'
	p[0] = ("dictvalue",p[2])
def p_dictdatalist(p):
	'dictdatalist : '
	p[0] = ("dictdatalist","")
def p_dictdatalist_multi(p):
	'dictdatalist : keyvalue COLON datalist COMMA dictdatalist'
	p[0] = ("dictdatalist", p[1],p[3],p[5])
def p_keyvalue(p):
	'''keyvalue : ID
				| BOOLEAN
				| INT
				| stringdata
				| FLOAT
				| funccall
				| sizefunccall
				| lenfunccall'''
	p[0] = ("keyvalue",p[1])
def p_arithmetic(p):
	'arithmetic : aexpr operator aexpr'
	p[0] = ("arithmetic",p[1],p[2],p[3])
def p_arithmetic_paren(p):
	'arithmetic : LPAREN aexpr operator aexpr RPAREN'
	p[0] = ("arithmetic",p[2],p[3],p[4])
def p_operator(p):
	'''operator : PLUS
				| MINUS
				| TIMES
				| DIVIDE'''
	p[0] = ("operator", p[1])
def p_aexpr(p):
	'aexpr : arithmetic'
	p[0] = ("aexpr",p[1])
def p_aexpr_primatives(p):
	'''aexpr : INT
			 | FLOAT
			 | funccall
			 | ID
			 | sizefunccall
			 | lenfunccall'''
	p[0] = ("aexpr",p[1])
def p_assignment(p):
	'assignment : ID EQUAL datalist SEMICOLON'
	p[0]  = ("assignment",p[1],p[3])
def p_assignment_list(p):
	'assignment : ID bracketfest EQUAL datalist'
	p[0] = ("assignment",p[1],p[2],p[4])
def p_bracketfest(p):
	'bracketfest : LSQUAREBRACKET idx RSQUAREBRACKET'
	p[0] = ("bracketfest",p[2])
def p_bracketfest_multi(p):
	'bracketfest : LSQUAREBRACKET idx RSQUAREBRACKET bracketfest'
	p[0] =("bracketfest",p[2],p[4])
def p_idx(p):
	'idx : datalist'
	p[0] =("idx",p[1])

def p_ifstatement(p):
	'ifstatement : IF LPAREN expr RPAREN LBRACKET nondefinitionblock RBRACKET'
	p[0] = ("ifstatement",p[3],p[6])
def p_nondefinitionblock(p):
	'nondefinitionblock : '
	p[0] = ("nondefinitionblock","")
def p_nondefinitionblock_multi(p):
	'nondefinitionblock : block SEMICOLON nondefinitionblock'
	p[0] = ("nondefinitionblock",p[1],p[3])
def p_block(p):
	'''block : fileopen
			 | printing
			 | ifstatement
			 | variabledeclaration
			 | commenting
			 | assignment
			 | ifelsestatement
			 | whilestatement
			 | forstatement
			 | functioncall
			 | codegenerationblock
			 | appendstatement'''
	p[0] = ("block",p[1])
def p_expr(p):
	'''expr : booleanprimitive'''
	p[0] = ("expr",p[1])
def p_expr_paren(p):
	'''expr : LPAREN booleanprimitive RPAREN'''
	p[0] = ("expr",p[2])
def p_booleanprimitive(p):
	'''booleanprimitive : TRUE
						| FALSE'''
	p[0] = ("booleanprimitive",p[1])
def p_expr_op(p):
	'expr : expr booleanop expr'
	p[0] = ("expr",p[1],p[2],p[3])
def p_expr_opparen(p):
	'expr : LBRACKET expr booleanop expr RBRACKET'
	p[0] = ("expr",p[2],p[3],p[4])
def p_booleanop(p):
	'''booleanop : OROR
				 | ANDAND
				 | EQUALEQUAL
				 | NOTEQUAL'''
def p_expr_arithmeticcomparison(p):
	'expr : arithmeticcomparison'
	p[0] = ("expr",p[1])
def p_expr_arithmeticcomparisonparen(p):
	'expr : LPAREN arithmeticcomparison RPAREN'
	p[0] = ("expr",p[2])
def p_arithmeticcomparison(p):
	'arithmeticcomparison : aexpr comparison aexpr'
	p[0] = ("arithmeticcomparison",p[1],p[2],p[3])
def p_comparison(p):
	'''comparison : LT
				  | GT
				  | GE
				  | LE
				  | EQUALEQUAL
				  | NOTEQUAl'''
	p[0] = ("comparison",p[1])
def p_expr_other(p):
	'expr : othercomparison'	
	p[0] = ("othercomparison",p[1])
def p_expr_otherparen(p):
	'expr : LPAREN othercomparison RPAREN'
	p[0] = ("othercomparison",p[2])
def p_othercomparison(p):
	'othercomparison : oexpr comparison oexpr'
	p[0] =("othercomparison",p[1],p[2],p[3])
def p_expr_complex(p):
	'expr : complexcomparison'
	p[0] = ("complexcomparison",p[1])
def p_expr_complexparen(p):
	'expr : LPAREN complexcomparison RPAREN'
	p[0] = ("complexcomparison",p[2])
def p_complexcomparison(p):
	'complexcomparison : cexpr ccomparison cexpr'
	p[0] =("complexcomparison",p[1],p[2],p[3])
def p_ccomparison(p):
	'''ccomparison : EQUALEQUAL
				   | NOTEQUAL'''
	p[0] =("ccomparison",p[1])
def p_cexpr(p):
	'cexpr : cexprlist'
	p[0] =("cexpr",p[1])
def p_cexpr_paren(p):
	'cexpr : LPAREN cexprlist RPAREN'
	p[0] = ("cexpr",p[2])
def p_cexprlist(p):
	'''cexprlist : tuplevalue
				 | listvalue
				 | dictvalue
				 | rangefunccall'''
	p[0] = ("cexprlist",p[1])
def p_oexpr(p):
	'oexpr : oexprlist'
	p[0] =("oexpr",p[1])
def p_oexpr_paren(p):
	'oexpr : LPAREN oexprlist RPAREN'
	p[0] = ("oexpr",p[2])
def p_oexprlist(p):
	'''oexprlist : ID
				 | stringdata
				 | funccall
				 | sizefunccall
				 | lenfunccall'''
	p[0] = ("oexprlist",p[1])

def p_codeblock_assignment(p):
	'codeblock : assignment'
	p[0] = ("codeblock",p[1])
def p_codeblock_ifstatement(p):
	'codeblock : ifstatement'
	p[0] = ("codeblock",p[1])
def p_codeblock_ifelsestatement(p):
	'codeblock : ifelsestatement'
	p[0] = ("codeblock",p[1])
def p_ifelsestatement(p):
	'ifelsestatement : IF LPAREN expr RPAREN LBRACKET nondefinitionblock RBRACKET ELSE LBRACKET nondefinitionblock RBRACKET'
	p[0] = ("ifelsestatement",p[3],p[6],p[10])
def p_whilestatement(p):
	'whilestatement : WHILE LPAREN expr RPAREN LBRACKET nondefinitionblock RBRACKET'
	p[0] = ("whilestatement",p[3],p[6])
def p_codeblock_whilestatement(p):
	'codeblock : whilestatement'
	p[0] = ("codeblock",p[1])
def p_codeblock_forstatement(p):
	'codeblock : forstatement'
	p[0] = ("codeblock", p[1])
def p_forstatement(p):
	'forstatement : FOR ID IN alist LBRACKET nondefinitionblock RBRACKET'
	p[0] = ("forstatement",p[2],p[4],p[6])
def p_alist(p):
	'''alist : ID
			 | listvalue
			 | tuplevalue
			 | dictvalue
			 | stringdata
			 | funccall
			 | rangefunccall'''
	p[0] = ("alist",p[1])

def p_codeblock_functioncall(p):
	'codeblock : functioncall'
	p[0] = ("codeblock",p[1])
def p_funccall(p):
	'funccall : ID LPAREN arglist RPAREN'
	p[0] = ("funccall",p[1],p[3])
def p_funccall_typecasting(p):
	'funccall : castfunc LPAREN datalist RPAREN'
	p[0] = ("funccallcastfunc",p[1],p[3])
def p_castfunc(p):
	'''castfunc : INTFUNC
				| FLOATFUNC
				| STRFUNC'''
	
def p_arglist(p):
	'arglist : '
	p[0] = ("arglist","")
def p_arglist_argopts(p):
	'arglist : argopts'
	p[0] = ("arglist",p[1])
def p_argopts(p):
	'argopts : argopt'
	p[0] = ("argopts",p[1])
def p_argopts_multi(p):
	'argopts : argopt COMMA argopts'
	p[0] = ("argopts",p[1],p[3])
def p_argopt(p):
	'argopt : datalist'
	p[0] = ("argopt",p[1])
def p_functioncall(p):
	'functioncall : funccall SEMICOLON'
	p[0] = ("functioncall",p[1])
	
def p_codeblock_functiondefinition(p):
	'codeblock : functiondefinition'
	p[0] = ("codeblock",p[1])
def p_functiondefinition(p):
	'functiondefinition : alltype ID LPAREN paramlist RPAREN LBRACKET nondefinitionblock RBRACKET'
	p[0] = ("functiondefinition",p[1],p[2],p[4],p[7])
def p_alltype(p):
	'''alltype : TYPE
			   | tupletype
			   | listtype
			   | dicttype
			   | typefunccall'''
	p[0] = ("alltype",p[1])
def p_paramlist(p):
	'paramlist : '
	p[0] = ("paramlist","")
def p_paramlist_paramopts(p):
	'paramlist : paramopts'
	p[0] = ("paramlist",p[1])
def p_paramopts(p):
	'paramopts : paramopt'
	p[0] = ("paramopts",p[1])
def p_paramopts_multi(p):
	'paramopts: paramopt COMMA paramopts'
	p[0] = ("paramopts",p[1],p[3])
def p_paramopt(p):
	'paramopt : alltype ID'
	p[0] = ("paramopt",p[1],p[2])

def p_codeblock_appendstatement(p):
	'codeblock : appendstatement'
	p[0] = ("codeblock",p[1])
def p_appendstatement(p):
	'appendstatement : ID fullstop APPEND LPAREN datalist RPAREN SEMICOLON'
	p[0] = ("appendstatement",p[1],p[5])

def p_codeblock_codegenerationblock(p):
	'codeblock : codegenerationblock'
	p[0] = ("codeblock",p[1])
def p_codegenerationblock(p):
	'codegenerationblock : CODEGENERATIONBEGIN cgoptions CODEGENERATIONEND'
	p[0] =("codegenerationblock",p[2])
def p_cgoptions_optionstatements(p):
	'cgoptions : optionstatements'
	p[0] = ("cgoptions",p[1])
def p_cgoptions(p):
	'cgoptions : '
	p[0] = ("cgoptions","")
def p_optionstatements_multi(p):
	'optionstatements : optionstatement optionstatements'
	p[0] = ("optionstatements",p[1],p[2])
def p_optionstatements(p):
	'optionstatements : optionstatement'
	p[0] = ("optionstatements", p[1])
def p_optionstatement(p):
	'optionstatement : PROGPARAMETER EQUAL RHS'
	p[0] = ("optionstatement",p[1],p[3])
def p_optionstatement_declaration(p):
	'optionstatement :  variabledeclaration'
def p_optionstatement_commenting(p):
	'optionstatement : commenting'
	p[0] =("optionstatement",p[1])
def p_rhs(p):
	'rhs : rhsvalue SEMICOLON'
	p[0] = ("rhs",p[1])
def p_rhs_function(p):
	'rhs : FUNCTION LPAREN RPAREN LBRACKET nondefinitionblock RBRACKET'
	p[0] = ("rhs-function",p[5])
def p_rhsvalue(p):
	'''rhsvalue : INT
				| stringdata
				| listvalue'''
	p[0] = ("rhsvalue",p[1])

def p_sizefunccall(p):
	'sizefunccall : ID FULLSTOP SIZEFUNC LPAREN RPAREN'
	p[0] = ("sizefunccall",p[1])
def p_typefunccall(p):
	'typefunccall : ID FULLSTOP TYPEFUNC LPAREN RPAREN'
	p[0] = ("typefunccall",p[1])
def p_lenfunccall(p):
	'lenfunccall : ID FULLSTOP LENFUNC LPAREN RPAREN'
	p[0] = ("lenfunccall",p[1])

def p_rangefunccall(p):
	'rangefunccall : RANGE LPAREN data RPAREN'
	p[0] = ("rangefunccall",p[3])
def p_rangefunccall_multi(p):
	'rangefunccall : RANGE LPAREN data COMMA data RPAREN'
	p[0] = ("rangefunccall",p[3],p[5])
def p_data(p):
	'''data : INT
			| ID'''
	p[0] = ("data",p[1])
	
prog = "!=,; 89 09 57 0. 1. 9.78 \"Hello My Name is \"() hello chester for # /* */  \n boolean && else false true || open int string float"
prog = prog + " : tuple type size list append dict while import <codegeneration> </codegeneration> _length _function_set kdfad$fasdf\n"
if_check_string = "\"if\" if" 
if_check_id = "if if"
if_check_pp ="_if if"
rbracket_check_string = "\"}\" }"
rbracket_check_comment = "}"
rbracket_check_pp = "_}"
lbracket_check_string = "\"{\" {"
lbracket_check_comment = "{"
lbracket_check_pp = "_{"
equal_check  = " = == <= >= != _=  \"=\" "
equalequal_check = "<= == >= != _=="
print_check = "print \"print\" _print "
for_check = "\"for\" for _for"
in_check = "\"in\" in int _in"
fullstop_check = ".98 0.98 . \".\"_." #im here
function_check = "function \"function\" _function"
return_check = "\"return\" return _return"
lsquarebracket_check = "\"[\" [ _["
rsquarebracket_check = "\"]\" ] _]"
plus_check = "\"+\" + _+"
minus_check = "\"-\" - _- -98 -0.9"
times_check = "\"*\" * _* /**/*//*"
divide_check = "\"\ \" \ _\\" #why i'm i getting double lines
lt_check = "\"<\" < _< <codegeneration></codegeneration> <="
le_check = "\"<=\" <= _<="
gt_check = "\">\" > _> <codegeneration></codegeneration> >="
ge_check = "\">=\" >= _>="
ne_check = "\"!=\" != _!="
comma_check = "\",\" , _,"
semicolon_check = "\";\" ; _;"
int_check = "98. 9 56 0. -1. -34 0 \"6\" _89 _-9"
float_check = "-97. 90.0 97. -78.0 \"-97. 90.0 97. -78.0\" _-89.0 _89."
string_check0 = '""'
check = "\"helloworld () # /**/ && else false true || open int float boolean string \n import <codegeneration></codegeneration> list append dict while tuple type size len _len _- : range\" range"
string_check2 = "helloworld () # /**/ && else false true || open int float boolean string \n import <codegeneration></codegeneration> list append dict while tuple type size len _len _- : range "
lparen_check = "("
rparen_check = ")"
id_check = "else false true open int float boolean string import <codegeneration></codegeneration> list append dict while tuple type size len _length _- range"
hash_check = "#"
cb_check = "/*"
ce_check = "*/"
andand_check = "&&"
else_check = "_else else"
false_check = "_false false"
true_check = "_true true"
oror_check = "||"
open_check = "open _open"
type_check = "int float string boolean _int _float _string _boolean"
newline_check = "\n"
import_check = "import _import"
cgb_check = "<codegeneration>"
cge_check = "</codegeneration>"
list_check = "list _list"
append_check = "append _append"
dict_check = "dict _dict"
while_check = "while _while"
tuple_check = "tuple _tuple"
typefunc_check = "type _type"
sizefunc_check = "size _size"
lenfunc_check = "len _len"
pp_check = "_length _range"
comment_check = " : range"
colon_check = ":"
rangefunc_check = "range"
akashalexer = lex.lex()
akashalexer.input(check)
while True:
	tok = akashalexer.token()
	if not tok :break
	print tok