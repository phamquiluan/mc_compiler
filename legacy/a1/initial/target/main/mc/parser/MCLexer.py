# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\61")
        buf.write("\u0176\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2")
        buf.write("\6\2i\n\2\r\2\16\2j\3\2\3\2\3\3\3\3\3\3\3\3\7\3s\n\3\f")
        buf.write("\3\16\3v\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4")
        buf.write("\u0081\n\4\f\4\16\4\u0084\13\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\7\22\u00d3")
        buf.write("\n\22\f\22\16\22\u00d6\13\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u00e1\n\23\3\24\6\24\u00e4\n")
        buf.write("\24\r\24\16\24\u00e5\3\25\3\25\3\26\3\26\5\26\u00ec\n")
        buf.write("\26\3\26\6\26\u00ef\n\26\r\26\16\26\u00f0\3\27\6\27\u00f4")
        buf.write("\n\27\r\27\16\27\u00f5\3\27\3\27\3\27\7\27\u00fb\n\27")
        buf.write("\f\27\16\27\u00fe\13\27\3\27\3\27\6\27\u0102\n\27\r\27")
        buf.write("\16\27\u0103\3\27\5\27\u0107\n\27\3\27\6\27\u010a\n\27")
        buf.write("\r\27\16\27\u010b\3\27\3\27\7\27\u0110\n\27\f\27\16\27")
        buf.write("\u0113\13\27\3\27\5\27\u0116\n\27\5\27\u0118\n\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\7\31\u0120\n\31\f\31\16\31\u0123")
        buf.write("\13\31\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3")
        buf.write("\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\62\3\62\3\62\7\62\u0162\n\62\f\62\16\62\u0165")
        buf.write("\13\62\3\62\3\62\3\63\3\63\3\63\7\63\u016c\n\63\f\63\16")
        buf.write("\63\u016f\13\63\3\63\3\63\5\63\u0173\n\63\3\63\3\63\3")
        buf.write("t\2\64\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\2+\2-\26")
        buf.write("/\2\61\27\63\30\65\31\67\329\33;\34=\35?\36A\37C E!G\"")
        buf.write("I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61\3\2\r\5\2\13\f\16")
        buf.write("\17\"\"\3\2\f\f\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2")
        buf.write("GGgg\3\2//\n\2$$))^^ddhhppttvv\4\2$$^^\t\2%&((AB``bb~")
        buf.write("~\u0080\u0080\5\2\f\f$$^^\2\u018a\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2-\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\3h\3")
        buf.write("\2\2\2\5n\3\2\2\2\7|\3\2\2\2\t\u0087\3\2\2\2\13\u008b")
        buf.write("\3\2\2\2\r\u0091\3\2\2\2\17\u0096\3\2\2\2\21\u009e\3\2")
        buf.write("\2\2\23\u00a5\3\2\2\2\25\u00a9\3\2\2\2\27\u00af\3\2\2")
        buf.write("\2\31\u00b2\3\2\2\2\33\u00b8\3\2\2\2\35\u00c1\3\2\2\2")
        buf.write("\37\u00c4\3\2\2\2!\u00c9\3\2\2\2#\u00d0\3\2\2\2%\u00e0")
        buf.write("\3\2\2\2\'\u00e3\3\2\2\2)\u00e7\3\2\2\2+\u00e9\3\2\2\2")
        buf.write("-\u0117\3\2\2\2/\u0119\3\2\2\2\61\u011c\3\2\2\2\63\u0127")
        buf.write("\3\2\2\2\65\u0129\3\2\2\2\67\u012b\3\2\2\29\u012d\3\2")
        buf.write("\2\2;\u012f\3\2\2\2=\u0131\3\2\2\2?\u0133\3\2\2\2A\u0135")
        buf.write("\3\2\2\2C\u0138\3\2\2\2E\u013b\3\2\2\2G\u013e\3\2\2\2")
        buf.write("I\u0141\3\2\2\2K\u0143\3\2\2\2M\u0146\3\2\2\2O\u0148\3")
        buf.write("\2\2\2Q\u014b\3\2\2\2S\u014d\3\2\2\2U\u014f\3\2\2\2W\u0151")
        buf.write("\3\2\2\2Y\u0153\3\2\2\2[\u0155\3\2\2\2]\u0157\3\2\2\2")
        buf.write("_\u0159\3\2\2\2a\u015b\3\2\2\2c\u015e\3\2\2\2e\u0168\3")
        buf.write("\2\2\2gi\t\2\2\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3\2\2")
        buf.write("\2kl\3\2\2\2lm\b\2\2\2m\4\3\2\2\2no\7\61\2\2op\7,\2\2")
        buf.write("pt\3\2\2\2qs\13\2\2\2rq\3\2\2\2sv\3\2\2\2tu\3\2\2\2tr")
        buf.write("\3\2\2\2uw\3\2\2\2vt\3\2\2\2wx\7,\2\2xy\7\61\2\2yz\3\2")
        buf.write("\2\2z{\b\3\2\2{\6\3\2\2\2|}\7\61\2\2}~\7\61\2\2~\u0082")
        buf.write("\3\2\2\2\177\u0081\n\3\2\2\u0080\177\3\2\2\2\u0081\u0084")
        buf.write("\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083")
        buf.write("\u0085\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0086\b\4\2\2")
        buf.write("\u0086\b\3\2\2\2\u0087\u0088\7k\2\2\u0088\u0089\7p\2\2")
        buf.write("\u0089\u008a\7v\2\2\u008a\n\3\2\2\2\u008b\u008c\7h\2\2")
        buf.write("\u008c\u008d\7n\2\2\u008d\u008e\7q\2\2\u008e\u008f\7c")
        buf.write("\2\2\u008f\u0090\7v\2\2\u0090\f\3\2\2\2\u0091\u0092\7")
        buf.write("x\2\2\u0092\u0093\7q\2\2\u0093\u0094\7k\2\2\u0094\u0095")
        buf.write("\7f\2\2\u0095\16\3\2\2\2\u0096\u0097\7d\2\2\u0097\u0098")
        buf.write("\7q\2\2\u0098\u0099\7q\2\2\u0099\u009a\7n\2\2\u009a\u009b")
        buf.write("\7g\2\2\u009b\u009c\7c\2\2\u009c\u009d\7p\2\2\u009d\20")
        buf.write("\3\2\2\2\u009e\u009f\7u\2\2\u009f\u00a0\7v\2\2\u00a0\u00a1")
        buf.write("\7t\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4")
        buf.write("\7i\2\2\u00a4\22\3\2\2\2\u00a5\u00a6\7h\2\2\u00a6\u00a7")
        buf.write("\7q\2\2\u00a7\u00a8\7t\2\2\u00a8\24\3\2\2\2\u00a9\u00aa")
        buf.write("\7y\2\2\u00aa\u00ab\7j\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad")
        buf.write("\7n\2\2\u00ad\u00ae\7g\2\2\u00ae\26\3\2\2\2\u00af\u00b0")
        buf.write("\7f\2\2\u00b0\u00b1\7q\2\2\u00b1\30\3\2\2\2\u00b2\u00b3")
        buf.write("\7d\2\2\u00b3\u00b4\7t\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6")
        buf.write("\7c\2\2\u00b6\u00b7\7m\2\2\u00b7\32\3\2\2\2\u00b8\u00b9")
        buf.write("\7e\2\2\u00b9\u00ba\7q\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc")
        buf.write("\7v\2\2\u00bc\u00bd\7k\2\2\u00bd\u00be\7p\2\2\u00be\u00bf")
        buf.write("\7w\2\2\u00bf\u00c0\7g\2\2\u00c0\34\3\2\2\2\u00c1\u00c2")
        buf.write("\7k\2\2\u00c2\u00c3\7h\2\2\u00c3\36\3\2\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8 \3\2\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb")
        buf.write("\7g\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7w\2\2\u00cd\u00ce")
        buf.write("\7t\2\2\u00ce\u00cf\7p\2\2\u00cf\"\3\2\2\2\u00d0\u00d4")
        buf.write("\t\4\2\2\u00d1\u00d3\t\5\2\2\u00d2\u00d1\3\2\2\2\u00d3")
        buf.write("\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2")
        buf.write("\u00d5$\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8\7v\2\2")
        buf.write("\u00d8\u00d9\7t\2\2\u00d9\u00da\7w\2\2\u00da\u00e1\7g")
        buf.write("\2\2\u00db\u00dc\7h\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de")
        buf.write("\7n\2\2\u00de\u00df\7u\2\2\u00df\u00e1\7g\2\2\u00e0\u00d7")
        buf.write("\3\2\2\2\u00e0\u00db\3\2\2\2\u00e1&\3\2\2\2\u00e2\u00e4")
        buf.write("\t\6\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5")
        buf.write("\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6(\3\2\2\2\u00e7")
        buf.write("\u00e8\t\6\2\2\u00e8*\3\2\2\2\u00e9\u00eb\t\7\2\2\u00ea")
        buf.write("\u00ec\t\b\2\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2")
        buf.write("\u00ec\u00ee\3\2\2\2\u00ed\u00ef\5)\25\2\u00ee\u00ed\3")
        buf.write("\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1,\3\2\2\2\u00f2\u00f4\5)\25\2\u00f3\u00f2")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5")
        buf.write("\u00f6\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8\5+\26\2")
        buf.write("\u00f8\u0118\3\2\2\2\u00f9\u00fb\5)\25\2\u00fa\u00f9\3")
        buf.write("\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd")
        buf.write("\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff")
        buf.write("\u0101\7\60\2\2\u0100\u0102\5)\25\2\u0101\u0100\3\2\2")
        buf.write("\2\u0102\u0103\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104")
        buf.write("\3\2\2\2\u0104\u0106\3\2\2\2\u0105\u0107\5+\26\2\u0106")
        buf.write("\u0105\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0118\3\2\2\2")
        buf.write("\u0108\u010a\5)\25\2\u0109\u0108\3\2\2\2\u010a\u010b\3")
        buf.write("\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d\u0111\7\60\2\2\u010e\u0110\5)\25\2\u010f")
        buf.write("\u010e\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f\3\2\2\2")
        buf.write("\u0111\u0112\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111\3")
        buf.write("\2\2\2\u0114\u0116\5+\26\2\u0115\u0114\3\2\2\2\u0115\u0116")
        buf.write("\3\2\2\2\u0116\u0118\3\2\2\2\u0117\u00f3\3\2\2\2\u0117")
        buf.write("\u00fc\3\2\2\2\u0117\u0109\3\2\2\2\u0118.\3\2\2\2\u0119")
        buf.write("\u011a\7^\2\2\u011a\u011b\t\t\2\2\u011b\60\3\2\2\2\u011c")
        buf.write("\u0121\7$\2\2\u011d\u0120\n\n\2\2\u011e\u0120\5/\30\2")
        buf.write("\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u0120\u0123\3")
        buf.write("\2\2\2\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2\u0122\u0124")
        buf.write("\3\2\2\2\u0123\u0121\3\2\2\2\u0124\u0125\7$\2\2\u0125")
        buf.write("\u0126\b\31\3\2\u0126\62\3\2\2\2\u0127\u0128\7-\2\2\u0128")
        buf.write("\64\3\2\2\2\u0129\u012a\7/\2\2\u012a\66\3\2\2\2\u012b")
        buf.write("\u012c\7,\2\2\u012c8\3\2\2\2\u012d\u012e\7\61\2\2\u012e")
        buf.write(":\3\2\2\2\u012f\u0130\7#\2\2\u0130<\3\2\2\2\u0131\u0132")
        buf.write("\7\'\2\2\u0132>\3\2\2\2\u0133\u0134\7?\2\2\u0134@\3\2")
        buf.write("\2\2\u0135\u0136\7~\2\2\u0136\u0137\7~\2\2\u0137B\3\2")
        buf.write("\2\2\u0138\u0139\7(\2\2\u0139\u013a\7(\2\2\u013aD\3\2")
        buf.write("\2\2\u013b\u013c\7?\2\2\u013c\u013d\7?\2\2\u013dF\3\2")
        buf.write("\2\2\u013e\u013f\7#\2\2\u013f\u0140\7?\2\2\u0140H\3\2")
        buf.write("\2\2\u0141\u0142\7>\2\2\u0142J\3\2\2\2\u0143\u0144\7>")
        buf.write("\2\2\u0144\u0145\7?\2\2\u0145L\3\2\2\2\u0146\u0147\7@")
        buf.write("\2\2\u0147N\3\2\2\2\u0148\u0149\7@\2\2\u0149\u014a\7?")
        buf.write("\2\2\u014aP\3\2\2\2\u014b\u014c\7*\2\2\u014cR\3\2\2\2")
        buf.write("\u014d\u014e\7+\2\2\u014eT\3\2\2\2\u014f\u0150\7}\2\2")
        buf.write("\u0150V\3\2\2\2\u0151\u0152\7\177\2\2\u0152X\3\2\2\2\u0153")
        buf.write("\u0154\7=\2\2\u0154Z\3\2\2\2\u0155\u0156\7.\2\2\u0156")
        buf.write("\\\3\2\2\2\u0157\u0158\7]\2\2\u0158^\3\2\2\2\u0159\u015a")
        buf.write("\7_\2\2\u015a`\3\2\2\2\u015b\u015c\t\13\2\2\u015c\u015d")
        buf.write("\b\61\4\2\u015db\3\2\2\2\u015e\u0163\7$\2\2\u015f\u0162")
        buf.write("\n\n\2\2\u0160\u0162\5/\30\2\u0161\u015f\3\2\2\2\u0161")
        buf.write("\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2")
        buf.write("\u0163\u0164\3\2\2\2\u0164\u0166\3\2\2\2\u0165\u0163\3")
        buf.write("\2\2\2\u0166\u0167\b\62\5\2\u0167d\3\2\2\2\u0168\u016d")
        buf.write("\7$\2\2\u0169\u016c\n\f\2\2\u016a\u016c\5/\30\2\u016b")
        buf.write("\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016c\u016f\3\2\2\2")
        buf.write("\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0170\3")
        buf.write("\2\2\2\u016f\u016d\3\2\2\2\u0170\u0172\7^\2\2\u0171\u0173")
        buf.write("\n\t\2\2\u0172\u0171\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174\u0175\b\63\6\2\u0175f\3\2\2\2\32")
        buf.write("\2jt\u0082\u00d4\u00e0\u00e5\u00eb\u00f0\u00f5\u00fc\u0103")
        buf.write("\u0106\u010b\u0111\u0115\u0117\u011f\u0121\u0161\u0163")
        buf.write("\u016b\u016d\u0172\7\b\2\2\3\31\2\3\61\3\3\62\4\3\63\5")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    BLOCK_CMT = 2
    LINE_CMT = 3
    INTTYPE = 4
    FLOATTYPE = 5
    VOIDTYPE = 6
    BOOLEAN = 7
    STRING = 8
    FOR = 9
    WHILE = 10
    DO = 11
    BREAK = 12
    CONTINUE = 13
    IF = 14
    ELSE = 15
    RETURN = 16
    ID = 17
    BOOLLIT = 18
    INTLIT = 19
    FLOATLIT = 20
    STRINGLIT = 21
    ADD_OP = 22
    SUB_OP = 23
    MUL_OP = 24
    DIV_OP = 25
    NOT_OP = 26
    MOD_OP = 27
    ASS_OP = 28
    OR_OP = 29
    AND_OP = 30
    EQUAL_OP = 31
    NOT_EQ_OP = 32
    LT_OP = 33
    LE_OP = 34
    GT_OP = 35
    GE_OP = 36
    LB = 37
    RB = 38
    LP = 39
    RP = 40
    SEMI = 41
    CM = 42
    LSB = 43
    RSB = 44
    ERROR_CHAR = 45
    UNCLOSE_STRING = 46
    ILLEGAL_ESCAPE = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'void'", "'boolean'", "'string'", "'for'", 
            "'while'", "'do'", "'break'", "'continue'", "'if'", "'else'", 
            "'return'", "'+'", "'-'", "'*'", "'/'", "'!'", "'%'", "'='", 
            "'||'", "'&&'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'('", "')'", "'{'", "'}'", "';'", "','", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "BLOCK_CMT", "LINE_CMT", "INTTYPE", "FLOATTYPE", "VOIDTYPE", 
            "BOOLEAN", "STRING", "FOR", "WHILE", "DO", "BREAK", "CONTINUE", 
            "IF", "ELSE", "RETURN", "ID", "BOOLLIT", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", 
            "MOD_OP", "ASS_OP", "OR_OP", "AND_OP", "EQUAL_OP", "NOT_EQ_OP", 
            "LT_OP", "LE_OP", "GT_OP", "GE_OP", "LB", "RB", "LP", "RP", 
            "SEMI", "CM", "LSB", "RSB", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "WS", "BLOCK_CMT", "LINE_CMT", "INTTYPE", "FLOATTYPE", 
                  "VOIDTYPE", "BOOLEAN", "STRING", "FOR", "WHILE", "DO", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "RETURN", "ID", "BOOLLIT", 
                  "INTLIT", "DIGIT", "EXP", "FLOATLIT", "ESC_LIT", "STRINGLIT", 
                  "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", "MOD_OP", 
                  "ASS_OP", "OR_OP", "AND_OP", "EQUAL_OP", "NOT_EQ_OP", 
                  "LT_OP", "LE_OP", "GT_OP", "GE_OP", "LB", "RB", "LP", 
                  "RP", "SEMI", "CM", "LSB", "RSB", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[23] = self.STRINGLIT_action 
            actions[47] = self.ERROR_CHAR_action 
            actions[48] = self.UNCLOSE_STRING_action 
            actions[49] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             raise UncloseString(self.text[1:]) 
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise IllegalEscape(self.text[1:]) 
     


