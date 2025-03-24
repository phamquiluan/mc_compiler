/**
 * Student name: Pham Qui Luan
 * Student ID : 1511899
 */
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::member {
def emit(self):
    tk = self.type
    if tk == UNCLOSE_STRING:       
        result = super.emit();
        raise UncloseString(result.text);
    elif tk == ILLEGAL_ESCAPE:
        result = super.emit();
        raise IllegalEscape(result.text);
    elif tk == ERROR_CHAR:
        result = super.emit();
        raise ErrorToken(result.text); 
    else:
        return super.emit();
}

options{
	language=Python3;
}

// -------------- PARSER -----------------
program: decls+ EOF;

// declaration
decls : vardecl|funcdecl;

vardecl  :vartype varid (CM varid)* SEMI;

vartype : INTTYPE|BOOLEAN|FLOATTYPE|STRING;
fultype : vartype LSB RSB |vartype|VOIDTYPE;

varid 	: ID (LSB INTLIT RSB)?;

funcdecl : fultype ID LB plist? RB block_s;

plist   : para (CM para)*;
para 	: vartype ID (LSB RSB)?;

// expr
expr  	: <assoc=right> expr2 ASS_OP expr
		| expr2;
expr2 	: <assoc=left>  expr2 OR_OP  expr3
		| expr3;
expr3 	: <assoc=left>  expr3 AND_OP expr4
		| expr4;
expr4 	: expr5 (EQUAL_OP|NOT_EQ_OP) expr5 
		| expr5;
expr5 	: expr6 (LT_OP|LE_OP|GT_OP|GE_OP) expr6
		| expr6;
expr6 	: <assoc=left> expr6 (ADD_OP|SUB_OP) expr7
		| expr7;
expr7 	: <assoc=left> expr7 (MUL_OP|MOD_OP|DIV_OP) expr8
		| expr8;
expr8 	: <assoc=right> (SUB_OP|NOT_OP) expr8
		| expr9;
expr9 	: term LSB expr RSB
		| term;
term 	: INTLIT
		| FLOATLIT
		| BOOLLIT
		| STRINGLIT 
		| LB expr RB
		| funcall
		| ID;

// stmt
stmt  	: if_s|dowhl_s|for_s|break_s|cont_s|ret_s|expr_s|block_s;

if_s	: IF LB expr RB stmt (ELSE stmt)?; 
dowhl_s : DO stmt+ WHILE expr SEMI;
for_s 	: FOR LB expr SEMI expr SEMI expr RB stmt;
break_s : BREAK SEMI;
cont_s 	: CONTINUE SEMI;
ret_s 	: RETURN expr? SEMI;
expr_s 	: expr SEMI;
funcall : ID LB (expr (CM expr)*)? RB;
block_s : LP vardecl* stmt* RP;

// ---------------- LEXER -----------------
WS  	 : [ \t\r\n\f]+  -> skip ;
BLOCK_CMT: '/*' .*? '*/' -> skip;
LINE_CMT : '//' ~[\n]*   -> skip;	

INTTYPE  : 'int' ;
FLOATTYPE: 'float';
VOIDTYPE : 'void' ;
BOOLEAN  : 'boolean';
STRING   : 'string';


FOR 	 : 'for';
WHILE 	 : 'while';
DO 		 : 'do';
BREAK    : 'break';
CONTINUE : 'continue';
IF 		 : 'if';
ELSE   	 : 'else';
RETURN   : 'return';

BOOLLIT  : 'true' | 'false';
INTLIT   : [0-9]+;
fragment DIGIT  : [0-9];
fragment EXP 	: [Ee][-]?DIGIT+;

// TODO: code here, check lai huhu :( 
FLOATLIT : DIGIT+ EXP
		 | DIGIT* '.' DIGIT+ EXP?
		 | DIGIT+ '.' DIGIT* EXP?;

fragment ESC_LIT  : '\\'[bfnrt'"\\];
STRINGLIT : '"'(~["\\]|ESC_LIT)*'"' {self.text=self.text[1:-1]};

ADD_OP : '+';
SUB_OP : '-';
MUL_OP : '*';
DIV_OP : '/';
NOT_OP : '!';
MOD_OP : '%';
ASS_OP : '=';
OR_OP  : '||';
AND_OP : '&&';
EQUAL_OP  : '=='; 
NOT_EQ_OP : '!=';
LT_OP  : '<';
LE_OP  : '<=';
GT_OP  : '>';
GE_OP  : '>=';

LB  : '(' ;
RB  : ')' ;
LP  : '{';
RP  : '}';
SEMI: ';' ;
CM  : ',';
LSB : '[';
RSB : ']';
ID       : [a-zA-Z_][a-zA-Z0-9_]*;


ERROR_CHAR: [~^#@$&`|?] { raise ErrorToken(self.text)};
UNCLOSE_STRING: '"'(~["\\]|ESC_LIT)* { raise UncloseString(self.text[1:]) }; 

ILLEGAL_ESCAPE: '"'(~[\n"\\]|ESC_LIT)*'\\'~[bfnrt'"\\]? { raise IllegalEscape(self.text[1:]) };


// doi voi 1 chuoi thi phai nhan dang luon CAP DAU NHAY "
// phai loai dau nhay trong self.text, trong python dung ab.[1:]
// unclose string khong co dong dau nhau [1:]
//
// vd: 
// "ab\r\m" (neu sau m co them ki tu thi sao ?? 
// hinh nhu la in toi m thoi)
// raise ra chuoi: abc\r\m (khong co dau nhay)
// luc tra ve token thi phai co cap dau nhay "
//
// tren python giong tren scala, chuoi co 1 nhay kep 
// thi phai viet tren 1 hang, phai co 3 dau nhay kep 
// thi moi xuong hang dc
//
// hoc bu t3 10 17 24


