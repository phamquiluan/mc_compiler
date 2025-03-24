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
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\5\22\u00da\n\22\3\23\6\23\u00dd")
        buf.write("\n\23\r\23\16\23\u00de\3\24\3\24\3\25\3\25\5\25\u00e5")
        buf.write("\n\25\3\25\6\25\u00e8\n\25\r\25\16\25\u00e9\3\26\6\26")
        buf.write("\u00ed\n\26\r\26\16\26\u00ee\3\26\3\26\3\26\7\26\u00f4")
        buf.write("\n\26\f\26\16\26\u00f7\13\26\3\26\3\26\6\26\u00fb\n\26")
        buf.write("\r\26\16\26\u00fc\3\26\5\26\u0100\n\26\3\26\6\26\u0103")
        buf.write("\n\26\r\26\16\26\u0104\3\26\3\26\7\26\u0109\n\26\f\26")
        buf.write("\16\26\u010c\13\26\3\26\5\26\u010f\n\26\5\26\u0111\n\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\7\30\u0119\n\30\f\30\16")
        buf.write("\30\u011c\13\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write(" \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3")
        buf.write("\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3\60\3\60\7\60\u0157\n\60\f\60\16\60\u015a\13\60")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\7\62\u0162\n\62\f\62\16")
        buf.write("\62\u0165\13\62\3\62\3\62\3\63\3\63\3\63\7\63\u016c\n")
        buf.write("\63\f\63\16\63\u016f\13\63\3\63\3\63\5\63\u0173\n\63\3")
        buf.write("\63\3\63\3t\2\64\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\2")
        buf.write(")\2+\25-\2/\26\61\27\63\30\65\31\67\329\33;\34=\35?\36")
        buf.write("A\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61\3\2\r\5")
        buf.write("\2\13\f\16\17\"\"\3\2\f\f\3\2\62;\4\2GGgg\3\2//\n\2$$")
        buf.write("))^^ddhhppttvv\4\2$$^^\5\2C\\aac|\6\2\62;C\\aac|\t\2%")
        buf.write("&((AB``bb~~\u0080\u0080\5\2\f\f$$^^\2\u018a\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("+\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\3h\3\2\2\2\5n\3\2\2\2\7|\3\2\2\2\t\u0087\3\2\2")
        buf.write("\2\13\u008b\3\2\2\2\r\u0091\3\2\2\2\17\u0096\3\2\2\2\21")
        buf.write("\u009e\3\2\2\2\23\u00a5\3\2\2\2\25\u00a9\3\2\2\2\27\u00af")
        buf.write("\3\2\2\2\31\u00b2\3\2\2\2\33\u00b8\3\2\2\2\35\u00c1\3")
        buf.write("\2\2\2\37\u00c4\3\2\2\2!\u00c9\3\2\2\2#\u00d9\3\2\2\2")
        buf.write("%\u00dc\3\2\2\2\'\u00e0\3\2\2\2)\u00e2\3\2\2\2+\u0110")
        buf.write("\3\2\2\2-\u0112\3\2\2\2/\u0115\3\2\2\2\61\u0120\3\2\2")
        buf.write("\2\63\u0122\3\2\2\2\65\u0124\3\2\2\2\67\u0126\3\2\2\2")
        buf.write("9\u0128\3\2\2\2;\u012a\3\2\2\2=\u012c\3\2\2\2?\u012e\3")
        buf.write("\2\2\2A\u0131\3\2\2\2C\u0134\3\2\2\2E\u0137\3\2\2\2G\u013a")
        buf.write("\3\2\2\2I\u013c\3\2\2\2K\u013f\3\2\2\2M\u0141\3\2\2\2")
        buf.write("O\u0144\3\2\2\2Q\u0146\3\2\2\2S\u0148\3\2\2\2U\u014a\3")
        buf.write("\2\2\2W\u014c\3\2\2\2Y\u014e\3\2\2\2[\u0150\3\2\2\2]\u0152")
        buf.write("\3\2\2\2_\u0154\3\2\2\2a\u015b\3\2\2\2c\u015e\3\2\2\2")
        buf.write("e\u0168\3\2\2\2gi\t\2\2\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2")
        buf.write("\2jk\3\2\2\2kl\3\2\2\2lm\b\2\2\2m\4\3\2\2\2no\7\61\2\2")
        buf.write("op\7,\2\2pt\3\2\2\2qs\13\2\2\2rq\3\2\2\2sv\3\2\2\2tu\3")
        buf.write("\2\2\2tr\3\2\2\2uw\3\2\2\2vt\3\2\2\2wx\7,\2\2xy\7\61\2")
        buf.write("\2yz\3\2\2\2z{\b\3\2\2{\6\3\2\2\2|}\7\61\2\2}~\7\61\2")
        buf.write("\2~\u0082\3\2\2\2\177\u0081\n\3\2\2\u0080\177\3\2\2\2")
        buf.write("\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0083\3")
        buf.write("\2\2\2\u0083\u0085\3\2\2\2\u0084\u0082\3\2\2\2\u0085\u0086")
        buf.write("\b\4\2\2\u0086\b\3\2\2\2\u0087\u0088\7k\2\2\u0088\u0089")
        buf.write("\7p\2\2\u0089\u008a\7v\2\2\u008a\n\3\2\2\2\u008b\u008c")
        buf.write("\7h\2\2\u008c\u008d\7n\2\2\u008d\u008e\7q\2\2\u008e\u008f")
        buf.write("\7c\2\2\u008f\u0090\7v\2\2\u0090\f\3\2\2\2\u0091\u0092")
        buf.write("\7x\2\2\u0092\u0093\7q\2\2\u0093\u0094\7k\2\2\u0094\u0095")
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
        buf.write("\7t\2\2\u00ce\u00cf\7p\2\2\u00cf\"\3\2\2\2\u00d0\u00d1")
        buf.write("\7v\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3\7w\2\2\u00d3\u00da")
        buf.write("\7g\2\2\u00d4\u00d5\7h\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7")
        buf.write("\7n\2\2\u00d7\u00d8\7u\2\2\u00d8\u00da\7g\2\2\u00d9\u00d0")
        buf.write("\3\2\2\2\u00d9\u00d4\3\2\2\2\u00da$\3\2\2\2\u00db\u00dd")
        buf.write("\t\4\2\2\u00dc\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df&\3\2\2\2\u00e0")
        buf.write("\u00e1\t\4\2\2\u00e1(\3\2\2\2\u00e2\u00e4\t\5\2\2\u00e3")
        buf.write("\u00e5\t\6\2\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2")
        buf.write("\u00e5\u00e7\3\2\2\2\u00e6\u00e8\5\'\24\2\u00e7\u00e6")
        buf.write("\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea*\3\2\2\2\u00eb\u00ed\5\'\24\2\u00ec")
        buf.write("\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ec\3\2\2\2")
        buf.write("\u00ee\u00ef\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1\5")
        buf.write(")\25\2\u00f1\u0111\3\2\2\2\u00f2\u00f4\5\'\24\2\u00f3")
        buf.write("\u00f2\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2")
        buf.write("\u00f5\u00f6\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f5\3")
        buf.write("\2\2\2\u00f8\u00fa\7\60\2\2\u00f9\u00fb\5\'\24\2\u00fa")
        buf.write("\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fa\3\2\2\2")
        buf.write("\u00fc\u00fd\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u0100\5")
        buf.write(")\25\2\u00ff\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0111")
        buf.write("\3\2\2\2\u0101\u0103\5\'\24\2\u0102\u0101\3\2\2\2\u0103")
        buf.write("\u0104\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2")
        buf.write("\u0105\u0106\3\2\2\2\u0106\u010a\7\60\2\2\u0107\u0109")
        buf.write("\5\'\24\2\u0108\u0107\3\2\2\2\u0109\u010c\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010e\3\2\2\2")
        buf.write("\u010c\u010a\3\2\2\2\u010d\u010f\5)\25\2\u010e\u010d\3")
        buf.write("\2\2\2\u010e\u010f\3\2\2\2\u010f\u0111\3\2\2\2\u0110\u00ec")
        buf.write("\3\2\2\2\u0110\u00f5\3\2\2\2\u0110\u0102\3\2\2\2\u0111")
        buf.write(",\3\2\2\2\u0112\u0113\7^\2\2\u0113\u0114\t\7\2\2\u0114")
        buf.write(".\3\2\2\2\u0115\u011a\7$\2\2\u0116\u0119\n\b\2\2\u0117")
        buf.write("\u0119\5-\27\2\u0118\u0116\3\2\2\2\u0118\u0117\3\2\2\2")
        buf.write("\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a\u011b\3")
        buf.write("\2\2\2\u011b\u011d\3\2\2\2\u011c\u011a\3\2\2\2\u011d\u011e")
        buf.write("\7$\2\2\u011e\u011f\b\30\3\2\u011f\60\3\2\2\2\u0120\u0121")
        buf.write("\7-\2\2\u0121\62\3\2\2\2\u0122\u0123\7/\2\2\u0123\64\3")
        buf.write("\2\2\2\u0124\u0125\7,\2\2\u0125\66\3\2\2\2\u0126\u0127")
        buf.write("\7\61\2\2\u01278\3\2\2\2\u0128\u0129\7#\2\2\u0129:\3\2")
        buf.write("\2\2\u012a\u012b\7\'\2\2\u012b<\3\2\2\2\u012c\u012d\7")
        buf.write("?\2\2\u012d>\3\2\2\2\u012e\u012f\7~\2\2\u012f\u0130\7")
        buf.write("~\2\2\u0130@\3\2\2\2\u0131\u0132\7(\2\2\u0132\u0133\7")
        buf.write("(\2\2\u0133B\3\2\2\2\u0134\u0135\7?\2\2\u0135\u0136\7")
        buf.write("?\2\2\u0136D\3\2\2\2\u0137\u0138\7#\2\2\u0138\u0139\7")
        buf.write("?\2\2\u0139F\3\2\2\2\u013a\u013b\7>\2\2\u013bH\3\2\2\2")
        buf.write("\u013c\u013d\7>\2\2\u013d\u013e\7?\2\2\u013eJ\3\2\2\2")
        buf.write("\u013f\u0140\7@\2\2\u0140L\3\2\2\2\u0141\u0142\7@\2\2")
        buf.write("\u0142\u0143\7?\2\2\u0143N\3\2\2\2\u0144\u0145\7*\2\2")
        buf.write("\u0145P\3\2\2\2\u0146\u0147\7+\2\2\u0147R\3\2\2\2\u0148")
        buf.write("\u0149\7}\2\2\u0149T\3\2\2\2\u014a\u014b\7\177\2\2\u014b")
        buf.write("V\3\2\2\2\u014c\u014d\7=\2\2\u014dX\3\2\2\2\u014e\u014f")
        buf.write("\7.\2\2\u014fZ\3\2\2\2\u0150\u0151\7]\2\2\u0151\\\3\2")
        buf.write("\2\2\u0152\u0153\7_\2\2\u0153^\3\2\2\2\u0154\u0158\t\t")
        buf.write("\2\2\u0155\u0157\t\n\2\2\u0156\u0155\3\2\2\2\u0157\u015a")
        buf.write("\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159")
        buf.write("`\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u015c\t\13\2\2\u015c")
        buf.write("\u015d\b\61\4\2\u015db\3\2\2\2\u015e\u0163\7$\2\2\u015f")
        buf.write("\u0162\n\b\2\2\u0160\u0162\5-\27\2\u0161\u015f\3\2\2\2")
        buf.write("\u0161\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3")
        buf.write("\2\2\2\u0163\u0164\3\2\2\2\u0164\u0166\3\2\2\2\u0165\u0163")
        buf.write("\3\2\2\2\u0166\u0167\b\62\5\2\u0167d\3\2\2\2\u0168\u016d")
        buf.write("\7$\2\2\u0169\u016c\n\f\2\2\u016a\u016c\5-\27\2\u016b")
        buf.write("\u0169\3\2\2\2\u016b\u016a\3\2\2\2\u016c\u016f\3\2\2\2")
        buf.write("\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u0170\3")
        buf.write("\2\2\2\u016f\u016d\3\2\2\2\u0170\u0172\7^\2\2\u0171\u0173")
        buf.write("\n\7\2\2\u0172\u0171\3\2\2\2\u0172\u0173\3\2\2\2\u0173")
        buf.write("\u0174\3\2\2\2\u0174\u0175\b\63\6\2\u0175f\3\2\2\2\32")
        buf.write("\2jt\u0082\u00d9\u00de\u00e4\u00e9\u00ee\u00f5\u00fc\u00ff")
        buf.write("\u0104\u010a\u010e\u0110\u0118\u011a\u0158\u0161\u0163")
        buf.write("\u016b\u016d\u0172\7\b\2\2\3\30\2\3\61\3\3\62\4\3\63\5")
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
    BOOLLIT = 17
    INTLIT = 18
    FLOATLIT = 19
    STRINGLIT = 20
    ADD_OP = 21
    SUB_OP = 22
    MUL_OP = 23
    DIV_OP = 24
    NOT_OP = 25
    MOD_OP = 26
    ASS_OP = 27
    OR_OP = 28
    AND_OP = 29
    EQUAL_OP = 30
    NOT_EQ_OP = 31
    LT_OP = 32
    LE_OP = 33
    GT_OP = 34
    GE_OP = 35
    LB = 36
    RB = 37
    LP = 38
    RP = 39
    SEMI = 40
    CM = 41
    LSB = 42
    RSB = 43
    ID = 44
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
            "IF", "ELSE", "RETURN", "BOOLLIT", "INTLIT", "FLOATLIT", "STRINGLIT", 
            "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", "MOD_OP", 
            "ASS_OP", "OR_OP", "AND_OP", "EQUAL_OP", "NOT_EQ_OP", "LT_OP", 
            "LE_OP", "GT_OP", "GE_OP", "LB", "RB", "LP", "RP", "SEMI", "CM", 
            "LSB", "RSB", "ID", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "WS", "BLOCK_CMT", "LINE_CMT", "INTTYPE", "FLOATTYPE", 
                  "VOIDTYPE", "BOOLEAN", "STRING", "FOR", "WHILE", "DO", 
                  "BREAK", "CONTINUE", "IF", "ELSE", "RETURN", "BOOLLIT", 
                  "INTLIT", "DIGIT", "EXP", "FLOATLIT", "ESC_LIT", "STRINGLIT", 
                  "ADD_OP", "SUB_OP", "MUL_OP", "DIV_OP", "NOT_OP", "MOD_OP", 
                  "ASS_OP", "OR_OP", "AND_OP", "EQUAL_OP", "NOT_EQ_OP", 
                  "LT_OP", "LE_OP", "GT_OP", "GE_OP", "LB", "RB", "LP", 
                  "RP", "SEMI", "CM", "LSB", "RSB", "ID", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[22] = self.STRINGLIT_action 
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
     


