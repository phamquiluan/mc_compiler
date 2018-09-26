import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
        self.assertTrue(TestLexer.checkLexeme("__a","__a,<EOF>",102))
        self.assertTrue(TestLexer.checkLexeme("a","a,<EOF>",158))
        self.assertTrue(TestLexer.checkLexeme("1a_","1,a_,<EOF>",103))
        self.assertTrue(TestLexer.checkLexeme("a","a,<EOF>",104))
        self.assertTrue(TestLexer.checkLexeme("true","true,<EOF>",105))
        self.assertTrue(TestLexer.checkLexeme("VOID","VOID,<EOF>",106))

    def test_keyword(self):
        """test keywords"""
        self.assertTrue(TestLexer.checkLexeme("bool","bool,<EOF>",107))
        self.assertTrue(TestLexer.checkLexeme("break","break,<EOF>",108))
        self.assertTrue(TestLexer.checkLexeme("continue","continue,<EOF>",109))
        self.assertTrue(TestLexer.checkLexeme("else","else,<EOF>",110))
        self.assertTrue(TestLexer.checkLexeme("for","for,<EOF>",111))
        self.assertTrue(TestLexer.checkLexeme("float","float,<EOF>",112))
        self.assertTrue(TestLexer.checkLexeme("if","if,<EOF>",113))
        self.assertTrue(TestLexer.checkLexeme("int","int,<EOF>",114))
        self.assertTrue(TestLexer.checkLexeme("return","return,<EOF>",115))
        self.assertTrue(TestLexer.checkLexeme("void","void,<EOF>",116))
        self.assertTrue(TestLexer.checkLexeme("do","do,<EOF>",117))
        self.assertTrue(TestLexer.checkLexeme("while","while,<EOF>",118))
        self.assertTrue(TestLexer.checkLexeme("true","true,<EOF>",119))
        self.assertTrue(TestLexer.checkLexeme("false","false,<EOF>",120))
        self.assertTrue(TestLexer.checkLexeme("string","string,<EOF>",121))
        self.assertTrue(TestLexer.checkLexeme("+a[4]","+,a,[,4,],<EOF>",161))

    def test_operator(self):
        """test operators"""
        self.assertTrue(TestLexer.checkLexeme("+","+,<EOF>",122))
        self.assertTrue(TestLexer.checkLexeme("-","-,<EOF>",123))
        self.assertTrue(TestLexer.checkLexeme("*","*,<EOF>",125))
        self.assertTrue(TestLexer.checkLexeme("/","/,<EOF>",126))
        self.assertTrue(TestLexer.checkLexeme("!","!,<EOF>",127))
        self.assertTrue(TestLexer.checkLexeme("%","%,<EOF>",128))
        self.assertTrue(TestLexer.checkLexeme("||","||,<EOF>",129))
        self.assertTrue(TestLexer.checkLexeme("&&","&&,<EOF>",130))
        self.assertTrue(TestLexer.checkLexeme("!=","!=,<EOF>",131))
        self.assertTrue(TestLexer.checkLexeme("==","==,<EOF>",132))
        self.assertTrue(TestLexer.checkLexeme("<","<,<EOF>",133))
        self.assertTrue(TestLexer.checkLexeme(">",">,<EOF>",134))
        self.assertTrue(TestLexer.checkLexeme("<=","<=,<EOF>",135))
        self.assertTrue(TestLexer.checkLexeme(">=",">=,<EOF>",136))
        self.assertTrue(TestLexer.checkLexeme("=","=,<EOF>",124))
        self.assertTrue(TestLexer.checkLexeme("//","<EOF>",162))

    def test_separator(self):
        """test separators"""
        self.assertTrue(TestLexer.checkLexeme("(","(,<EOF>",137))
        self.assertTrue(TestLexer.checkLexeme(")","),<EOF>",138))
        self.assertTrue(TestLexer.checkLexeme("{","{,<EOF>",139))
        self.assertTrue(TestLexer.checkLexeme("}","},<EOF>",140))
        self.assertTrue(TestLexer.checkLexeme("[","[,<EOF>",141))
        self.assertTrue(TestLexer.checkLexeme("]","],<EOF>",142))
        self.assertTrue(TestLexer.checkLexeme(";",";,<EOF>",143))
        self.assertTrue(TestLexer.checkLexeme(",",",,<EOF>",144))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",145))
        self.assertTrue(TestLexer.checkLexeme("0","0,<EOF>",146))
        self.assertTrue(TestLexer.checkLexeme("+01a","+,01,a,<EOF>",147))
        self.assertTrue(TestLexer.checkLexeme("-2","-,2,<EOF>",148))
        self.assertTrue(TestLexer.checkLexeme("123_","123,_,<EOF>",149))
        self.assertTrue(TestLexer.checkLexeme("{123","{,123,<EOF>",150))

    def test_floatlit(self):
        self.assertTrue(TestLexer.checkLexeme("1.2","1.2,<EOF>",151))
        self.assertTrue(TestLexer.checkLexeme("1.","1.,<EOF>",152))
        self.assertTrue(TestLexer.checkLexeme(".1",".1,<EOF>",153))
        self.assertTrue(TestLexer.checkLexeme("1.2e-2","1.2e-2,<EOF>",154))
        self.assertTrue(TestLexer.checkLexeme("12e8","12e8,<EOF>",155))
        self.assertTrue(TestLexer.checkLexeme("0.33E-2","0.33E-2,<EOF>",156))
        self.assertTrue(TestLexer.checkLexeme("128e-42","128e-42,<EOF>",157))
        self.assertTrue(TestLexer.checkLexeme("143e","143,e,<EOF>",159))
        self.assertTrue(TestLexer.checkLexeme("e-42","e,-,42,<EOF>",160))

    def test_string(self):
         self.assertTrue(TestLexer.checkLexeme("\"this is string\" \n\t\b\r\f","this is string,<EOF>",172))

    def test_ws(self):
        self.assertTrue(TestLexer.checkLexeme("\t","<EOF>",163))
        self.assertTrue(TestLexer.checkLexeme("\n_a","_a,<EOF>",164))
        self.assertTrue(TestLexer.checkLexeme("\b211","211,<EOF>",165))
        self.assertTrue(TestLexer.checkLexeme("\ffalse","false,<EOF>",166))
        self.assertTrue(TestLexer.checkLexeme("\r}","},<EOF>",167))
        self.assertTrue(TestLexer.checkLexeme("\"}","Unclosed String: }",168))
        self.assertTrue(TestLexer.checkLexeme("/\"}","/,Unclosed String: }",169))

    def test_commment(self):
        self.assertTrue(TestLexer.checkLexeme(
            "// line commment", "<EOF>", 170))
        self.assertTrue(TestLexer.checkLexeme(
            "/* block commment */", "<EOF>", 171))
        self.assertTrue(TestLexer.checkLexeme(
            "/* */", "<EOF>", 180))
        self.assertTrue(TestLexer.checkLexeme(
            "// \n", "<EOF>", 181))

    def test_complex(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a[4]}{&&=__a", "a,[,4,],},{,&&,=,__a,<EOF>", 173))
        self.assertTrue(TestLexer.checkLexeme(
            "{truefalseforifid", "{,truefalseforifid,<EOF>", 174))
        self.assertTrue(TestLexer.checkLexeme(
            "e-32__a1.2,>=||", "e,-,32,__a1,.2,,,>=,||,<EOF>", 175))
        self.assertTrue(TestLexer.checkLexeme(
            "true false for if id", "true,false,for,if,id,<EOF>", 176))
        self.assertTrue(TestLexer.checkLexeme("1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42",
                                              "1.2,1.,.1,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,<EOF>", 177))

    def test_more(self):
        self.assertTrue(TestLexer.checkLexeme(
            "01 010 100 1000 10000", "01,010,100,1000,10000,<EOF>", 178))
        self.assertTrue(TestLexer.checkLexeme(
            "foo(x)[3+12.1e-54+x[x[2]+1]];", "foo,(,x,),[,3,+,12.1e-54,+,x,[,x,[,2,],+,1,],],;,<EOF>", 179))
        self.assertTrue(TestLexer.checkLexeme(
            """
            void goo ( float x [ ] ) {
            float y [ 10 ] ;
            int z [ 10 ] ;
            foo ( x ) ; //CORRECT
            foo ( y ) ; //CORRECT
            foo ( z ) ; //WRONG
            }
            """, "void,goo,(,float,x,[,],),{,float,y,[,10,],;,int,z,[,10,],;,foo,(,x,),;,foo,(,y,),;,foo,(,z,),;,},<EOF>", 182))

        self.assertTrue(TestLexer.checkLexeme(
            """
            {
            putIntLn ( i ) ;
            putIntLn ( main ) ;
            putIntLn ( f ) ;
            }
        """, "{,putIntLn,(,i,),;,putIntLn,(,main,),;,putIntLn,(,f,),;,},<EOF>", 183))

        self.assertTrue(TestLexer.checkLexeme(
            """
            {
            main = f = i += 100;
            }
        """, "{,main,=,f,=,i,+,=,100,;,},<EOF>", 184))

        self.assertTrue(TestLexer.checkLexeme(
            "Abc*/Abnc", "Abc,*,/,Abnc,<EOF>", 185))

        self.assertTrue(TestLexer.checkLexeme(
            "aB aB8 _abc int float", "aB,aB8,_abc,int,float,<EOF>", 186))
        
        self.assertTrue(TestLexer.checkLexeme(
            """
            int i ;
            int f ( ) {
            return 200e12;
            }
        """, "int,i,;,int,f,(,),{,return,200e12,;,},<EOF>", 187))

        self.assertTrue(TestLexer.checkLexeme(
            """
            boolean b; // a variable of type boolean
            int i; // a variable of type int
            float f; // a variable of type float
            boolean ba[5]; // a variable of type array on boolean
            int ia[3]; // a variable of type array on int
            float fa[100]; // a variable of type array on float
        """, "boolean,b,;,int,i,;,float,f,;,boolean,ba,[,5,],;,int,ia,[,3,],;,float,fa,[,100,],;,<EOF>", 188))

        self.assertTrue(TestLexer.checkLexeme(
            "12.e-12t", "12.e-12,t,<EOF>", 189))

        self.assertTrue(TestLexer.checkLexeme(
            "true4__", "true4__,<EOF>", 190))

        self.assertTrue(TestLexer.checkLexeme(
            "\"this is string\"", "this is string,<EOF>", 191))

        self.assertTrue(TestLexer.checkLexeme(
        "\"abc def", "Unclosed String: abc def", 192))

        self.assertTrue(TestLexer.checkLexeme(
            "aaa@","aaa,Error Token @", 193))

        self.assertTrue(TestLexer.checkLexeme("@aas", "Error Token @", 194))

        self.assertTrue(TestLexer.checkLexeme(
        "\\","<EOF>", 195))

        self.assertTrue(TestLexer.checkLexeme(
            "int a = 10", "int,a,=,10,<EOF>", 196))

        self.assertTrue(TestLexer.checkLexeme("""{if(a~.~b)}""", "{,if,(,a,Error Token ~", 197))

        self.assertTrue(TestLexer.checkLexeme(
            "int a = 10", "int,a,=,10,<EOF>", 198))

        self.assertTrue(TestLexer.checkLexeme(
            "?123", "Error Token ?", 199))

        self.assertTrue(TestLexer.checkLexeme(
            "aaa?123", "aaa,Error Token ?", 200))


        
        
        


