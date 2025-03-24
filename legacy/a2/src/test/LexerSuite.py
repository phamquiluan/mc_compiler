import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
	
	
	def test_101(self):
		inp = "abc"
		out = "abc,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,101))
	
	def test_102(self):
		inp = "main int {"
		out = "main,int,{,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,102))
	
	def test_103(self):
		inp = """ "aaaa" """
		out = "aaaa,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,103))
	
	def test_104(self):
		inp = """ \"aaaa """
		out = """Unclosed String: aaaa """
		self.assertTrue(TestLexer.checkLexeme(inp,out,104))
	
	def test_105(self):
		inp = """} int main {"""
		out = """},int,main,{,<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,105))
	
	def test_106(self):
		inp = """main int {"""
		out = """main,int,{,<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,106))
	
	def test_107(self):
		inp = """void main (){}"""
		out = """void,main,(,),{,},<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,107))

	def test_108(self):
		inp = "void main (){ a = 1 ;}"
		out = """void,main,(,),{,a,=,1,;,},<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,108))
	
	def test_109(self):
		inp = """ void foo(int i){}"""
		out = """void,foo,(,int,i,),{,},<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,109))
	
	def test_110(self):
		inp = "for(int i = 1; i <= rows; i=i+2)"
		out = """for,(,int,i,=,1,;,i,<=,rows,;,i,=,i,+,2,),<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,110))
	
	def test_111(self):
		inp = """ void foo(int i){}"""
		out = """void,foo,(,int,i,),{,},<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,111))
	
	def test_112(self):
		inp = """int main (){putIntLn(4);}"""
		out = "int,main,(,),{,putIntLn,(,4,),;,},<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,112))
	
	def test_113(self):
		inp = """int_int"""
		out = "int_int,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,113))
	
	def test_114(self):
		inp = """a%b"""
		out = "a,%,b,<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp,out,114))
	
	def test_115(self):
		inp = """ad=b+e"""
		out = "ad,=,b,+,e,<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp,out,115))
	
	def test_116(self):
		inp = """//"""
		out = "<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,116))
	
	def test_117(self):
		inp = """/**/"""
		out =  "<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,117))
	
	def test_118(self):
		inp = """//This is a line commnent"""
		out =  "<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,118))
	
	def test_119(self):
		inp = """/*This is a block comment*/"""
		out = "<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp,out,119))
	
	def test_120(self):
		inp = """//This is a line commnent///////// every thing"""
		out = "<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp,out,120))
	
	def test_121(self):
		inp = """//This is a line commnent//
        //
        //
        /// every thing"""
		out =  "<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,121))
	
	def test_122(self):
		inp = """/********This is a block comment*/"""
		out = "<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,122))
	
	def test_123(self):
		inp ="""//This is a line commnent///////// every thing"""
		out ="<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,123))
	
	def test_124(self):
		inp = """//This is a line commnent//
   		//
   		//
   		/// every thing"""
		out ="<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,124))
	
	def test_125(self):
		inp ="""/********This is a block comment*/"""
		out ="<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,125))
	
	def test_126(self):
		inp ="""/********This is
   				a block comment
   						inn many line*/"""
		out ="<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,126))
	
	def test_127(self):
		inp ="""//This is /*This is a block comment*/ ???"""
		out ="<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,127))
	
	def test_128(self):
		inp = """/*
   				//This is a line commnent
   				*/"""
		out ="<EOF>"  
		self.assertTrue(TestLexer.checkLexeme(inp,out,128))
	
	def test_129(self):
		inp ="""_abcd__abcd"""
		out ="_abcd__abcd,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,129))
	
	def test_130(self):
		inp ="""__1431997"""
		out ="__1431997,<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp,out,130))
	
	def test_131(self):
		inp ="""pvl12 PVL12 HYD123 defPVH 123PHV _ASUS _DELL 1a1A1"""
		out ="pvl12,PVL12,HYD123,defPVH,123,PHV,_ASUS,_DELL,1,a1A1,<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp,out,131))
	
	def test_132(self):
		inp ="""boolean int float void string"""
		out ="boolean,int,float,void,string,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,132))
	
	def test_133(self):
		inp ="""break continue if else"""
		out ="break,continue,if,else,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,133))
	
	def test_134(self):
		inp ="""break continue ifelse"""
		out ="break,continue,ifelse,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,134))
	
	def test_135(self):
		inp ="""true false"""
		out ="true,false,<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp,out,135))
	
	def test_136(self):
		inp ="""+++"""
		out ="+,+,+,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,136))
	
	def test_137(self):
		inp ="""-/*"""
		out ="-,/,*,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,137))
	
	def test_138(self):
		inp ="""!aaa%%!"""
		out ="!,aaa,%,%,!,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,138))
	
	def test_139(self):
		inp ="""!aaa%%!"""
		out ="!,aaa,%,%,!,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,139))
	
	def test_140(self):
		inp ="""iNum||fNum&&dNum"""
		out ="iNum,||,fNum,&&,dNum,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,140))
	
	def test_141(self):
		inp ="""iNum!=fNum abc==adc"""
		out ="iNum,!=,fNum,abc,==,adc,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,141))
	
	def test_142(self):
		inp ="""i<j>k"""
		out ="i,<,j,>,k,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,142))
	
	def test_143(self):
		inp ="""<=<=<="""
		out ="<=,<=,<=,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,143))
	
	def test_144(self):
		inp ="""<=<>=<=>=="""
		out ="<=,<,>=,<=,>=,=,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,144))
	
	def test_145(self):
		inp ="""============="""
		out ="==,==,==,==,==,==,=,<EOF>"  
		self.assertTrue(TestLexer.checkLexeme(inp,out,145))
	
	def test_146(self):
		inp ="""!==!====!=====!=="""
		out ="!=,=,!=,==,=,!=,==,==,!=,=,<EOF>"	
		self.assertTrue(TestLexer.checkLexeme(inp,out,146))
	
	def test_147(self):
		inp ="""=!<><>==<><>==<><>!="""
		out ="=,!,<,>,<,>=,=,<,>,<,>=,=,<,>,<,>,!=,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,147))
	
	def test_148(self):
		inp ="""!a!a!a!a!a=!=!=aaa!<><>"""
		out ="!,a,!,a,!,a,!,a,!,a,=,!=,!=,aaa,!,<,>,<,>,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,148))
	
	def test_149(self):
		inp ="""{}{}{}"""
		out ="{,},{,},{,},<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,149))
	
	def test_150(self):
		inp ="""(foo)(abc)(int)"""
		out ="(,foo,),(,abc,),(,int,),<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,150))
	
	def test_151(self):
		inp ="""int[] foo(int arr[5],float brr[0])"""
		out ="int,[,],foo,(,int,arr,[,5,],,,float,brr,[,0,],),<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,151))
	
	def test_152(self):
		inp ="""int i,j,l;"""
		out ="int,i,,,j,,,l,;,<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp,out,152))
	
	def test_153(self):
		inp ="""(,){;}"""
		out ="(,,,),{,;,},<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,153))
	
	def test_154(self):
		inp ="""a=(b+c)*d-(17*2-5)"""
		out ="a,=,(,b,+,c,),*,d,-,(,17,*,2,-,5,),<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,154))
	
	def test_155(self):
		inp ="""foo(2)[3+x]=a[b[5]]+2;"""
		out ="foo,(,2,),[,3,+,x,],=,a,[,b,[,5,],],+,2,;,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,155))
	
	def test_156(self):
		inp ="""if(true){a<=b && c>d}"""
		out ="if,(,true,),{,a,<=,b,&&,c,>,d,},<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,156))
	
	def test_157(self):
		inp ="""{{(abc)}}"""
		out ="{,{,(,abc,),},},<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,157))
	
	def test_158(self):
		inp ="""i++4++5--7!=8"""
		out ="i,+,+,4,+,+,5,-,-,7,!=,8,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,158))
	
	def test_159(self):
		inp ="""0"""
		out ="0,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,159))
	
	def test_160(self):
		inp ="""00000"""
		out ="00000,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,160))
	
	def test_161(self):
		inp ="""143"""
		out ="143,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,161))
	
	def test_162(self):
		inp ="""11.2 11. .21 15e2"""
		out ="11.2,11.,.21,15e2,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,162))
	
	def test_163(self):
		inp ="""78.2E-2 234.2e-2 .155E2 9.10"""
		out ="78.2E-2,234.2e-2,.155E2,9.10,<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp,out,163))
	
	def test_164(self):
		inp ="""12e87 0.433E-34 1428e-442"""
		out ="12e87,0.433E-34,1428e-442,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,164))
	
	def test_165(self):
		inp ="""12e8704.433E-341428e-442"""
		out ="12e8704,.433E-341428,e,-,442,<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp,out,165))
	
	def test_166(self):
		inp ="""12e8704.433E+341428e-+442"""
		out ="12e8704,.433,E,+,341428,e,-,+,442,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,166))
	
	def test_167(self):
		inp ="""12e-87+04.43-3E-341+428e-44-2"""
		out ="12e-87,+,04.43,-,3E-341,+,428e-44,-,2,<EOF>" 
		self.assertTrue(TestLexer.checkLexeme(inp,out,167))
	
	def test_168(self):
		inp ="""143+143.0+143e5+143e-5+143.e5+143.15e5"""
		out ="143,+,143.0,+,143e5,+,143e-5,+,143.e5,+,143.15e5,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,168))
	
	def test_169(self):
		inp =""" "phamquiluan" """
		out ="phamquiluan,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,169))
	
	def test_170(self):
		inp =""" "pham\nqui\nluan" """
		out ="""pham\nqui\nluan,<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,170))
	
	def test_1700(self):
		inp =""" "phamquiluan  " """
		out ="""phamquiluan  ,<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,1700))

	def test_171(self):
		inp =""" "pham\bqui\fluan" """
		out ="""pham\bqui\fluan,<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,171))
	
	# def test_172(self):
	# 	inp =""" "pham\rq\tl" """
	# 	out ="""pham\rq\tl,<EOF>"""
	# 	self.assertTrue(TestLexer.checkLexeme(inp,out,172))


	def test_172(self):
		inp =""" "" """
		out =""",<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,172))


	def test_173(self):
		inp =""" "'" """
		out ="""',<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,173))
	
	def test_174(self):
		inp =""" "\'" """
		out ="""\',<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,174))
	
	# def test_175(self):
	# 	inp =""" "\\" """
	# 	out ="""\\,<EOF>"""
	# 	self.assertTrue(TestLexer.checkLexeme(inp,out,175))
	
	# def test_175(self):
	# 	inp =""" "\\" """
	# 	out ="""\\,<EOF>"""
	# 	self.assertTrue(TestLexer.checkLexeme(inp,out,175))

	def test_175(self):
		inp =""" "\n" """
		out ="""\n,<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,175))

	# def test_176(self):
	# 	inp =""" "pham \n qui luan \n \r hoc \t mon \f \b mon hoc \\ \' PPL" """
	# 	out ="""pham \n qui luan \n \r hoc \t mon \f \b mon hoc \\ \' PPL,<EOF>"""
	# 	self.assertTrue(TestLexer.checkLexeme(inp,out,176))
	
	def test_176(self):
		inp =""" " """
		out ="""Unclosed String:  """
		self.assertTrue(TestLexer.checkLexeme(inp,out,176))

	# def test_177(self):
	# 	inp =""" "pham """
	# 	out ="""Unclosed String: pham """
	# 	self.assertTrue(TestLexer.checkLexeme(inp,out,177))
	
	def test_177(self):
		inp =""" "pham\\ """
		out ="""Illegal Escape In String: pham\\ """
		self.assertTrue(TestLexer.checkLexeme(inp,out,177))


	def test_178(self):
		inp ="""putString("This is String?)"""
		out ="""putString,(,Unclosed String: This is String?)"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,178))
	
	# def test_179(self):
	# 	inp = """putString("This is |String")"""
	# 	out ="""putString,(,Unclosed String: This is"""
	# 	self.assertTrue(TestLexer.checkLexeme(inp,out,179))
	
	def test_179(self):
		inp =""" "phamquiluan /**/" """
		out ="""phamquiluan /**/,<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,179))
	

	def test_180(self):
		inp =""" "phamquiluan //pvl" """
		out ="""phamquiluan //pvl,<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,180))
	
	def test_181(self):
		inp =""" "phamvanlinh /*****////////*//*" """
		out ="""phamvanlinh /*****////////*//*,<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,181))
	
	def test_182(self):
		inp =""" "\z"""
		out ="""Illegal Escape In String: \z"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,182))
	
	def test_183(self):
		inp =""" "aaaa\z"""
		out ="""Illegal Escape In String: aaaa\z""" 
		self.assertTrue(TestLexer.checkLexeme(inp,out,183))
	
	def test_184(self):
		inp =""" "aaaa\p"""
		out ="""Illegal Escape In String: aaaa\p"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,184))
	
	def test_185(self):
		inp =""" "aaaa\g" """
		out ="""Illegal Escape In String: aaaa\g"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,185))
	
	def test_186(self):
		inp =""" "\!!!!!!" """
		out ="""Illegal Escape In String: \!"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,186))
	
	def test_187(self):
		inp =""" "\____" """
		out ="""Illegal Escape In String: \_"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,187))
	
	def test_188(self):
		inp =""" ABCD int float""abc\""""
		out ="""ABCD,int,float,,abc,Unclosed String: """
		self.assertTrue(TestLexer.checkLexeme(inp,out,188))
	
	# def test_189(self):
	# 	inp =""" \\ """
	# 	out ="""ErrorToken \\ """
	# 	self.assertTrue(TestLexer.checkLexeme(inp,out,189))
	
	def test_189(self):
		inp ="""abc#"""
		out ="""abc,Error Token #"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,189))

	def test_190(self):
		inp ="""`#"""
		out ="""Error Token `"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,190))
	
	def test_191(self):
		inp ="""$$$###########"""
		out ="""Error Token $""" 
		self.assertTrue(TestLexer.checkLexeme(inp,out,191))
	
	# def test_192(self):
	# 	inp =""" ^$$$########### """
	# 	out ="""Error Token ^"""
	# 	self.assertTrue(TestLexer.checkLexeme(inp,out,192))
	
	def test_192(self):
		inp ="""&$$$###########"""
		out ="""Error Token &"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,192))

	def test_193(self):
		inp ="""|&$$$###########"""
		out ="""Error Token |"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,193))
	
	# def test_194(self):
	# 	inp ="""~|&$$$###########"""
	# 	out ="""Error Token ~"""
	# 	self.assertTrue(TestLexer.checkLexeme(inp,out,194))

	def test_194(self):
		inp ="""int checkPrimeNumber(int n)
             {
                for(i=2; i<=n/2; i=i+1)
                {
                /* condition for non-prime number */
                    if(n%i == 0)
                    {
                        flag = 0;
                        break;
                    }
                }
             }"""
		out ="""int,checkPrimeNumber,(,int,n,),{,for,(,i,=,2,;,i,<=,n,/,2,;,i,=,i,+,1,),{,if,(,n,%,i,==,0,),{,flag,=,0,;,break,;,},},},<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,194))
	
	def test_195(self):
		inp ="""int main() {
                int gd = DETECT, gm;
                /* initialization
                of graphic mode */
                initgraph(&gd, &gm, "C:\\TC\\BGI");
                line(100,100,200, 200);
                getch();
                closegraph();
                return 0;
             }"""
		out ="""int,main,(,),{,int,gd,=,DETECT,,,gm,;,initgraph,(,Error Token &""" 
		self.assertTrue(TestLexer.checkLexeme(inp,out,195))
	
	def test_196(self):
		inp ="""// ham tinh so mu
             int power(int, int);
             void main(void)
             {
             printf("2 mu 2 = %d.\n", power(2, 2));
             printf("2 mu 3 = %d.\n", power(2, 3));
             }"""
		out ="""int,power,(,int,,,int,),;,void,main,(,void,),{,printf,(,2 mu 2 = %d.\n,,,power,(,2,,,2,),),;,printf,(,2 mu 3 = %d.\n,,,power,(,2,,,3,),),;,},<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,196))
	
	def test_197(self):
		inp ="""void in_cuuchuong2(void)
             {
                        for(int i=1;i<=10;i=i+1)
                                     printf("\n2 x %d = %d\n", i, i*2);
             }"""
		out ="""void,in_cuuchuong2,(,void,),{,for,(,int,i,=,1,;,i,<=,10,;,i,=,i,+,1,),printf,(,\n2 x %d = %d\n,,,i,,,i,*,2,),;,},<EOF>"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,197))
	
	def test_198(self):
		inp ="""int main(void)
             {
                    {int z;
                     int y;
                     printf("nhap z:");
                     scanf("%d",z);
                     printf("nhap y:");
                     scanf("%d",y);
                     printf("%d + %d = %d\n", z, y,add(z, y));
                     printf ("gia tri tuyet doi cua %d la %d, y, abs(y));}}"""
		out ="""int,main,(,void,),{,{,int,z,;,int,y,;,printf,(,nhap z:,),;,scanf,(,%d,,,z,),;,printf,(,nhap y:,),;,scanf,(,%d,,,y,),;,printf,(,%d + %d = %d
,,,z,,,y,,,add,(,z,,,y,),),;,printf,(,Unclosed String: gia tri tuyet doi cua %d la %d, y, abs(y));}}"""
		self.assertTrue(TestLexer.checkLexeme(inp,out,198))
	
	def test_199(self):
		inp = "hihi"
		out = "hihi,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,199))
	
	def test_200(self):
		inp = "hihi1"
		out = "hihi1,<EOF>"
		self.assertTrue(TestLexer.checkLexeme(inp,out,200))
