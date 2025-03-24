import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):

    # def test_int(self):
    #     """Simple program: void main() { putInt(100); } """
    #     input = """void main(){
    #         int a;
    #         a=1;
    #         putInt(a);
    #      }"""
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))

    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],VoidType(),Block([],[
    # 			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))

    # def test_03(self):
    #     input = """void main() {putFloat(100.02);}"""
    #     expect = "100.02"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))

    # def test_04(self):
    #     input = """void main() {putFloat(143.15e5);}"""
    #     expect = "1.4315E7"
    #     self.assertTrue(TestCodeGen.test(input,expect,504))

    # def test_05(self):
    #     input = """void main() {putFloat(143.15e5);}"""
    #     expect = "1.4315E7"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))

    # def test_06(self):
    #     input = """void main(){
    #         if(true)
    #             putInt(1);
    #         else
    #             putInt(1);
    #      }"""
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_07(self):
    #     input = """
    #     void main(){
    #         int a;
    #         a = 4;
    #         putFloatLn(foo(a));
    #     }
    #     float foo(int a){
    #         int foo;
    #         foo = 5;
    #         return foo + a;
    #     }
    #     """
    #     expect = """9.0\n"""
    #     self.assertTrue(TestCodeGen.test(input,expect,507))

    # def test_08(self):
    #     input = """void main () {
    #      putIntLn(000);
    #      }"""
    #     expect = "0\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,508))

    # def test_09(self):
    #     input = """void main () {
    #      putFloatLn(1.0);
    #      }"""
    #     expect = "1.0\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,509))

    # def test_10(self):
    #     input = """void main () {
    #      putFloatLn(10.5);
    #      }"""
    #     expect = "10.5\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,510))

    # def test_11(self):
    #     input = """void main () {
    #      putFloatLn(100.14);
    #      }"""
    #     expect = "100.14\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,511))

    # def test_12(self):
    #     input = """void main () {
    #      putBoolLn(true);
    #      }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,512))

    # def test_13(self):
    #     input = """
    #         void main () {
    #             putStringLn("programming");
    #         }"""
    #     expect = "programming\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,513))

    # def test_14(self):
    #     input = """int a;
    #      float b;
    #      void main () {
    #      }
    #      boolean c;"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,514))

    # def test_15(self):
    #     input =  """
    #         int arr[5];
    #         void main () { }
    #      """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,515))

    # def test_16(self):
    #     input = """int a;
    #      float b;
    #      float frr[4];
    #      int arr[5];
    #      string aStr[4];
    #      void main () { }
    #      """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,516))

    # def test_17(self):
    #     """Program => Test global variable and function whose return type is voidtype."""
    #     input = """int a;
    #      float b;
    #      float frr[4];
    #      int arr[5];
    #      string aStr[4];
    #      void main () {
    #      }
    #      void funcVoid(){
    #      }
    #      """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,517))

    # def test_18(self):
    #     """Program => Main function: declared variable primitive type"""
    #     input = """int a;
    #      float b;
    #      float frr[4];
    #      int arr[5];
    #      string aStr[4];
    #      void main () {
    #       int a;
    #       float b;
    #      }
    #      """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,518))


    # def test_19(self):
    #     """Program => Main function: It's declared variable primitive and array type"""
    #     input = """int a;
    #         float b;
    #         float frr[4];
    #         string aStr[4];
    #         void main () {
    #             int a;
    #             float b;
    #             int arr[5];
    #         }
    #      """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,519))

    # def test_20(self):
    #     """Program => funcVoid function: It's declared variable primitive type in parameter and body"""
    #     input = """int a;
    #      float b;
    #      float frr[4];
    #      void main () {
    #       int a;
    #       float b;
    #       int arr[5];
    #      }
    #      void funcVoid(int a, int b){
    #       int c;
    #       float d,e,f;
    #      }
    #      """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,520))

    # def test_21(self):
    #     """Program => funcVoid function: It's declared variable primitive and array type in parameter and body"""
    #     input = """int a;
    #      float b;
    #      float frr[4];
    #      void main () {
    #       int a;
    #       float b;
    #       int arr[5];
    #      }
    #      void funcVoid(int a, string b, int arr[]){
    #       int c;
    #       float funcFrr[10];
    #      }
    #      """
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,521))

    # def test_22(self):
    #     """Program => manipulate data in Main function: simple assign the IntLiteral value to global variable IntType."""
    #     input = """int a;
    #      int arr[5];
    #      void main () {
    #       a = 10;
    #       putIntLn(a);
    #      }
    #      """
    #     expect = "10\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,522))

    # def test_23(self):
    #     """Program => manipulate data in Main function: simple assign the FloatLiteral value to global variable FloatType."""
    #     input = """int a;
    #      float b;
    #      int arr[5];
    #      void main () {
    #       b = 10.5;
    #       putFloatLn(b);
    #      }
    #      """
    #     expect = "10.5\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,523))

    # def test_24(self):
    #     """Program => manipulate data in Main function: simple assign the BoolLiteral value to global variable BoolType."""
    #     input = """int a;
    #      float b;
    #      boolean isTrue;
    #      int arr[5];
    #      void main () {
    #       isTrue = false;
    #       putBoolLn(isTrue);
    #      }
    #      """
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,524))

    # def test_25(self):
    #     """Program => manipulate data in Main function: simple assign the StringLiteral value to global variable StringType."""
    #     input = """int a;
    #      float b;
    #      string str;
    #      int arr[5];
    #      void main () {
    #       str = "testString";
    #       putStringLn(str);
    #      }
    #      """
    #     expect = "testString\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,525))

    # def test_26(self):
    #     """rogram => manipulate data in Main function: simple assign the IntLiteral value to global variable ArrayType(IntType)."""
    #     input = """int arr[5];
    #      void main () {
    #       arr[0]=15;
    #       putIntLn(arr[0]);
    #      }
    #      """
    #     expect = "15\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,526))

    # def test_27(self):
    #     """Program => manipulate data in Main function: simple assign the FloatLiteral value to global variable ArrayType(FloatType)"""
    #     input = """int arr[5];
    #      float frr[4];
    #      void main () {
    #       frr[0] = 14.3;
    #       putFloatLn(frr[0]);
    #      }
    #      """
    #     expect = "14.3\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,527))

    # def test_28(self):
    #     """Program => manipulate data in Main function: simple assign the StringLiteral value to global variable ArrayType(StringType)."""
    #     input = """int arr[5];
    #      string str[4];
    #      void main () {
    #       str[0] = "StringGlobal";
    #       putStringLn(str[0]);
    #      }
    #      """
    #     expect = "StringGlobal\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,528))

    # def test_29(self):
    #     """Program => manipulate data in Main function: simple assign the BoolLiteral value to global variable ArrayType(BoolType)."""
    #     input = """int arr[5];
    #      boolean brr[4];
    #      void main () {
    #       brr[0] = false;
    #       putBoolLn(brr[0]);
    #      }
    #      """
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,529))

    # def test_30(self):
    #     """Program => manipulate data in Main function: simple assign the IntLiteral value to local variable IntType."""
    #     input = """int a, b;
    #      void main () {
    #       int iNum;
    #       iNum = 9;
    #       putInt(iNum);
    #      }
    #      """
    #     expect = "9"
    #     self.assertTrue(TestCodeGen.test(input,expect,530))

    # def test_31(self):
    #     """Program => manipulate data in Main function: simple assign the FloatLiteral value to local variable FloatType."""
    #     input = """int a, b;
    #      void main () {
    #       float fNum;
    #       fNum = 9.15;
    #       putFloat(fNum);
    #      }
    #      """
    #     expect = "9.15"
    #     self.assertTrue(TestCodeGen.test(input,expect,531))

    # def test_32(self):
    #     """Program => manipulate data in Main function: simple assign the BoolLiteral value to local variable BoolType."""
    #     input = """int a, b;
    #      void main () {
    #       boolean isTrue;
    #       isTrue = true;
    #       putBool(isTrue);
    #      }
    #      """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,532))

    # def test_33(self):
    #     """Program => manipulate data in Main function: simple assign the StringLiteral value to local variable StringType."""
    #     input = """int a, b;
    #      void main () {
    #       string str;
    #       str = "LocalString";
    #       putStringLn(str);
    #      }
    #      """
    #     expect = "LocalString\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,533))

    # def test_34(self):
    #     """Program => manipulate data in Main function: simple assign the IntLiteral value to local variable ArrayType(IntType)."""
    #     input = """int a, b;
    #      void main () {
    #       int arr[5];
    #       arr[0] = 111;
    #       putInt(arr[0]);
    #      }
    #      """
    #     expect = "111"
    #     self.assertTrue(TestCodeGen.test(input,expect,534))

    # def test_35(self):
    #     """Program => manipulate data in Main function: simple assign the FloatLiteral value to local variable ArrayType(FloatType)."""
    #     input = """int a, b;
    #      void main () {
    #       float arr[5];
    #       arr[0] = 111.2;
    #       putFloat(arr[0]);
    #      }
    #      """
    #     expect = "111.2"
    #     self.assertTrue(TestCodeGen.test(input,expect,535))

    # def test_36(self):
    #     """Program => manipulate data in Main function: Assign the int value to local variable FloatType (have coercion)."""
    #     input = """int a, b;
    #      void main () {
    #       float fNum;
    #       fNum = 19;
    #       putFloat(fNum);
    #      }
    #      """
    #     expect = "19.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,536))

    # def test_37(self):
    #     """Program => manipulate data in Main function: Assign variable to variable (local & global), type: primitive type: IntType"""
    #     input = """int a, b;
    #      void main () {
    #       int iNum;
    #       a = -1;
    #       iNum = a;
    #       putInt(iNum);
    #      }
    #      """
    #     expect = "-1"
    #     self.assertTrue(TestCodeGen.test(input,expect,537))

    # def test_38(self):
    #     """Program => manipulate data in Main function: Assign variable to variable (local & global), type: primitive type - FloatType"""
    #     input = """float a, b;
    #      void main () {
    #       float fNum;
    #       a = 11.5;
    #       fNum = a;
    #       putFloat(fNum);
    #      }
    #      """
    #     expect = "11.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,538))

    # def test_39(self):
    #     """Program => manipulate data in Main function: Assign variable to variable (global & global), type: primitive type - StringType"""
    #     input = """string str1;
    #      string str2;
    #      void main () {
    #       str1 = "strDemo";
    #       str2 = str1;
    #       putString(str2);
    #      }
    #      """
    #     expect = "strDemo"
    #     self.assertTrue(TestCodeGen.test(input,expect,539))    


    # def test_40(self):
    #     """Program => manipulate data in Main function: Assign var to var (global & local), coercion int to float"""
    #     input = """float fNum;
    #      string str2;
    #      void main () {
    #       int iNum;
    #       iNum = 14;
    #       fNum = iNum;
    #       putFloat(fNum);
    #      }"""
    #     expect = "14.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,540))

    # def test_41(self):
    #     """Program => manipulate data in Main function: Assign recur 2 times: true and false"""
    #     input = """float fNum;
    #      string str2;
    #      void main () {
    #       boolean isT,isTrue;
    #       isT = true;
    #       isTrue = false;
    #       isT = isTrue = true;
    #       putBool(isT);
    #      }"""
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,541))

    # def test_42(self):
    #     """Program => manipulate data in Main function: Assign recur 2 times: Arraytype - StringType"""
    #     input = """float fNum;
    #      string str[4];
    #      void main () {
    #       str[0] = "null";
    #       str[1] = "text";
    #       str[2] = "notNull";
    #       str[0] = str[1] = "final";
    #       putString(str[0]);
    #      }"""
    #     expect = "final"
    #     self.assertTrue(TestCodeGen.test(input,expect,542))

    # def test_43(self):
    #     """Program => manipulate data in Main function: Assign recur 2 times: Arraytype and primitiveType"""
    #     input = """
    #      void main () {
    #       int arr[4];
    #       arr[0] = 1;
    #       arr[1] = 2;
    #       arr[2] = 3;
    #       putInt(arr[1]);
    #      }"""
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input,expect,543))

    # def test_44(self):
    #     """Program => manipulate data in Main function: Assign recur many times: Arraytype and primitiveType"""
    #     input = """
    #     float fNum;
    #     string str[4];
    #     void main () {
    #         int arr[4];
    #         int a,b;
    #         a = b = 10;
    #         arr[0]= a;
    #         arr[1] = arr[0] = b = a;
    #         arr[2] = a = arr[0]= 18;
    #         putIntLn(arr[2]);
    #      }"""
    #     expect = "18\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,544))

    # def test_45(self):
    #     """Program => manipulate data in Main function: Assign recur many times: It's has coercion!"""
    #     input = """float fNum;
    #      string str[4];
    #      void main () {
    #       int arr[4];
    #       int a,b;
    #       float f;
    #       fNum = a = b = 10;
    #       f = arr[0]= a;
    #       fNum = arr[1] = arr[0] = b = a;
    #       putFloatLn(fNum);
    #      }"""
    #     expect = "10.0\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,545))

    # def test_46(self):
    #     """Program => manipulate data in Main function: Assign recur many times: It's has complex coercion!"""
    #     input = """int a, b;
    #      int gArr[4];
    #      void main () {
    #       int arr[4];
    #       int c,d;
    #       a = 1;
    #       b = a = 1;
    #       c = a;
    #       b = a = c = b;
    #       gArr[0] = arr[0] = 1;
    #       gArr[1] = gArr[0] = 11;
    #       d = gArr[1] = arr[3] = gArr[0] = a = gArr[2] = b = 11;
    #       putIntLn(gArr[1]);
    #      }"""
    #     expect = "11\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,546))

    # def test_47(self):
    #     """Program => manipulate data in Main function: Assign recur many times type array type and primitive type of FloatType (coercion)"""
    #     input = """float a, b;
    #      float gArr[4];
    #      void main () {
    #       int arr[4];
    #       int c,d;
    #       c = 1;
    #       c = d = 3;
    #       a = c;
    #       b = d = 4;
    #       arr[0] = 5;
    #       gArr[0] = arr[0] = 11;
    #       gArr[1] = gArr[2] = arr[2] = c;
    #       putFloatLn(gArr[2]);
    #      }"""
    #     expect = "3.0\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,547))

    # def test_48(self):
    #     """Program => manipulate data in Main function: Assign recur many times type array type and primitive type of BooleanType"""
    #     input = """boolean a, b;
    #      boolean gArr[4];
    #      void main () {
    #       boolean arr[4];
    #       boolean c,d;
    #       c = true;
    #       c = d = false;
    #       a = c;
    #       b = d = false;
    #       arr[0] = true;
    #       gArr[0] = arr[0] = true;
    #       gArr[1] = gArr[2] = arr[2] = d;
    #       putBoolLn(gArr[1]);
    #      }"""
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,548))

    # def test_49(self):
    #     """Program => manipulate data in Main function: Assign recur many times type array type and primitive type of StringType"""
    #     input = """string a, b;
    #      string gArr[4];
    #      void main () {
    #       string arr[4];
    #       string c,d;
    #       c = "ccc";
    #       c = d = "cd";
    #       a = c;
    #       b = d = "string";
    #       arr[0] = "strDemo";
    #       gArr[0] = arr[0] = "stringDemo";
    #       gArr[1] = gArr[2] = arr[2] = arr[0];
    #       putStringLn(gArr[1]);
    #      }"""
    #     expect =  "stringDemo\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,549))

    # def test_50(self):
    #     """Program => manipulate data in Main function: Expression : Operator are add, minus; operand are array cell, literal in"""
    #     input = """int a,b,c;
    #         int arr[3];
    #         void main () {
    #             int iNum, i,j;
    #             arr[0] = 0;
    #             arr[1] = 1;
    #             arr[2] = 2;
    #             a = 3;
    #             b = a + 2;
    #             c = b + a + 3;
    #             iNum = arr[0] + c + (arr[1] - b) - (arr[2] - arr[0]);
    #             i = iNum - arr[0] + arr[1] - arr[2] - c;
    #             j = iNum - i + 11;
    #             putIntLn(j);
    #         }"""
    #     expect = "23\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,550))



    # def test_51(self):
    #     """Program => manipulate data in Main function: Expression : Operator are add, minus; operand are array cell, literal :float and int"""
    #     input = """int a,b,c;
    #     int arr[3];
    #     float fa,fb,fc;
    #     float frr[4];
    #     void main () {
    #      float fNum;
    #      arr[0] = arr[1] = arr[2] = 3;
    #      a = 3;
    #      b = a + 2;
    #      c = b + a + 3;
    #      fNum = a + b + arr[0] - 1;
    #      fa = fNum + c;
    #      fb = fa + a;
    #      fc = fb + b;
    #      frr[0] = fa + fb + fc;
    #      frr[1] = frr[0] + a + b +c;
    #      putFloatLn(frr[1]);
    #     }"""
    #     expect = "93.0\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,551))

    # def test_52(self):
    #     """Program => manipulate data in Main function: Expression : Operator are add, minus, mul; operand are array cell, literal :float and int"""
    #     input = """int a,b,c;
    #     int arr[3];
    #     float fa,fb,fc;
    #     float frr[4];
    #     void main () {
    #      float fNum;
    #      arr[0] = arr[1] = arr[2] = 3;
    #      a = 3*5;
    #      b = a + 2;
    #      c = b + a*3;
    #      fNum = a + b + arr[0]*4;
    #      fa = fNum + c*arr[0];
    #      fb = fa + a*arr[1];
    #      fc = fb + b*arr[2]+ fNum*a;
    #      frr[0] = fa*a + fb*b + fc*c;
    #      frr[1] = frr[0] + a*b*c;
    #      putFloatLn(frr[1]);
    #     }"""
    #     expect = "85067.0\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,552))

    # def test_53(self):
    #     """Program => manipulate data in Main function: Expression : Operator are add, minus, mul, div; operand are array cell, literal :float and int"""
    #     input = """int a,b,c;
    #     int arr[3];
    #     float fa,fb,fc;
    #     float frr[4];
    #     void main () {
    #      float fNum;
    #      arr[0] = arr[1] = arr[2] = 3;
    #      a = 3*5;
    #      b = a/2;
    #      c = b + a*3;
    #      fNum = a + b/arr[1] + arr[0]*4;
    #      fa = fNum/arr[0] + c*arr[0];
    #      fb = fa + a*arr[1] + a/arr[0];
    #      fc = fb + b*arr[2]+ fNum*a + fNum/(arr[0] + a);
    #      frr[0] = fa*a + fb/b + fc/c;
    #      frr[1] = frr[0] + a*b/c;
    #      putFloatLn(frr[1]);
    #     }"""
    #     expect = "2530.7573\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,553))

    # def test_54(self):
    #     """Program => manipulate data in Main function: Expression : Operator is Modulus; operand are array cell, literal : int"""
    #     input = """int a,b,c;
    #     int arr[3];
    #     void main () {
    #      arr[0] = arr[1] = arr[2] = 3;
    #      b = 10 % arr[0];
    #      putIntLn(arr[2]);
    #     }"""
    #     expect = "3\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,554))

    # def test_55(self):
    #     """Program => manipulate data in Main function: Expression : Operator is Modulus; operand are array cell, literal : int"""
    #     input = """int a,b,c;
    #     int arr[3];
    #     void main () {
    #      arr[0] = arr[1] = arr[2] = 3;
    #      a = 19;
    #      b = a + a % arr[0];
    #      c = b%a + arr[0]*arr[1];
    #      arr[2] = (c*a)%b;
    #      putIntLn(arr[2]);
    #     }"""
    #     expect = "10\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,555))

    # def test_56(self):
    #     """Program => manipulate data in Main function: UniryOp : Operator is Negative; operand is boolLiteral"""
    #     input = """boolean isTrue;
    #     boolean arr[4];
    #     void main () {
    #      boolean isT, isF;
    #      arr[0] = arr[1] = arr[2] = false;
    #      isT = !arr[0];
    #      isF = !(!arr[1]);
    #      isTrue = !!!!!!isF;
    #      putBoolLn(isTrue);
        
    #     }"""
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,556))

    # def test_57(self):
    #     """Program => manipulate data in Main function: UniryOp : Operator is Minus; operand is IntLiteral"""
    #     input = """int arr[4];
    #     void main () {
    #      int iNum, i , j;
    #      arr[0] = arr[1] = arr[2] = 10;
    #      i = -arr[0];
    #      j = -arr[1];
    #      iNum = i + j;
    #      putIntLn(iNum);
    #     }"""
    #     expect = "-20\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,557))

    # def test_58(self):
    #     """Program => manipulate data in Main function: UniryOp : Operator is Minus; operand is FloatLiteral"""
    #     input = """float arr[4];
    #     void main () {
    #      float fNum, i , j;
    #      arr[0] = arr[1] = 11.5;
    #      arr[2] = 8.5;
    #      i = -arr[0] + -arr[1];
    #      j = -arr[2]*3;
    #      fNum = i + j;
    #      putFloatLn(fNum);
    #     }"""
    #     expect = "-48.5\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,558))

    # def test_59(self):
    #     """Program => manipulate data in Main function: Operator are < ; operand is IntLiteral"""
    #     input = """float arr[4];
    #     void main () {
    #      int a, b;
    #      boolean isTrue;
    #      a = 10;
    #      b = 11;
    #      isTrue = a > b ;
    #      putBoolLn(isTrue);
    #     }"""
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,559))

    # def test_60(self):
    #     """Program => manipulate data in Main function: Operator are <= ; operand is FloatLiteral"""
    #     input = """float arr[4];
    #     void main () {
    #      float a, b;
    #      boolean isTrue;
    #      a = 11.0;
    #      b = 11;
    #      isTrue = a <= b ;
    #      putBoolLn(isTrue);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,560))

    # def test_61(self):
    #     """Program => manipulate data in Main function: Operator are > ; operand is IntLiteral"""
    #     input = """float arr[4];
    #     void main () {
    #      int arr[4], b;
    #      boolean isTrue;
    #      arr[0] = 11;
    #      arr[1] = arr[0] + 2;
    #      isTrue = arr[1] > 12 ;
    #      putBoolLn(isTrue);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,561))

    # def test_62(self):
    #     """Program => manipulate data in Main function: Operator are >= ; operand is FloatLiteral"""
    #     input = """float arr[4];
    #     void main () {
    #      float arr[4], b;
    #      boolean isTrue;
    #      arr[0] = 11.5;
    #      arr[1] = arr[0] + 2.5;
    #      isTrue = arr[1] >= 14.0 ;
    #      putBoolLn(isTrue);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,562))

    # def test_63(self):
    #     """Program => manipulate data in Main function: Operator are == ; operand is IntLiteral"""
    #     input = """float arr[4];
    #     void main () {
    #      boolean isTrue;
    #      int a, b, arr[2];
    #      isTrue = false;
    #      a = 14;
    #      b = 12;
    #      arr[0] = 14;
    #      isTrue = arr[0] == a;
    #      putBoolLn(isTrue);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,563))

    # def test_64(self):
    #     """Program => manipulate data in Main function: Operator are == ; operand is BoolLiteral"""
    #     input = """
    #     void main () {
    #      boolean arr[2];
    #      boolean a;
    #      boolean isTrue;
    #      a = false;
    #      arr[0] = !a;
    #      isTrue = arr[0] == !a;
    #      putBoolLn(isTrue);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,564))

    # def test_65(self):
    #     """Program => manipulate data in Main function: Operator are != ; operand is IntLiteral"""
    #     input = """
    #     void main () {
    #      int a, b;
    #      boolean isTrue;
    #      int arr[2];
    #      a = 10;
    #      b = 11;
    #      arr[0] = b%a + a;
    #      arr[1] = a%b + b;
    #      isTrue = arr[1] != arr[0];
    #      putBoolLn(isTrue);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,565))

    # def test_66(self):
    #     """Program => manipulate data in Main function: Operator are != ; operand is BoolLiteral"""
    #     input = """
    #     void main () {
    #      boolean a, b, isTrue;
    #      boolean arr[3];
    #      a = true;
    #      b = !true;
    #      arr[0] = !!a;
    #      arr[1] = !b;
    #      isTrue = arr[0] != !arr[1];
    #      putBoolLn(isTrue);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,566))

    # def test_67(self):
    #     """Program => manipulate data in Main function: Operator are && ; operand is BoolLiteral"""
    #     input = """
    #     void main () {
    #      boolean a, b, isTrue;
    #      boolean arr[3];
    #      a = true;
    #      b = !true;
    #      arr[0] = !!a;
    #      arr[1] = !b;
    #      isTrue = arr[0] && arr[1];
    #      putBoolLn(isTrue);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,567))

    # def test_68(self):
    #     """Program => manipulate data in Main function: Operator are || ; operand is BoolLiteral"""
    #     input = """
    #     void main () {
    #      boolean a, b, isTrue;
    #      boolean arr[3];
    #      a = true;
    #      b = !true;
    #      arr[0] = !!a;
    #      arr[1] = !b;
    #      isTrue = arr[0] || !arr[1];
    #      putBoolLn(isTrue);
    #     }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,568))

    # def test_69(self):
    #     """Program => manipulate data in Main function: Short-circuit evaluation : operator is &&"""
    #     input = """
    #     void main () {
    #      int a;
    #      boolean isTrue;
    #      isTrue = (a=1) == 1 && (a=3) == 3 && (a=6) == 5 && (a=8) == 8;
    #      putIntLn(a);
    #     }"""
    #     expect = "6\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,569))

    # def test_70(self):
    #     """Program => manipulate data in Main function: Short-circuit evaluation : operator is ||"""
    #     input = """
    #     void main () {
    #      int a;
    #      boolean isTrue;
    #      isTrue = (a=1) != 1 || (a=3) != 3 || (a=9) != 5 || (a=8) != 8;
    #      putIntLn(a);
    #     }"""
    #     expect = "9\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,570))

    # def test_71(self):
    #     """Program => manipulate data in Main function: Short-circuit evaluation : operator are || and &&"""
    #     input = """
    #     void main () {
    #      int a;
    #      boolean isTrue;
    #      isTrue = (a=1) != 1 || (a=3) != 3 && (a=9) != 5 || (a=8) != 8 || (a=11)!=11;
    #      putIntLn(a);
    #     }"""
    #     expect = "11\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,571))

    # def test_72(self):
    #     """another Program => manipulate data in Main function: Short-circuit evaluation : operator are || and &&"""
    #     input = """
    #     void main () {
    #      int a;
    #      boolean isTrue;
    #      isTrue = (a=1) != 1 && (a=3) != 3 && (a=9) != 5 || (a=8) != 8 && (a=11)!=11;
    #      putIntLn(a);
    #     }"""
    #     expect = "8\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,572))

    # def test_73(self):
    #     """Program => manipulate data in Main function: Combine operator: +,/,%,<,>,<=,>="""
    #     input = """int a,b,c;
    #     float fa,fb,fc;
    #     void main () {
    #      boolean isTrue;
    #      a = 1;
    #      b = a + 1;
    #      c = b % 1;
    #      fa = (a+b)/(c+a);
    #      fb = (fa+a)/(c+b);
    #      fc = fa * fb / c;
    #      isTrue = fa <= fb;
    #      putBoolLn(isTrue);
    #     }"""
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,573))

    # def test_74(self):
    #     """Program => manipulate data in Main function: Combine operator: +,-,*,/,%,<,>,<=,>=, ==, !="""
    #     input = """int a,b,c;
    #         float fa,fb,fc;
    #         void main () {
    #          boolean isTrue, isT, isF;
    #          a = 10;
    #          b = a * 2;
    #          c = b / 7;
    #          fa = (a*b)-(c/a);
    #          fb = a*(fa+a)*(c-b);
    #          fc = fa * fb / c;
    #          isT = fa < fc;
    #          isF = fb >= fa;
    #          isTrue = isT ==isF;
    #          putBoolLn(isTrue);
    #         }"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,574))

    # def test_75(self):
    #     """Program => manipulate data in Main function: Combine operator: +,-,*,/,%,<,>,<=,>=, ==, !=, &&, ||"""
    #     input = """int a,b,c;
    #     float fa,fb,fc;
    #     void main () {
    #      int arr[3];
    #      boolean isTrue, isT, isF;
    #      a = 10;
    #      b = a * 2;
    #      c = b / 7;
    #      arr[0] = c + b/2;
    #      arr[1] = a/2 + c/3;
    #      arr[2] = b*a/4 + c/4;
    #      fa = (arr[0]*b/a)-(c*arr[2]-arr[1]);
    #      fb = a*(fa+arr[2])*(c-arr[1]);
    #      fc = fa * fb / arr[2];
    #      isT = fa < fc;
    #      isF = fb >= fa;
    #      isTrue = isT || isF && (a = a + 3) < 17 || (c = a + 7) != 19 && (arr[2] = b + c) != 11;
    #      putInt(arr[2]);
    #     }"""
    #     expect = "50"
    #     self.assertTrue(TestCodeGen.test(input,expect,575))

    # def test_76(self):
    #     """Program => manipulate data in Main function: if no else stmt"""
    #     input = """
    #     void main () {
    #      int a;
    #      a = 1;
    #      if(a>1){
    #        a = 10;
    #      }
    #      putIntLn(a);
    #     }"""
    #     expect = "1\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,576))

    # def test_77(self):
    #     """Program => manipulate data in Main function: return stmt"""
    #     input = """
    #         void main () {
    #          float a;
    #          a = ax(2);
    #          putFloat(a);
    #         }
    #         float ax(int a){
    #         if(a==2)
    #          return 1.2;
    #         return 2.0;
    #     }"""
    #     expect = "1.2"
    #     self.assertTrue(TestCodeGen.test(input,expect,577))

    # def test_78(self):
    #     """Program => manipulate data in Main function: return void stmt"""
    #     input  = """
    #     void main () {
        
    #     }
    #     void foo(int a){
    #      if(a>1)
    #        return;
    #       else{
    #        a = a + 2;
    #        return;
    #       }
    #     }"""
    #     expect = ""
    #     self.assertTrue(TestCodeGen.test(input,expect,578))

    # def test_79(self):
    #     """Program => manipulate data in Main function:another return void stmt and print Int"""
    #     input = """
    #     void main () {
    #      int a;
    #      a = 1;
    #      test(a);
    #     }
    #     void test(int a){
    #      putInt(a);
    #     }"""
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,579))

    # def test_80(self):
    #     """Program => manipulate data in Main function: if-else stmt simple!(enter thenStmt)"""
    #     input = """
    #     void main () {
    #      int a;
    #      a = 2;
    #      if(a>1){
    #        a = 10;
    #      }
    #      else{
    #        a = 11;
    #      }
    #      putInt(a);
    #     }"""
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,580))

    # def test_81(self):
    #     """Program => manipulate data in Main function: if-else stmt simple!(enter elseStmt)"""
    #     input = """
    #     void main () {
    #      int a;
    #      a = 2;
    #      if(a>5){
    #        a = 10;
    #      }
    #      else{
    #        a = 11;
    #      }
    #      putInt(a);
    #     }"""
    #     expect = "11"
    #     self.assertTrue(TestCodeGen.test(input,expect,581))

    # def test_82(self):
    #     """Program => manipulate data in Main function: if no else stmt inner if-else stmt"""
    #     input = """
    #     void main () {
    #      int a;
    #      a = 2;
    #      if(a>5){
    #        if(a%2==0)
    #          a = a*2;
    #      }
    #      else{
    #        a = 11;
    #        if(a%3!=0)
    #          a = a*3;
    #      }
    #      putInt(a);
    #     }"""
    #     expect = "33"
    #     self.assertTrue(TestCodeGen.test(input,expect,582))

    # def test_83(self):
    #     """Program => manipulate data in Main function: if-else stmt inner if-else stmt"""
    #     input = """
    #     void main () {
    #      int a;
    #      a = 2;
    #      if(a>5){
    #        if(a%2==0)
    #          a = a*2;
    #        else
    #          a = a/2;
    #      }
    #      else{
    #        a = 11;
    #        if(a%3==0)
    #          a = a*3;
    #        else
    #          a = a*3/2;
    #      }
    #      putIntLn(a);
    #     }"""
    #     expect = "16\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,583))

    # def test_84(self):
    #     """Program => manipulate data in Main function: dowhile stmt simple!"""
    #     input = """
    #         void main () {
    #             int a;
    #             a = 1;
    #             do{
    #                 putInt(a);
    #                 a=a+1;
    #             } while(a<5);
    #         }"""
    #     expect = "1234"
    #     self.assertTrue(TestCodeGen.test(input,expect,584))

    # def test_85(self):
    #     """Program => manipulate data in Main function: dowhile stmt simple - It has continue stmt!"""
    #     input = """
    #     void main () {
    #      int a, iSum;
    #      a = 0;
    #      iSum = 0;
    #      do{
    #      a = a + 1;
    #      if(a%2==0)
    #        continue;
    #      iSum = iSum + a;
    #      }while(a<20);
    #      putInt(iSum);
    #     }"""
    #     expect = "100"
    #     self.assertTrue(TestCodeGen.test(input,expect,585))

    # def test_86(self):
    #     """Program => manipulate data in Main function: dowhile stmt simple - It has break stmt!"""
    #     input = """
    #     void main () {
    #      int a, iSum;
    #      a = 0;
    #      iSum = 0;
    #      do{
    #      a = a + 1;
    #      if(a>17)
    #        break;
    #      iSum = iSum + a;
    #      }while(a<20);
    #      putInt(iSum);
    #     }"""
    #     expect = "153"
    #     self.assertTrue(TestCodeGen.test(input,expect,586))

    # def test_87(self):
    #     """Program => manipulate data in Main function: dowhile stmt simple - It have continue stmt & break stmt!"""
    #     input = """
    #     void main () {
    #      int a, iSum;
    #      a = 0;
    #      iSum = 0;
    #      do{
    #      a = a + 1;
    #      if(a>17)
    #        break;
    #      if(a%2==0)
    #        continue;
    #      iSum = iSum + a;
    #      }while(a<20);
    #      putInt(iSum);
    #     }"""
    #     expect = "81"
    #     self.assertTrue(TestCodeGen.test(input,expect,587))

    # def test_88(self):
    #     """Program => manipulate data in Main function: dowhile stmt inner dowhile stmt!"""
    #     input = """
    #     void main () {
    #      int a,b, iSum;
    #      a = 0;
    #      b = 0;
    #      iSum = 0;
    #      do{
    #      b = 0;
    #      a = a + 1;
    #      do{
    #        b = b +1;
    #        iSum = iSum + b;
    #      }while(b<a);
    #      iSum = iSum + a;
    #      }while(a<20);
    #      putInt(iSum);
    #     }"""
    #     expect = "1750"
    #     self.assertTrue(TestCodeGen.test(input,expect,588))

    # def test_89(self):
    #     """Program => manipulate data in Main function: dowhile stmt inner dowhile stmt complex: It have break and continue stmt!"""
    #     input = """
    #     void main () {
    #      int a,b, iSum;
    #      a = 0;
    #      b = 0;
    #      iSum = 0;
    #      do{
    #      b = 0;
    #      a = a + 1;
    #      do{
    #        b = b +1;
    #        if(b>10)
    #          break;
    #        if(b%2==1)
    #          continue;
    #        iSum = iSum + b;
    #      }while(b<a);
    #      if(a%b==0)
    #        continue;
    #      if(a+b>40)
    #        break;
    #      iSum = iSum + a;
    #      }while(a<20);
        
    #      putIntLn(iSum);
    #     }"""
    #     expect = "554\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,589))

    # def test_90(self):
    #     """Program => manipulate data in Main function: for stmt simple"""
    #     input = """
    #     void main () {
    #      int a;
    #      for(a = 0; a < 10; a = a + 1){
    #        putInt(a);
    #        break;
    #      }
    #     }"""
    #     expect = "0"
    #     self.assertTrue(TestCodeGen.test(input,expect,590))

    # def test_91(self):
    #     """Program => manipulate data in Main function: for stmt simple: It has continue stmt"""
    #     input = """
    #     void main () {
    #      int a,b, iSum;
    #      iSum = 0;
    #      for(a = 0; a < 10; a = a + 1){
    #        if(a%2==0)
    #          continue;
    #        iSum = iSum + a;
    #      }
    #      putInt(iSum);
    #     }"""
    #     expect = "25"
    #     self.assertTrue(TestCodeGen.test(input,expect,591))

    # def test_92(self):
    #     """Program => manipulate data in Main function: for stmt simple: It has break stmt"""
    #     input = """
    #     void main () {
    #      int a,b, iSum;
    #      iSum = 0;
    #      for(a = 0; a < 10; a = a + 1){
    #        if(iSum > 27)
    #          break;
    #        iSum = iSum + a;
    #      }
    #      putInt(iSum);
    #     }"""
    #     expect = "28"
    #     self.assertTrue(TestCodeGen.test(input,expect,592))

    # def test_93(self):
    #     """Program => manipulate data in Main function: for stmt simple: It have continue stmt and break stmt"""
    #     input = """
    #     void main () {
    #      int a,b, iSum;
    #      iSum = 0;
    #      for(a = 0; a < 10; a = a + 1){
    #        if(iSum > 27)
    #          break;
    #        if(a%3!=0)
    #          continue;
    #        iSum = iSum + a;
    #      }
    #      putIntLn(iSum);
    #     }"""
    #     expect = "18\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,593))

    # def test_94(self):
    #     """Program => manipulate data in Main function: for stmt innner for stmt: It have continue stmt and break stmt"""
    #     input = """
    #     void main () {
    #      int a,b, iSum;
    #      iSum = 0;
    #      for(a = 0; a < 10; a = a + 1){
    #        for(b = 0; b < a ; b = b + 1){
    #          if(a+b>17)
    #            break;
    #          if(b%2==0)
    #            continue;
    #          iSum = iSum + b;
    #        }
    #        if(iSum > 27)
    #          break;
    #        if(a%3!=0)
    #          continue;
    #        iSum = iSum + a;
    #      }
    #      putIntLn(iSum);
    #     }"""
    #     expect = "37\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,594))

    # def test_95(self):
    #     """Program => manipulate data in Main function: block inner main block"""
    #     input = """int i,j;
    #     void main () {
    #      int a,b, iSum;
    #      i = 10;
    #      {
    #        float i;
    #        i = 11.8;
    #        putFloat(i);
    #      }
    #      {
    #        i = 11;
    #      }
    #      putIntLn(i);
    #     }"""
    #     expect = "11.811\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,595))

    # def test_96(self):
    #     """Program => manipulate data in Main function: block inner block"""
    #     input = """int i,j;
    #     void main () {
    #      int a,b, iSum;
    #      i = 10;
    #      {
    #        float i;
    #        i = 14.3;
    #        {
    #          int i;
    #          i = 19;
    #          putInt(i);
    #        }
    #        putFloat(i);
    #      }
    #      putInt(i);
    #     }"""
    #     expect = "1914.310" 
    #     self.assertTrue(TestCodeGen.test(input,expect,596))

    # def test_97(self):
    #     """Program => Funcall is stmt in main function"""
    #     input = """int a;
    #     void main () {
    #      int b;
    #      b = 5;
    #      foo(b);
    #      putFloat(foo(b));
    #     }
    #     int foo(int a){
    #      return a*a;
    #     }"""
    #     expect = "25.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,597))

    def test_98(self):
        """Program => Funcall is expression in BinaryOp in main function"""
        input = """
        void main () {
         putIntLn(foo());
        }
        int foo(){
         return 1;
        }"""
        expect = "1\n"
        self.assertTrue(TestCodeGen.test(input,expect,598))

    # def test_99(self):
    #     """Program => Funcall is expression in BinaryOp in main function - return type of Function is ArrayPointerType - FloatType"""
    #     input = """
    #     void main () {
    #      float arr[3];
    #      arr[2]=1.5;
    #      foo(arr);
    #      arr[2] = foo(arr)[2] + 1.1;
    #      putFloatLn(arr[2]);
    #     }
    #     float[] foo(float x[]){
    #      x[2] = 5.1;
    #      return x;
    #     }
    #     """
    #     expect = "6.2\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,599))

    # def test_100(self):
    #     """Program => Funcall is expression in BinaryOp in main function - return type of Function is ArrayPointerType - StringType"""
    #     input = """
    #     void main () {
    #      string arr[3];
    #      arr[2]="stringMain";
    #      arr[2] = foo(arr)[2];
    #      putStringLn(arr[2]);
    #     }
    #     string[] foo(string x[]){
    #      x[2] = "stringFoo";
    #      return x;
    #     }
    #     """
    #     expect = "stringFoo\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,600))

    # def test_101(self):
    #     """Program => return stmt in if-else stmt in function call"""
    #     input = """
    #     void main () {
    #      int a, b, res;
    #      a = 1;
    #      b = 1;
    #      res = foo(a,b);
    #      putIntLn(res);
    #     }
    #     int foo(int a, int b){
    #        if(a==b)
    #          return 111;
    #        else
    #          return 222;
    #     }
    #     """
    #     expect = "111\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,601))

    # def test_102(self):
    #     """Program => return stmt in if-else stmt in function call : Many complex function were checked"""
    #     input = """void main(){
    #      int a, b, res;
    #      a = 11;
    #      b = 12;
    #      res = foo(a,b);
    #      putIntLn(res);
    #     }
    #     int foo(int a, int b){
    #      if(a!=b){
    #        if(a!=1){
    #          a = a + 1;
    #        }else{
    #          if(b==1){
    #            return 1;
    #          }else{
    #            a = a + 3;
    #          }
    #        }
    #        return a;
    #      }else{
    #        return 0;
    #      }
    #     }
    #     int complex(int a, int b, int c){
    #      if(a!=b){
    #        return a;
    #      }else{
    #        if(c == b){
    #          return c;
    #        }else{
    #          return b;
    #        }
    #      }
    #     }
    #     """
    #     expect = "12\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,602))

    # def test_103(self):
    #     """Program => function main draw starts"""
    #     input = """void main(){
    #      int i,j,k;
    #      for(i=1;i<=7;i=i+1){
    #        for(j=1;j<=i;j=j+1)
    #          putInt(j);
    #        for(k=7-i;k>=1;k=k-1)
    #          putString("*");
    #        putString("");
    #      }
    #      putString("");
    #     }
    #     """
    #     expect = """1******12*****123****1234***12345**123456*1234567"""
    #     self.assertTrue(TestCodeGen.test(input,expect,603))

    # def test_104(self):
    #     """Special program => recursive factorial 10"""
    #     input = """
    #     int factorial(int i){
    #      if(i<=1){
    #        return 1;
    #      }
    #      return i * factorial(i - 1);
    #     }
    #     void main(){
    #      int i, j;
    #      i = 10;
    #      j = factorial(i);
    #      putIntLn(j);
    #     }
    #     """
    #     expect = "3628800\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,604))

    # def test_105(self):
    #     """Special program => recursive Fibonacci 10"""
    #     input = """
    #     int Fibonacci(int i){
    #      if(i==0){
    #        return 0;
    #      }
    #      if(i==1){
    #        return 1;
    #      }
    #      return Fibonacci(i - 1) + Fibonacci(i - 2);
    #     }
    #     void main(){
    #      int i;
    #      for(i = 0; i < 10; i = i + 1){
    #        putInt(Fibonacci(i));
    #      }
    #     }
    #     """
    #     expect = "0112358132134"
    #     self.assertTrue(TestCodeGen.test(input,expect,605))

