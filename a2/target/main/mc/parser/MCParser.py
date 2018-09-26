# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\61")
        buf.write("\u0127\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\3\2\6\2>\n\2\r\2\16\2?\3\2\3\2\3\3\3\3\5\3F\n\3\3\4\3")
        buf.write("\4\3\4\3\4\7\4L\n\4\f\4\16\4O\13\4\3\4\3\4\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\5\6[\n\6\3\7\3\7\3\7\3\7\5\7a\n\7")
        buf.write("\3\b\3\b\3\b\3\b\5\bg\n\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t")
        buf.write("o\n\t\f\t\16\tr\13\t\3\n\3\n\3\n\3\n\5\nx\n\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\5\13\177\n\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\7\f\u0087\n\f\f\f\16\f\u008a\13\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\7\r\u0092\n\r\f\r\16\r\u0095\13\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u009c\n\16\3\17\3\17\3\17\3\17\3\17\5")
        buf.write("\17\u00a3\n\17\3\20\3\20\3\20\3\20\3\20\3\20\7\20\u00ab")
        buf.write("\n\20\f\20\16\20\u00ae\13\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\7\21\u00b6\n\21\f\21\16\21\u00b9\13\21\3\22\3\22")
        buf.write("\3\22\5\22\u00be\n\22\3\23\3\23\3\23\3\23\3\23\3\23\5")
        buf.write("\23\u00c6\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u00d2\n\24\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u00dc\n\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\5\26\u00e5\n\26\3\27\3\27\6\27\u00e9\n\27\r")
        buf.write("\27\16\27\u00ea\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\5\33\u0103\n\33\3\33\3\33\3\34\3\34\3")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\7\35\u010f\n\35\f\35\16\35")
        buf.write("\u0112\13\35\5\35\u0114\n\35\3\35\3\35\3\36\3\36\7\36")
        buf.write("\u011a\n\36\f\36\16\36\u011d\13\36\3\36\7\36\u0120\n\36")
        buf.write("\f\36\16\36\u0123\13\36\3\36\3\36\3\36\2\6\26\30\36 \37")
        buf.write("\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:\2\b\4\2\6\7\t\n\3\2 !\3\2\"%\3\2\27\30\4\2\31")
        buf.write("\32\34\34\4\2\30\30\33\33\2\u012f\2=\3\2\2\2\4E\3\2\2")
        buf.write("\2\6G\3\2\2\2\bR\3\2\2\2\nZ\3\2\2\2\f\\\3\2\2\2\16b\3")
        buf.write("\2\2\2\20k\3\2\2\2\22s\3\2\2\2\24~\3\2\2\2\26\u0080\3")
        buf.write("\2\2\2\30\u008b\3\2\2\2\32\u009b\3\2\2\2\34\u00a2\3\2")
        buf.write("\2\2\36\u00a4\3\2\2\2 \u00af\3\2\2\2\"\u00bd\3\2\2\2$")
        buf.write("\u00c5\3\2\2\2&\u00d1\3\2\2\2(\u00db\3\2\2\2*\u00dd\3")
        buf.write("\2\2\2,\u00e6\3\2\2\2.\u00f0\3\2\2\2\60\u00fa\3\2\2\2")
        buf.write("\62\u00fd\3\2\2\2\64\u0100\3\2\2\2\66\u0106\3\2\2\28\u0109")
        buf.write("\3\2\2\2:\u0117\3\2\2\2<>\5\4\3\2=<\3\2\2\2>?\3\2\2\2")
        buf.write("?=\3\2\2\2?@\3\2\2\2@A\3\2\2\2AB\7\2\2\3B\3\3\2\2\2CF")
        buf.write("\5\6\4\2DF\5\16\b\2EC\3\2\2\2ED\3\2\2\2F\5\3\2\2\2GH\5")
        buf.write("\b\5\2HM\5\f\7\2IJ\7+\2\2JL\5\f\7\2KI\3\2\2\2LO\3\2\2")
        buf.write("\2MK\3\2\2\2MN\3\2\2\2NP\3\2\2\2OM\3\2\2\2PQ\7*\2\2Q\7")
        buf.write("\3\2\2\2RS\t\2\2\2S\t\3\2\2\2TU\5\b\5\2UV\7,\2\2VW\7-")
        buf.write("\2\2W[\3\2\2\2X[\5\b\5\2Y[\7\b\2\2ZT\3\2\2\2ZX\3\2\2\2")
        buf.write("ZY\3\2\2\2[\13\3\2\2\2\\`\7.\2\2]^\7,\2\2^_\7\24\2\2_")
        buf.write("a\7-\2\2`]\3\2\2\2`a\3\2\2\2a\r\3\2\2\2bc\5\n\6\2cd\7")
        buf.write(".\2\2df\7&\2\2eg\5\20\t\2fe\3\2\2\2fg\3\2\2\2gh\3\2\2")
        buf.write("\2hi\7\'\2\2ij\5:\36\2j\17\3\2\2\2kp\5\22\n\2lm\7+\2\2")
        buf.write("mo\5\22\n\2nl\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2q\21")
        buf.write("\3\2\2\2rp\3\2\2\2st\5\b\5\2tw\7.\2\2uv\7,\2\2vx\7-\2")
        buf.write("\2wu\3\2\2\2wx\3\2\2\2x\23\3\2\2\2yz\5\26\f\2z{\7\35\2")
        buf.write("\2{|\5\24\13\2|\177\3\2\2\2}\177\5\26\f\2~y\3\2\2\2~}")
        buf.write("\3\2\2\2\177\25\3\2\2\2\u0080\u0081\b\f\1\2\u0081\u0082")
        buf.write("\5\30\r\2\u0082\u0088\3\2\2\2\u0083\u0084\f\4\2\2\u0084")
        buf.write("\u0085\7\36\2\2\u0085\u0087\5\30\r\2\u0086\u0083\3\2\2")
        buf.write("\2\u0087\u008a\3\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089")
        buf.write("\3\2\2\2\u0089\27\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u008c")
        buf.write("\b\r\1\2\u008c\u008d\5\32\16\2\u008d\u0093\3\2\2\2\u008e")
        buf.write("\u008f\f\4\2\2\u008f\u0090\7\37\2\2\u0090\u0092\5\32\16")
        buf.write("\2\u0091\u008e\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091")
        buf.write("\3\2\2\2\u0093\u0094\3\2\2\2\u0094\31\3\2\2\2\u0095\u0093")
        buf.write("\3\2\2\2\u0096\u0097\5\34\17\2\u0097\u0098\t\3\2\2\u0098")
        buf.write("\u0099\5\34\17\2\u0099\u009c\3\2\2\2\u009a\u009c\5\34")
        buf.write("\17\2\u009b\u0096\3\2\2\2\u009b\u009a\3\2\2\2\u009c\33")
        buf.write("\3\2\2\2\u009d\u009e\5\36\20\2\u009e\u009f\t\4\2\2\u009f")
        buf.write("\u00a0\5\36\20\2\u00a0\u00a3\3\2\2\2\u00a1\u00a3\5\36")
        buf.write("\20\2\u00a2\u009d\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\35")
        buf.write("\3\2\2\2\u00a4\u00a5\b\20\1\2\u00a5\u00a6\5 \21\2\u00a6")
        buf.write("\u00ac\3\2\2\2\u00a7\u00a8\f\4\2\2\u00a8\u00a9\t\5\2\2")
        buf.write("\u00a9\u00ab\5 \21\2\u00aa\u00a7\3\2\2\2\u00ab\u00ae\3")
        buf.write("\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\37")
        buf.write("\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0\b\21\1\2\u00b0")
        buf.write("\u00b1\5\"\22\2\u00b1\u00b7\3\2\2\2\u00b2\u00b3\f\4\2")
        buf.write("\2\u00b3\u00b4\t\6\2\2\u00b4\u00b6\5\"\22\2\u00b5\u00b2")
        buf.write("\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8!\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba")
        buf.write("\u00bb\t\7\2\2\u00bb\u00be\5\"\22\2\u00bc\u00be\5$\23")
        buf.write("\2\u00bd\u00ba\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be#\3\2")
        buf.write("\2\2\u00bf\u00c0\5&\24\2\u00c0\u00c1\7,\2\2\u00c1\u00c2")
        buf.write("\5\24\13\2\u00c2\u00c3\7-\2\2\u00c3\u00c6\3\2\2\2\u00c4")
        buf.write("\u00c6\5&\24\2\u00c5\u00bf\3\2\2\2\u00c5\u00c4\3\2\2\2")
        buf.write("\u00c6%\3\2\2\2\u00c7\u00d2\7\24\2\2\u00c8\u00d2\7\25")
        buf.write("\2\2\u00c9\u00d2\7\23\2\2\u00ca\u00d2\7\26\2\2\u00cb\u00cc")
        buf.write("\7&\2\2\u00cc\u00cd\5\24\13\2\u00cd\u00ce\7\'\2\2\u00ce")
        buf.write("\u00d2\3\2\2\2\u00cf\u00d2\58\35\2\u00d0\u00d2\7.\2\2")
        buf.write("\u00d1\u00c7\3\2\2\2\u00d1\u00c8\3\2\2\2\u00d1\u00c9\3")
        buf.write("\2\2\2\u00d1\u00ca\3\2\2\2\u00d1\u00cb\3\2\2\2\u00d1\u00cf")
        buf.write("\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\'\3\2\2\2\u00d3\u00dc")
        buf.write("\5*\26\2\u00d4\u00dc\5,\27\2\u00d5\u00dc\5.\30\2\u00d6")
        buf.write("\u00dc\5\60\31\2\u00d7\u00dc\5\62\32\2\u00d8\u00dc\5\64")
        buf.write("\33\2\u00d9\u00dc\5\66\34\2\u00da\u00dc\5:\36\2\u00db")
        buf.write("\u00d3\3\2\2\2\u00db\u00d4\3\2\2\2\u00db\u00d5\3\2\2\2")
        buf.write("\u00db\u00d6\3\2\2\2\u00db\u00d7\3\2\2\2\u00db\u00d8\3")
        buf.write("\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00da\3\2\2\2\u00dc)")
        buf.write("\3\2\2\2\u00dd\u00de\7\20\2\2\u00de\u00df\7&\2\2\u00df")
        buf.write("\u00e0\5\24\13\2\u00e0\u00e1\7\'\2\2\u00e1\u00e4\5(\25")
        buf.write("\2\u00e2\u00e3\7\21\2\2\u00e3\u00e5\5(\25\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5+\3\2\2\2\u00e6\u00e8")
        buf.write("\7\r\2\2\u00e7\u00e9\5(\25\2\u00e8\u00e7\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2")
        buf.write("\u00eb\u00ec\3\2\2\2\u00ec\u00ed\7\f\2\2\u00ed\u00ee\5")
        buf.write("\24\13\2\u00ee\u00ef\7*\2\2\u00ef-\3\2\2\2\u00f0\u00f1")
        buf.write("\7\13\2\2\u00f1\u00f2\7&\2\2\u00f2\u00f3\5\24\13\2\u00f3")
        buf.write("\u00f4\7*\2\2\u00f4\u00f5\5\24\13\2\u00f5\u00f6\7*\2\2")
        buf.write("\u00f6\u00f7\5\24\13\2\u00f7\u00f8\7\'\2\2\u00f8\u00f9")
        buf.write("\5(\25\2\u00f9/\3\2\2\2\u00fa\u00fb\7\16\2\2\u00fb\u00fc")
        buf.write("\7*\2\2\u00fc\61\3\2\2\2\u00fd\u00fe\7\17\2\2\u00fe\u00ff")
        buf.write("\7*\2\2\u00ff\63\3\2\2\2\u0100\u0102\7\22\2\2\u0101\u0103")
        buf.write("\5\24\13\2\u0102\u0101\3\2\2\2\u0102\u0103\3\2\2\2\u0103")
        buf.write("\u0104\3\2\2\2\u0104\u0105\7*\2\2\u0105\65\3\2\2\2\u0106")
        buf.write("\u0107\5\24\13\2\u0107\u0108\7*\2\2\u0108\67\3\2\2\2\u0109")
        buf.write("\u010a\7.\2\2\u010a\u0113\7&\2\2\u010b\u0110\5\24\13\2")
        buf.write("\u010c\u010d\7+\2\2\u010d\u010f\5\24\13\2\u010e\u010c")
        buf.write("\3\2\2\2\u010f\u0112\3\2\2\2\u0110\u010e\3\2\2\2\u0110")
        buf.write("\u0111\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2")
        buf.write("\u0113\u010b\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\3")
        buf.write("\2\2\2\u0115\u0116\7\'\2\2\u01169\3\2\2\2\u0117\u011b")
        buf.write("\7(\2\2\u0118\u011a\5\6\4\2\u0119\u0118\3\2\2\2\u011a")
        buf.write("\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c\u0121\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u0120\5")
        buf.write("(\25\2\u011f\u011e\3\2\2\2\u0120\u0123\3\2\2\2\u0121\u011f")
        buf.write("\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0124\3\2\2\2\u0123")
        buf.write("\u0121\3\2\2\2\u0124\u0125\7)\2\2\u0125;\3\2\2\2\34?E")
        buf.write("MZ`fpw~\u0088\u0093\u009b\u00a2\u00ac\u00b7\u00bd\u00c5")
        buf.write("\u00d1\u00db\u00e4\u00ea\u0102\u0110\u0113\u011b\u0121")
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
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'!'", "'%'", "'='", "'||'", "'&&'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'('", "')'", "'{'", 
                     "'}'", "';'", "','", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "WS", "BLOCK_CMT", "LINE_CMT", "INTTYPE", 
                      "FLOATTYPE", "VOIDTYPE", "BOOLEAN", "STRING", "FOR", 
                      "WHILE", "DO", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "RETURN", "BOOLLIT", "INTLIT", "FLOATLIT", "STRINGLIT", 
                      "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", 
                      "MOD_OP", "ASS_OP", "OR_OP", "AND_OP", "EQUAL_OP", 
                      "NOT_EQ_OP", "LT_OP", "LE_OP", "GT_OP", "GE_OP", "LB", 
                      "RB", "LP", "RP", "SEMI", "CM", "LSB", "RSB", "ID", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decls = 1
    RULE_vardecl = 2
    RULE_vartype = 3
    RULE_fultype = 4
    RULE_varid = 5
    RULE_funcdecl = 6
    RULE_plist = 7
    RULE_para = 8
    RULE_expr = 9
    RULE_expr2 = 10
    RULE_expr3 = 11
    RULE_expr4 = 12
    RULE_expr5 = 13
    RULE_expr6 = 14
    RULE_expr7 = 15
    RULE_expr8 = 16
    RULE_expr9 = 17
    RULE_term = 18
    RULE_stmt = 19
    RULE_if_s = 20
    RULE_dowhl_s = 21
    RULE_for_s = 22
    RULE_break_s = 23
    RULE_cont_s = 24
    RULE_ret_s = 25
    RULE_expr_s = 26
    RULE_funcall = 27
    RULE_block_s = 28

    ruleNames =  [ "program", "decls", "vardecl", "vartype", "fultype", 
                   "varid", "funcdecl", "plist", "para", "expr", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr8", 
                   "expr9", "term", "stmt", "if_s", "dowhl_s", "for_s", 
                   "break_s", "cont_s", "ret_s", "expr_s", "funcall", "block_s" ]

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
    BOOLLIT=17
    INTLIT=18
    FLOATLIT=19
    STRINGLIT=20
    ADD_OP=21
    SUB_OP=22
    MUL_OP=23
    DIV_OP=24
    NOT_OP=25
    MOD_OP=26
    ASS_OP=27
    OR_OP=28
    AND_OP=29
    EQUAL_OP=30
    NOT_EQ_OP=31
    LT_OP=32
    LE_OP=33
    GT_OP=34
    GE_OP=35
    LB=36
    RB=37
    LP=38
    RP=39
    SEMI=40
    CM=41
    LSB=42
    RSB=43
    ID=44
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

        def decls(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.DeclsContext)
            else:
                return self.getTypedRuleContext(MCParser.DeclsContext,i)


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
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.decls()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.VOIDTYPE) | (1 << MCParser.BOOLEAN) | (1 << MCParser.STRING))) != 0)):
                    break

            self.state = 63
            self.match(MCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MCParser.VardeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MCParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return MCParser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = MCParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VardeclContext(ParserRuleContext):

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
            return MCParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MCParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.vartype()
            self.state = 70
            self.varid()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 71
                self.match(MCParser.CM)
                self.state = 72
                self.varid()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
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
        self.enterRule(localctx, 6, self.RULE_vartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
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

    class FultypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(MCParser.VartypeContext,0)


        def LSB(self):
            return self.getToken(MCParser.LSB, 0)

        def RSB(self):
            return self.getToken(MCParser.RSB, 0)

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
        self.enterRule(localctx, 8, self.RULE_fultype)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.vartype()
                self.state = 83
                self.match(MCParser.LSB)
                self.state = 84
                self.match(MCParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.vartype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
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
        self.enterRule(localctx, 10, self.RULE_varid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(MCParser.ID)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LSB:
                self.state = 91
                self.match(MCParser.LSB)
                self.state = 92
                self.match(MCParser.INTLIT)
                self.state = 93
                self.match(MCParser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncdeclContext(ParserRuleContext):

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
            return MCParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MCParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.fultype()
            self.state = 97
            self.match(MCParser.ID)
            self.state = 98
            self.match(MCParser.LB)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.BOOLEAN) | (1 << MCParser.STRING))) != 0):
                self.state = 99
                self.plist()


            self.state = 102
            self.match(MCParser.RB)
            self.state = 103
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
        self.enterRule(localctx, 14, self.RULE_plist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.para()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MCParser.CM:
                self.state = 106
                self.match(MCParser.CM)
                self.state = 107
                self.para()
                self.state = 112
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
        self.enterRule(localctx, 16, self.RULE_para)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.vartype()
            self.state = 114
            self.match(MCParser.ID)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MCParser.LSB:
                self.state = 115
                self.match(MCParser.LSB)
                self.state = 116
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
        self.enterRule(localctx, 18, self.RULE_expr)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.expr2(0)
                self.state = 120
                self.match(MCParser.ASS_OP)
                self.state = 121
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 129
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 130
                    self.match(MCParser.OR_OP)
                    self.state = 131
                    self.expr3(0) 
                self.state = 136
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.expr4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 140
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 141
                    self.match(MCParser.AND_OP)
                    self.state = 142
                    self.expr4() 
                self.state = 147
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
        self.enterRule(localctx, 24, self.RULE_expr4)
        self._la = 0 # Token type
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.expr5()
                self.state = 149
                _la = self._input.LA(1)
                if not(_la==MCParser.EQUAL_OP or _la==MCParser.NOT_EQ_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 150
                self.expr5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
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
        self.enterRule(localctx, 26, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.expr6(0)
                self.state = 156
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.LT_OP) | (1 << MCParser.LE_OP) | (1 << MCParser.GT_OP) | (1 << MCParser.GE_OP))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 157
                self.expr6(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.expr7(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 170
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 165
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 166
                    _la = self._input.LA(1)
                    if not(_la==MCParser.ADD_OP or _la==MCParser.SUB_OP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 167
                    self.expr7(0) 
                self.state = 172
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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr7, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MCParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 176
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 177
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.MUL_OP) | (1 << MCParser.DIV_OP) | (1 << MCParser.MOD_OP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 178
                    self.expr8() 
                self.state = 183
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
        self.enterRule(localctx, 32, self.RULE_expr8)
        self._la = 0 # Token type
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.SUB_OP, MCParser.NOT_OP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                _la = self._input.LA(1)
                if not(_la==MCParser.SUB_OP or _la==MCParser.NOT_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 185
                self.expr8()
                pass
            elif token in [MCParser.BOOLLIT, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRINGLIT, MCParser.LB, MCParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
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
        self.enterRule(localctx, 34, self.RULE_expr9)
        try:
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.term()
                self.state = 190
                self.match(MCParser.LSB)
                self.state = 191
                self.expr()
                self.state = 192
                self.match(MCParser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
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


        def ID(self):
            return self.getToken(MCParser.ID, 0)

        def getRuleIndex(self):
            return MCParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MCParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_term)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(MCParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.match(MCParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.match(MCParser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 200
                self.match(MCParser.STRINGLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 201
                self.match(MCParser.LB)
                self.state = 202
                self.expr()
                self.state = 203
                self.match(MCParser.RB)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 205
                self.funcall()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 206
                self.match(MCParser.ID)
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
        self.enterRule(localctx, 38, self.RULE_stmt)
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MCParser.IF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.if_s()
                pass
            elif token in [MCParser.DO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.dowhl_s()
                pass
            elif token in [MCParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 211
                self.for_s()
                pass
            elif token in [MCParser.BREAK]:
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                self.break_s()
                pass
            elif token in [MCParser.CONTINUE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 213
                self.cont_s()
                pass
            elif token in [MCParser.RETURN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 214
                self.ret_s()
                pass
            elif token in [MCParser.BOOLLIT, MCParser.INTLIT, MCParser.FLOATLIT, MCParser.STRINGLIT, MCParser.SUB_OP, MCParser.NOT_OP, MCParser.LB, MCParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 215
                self.expr_s()
                pass
            elif token in [MCParser.LP]:
                self.enterOuterAlt(localctx, 8)
                self.state = 216
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
        self.enterRule(localctx, 40, self.RULE_if_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(MCParser.IF)
            self.state = 220
            self.match(MCParser.LB)
            self.state = 221
            self.expr()
            self.state = 222
            self.match(MCParser.RB)
            self.state = 223
            self.stmt()
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 224
                self.match(MCParser.ELSE)
                self.state = 225
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
        self.enterRule(localctx, 42, self.RULE_dowhl_s)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(MCParser.DO)
            self.state = 230 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 229
                self.stmt()
                self.state = 232 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.FOR) | (1 << MCParser.DO) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.IF) | (1 << MCParser.RETURN) | (1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.ID))) != 0)):
                    break

            self.state = 234
            self.match(MCParser.WHILE)
            self.state = 235
            self.expr()
            self.state = 236
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
        self.enterRule(localctx, 44, self.RULE_for_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MCParser.FOR)
            self.state = 239
            self.match(MCParser.LB)
            self.state = 240
            self.expr()
            self.state = 241
            self.match(MCParser.SEMI)
            self.state = 242
            self.expr()
            self.state = 243
            self.match(MCParser.SEMI)
            self.state = 244
            self.expr()
            self.state = 245
            self.match(MCParser.RB)
            self.state = 246
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
        self.enterRule(localctx, 46, self.RULE_break_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(MCParser.BREAK)
            self.state = 249
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
        self.enterRule(localctx, 48, self.RULE_cont_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(MCParser.CONTINUE)
            self.state = 252
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
        self.enterRule(localctx, 50, self.RULE_ret_s)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(MCParser.RETURN)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LB) | (1 << MCParser.ID))) != 0):
                self.state = 255
                self.expr()


            self.state = 258
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
        self.enterRule(localctx, 52, self.RULE_expr_s)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.expr()
            self.state = 261
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
        self.enterRule(localctx, 54, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.match(MCParser.ID)
            self.state = 264
            self.match(MCParser.LB)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LB) | (1 << MCParser.ID))) != 0):
                self.state = 265
                self.expr()
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MCParser.CM:
                    self.state = 266
                    self.match(MCParser.CM)
                    self.state = 267
                    self.expr()
                    self.state = 272
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 275
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

        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MCParser.VardeclContext)
            else:
                return self.getTypedRuleContext(MCParser.VardeclContext,i)


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
        self.enterRule(localctx, 56, self.RULE_block_s)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(MCParser.LP)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.INTTYPE) | (1 << MCParser.FLOATTYPE) | (1 << MCParser.BOOLEAN) | (1 << MCParser.STRING))) != 0):
                self.state = 278
                self.vardecl()
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MCParser.FOR) | (1 << MCParser.DO) | (1 << MCParser.BREAK) | (1 << MCParser.CONTINUE) | (1 << MCParser.IF) | (1 << MCParser.RETURN) | (1 << MCParser.BOOLLIT) | (1 << MCParser.INTLIT) | (1 << MCParser.FLOATLIT) | (1 << MCParser.STRINGLIT) | (1 << MCParser.SUB_OP) | (1 << MCParser.NOT_OP) | (1 << MCParser.LB) | (1 << MCParser.LP) | (1 << MCParser.ID))) != 0):
                self.state = 284
                self.stmt()
                self.state = 289
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 290
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
        self._predicates[10] = self.expr2_sempred
        self._predicates[11] = self.expr3_sempred
        self._predicates[14] = self.expr6_sempred
        self._predicates[15] = self.expr7_sempred
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
         




