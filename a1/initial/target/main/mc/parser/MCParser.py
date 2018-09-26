# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61")
        buf.write("\u012c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\3\2\3\2\6\2A\n\2\r\2\16\2B\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\7\3K\n\3\f\3\16\3N\13\3\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\5\7`\n\7\3")
        buf.write("\b\3\b\3\b\3\b\5\bf\n\b\3\t\3\t\3\t\3\t\5\tl\n\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\7\nt\n\n\f\n\16\nw\13\n\3\13\3\13\3")
        buf.write("\13\3\13\5\13}\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u0084\n\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\7\r\u008c\n\r\f\r\16\r\u008f")
        buf.write("\13\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u0097\n\16\f")
        buf.write("\16\16\16\u009a\13\16\3\17\3\17\3\17\3\17\3\17\5\17\u00a1")
        buf.write("\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00a8\n\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\7\21\u00b0\n\21\f\21\16\21\u00b3")
        buf.write("\13\21\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u00bb\n\22\f")
        buf.write("\22\16\22\u00be\13\22\3\23\3\23\3\23\5\23\u00c3\n\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\5\24\u00cb\n\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u00d7\n")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u00e1")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u00ea\n")
        buf.write("\27\3\30\3\30\6\30\u00ee\n\30\r\30\16\30\u00ef\3\30\3")
        buf.write("\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\5\34")
        buf.write("\u0108\n\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3")
        buf.write("\36\3\36\7\36\u0114\n\36\f\36\16\36\u0117\13\36\5\36\u0119")
        buf.write("\n\36\3\36\3\36\3\37\3\37\7\37\u011f\n\37\f\37\16\37\u0122")
        buf.write("\13\37\3\37\7\37\u0125\n\37\f\37\16\37\u0128\13\37\3\37")
        buf.write("\3\37\3\37\2\6\30\32 \" \2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<\2\b\4\2\6\7\t\n\3\2")
        buf.write("!\"\3\2#&\3\2\30\31\4\2\32\33\35\35\4\2\31\31\34\34\2")
        buf.write("\u0133\2@\3\2\2\2\4F\3\2\2\2\6Q\3\2\2\2\bS\3\2\2\2\nX")
        buf.write("\3\2\2\2\f_\3\2\2\2\16a\3\2\2\2\20g\3\2\2\2\22p\3\2\2")
        buf.write("\2\24x\3\2\2\2\26\u0083\3\2\2\2\30\u0085\3\2\2\2\32\u0090")
        buf.write("\3\2\2\2\34\u00a0\3\2\2\2\36\u00a7\3\2\2\2 \u00a9\3\2")
        buf.write("\2\2\"\u00b4\3\2\2\2$\u00c2\3\2\2\2&\u00ca\3\2\2\2(\u00d6")
        buf.write("\3\2\2\2*\u00e0\3\2\2\2,\u00e2\3\2\2\2.\u00eb\3\2\2\2")
        buf.write("\60\u00f5\3\2\2\2\62\u00ff\3\2\2\2\64\u0102\3\2\2\2\66")
        buf.write("\u0105\3\2\2\28\u010b\3\2\2\2:\u010e\3\2\2\2<\u011c\3")
        buf.write("\2\2\2>A\5\4\3\2?A\5\20\t\2@>\3\2\2\2@?\3\2\2\2AB\3\2")
        buf.write("\2\2B@\3\2\2\2BC\3\2\2\2CD\3\2\2\2DE\7\2\2\3E\3\3\2\2")
        buf.write("\2FG\5\6\4\2GL\5\16\b\2HI\7,\2\2IK\5\16\b\2JH\3\2\2\2")
        buf.write("KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MO\3\2\2\2NL\3\2\2\2OP\7")
        buf.write("+\2\2P\5\3\2\2\2QR\t\2\2\2R\7\3\2\2\2ST\5\6\4\2TU\7-\2")
        buf.write("\2UV\7\25\2\2VW\7.\2\2W\t\3\2\2\2XY\5\6\4\2YZ\7-\2\2Z")
        buf.write("[\7.\2\2[\13\3\2\2\2\\`\5\n\6\2]`\5\6\4\2^`\7\b\2\2_\\")
        buf.write("\3\2\2\2_]\3\2\2\2_^\3\2\2\2`\r\3\2\2\2ae\7\23\2\2bc\7")
        buf.write("-\2\2cd\7\25\2\2df\7.\2\2eb\3\2\2\2ef\3\2\2\2f\17\3\2")
        buf.write("\2\2gh\5\f\7\2hi\7\23\2\2ik\7\'\2\2jl\5\22\n\2kj\3\2\2")
        buf.write("\2kl\3\2\2\2lm\3\2\2\2mn\7(\2\2no\5<\37\2o\21\3\2\2\2")
        buf.write("pu\5\24\13\2qr\7,\2\2rt\5\24\13\2sq\3\2\2\2tw\3\2\2\2")
        buf.write("us\3\2\2\2uv\3\2\2\2v\23\3\2\2\2wu\3\2\2\2xy\5\6\4\2y")
        buf.write("|\7\23\2\2z{\7-\2\2{}\7.\2\2|z\3\2\2\2|}\3\2\2\2}\25\3")
        buf.write("\2\2\2~\177\5\30\r\2\177\u0080\7\36\2\2\u0080\u0081\5")
        buf.write("\26\f\2\u0081\u0084\3\2\2\2\u0082\u0084\5\30\r\2\u0083")
        buf.write("~\3\2\2\2\u0083\u0082\3\2\2\2\u0084\27\3\2\2\2\u0085\u0086")
        buf.write("\b\r\1\2\u0086\u0087\5\32\16\2\u0087\u008d\3\2\2\2\u0088")
        buf.write("\u0089\f\4\2\2\u0089\u008a\7\37\2\2\u008a\u008c\5\32\16")
        buf.write("\2\u008b\u0088\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008b")
        buf.write("\3\2\2\2\u008d\u008e\3\2\2\2\u008e\31\3\2\2\2\u008f\u008d")
        buf.write("\3\2\2\2\u0090\u0091\b\16\1\2\u0091\u0092\5\34\17\2\u0092")
        buf.write("\u0098\3\2\2\2\u0093\u0094\f\4\2\2\u0094\u0095\7 \2\2")
        buf.write("\u0095\u0097\5\34\17\2\u0096\u0093\3\2\2\2\u0097\u009a")
        buf.write("\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write("\33\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u009c\5\36\20\2")
        buf.write("\u009c\u009d\t\3\2\2\u009d\u009e\5\36\20\2\u009e\u00a1")
        buf.write("\3\2\2\2\u009f\u00a1\5\36\20\2\u00a0\u009b\3\2\2\2\u00a0")
        buf.write("\u009f\3\2\2\2\u00a1\35\3\2\2\2\u00a2\u00a3\5 \21\2\u00a3")
        buf.write("\u00a4\t\4\2\2\u00a4\u00a5\5 \21\2\u00a5\u00a8\3\2\2\2")
        buf.write("\u00a6\u00a8\5 \21\2\u00a7\u00a2\3\2\2\2\u00a7\u00a6\3")
        buf.write("\2\2\2\u00a8\37\3\2\2\2\u00a9\u00aa\b\21\1\2\u00aa\u00ab")
        buf.write("\5\"\22\2\u00ab\u00b1\3\2\2\2\u00ac\u00ad\f\4\2\2\u00ad")
        buf.write("\u00ae\t\5\2\2\u00ae\u00b0\5\"\22\2\u00af\u00ac\3\2\2")
        buf.write("\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2")
        buf.write("\3\2\2\2\u00b2!\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5")
        buf.write("\b\22\1\2\u00b5\u00b6\5$\23\2\u00b6\u00bc\3\2\2\2\u00b7")
        buf.write("\u00b8\f\4\2\2\u00b8\u00b9\t\6\2\2\u00b9\u00bb\5$\23\2")
        buf.write("\u00ba\u00b7\3\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00ba\3")
        buf.write("\2\2\2\u00bc\u00bd\3\2\2\2\u00bd#\3\2\2\2\u00be\u00bc")
        buf.write("\3\2\2\2\u00bf\u00c0\t\7\2\2\u00c0\u00c3\5$\23\2\u00c1")
        buf.write("\u00c3\5&\24\2\u00c2\u00bf\3\2\2\2\u00c2\u00c1\3\2\2\2")
        buf.write("\u00c3%\3\2\2\2\u00c4\u00c5\5(\25\2\u00c5\u00c6\7-\2\2")
        buf.write("\u00c6\u00c7\5\26\f\2\u00c7\u00c8\7.\2\2\u00c8\u00cb\3")
        buf.write("\2\2\2\u00c9\u00cb\5(\25\2\u00ca\u00c4\3\2\2\2\u00ca\u00c9")
        buf.write("\3\2\2\2\u00cb\'\3\2\2\2\u00cc\u00d7\7\23\2\2\u00cd\u00d7")
        buf.write("\7\25\2\2\u00ce\u00d7\7\26\2\2\u00cf\u00d7\7\24\2\2\u00d0")
        buf.write("\u00d7\7\27\2\2\u00d1\u00d2\7\'\2\2\u00d2\u00d3\5\26\f")
        buf.write("\2\u00d3\u00d4\7(\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d7")
        buf.write("\5:\36\2\u00d6\u00cc\3\2\2\2\u00d6\u00cd\3\2\2\2\u00d6")
        buf.write("\u00ce\3\2\2\2\u00d6\u00cf\3\2\2\2\u00d6\u00d0\3\2\2\2")
        buf.write("\u00d6\u00d1\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7)\3\2\2")
        buf.write("\2\u00d8\u00e1\5,\27\2\u00d9\u00e1\5.\30\2\u00da\u00e1")
        buf.write("\5\60\31\2\u00db\u00e1\5\62\32\2\u00dc\u00e1\5\64\33\2")
        buf.write("\u00dd\u00e1\5\66\34\2\u00de\u00e1\58\35\2\u00df\u00e1")
        buf.write("\5<\37\2\u00e0\u00d8\3\2\2\2\u00e0\u00d9\3\2\2\2\u00e0")
        buf.write("\u00da\3\2\2\2\u00e0\u00db\3\2\2\2\u00e0\u00dc\3\2\2\2")
        buf.write("\u00e0\u00dd\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00df\3")
        buf.write("\2\2\2\u00e1+\3\2\2\2\u00e2\u00e3\7\20\2\2\u00e3\u00e4")
        buf.write("\7\'\2\2\u00e4\u00e5\5\26\f\2\u00e5\u00e6\7(\2\2\u00e6")
        buf.write("\u00e9\5*\26\2\u00e7\u00e8\7\21\2\2\u00e8\u00ea\5*\26")
        buf.write("\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea-\3\2")
        buf.write("\2\2\u00eb\u00ed\7\r\2\2\u00ec\u00ee\5*\26\2\u00ed\u00ec")
        buf.write("\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2\7\f\2\2")
        buf.write("\u00f2\u00f3\5\26\f\2\u00f3\u00f4\7+\2\2\u00f4/\3\2\2")
        buf.write("\2\u00f5\u00f6\7\13\2\2\u00f6\u00f7\7\'\2\2\u00f7\u00f8")
        buf.write("\5\26\f\2\u00f8\u00f9\7+\2\2\u00f9\u00fa\5\26\f\2\u00fa")
        buf.write("\u00fb\7+\2\2\u00fb\u00fc\5\26\f\2\u00fc\u00fd\7(\2\2")
        buf.write("\u00fd\u00fe\5*\26\2\u00fe\61\3\2\2\2\u00ff\u0100\7\16")
        buf.write("\2\2\u0100\u0101\7+\2\2\u0101\63\3\2\2\2\u0102\u0103\7")
        buf.write("\17\2\2\u0103\u0104\7+\2\2\u0104\65\3\2\2\2\u0105\u0107")
        buf.write("\7\22\2\2\u0106\u0108\5\26\f\2\u0107\u0106\3\2\2\2\u0107")
        buf.write("\u0108\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010a\7+\2\2")
        buf.write("\u010a\67\3\2\2\2\u010b\u010c\5\26\f\2\u010c\u010d\7+")
        buf.write("\2\2\u010d9\3\2\2\2\u010e\u010f\7\23\2\2\u010f\u0118\7")
        buf.write("\'\2\2\u0110\u0115\5\26\f\2\u0111\u0112\7,\2\2\u0112\u0114")
        buf.write("\5\26\f\2\u0113\u0111\3\2\2\2\u0114\u0117\3\2\2\2\u0115")
        buf.write("\u0113\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0119\3\2\2\2")
        buf.write("\u0117\u0115\3\2\2\2\u0118\u0110\3\2\2\2\u0118\u0119\3")
        buf.write("\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\7(\2\2\u011b;\3")
        buf.write("\2\2\2\u011c\u0120\7)\2\2\u011d\u011f\5\4\3\2\u011e\u011d")
        buf.write("\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2\u0120")
        buf.write("\u0121\3\2\2\2\u0121\u0126\3\2\2\2\u0122\u0120\3\2\2\2")
        buf.write("\u0123\u0125\5*\26\2\u0124\u0123\3\2\2\2\u0125\u0128\3")
        buf.write("\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0129")
        buf.write("\3\2\2\2\u0128\u0126\3\2\2\2\u0129\u012a\7*\2\2\u012a")
        buf.write("=\3\2\2\2\34@BL_eku|\u0083\u008d\u0098\u00a0\u00a7\u00b1")
        buf.write("\u00bc\u00c2\u00ca\u00d6\u00e0\u00e9\u00ef\u0107\u0115")
        buf.write("\u0118\u0120\u0126")
        return buf.getvalue()


class MCParser ( Parser ):

    grammarFileName = "MC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'int'", "'float'", "'void'", "'boolean'", "'string'", 
                     "'for'", "'while'", "'do'", "'break'", "'continue'", 
                     "'if'", "'else'", "'return'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'!'", "'%'", "'='", "'||'", "'&&'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'('", 
                     "')'", "'{'", "'}'", "';'", "','", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "WS", "BLOCK_CMT", "LINE_CMT", "INTTYPE", 
                      "FLOATTYPE", "VOIDTYPE", "BOOLEAN", "STRING", "FOR", 
                      "WHILE", "DO", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "RETURN", "ID", "BOOLLIT", "INTLIT", "FLOATLIT", "STRINGLIT", 
                      "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", 
                      "MOD_OP", "ASS_OP", "OR_OP", "AND_OP", "EQUAL_OP", 
                      "NOT_EQ_OP", "LT_OP", "LE_OP", "GT_OP", "GE_OP", "LB", 
                      "RB", "LP", "RP", "SEMI", "CM", "LSB", "RSB", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_vardec = 1
    RULE_vartype = 2
    RULE_arrtype = 3
    RULE_arptype = 4
    RULE_fultype = 5
    RULE_varid = 6
    RULE_funcdec = 7
    RULE_plist = 8
    RULE_para = 9
    RULE_expr = 10
    RULE_expr2 = 11
    RULE_expr3 = 12
    RULE_expr4 = 13
    RULE_expr5 = 14
    RULE_expr6 = 15
    RULE_expr7 = 16
    RULE_expr8 = 17
    RULE_expr9 = 18
    RULE_term = 19
    RULE_stmt = 20
    RULE_if_s = 21
    RULE_dowhl_s = 22
    RULE_for_s = 23
    RULE_break_s = 24
    RULE_cont_s = 25
    RULE_ret_s = 26
    RULE_expr_s = 27
    RULE_funcall = 28
    RULE_block_s = 29

    ruleNames =  [ "program", "vardec", "vartype", "arrtype", "arptype", 
                   "fultype", "varid", "funcdec", "plist", "para", "expr", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "expr7", 
                   "expr8", "expr9", "term", "stmt", "if_s", "dowhl_s", 
                   "for_s", "break_s", "cont_s", "ret_s", "expr_s", "funcall", 
                   "block_s" ]

    EOF = Token.EOF
    WS=1
    BLOCK_CMT=2
    LINE_CMT=3
    INTTYPE=4
    FLOATTYPE=5
    VOIDTYPE=6
    BOOLEAN=7
    STRING=8
    FOR=9
    WHILE=10
    DO=11
    BREAK=12
    CONTINUE=13
    IF=14
    ELSE=15
    RETURN=16
    ID=17
    BOOLLIT=18
    INTLIT=19
    FLOATLIT=20
    STRINGLIT=21
    ADD_OP=22
    SUB_OP=23
    MUL_OP=24
    DIV_OP=25
    NOT_OP=26
    MOD_OP=27
    ASS_OP=28
    OR_OP=29
    AND_OP=30
    EQUAL_OP=31
    NOT_EQ_OP=32
    LT_OP=33
    LE_OP=34
    GT_OP=35
    GE_OP=36
    LB=37
    RB=38
    LP=39
    RP=40
    SEMI=41
    CM=42
    LSB=43
    RSB=44
    ERROR_CHAR=45
    UNCLOSE_STRING=46
    ILLEGAL_ESCAPE=47

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MCParser.EOF, 0)

        def vardec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VardecContext)
            else:
                return self.getTypedRuleContext(MCParser.VardecContext,i)


        def funcdec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.FuncdecContext)
            else:
                return self.getTypedRuleContext(MCParser.FuncdecContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 60
                    self.vardec()
                    pass

                elif la_ == 2:
                    self.state = 61
                    self.funcdec()
                    pass


                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.VOIDTYPE) | (1 << MCParser.BOOLEAN) | (1 << MCParser.STRING))) != 0)):
                    break

            self.state = 66
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VardecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(MCParser.VartypeContext,0)


        def varid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VaridContext)
            else:
                return self.getTypedRuleContext(MCParser.VaridContext,i)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_vardec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardec" ):
                return visitor.visitVardec(self)
            else:
                return visitor.visitChildren(self)




    def vardec(self):

        localctx = MCParser.VardecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vardec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.vartype()
            self.state = 69
            self.varid()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 70
                self.match(MCParser.CM)
                self.state = 71
                self.varid()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VartypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MCParser.INTTYPE, 0)

        def BOOLEAN(self):
            return self.getToken(MCParser.BOOLEAN, 0)

        def FLOATTYPE(self):
            return self.getToken(MCParser.FLOATTYPE, 0)

        def STRING(self):
            return self.getToken(MCParser.STRING, 0)

        def getRuleIndex(self):
            return MCParser.RULE_vartype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype" ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = MCParser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.BOOLEAN) | (1 << MCParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArrtypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(MCParser.VartypeContext,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_arrtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrtype" ):
                return visitor.visitArrtype(self)
            else:
                return visitor.visitChildren(self)




    def arrtype(self):

        localctx = MCParser.ArrtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arrtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.vartype()
            self.state = 82
            self.match(MCParser.LSB)
            self.state = 83
            self.match(MCParser.INTLIT)
            self.state = 84
            self.match(MCParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArptypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(MCParser.VartypeContext,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_arptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArptype" ):
                return visitor.visitArptype(self)
            else:
                return visitor.visitChildren(self)




    def arptype(self):

        localctx = MCParser.ArptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arptype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.vartype()
            self.state = 87
            self.match(MCParser.LSB)
            self.state = 88
            self.match(MCParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FultypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arptype(self):
            return self.getTypedRuleContext(MCParser.ArptypeContext,0)


        def vartype(self):
            return self.getTypedRuleContext(MCParser.VartypeContext,0)


        def VOIDTYPE(self):
            return self.getToken(MCParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_fultype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFultype" ):
                return visitor.visitFultype(self)
            else:
                return visitor.visitChildren(self)




    def fultype(self):

        localctx = MCParser.FultypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fultype)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.arptype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.vartype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.match(MCParser.VOIDTYPE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VaridContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_varid

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarid" ):
                return visitor.visitVarid(self)
            else:
                return visitor.visitChildren(self)




    def varid(self):

        localctx = MCParser.VaridContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_varid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(MCParser.ID)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LSB:
                self.state = 96
                self.match(MCParser.LSB)
                self.state = 97
                self.match(MCParser.INTLIT)
                self.state = 98
                self.match(MCParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncdecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fultype(self):
            return self.getTypedRuleContext(MCParser.FultypeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def block_s(self):
            return self.getTypedRuleContext(MCParser.Block_sContext,0)


        def plist(self):
            return self.getTypedRuleContext(MCParser.PlistContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_funcdec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdec" ):
                return visitor.visitFuncdec(self)
            else:
                return visitor.visitChildren(self)




    def funcdec(self):

        localctx = MCParser.FuncdecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcdec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.fultype()
            self.state = 102
            self.match(MCParser.ID)
            self.state = 103
            self.match(MCParser.LB)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.BOOLEAN) | (1 << MCParser.STRING))) != 0):
                self.state = 104
                self.plist()


            self.state = 107
            self.match(MCParser.RB)
            self.state = 108
            self.block_s()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PlistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ParaContext)
            else:
                return self.getTypedRuleContext(MCParser.ParaContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_plist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlist" ):
                return visitor.visitPlist(self)
            else:
                return visitor.visitChildren(self)




    def plist(self):

        localctx = MCParser.PlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_plist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.para()
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 111
                self.match(MCParser.CM)
                self.state = 112
                self.para()
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(MCParser.VartypeContext,0)


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_para

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPara" ):
                return visitor.visitPara(self)
            else:
                return visitor.visitChildren(self)




    def para(self):

        localctx = MCParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.vartype()
            self.state = 119
            self.match(MCParser.ID)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LSB:
                self.state = 120
                self.match(MCParser.LSB)
                self.state = 121
                self.match(MCParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MCParser.Expr2Context,0)


        def ASS_OP(self):
            return self.getToken(MCParser.ASS_OP, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MCParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.expr2(0)
                self.state = 125
                self.match(MCParser.ASS_OP)
                self.state = 126
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MCParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MCParser.Expr2Context,0)


        def OR_OP(self):
            return self.getToken(MCParser.OR_OP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 134
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 135
                    self.match(MCParser.OR_OP)
                    self.state = 136
                    self.expr3(0) 
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MCParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MCParser.Expr3Context,0)


        def AND_OP(self):
            return self.getToken(MCParser.AND_OP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 145
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 146
                    self.match(MCParser.AND_OP)
                    self.state = 147
                    self.expr4() 
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Expr5Context)
            else:
                return self.getTypedRuleContext(MCParser.Expr5Context,i)


        def EQUAL_OP(self):
            return self.getToken(MCParser.EQUAL_OP, 0)

        def NOT_EQ_OP(self):
            return self.getToken(MCParser.NOT_EQ_OP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)




    def expr4(self):

        localctx = MCParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr4)
        self._la = 0 # Token type
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.expr5()
                self.state = 154
                _la = self._input.LA(1)
                if not(_la==MCParser.EQUAL_OP or _la==MCParser.NOT_EQ_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 155
                self.expr5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.expr5()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.Expr6Context)
            else:
                return self.getTypedRuleContext(MCParser.Expr6Context,i)


        def LT_OP(self):
            return self.getToken(MCParser.LT_OP, 0)

        def LE_OP(self):
            return self.getToken(MCParser.LE_OP, 0)

        def GT_OP(self):
            return self.getToken(MCParser.GT_OP, 0)

        def GE_OP(self):
            return self.getToken(MCParser.GE_OP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MCParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.expr6(0)
                self.state = 161
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LT_OP) | (1 << MCParser.LE_OP) | (1 << MCParser.GT_OP) | (1 << MCParser.GE_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 162
                self.expr6(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.expr6(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MCParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MCParser.Expr6Context,0)


        def ADD_OP(self):
            return self.getToken(MCParser.ADD_OP, 0)

        def SUB_OP(self):
            return self.getToken(MCParser.SUB_OP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.expr7(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 170
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 171
                    _la = self._input.LA(1)
                    if not(_la==MCParser.ADD_OP or _la==MCParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 172
                    self.expr7(0) 
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(MCParser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(MCParser.Expr7Context,0)


        def MUL_OP(self):
            return self.getToken(MCParser.MUL_OP, 0)

        def MOD_OP(self):
            return self.getToken(MCParser.MOD_OP, 0)

        def DIV_OP(self):
            return self.getToken(MCParser.DIV_OP, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MCParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr7, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 181
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 182
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MUL_OP) | (1 << MCParser.DIV_OP) | (1 << MCParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 183
                    self.expr8() 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Expr8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(MCParser.Expr8Context,0)


        def SUB_OP(self):
            return self.getToken(MCParser.SUB_OP, 0)

        def NOT_OP(self):
            return self.getToken(MCParser.NOT_OP, 0)

        def expr9(self):
            return self.getTypedRuleContext(MCParser.Expr9Context,0)


        def getRuleIndex(self):
            return MCParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = MCParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expr8)
        self._la = 0 # Token type
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.SUB_OP, MCParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                _la = self._input.LA(1)
                if not(_la==MCParser.SUB_OP or _la==MCParser.NOT_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 190
                self.expr8()
                pass
            elif token in [MCParser.ID, MCParser.BOOLLIT, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRINGLIT, MCParser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.expr9()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(MCParser.TermContext,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = MCParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expr9)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.term()
                self.state = 195
                self.match(MCParser.LSB)
                self.state = 196
                self.expr()
                self.state = 197
                self.match(MCParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def INTLIT(self):
            return self.getToken(MCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MCParser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MCParser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MCParser.STRINGLIT, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def funcall(self):
            return self.getTypedRuleContext(MCParser.FuncallContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MCParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_term)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(MCParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(MCParser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.match(MCParser.FLOATLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 205
                self.match(MCParser.BOOLLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 206
                self.match(MCParser.STRINGLIT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 207
                self.match(MCParser.LB)
                self.state = 208
                self.expr()
                self.state = 209
                self.match(MCParser.RB)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 211
                self.funcall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_s(self):
            return self.getTypedRuleContext(MCParser.If_sContext,0)


        def dowhl_s(self):
            return self.getTypedRuleContext(MCParser.Dowhl_sContext,0)


        def for_s(self):
            return self.getTypedRuleContext(MCParser.For_sContext,0)


        def break_s(self):
            return self.getTypedRuleContext(MCParser.Break_sContext,0)


        def cont_s(self):
            return self.getTypedRuleContext(MCParser.Cont_sContext,0)


        def ret_s(self):
            return self.getTypedRuleContext(MCParser.Ret_sContext,0)


        def expr_s(self):
            return self.getTypedRuleContext(MCParser.Expr_sContext,0)


        def block_s(self):
            return self.getTypedRuleContext(MCParser.Block_sContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_stmt)
        try:
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.if_s()
                pass
            elif token in [MCParser.DO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.dowhl_s()
                pass
            elif token in [MCParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.for_s()
                pass
            elif token in [MCParser.BREAK]:
                self.enterOuterAlt(localctx, 4)
                self.state = 217
                self.break_s()
                pass
            elif token in [MCParser.CONTINUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 218
                self.cont_s()
                pass
            elif token in [MCParser.RETURN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 219
                self.ret_s()
                pass
            elif token in [MCParser.ID, MCParser.BOOLLIT, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRINGLIT, MCParser.SUB_OP, MCParser.NOT_OP, MCParser.LB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 220
                self.expr_s()
                pass
            elif token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 221
                self.block_s()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MCParser.IF, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(MCParser.ELSE, 0)

        def getRuleIndex(self):
            return MCParser.RULE_if_s

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_s" ):
                return visitor.visitIf_s(self)
            else:
                return visitor.visitChildren(self)




    def if_s(self):

        localctx = MCParser.If_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_if_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MCParser.IF)
            self.state = 225
            self.match(MCParser.LB)
            self.state = 226
            self.expr()
            self.state = 227
            self.match(MCParser.RB)
            self.state = 228
            self.stmt()
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 229
                self.match(MCParser.ELSE)
                self.state = 230
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dowhl_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MCParser.DO, 0)

        def WHILE(self):
            return self.getToken(MCParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_dowhl_s

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDowhl_s" ):
                return visitor.visitDowhl_s(self)
            else:
                return visitor.visitChildren(self)




    def dowhl_s(self):

        localctx = MCParser.Dowhl_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_dowhl_s)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MCParser.DO)
            self.state = 235 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 234
                self.stmt()
                self.state = 237 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.FOR) | (1 << MCParser.DO) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.IF) | (1 << MCParser.RETURN) | (1 << MCParser.ID) | (1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LB) | (1 << MCParser.LP))) != 0)):
                    break

            self.state = 239
            self.match(MCParser.WHILE)
            self.state = 240
            self.expr()
            self.state = 241
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MCParser.FOR, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MCParser.ExprContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.SEMI)
            else:
                return self.getToken(MCParser.SEMI, i)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def stmt(self):
            return self.getTypedRuleContext(MCParser.StmtContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_for_s

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_s" ):
                return visitor.visitFor_s(self)
            else:
                return visitor.visitChildren(self)




    def for_s(self):

        localctx = MCParser.For_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_for_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(MCParser.FOR)
            self.state = 244
            self.match(MCParser.LB)
            self.state = 245
            self.expr()
            self.state = 246
            self.match(MCParser.SEMI)
            self.state = 247
            self.expr()
            self.state = 248
            self.match(MCParser.SEMI)
            self.state = 249
            self.expr()
            self.state = 250
            self.match(MCParser.RB)
            self.state = 251
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Break_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MCParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_break_s

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_s" ):
                return visitor.visitBreak_s(self)
            else:
                return visitor.visitChildren(self)




    def break_s(self):

        localctx = MCParser.Break_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_break_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(MCParser.BREAK)
            self.state = 254
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cont_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MCParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_cont_s

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCont_s" ):
                return visitor.visitCont_s(self)
            else:
                return visitor.visitChildren(self)




    def cont_s(self):

        localctx = MCParser.Cont_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_cont_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(MCParser.CONTINUE)
            self.state = 257
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ret_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MCParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_ret_s

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet_s" ):
                return visitor.visitRet_s(self)
            else:
                return visitor.visitChildren(self)




    def ret_s(self):

        localctx = MCParser.Ret_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ret_s)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(MCParser.RETURN)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.ID) | (1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LB))) != 0):
                self.state = 260
                self.expr()


            self.state = 263
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expr_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MCParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(MCParser.SEMI, 0)

        def getRuleIndex(self):
            return MCParser.RULE_expr_s

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_s" ):
                return visitor.visitExpr_s(self)
            else:
                return visitor.visitChildren(self)




    def expr_s(self):

        localctx = MCParser.Expr_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expr_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.expr()
            self.state = 266
            self.match(MCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def LB(self):
            return self.getToken(MCParser.LB, 0)

        def RB(self):
            return self.getToken(MCParser.RB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.ExprContext)
            else:
                return self.getTypedRuleContext(MCParser.ExprContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(MCParser.CM)
            else:
                return self.getToken(MCParser.CM, i)

        def getRuleIndex(self):
            return MCParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MCParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(MCParser.ID)
            self.state = 269
            self.match(MCParser.LB)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.ID) | (1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LB))) != 0):
                self.state = 270
                self.expr()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MCParser.CM:
                    self.state = 271
                    self.match(MCParser.CM)
                    self.state = 272
                    self.expr()
                    self.state = 277
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 280
            self.match(MCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Block_sContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(MCParser.LP, 0)

        def RP(self):
            return self.getToken(MCParser.RP, 0)

        def vardec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VardecContext)
            else:
                return self.getTypedRuleContext(MCParser.VardecContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.StmtContext)
            else:
                return self.getTypedRuleContext(MCParser.StmtContext,i)


        def getRuleIndex(self):
            return MCParser.RULE_block_s

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_s" ):
                return visitor.visitBlock_s(self)
            else:
                return visitor.visitChildren(self)




    def block_s(self):

        localctx = MCParser.Block_sContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_block_s)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(MCParser.LP)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.BOOLEAN) | (1 << MCParser.STRING))) != 0):
                self.state = 283
                self.vardec()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.FOR) | (1 << MCParser.DO) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.IF) | (1 << MCParser.RETURN) | (1 << MCParser.ID) | (1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LB) | (1 << MCParser.LP))) != 0):
                self.state = 289
                self.stmt()
                self.state = 294
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 295
            self.match(MCParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expr2_sempred
        self._predicates[12] = self.expr3_sempred
        self._predicates[15] = self.expr6_sempred
        self._predicates[16] = self.expr7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




