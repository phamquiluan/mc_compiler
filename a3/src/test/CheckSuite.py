import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
    def test_00(self):
        input = """
            int foo(){
                return 1;
            }
            void main(){}
            """
        expect="Unreachable function: foo"
        self.assertTrue(TestChecker.test(input,expect,400))


    def test_01(self):
        input = """
            int a(){}
            int a;
            void main(){
                a();
            }
            """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_02(self):
        input = """
            void main(){a(1,2);}
            int a(int a, float a){}
            """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,402))


    def test_03(self):
        input = """
            void main(){a();}
            int a(){
                int a,a;
            }
            """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_04(self):
        input = """
            void main(){a(true);}
            int a(boolean a){
                float a;
            }
            """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))
        
    def test_05(self):
       """More complex program"""
       input = """void main () {
           putIntLn();
        }"""
       expect = "Type Mismatch In Expression: " + str(CallExpr(Id("putIntLn"),[]))
       self.assertTrue(TestChecker.test(input,expect,405))

    def test_06(self):
       """More complex program"""
       input = """void main () {
           putIntLn(getInt(4));
       }"""
       expect = "Type Mismatch In Expression: " + str(CallExpr(Id("getInt"),[IntLiteral(4)]))
       self.assertTrue(TestChecker.test(input,expect,406))

    def test_07(self):
       """Simple program: int main() {} """
       input = Program([FuncDecl(Id("main"),[],VoidType(),Block([],[
           CallExpr(Id("foo"),[])]))])
       expect = "Undeclared Function: foo"
       self.assertTrue(TestChecker.test(input,expect,407))

    def test_08(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],VoidType(),Block([],[
                    CallExpr(Id("putIntLn"),[
                        CallExpr(Id("getInt"),[IntLiteral(4)])
                        ])]))])
        expect = "Type Mismatch In Expression: " + str(CallExpr(Id("getInt"),[IntLiteral(4)]))
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_09(self):
        """More complex program"""
        input = Program([
                FuncDecl(Id("main"),[],VoidType(),Block([],[
                    CallExpr(Id("putIntLn"),[])]))])
        expect = "Type Mismatch In Expression: " + str(CallExpr(Id("putIntLn"),[]))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_10(self):
        inp = "void main () {writeIntLn(3);}"
        out = "Undeclared Function: writeIntLn"
        self.assertTrue(TestChecker.test(inp,out,410))

    def test_11(self):
        inp = "void main () {getInt(3);}"
        out = "Type Mismatch In Expression: " + str(CallExpr(Id("getInt"), [IntLiteral(3)]))
        self.assertTrue(TestChecker.test(inp,out,411))

    def test_12(self):
        inp = "void main () {putIntLn();}"
        out =  "Type Mismatch In Expression: " + str(CallExpr(Id("putIntLn"), []))
        self.assertTrue(TestChecker.test(inp,out,412))

    def test_13(self):
        inp = Program([FuncDecl(Id("main"), [], VoidType(), Block([],[CallExpr(Id("putIntLn"), [])]))])
        out = "Type Mismatch In Expression: " + str(CallExpr(Id("putIntLn"), []))
        self.assertTrue(TestChecker.test(inp,out,413))

    def test_14(self):
        inp = """ 
            void main(){
                putIntLn(1.2);
            }
        """
        out = "Type Mismatch In Expression: " + str(CallExpr(Id("putIntLn"), [FloatLiteral(float(1.2))]))
        self.assertTrue(TestChecker.test(inp,out,414))

    def test_15(self):
        inp = """
        int number, iNum, iNum;
        void main(){}
        """
        out = "Redeclared Variable: iNum"
        self.assertTrue(TestChecker.test(inp,out,415))

    def test_16(self):
        inp = """
        int foo(int a, int a){
            return 1;
        }
        void main(){
            foo(1,2);
        }
        """
        out = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(inp,out,416))

    def test_17(self):
        inp = """int foo(int a){
        int arr;
        float arr;
        }
        void main(){foo(1);}
        """
        out = "Redeclared Variable: arr" 
        self.assertTrue(TestChecker.test(inp,out,417))

    def test_18(self):
        inp = """int foo(int a){
        int a;
        float arr;
        }
        void main(){
            foo(1);
        }
        """
        out = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(inp,out,418))

    def test_19(self):
        inp = """
            int foo(){
                { 
                    int i,j,j;
                } 
            }
            void main(){
                foo();
            }
            """
        out = "Redeclared Variable: j"
        self.assertTrue(TestChecker.test(inp,out,419))

    def test_20(self):
        inp = """int a,b;
        int foo(int a,int b){
            return 1;
        }
        int a; 
        void main(){
            foo(1,2);
        }
        """
        out = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(inp,out,420))

    def test_21(self):
        inp = """
        void main(){

        }
        void main(){
            int a,b;
            float fNum;
        }"""
        out = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(inp,out,421))

    def test_22(self):
        inp = """
        int main;
        void main(){
            int a,b;
            float fNum;
        }"""
        out = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(inp,out,422))

    def test_23(self):
        inp = """
        int number;
        void main(){
            int a,b;
            float fNum;
        }
        int main;"""
        out = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(inp,out,423))

    def test_24(self):
        inp = """
        int number[10];
        void main(){
            int b;
            float fNum;
        }
        int number;"""
        out = "Redeclared Variable: number"
        self.assertTrue(TestChecker.test(inp,out,424))

    def test_25(self):
        inp = """
        int number[10];
        void main(){
            int ar,b;
            float fNum;
            foo(1,2);
        }
        int foo(int a, int b){
            int ar, br;
        }
        float number;"""
        out = "Redeclared Variable: number"
        self.assertTrue(TestChecker.test(inp,out,425))

    def test_26(self):
        inp = """
        int number[10];
        void main(){
            int ar,b;
            float fNum;
            foo(1,2,"hihi");
        }
        int foo(int a, int b, string a){
            int ar, br;
        }
        float numberOne;"""
        out = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(inp,out,426))

    def test_27(self):
        inp = """
        int number[10];
        void main(){
            int ar,b;
            float fNum;
            foo(1,2,"hihi");
        }
        int foo(int a, int b, string str){
            int ar, br;
        }
        float numberOne;
        void foo(int a, int c){

        }"""
        out = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(inp,out,427))

    def test_28(self):
        inp = """
        int number[10];
        void main(){
            int ar,b;
            float fNum;
            foo(1,2,"a");
        }
        int foo(int a, int b, string str){
            int ar, br;
            {
                int a;
                {
                    int abc;
                    int abc;
                }
            }
        }
        float numberOne;"""
        out = "Redeclared Variable: abc"
        self.assertTrue(TestChecker.test(inp,out,428))

    def test_29(self):
        inp = """
        int a[10],c;
        int foo(int size, int arr[]){
            int number;
            b;
        }
        void main(){
            int a[1];
            foo(10,a);
        }
        """
        out = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(inp,out,429))

    def test_30(self):
        inp = """
        int a[10],c;
        int foo(int size, int arr[]){
            int iNum;
            a[1]=number;
        }
        void main(){
            int a[1];
            foo(10,a);   
        }
        """
        out = "Undeclared Identifier: number"
        self.assertTrue(TestChecker.test(inp,out,430))

    def test_31(self):
        inp = """
        int a[10],c;
        int foo(int size, int arr[]){
            int iNum;
            if(true){
                h = 1;
            }
        }
        void main(){
            int a[1];
            foo(10,a);
        }
        """
        out = "Undeclared Identifier: h"
        self.assertTrue(TestChecker.test(inp,out,431))

    def test_32(self):
        inp = """
        int foo(){
            for(h; iNum < 10; iNum = iNum *2){ }
            return 1;
        }
        void main(){
            foo();
        }
        """
        out = "Undeclared Identifier: h"
        self.assertTrue(TestChecker.test(inp,out,432))

    def test_33(self):
        inp = """
        int a[10],c;
        int foo(int size, int arr[]){
            int iNum;
            for(iNum = 1; iNum < 10; iNum = iNum *2){
                num;
            }
            return 1;
        }
        void main(){
            int a[1];
            foo(10,a);
        }
        """
        out = "Undeclared Identifier: num"
        self.assertTrue(TestChecker.test(inp,out,433))

    def test_34(self):
        inp = """
        int a[10],c;
        int foo(int size, int arr[]){
            int iNum;
            do{
                iNum = 1;
            }while(numberOne);

            return 1;
        }
        void main(){
            int a[1];
            foo(10,a);
        }
        """
        out = "Undeclared Identifier: numberOne"
        self.assertTrue(TestChecker.test(inp,out,434))

    def test_35(self):
        inp = """
        int a[10],c;
        int foo(int size, int arr[]){
            int iNum;
            do{
                iNum = 1;
                numberOne;
            }
            while(iNum<10);

            return 1;
        }
        void main(){
            int a[1];
            foo(10,a);
        }
        """
        out = "Undeclared Identifier: numberOne"
        self.assertTrue(TestChecker.test(inp,out,435))

    def test_36(self):
        inp = """
        int a[10],c;
        int foo(int size, int arr[]){
            int iNum;
            if(true){
                iNum = 1;
            }
            else{
                inum = 10;
            }
            return 1;
        }
        void main(){
            int a[1];
            foo(10,a);
        }
        """
        out = "Undeclared Identifier: inum"
        self.assertTrue(TestChecker.test(inp,out,436))

    def test_37(self):
        inp = """
        int a[10],c;
        int m(int size, int arr[]){
            foo();
        }
        void main(){
            int a[1];
            m(10,a);
        }
        """
        out = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(inp,out,437))

    def test_38(self):
        inp = """
        int a[10],c;
        void m(int size, int arr[]){
            {complex(10);}
        }
        void main(){
            int a[1];
            m(10,a);
        }
        """
        out = "Undeclared Function: complex"
        self.assertTrue(TestChecker.test(inp,out,438))

    def test_39(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            int i;
            if(true){
                size = i;
            }
            else{
                complex(10);
            }
        }
        """
        out = "Undeclared Function: complex"
        self.assertTrue(TestChecker.test(inp,out,439))

    def test_40(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            int i;
            for(i = 0; i < 100; i = i + 1){
                foo();
            }
        }
        """
        out = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(inp,out,440))

    def test_41(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            int i;
            do{
                complex();
            }
            while(true);
        }
        """
        out = "Undeclared Function: complex"
        self.assertTrue(TestChecker.test(inp,out,441))

    def test_42(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            int i;
            if(i){
                i = 0;
            }
        }
        """
        out = "Type Mismatch In Statement: " + str(If(Id("i"),Block([],[BinaryOp("=",Id("i"),IntLiteral(int(0)))]),None))
        self.assertTrue(TestChecker.test(inp,out,442))

    def test_43(self):
        inp = """int a[10],c;
         void main(){
            int size;
            int i;
            if(10.5){
                i = 0;
            }
         }
        """
        out = "Type Mismatch In Statement: " + str(If(FloatLiteral(float(10.5)),Block([],[BinaryOp("=",Id("i"),IntLiteral(int(0)))]),None))
        self.assertTrue(TestChecker.test(inp,out,443))

    def test_44(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            int i;
            if("true"){
                i = 0;
            }
        }
        """
        out = "Type Mismatch In Statement: " + str(If(StringLiteral("true"),Block([],[BinaryOp("=",Id("i"),IntLiteral(int(0)))]),None))
        self.assertTrue(TestChecker.test(inp,out,444))

    def test_45(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            int i;
            for(true; i< 10; i= i+1){
            }
        }
        """
        out = "Type Mismatch In Statement: " + str(For(BooleanLiteral(True),BinaryOp("<",Id("i"),IntLiteral(int(10))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([],[])))
        self.assertTrue(TestChecker.test(inp,out,445))

    def test_46(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            float j;
            int i;
            for(j = 14.3; i< 10; i= i+1){ }
        }
        """
        out = "Type Mismatch In Statement: " + str(For(BinaryOp("=",Id("j"),FloatLiteral(float(14.3))),BinaryOp("<",Id("i"),IntLiteral(int(10))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(int(1)))),Block([],[])))
        self.assertTrue(TestChecker.test(inp,out,446))

    def test_47(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            float j;
            int i;
            for(i=1; i = size +10; i= i+1){ }
        }
        """
        out = "Type Mismatch In Statement: " + str(For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("=",Id("i"),BinaryOp("+",Id("size"),IntLiteral(10))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([],[])))
        self.assertTrue(TestChecker.test(inp,out,447))

    def test_48(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            float j;
            int i;
        for(i=1; j = 10.5; i= i+1){ }
        }
        """
        out = "Type Mismatch In Statement: " + str(For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("=",Id("j"),FloatLiteral(float(10.5))),BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([],[])))
        self.assertTrue(TestChecker.test(inp,out,448))

    def test_49(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            float j;
            int i;
            for(i=1; i < 10; 14.3){ }
        }
        """
        out = "Type Mismatch In Statement: " + str(For(BinaryOp("=",Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),FloatLiteral(float(14.3)),Block([],[])))
        self.assertTrue(TestChecker.test(inp,out,449))

    def test_50(self):
        inp = """int a[10],c;
        void main(){
        int size;
        float j;
        int i;
        do{
         i = i + 1;
        }while(i);
        }
        """
        out = "Type Mismatch In Statement: " + str(Dowhile([Block([],[BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],Id("i")))
        self.assertTrue(TestChecker.test(inp,out,450))

    def test_51(self):
        inp = """int a[10],c;
        void main(){
        int size;
        float j;
        int i;
        do{
         i = i + 1;
        }while("false");
        }"""
        out = "Type Mismatch In Statement: " + str(Dowhile([Block([],[BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],StringLiteral("false")))
        self.assertTrue(TestChecker.test(inp,out,451))

    def test_52(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            float j;
            int i;
            do{
                i = i + 1;
            }while(15.10);
        }
        """
        out = "Type Mismatch In Statement: " + str(Dowhile([Block([],[BinaryOp("=",Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],FloatLiteral(float(15.1))))
        self.assertTrue(TestChecker.test(inp,out,452))

    def test_53(self):
        inp =  """int a[10],c;
        void main(){
        int size;
        float j;
        int i;
        return i;
        }"""
        out = "Type Mismatch In Statement: " + str(Return(Id("i")))
        self.assertTrue(TestChecker.test(inp,out,453))

    def test_54(self):
        inp = """
        int a[10],c;
        void main(){
            int size;
            float j;
            int i;
            return "void";
        }
        """
        out = "Type Mismatch In Statement: " + str(Return(StringLiteral("void")))
        self.assertTrue(TestChecker.test(inp,out,454))

    def test_55(self):
        inp =  """
        int a[10],c;
        int complex(){
            int size;
            float j;
            int i;
            return 10.6;
        }
        void main(){}
        """
        out = "Type Mismatch In Statement: " + str(Return(FloatLiteral(float(10.6))))
        self.assertTrue(TestChecker.test(inp,out,455))

    def test_56(self):
        inp = """
        int a[10],c;
        int complex(){
            int size;
            float j;
            int i;
            return true;
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(BooleanLiteral(True)))
        self.assertTrue(TestChecker.test(inp,out,456))

    def test_57(self):
        inp = """
        int a[10],c;
        int complex(){
            int size;
            float j;
            int i;
            return;
        }
        void main(){ complex();}
      """
        out = "Type Mismatch In Statement: " + str(Return(None))
        self.assertTrue(TestChecker.test(inp,out,457))

    def test_58(self):
        inp = """
        int a[10],c;
        float complex(){
            int size;
            float j;
            boolean isTrue;
            int i;
            isTrue = true;
            return isTrue;
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(Id("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,458))

    def test_59(self):
        inp = """
        int a[10],c;
        float complex(){
            int size;
            float j;
            boolean isTrue;
            int i;
            isTrue = true;
            return "isTrue";
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(StringLiteral("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,459))


    def test_60(self):
        inp = """
        int a[10],c;
        string complex(){
            int size;
            float j;
            boolean isTrue;
            int i;
            isTrue = true;
            return isTrue;
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(Id("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,460))

    def test_61(self):
        inp = """
        int a[10],c;
        string complex(){
            int size;
            float j;
            boolean isTrue;
            int i;
            isTrue = true;
            return;
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(None))
        self.assertTrue(TestChecker.test(inp,out,461))

    def test_62(self):
        inp = """
        int a[10],c;
        boolean complex(){
            int size;
            float j;
            boolean isTrue;
            int i;
            isTrue = true;
            return 14;
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(IntLiteral(14)))
        self.assertTrue(TestChecker.test(inp,out,462))

    def test_63(self):
        inp = """
        int a[10],c;
        boolean complex(){
            int size;
            float j;
            boolean isTrue;
            int i;
            isTrue = true;
            return 14.5;
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(FloatLiteral(float(14.5))))
        self.assertTrue(TestChecker.test(inp,out,463))

    def test_64(self):
        inp = """
        int a[10],c;
        boolean complex(){
            int size;
            float j;
            boolean isTrue;
            int i;
            isTrue = true;
            return;
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(None))
        self.assertTrue(TestChecker.test(inp,out,464))

    def test_65(self):
        inp = """
        int a[10],c;
        int[] complex(){
            int size;
            float j;
            boolean isTrue;
            int i;
            isTrue = true;
            return;
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(None))
        self.assertTrue(TestChecker.test(inp,out,465))

    def test_66(self):
        inp = """
        int a[10],c;
        int[] complex(){
            int size;
            float j;
            boolean isTrue;
            int i;
            isTrue = true;
            return i+1;
        }
        void main(){ complex();}
        
        """
        out = "Type Mismatch In Statement: " + str(Return(BinaryOp("+",Id("i"),IntLiteral(1))))
        self.assertTrue(TestChecker.test(inp,out,466))

    def test_67(self):
        inp = """
        int a[10],c;
        int[] complex(){
            int size;
            float j;
            boolean isTrue;
            int i;
            isTrue = true;
            return i+1.5;
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(BinaryOp("+",Id("i"),FloatLiteral(float(1.5)))))
        self.assertTrue(TestChecker.test(inp,out,47))

    def test_68(self):
        inp = """
        int a[10],c;
        int[] complex(){
            int size;
            float j;
            boolean isTrue;
            int i;
            isTrue = true;
            return isTrue;
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(Id("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,468))

    def test_69(self):
        inp = """
        int a[10],c;
        int[] complex(){
            int size;
            float j;
            boolean isTrue;
            int i;
            isTrue = true;
            return "true";
        }
        void main(){complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(StringLiteral("true")))
        self.assertTrue(TestChecker.test(inp,out,469))

    def test_70(self):
        inp = """
        int a[10],c;
        int[] complex(){
            int size;
            float j[10];
            boolean isTrue;
            int i;
            isTrue = true;
           return j;
        }
        void main(){complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(Id("j")))
        self.assertTrue(TestChecker.test(inp,out,470))

    def test_71(self):
        inp = """
        int a[10],c;
        int[] complex(){
            int size;
            float j[10];
            boolean isTrue[10];
            int i;
            return isTrue;
        }
        void main(){complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(Id("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,471))

    def test_72(self):
        inp = """
        int a[10],c;
        int[] complex(){
            int size;
            string arr[10];
            float j[10];
            boolean isTrue[10];
            int i;
            return arr;
        }
        void main(){complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(Id("arr")))
        self.assertTrue(TestChecker.test(inp,out,472))

    def test_73(self):
        inp = """
        int a[10],c;
        float[] foo(){
            float a[1];
            return a;
        }
        int[] complex(){
            int size;
            string arr[10];
            float j[10];
            boolean isTrue[10];
            int i;
            return foo();
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(CallExpr(Id("foo"),[])))
        self.assertTrue(TestChecker.test(inp,out,473))

    def test_74(self):
        inp = """
        int a[10],c;
        boolean[] foo(){
            boolean a[1];
            return a;
        }
        int[] complex(){
            int size;
            string arr[10];
            float j[10];
            boolean isTrue[10];
            int i;
            return foo();
        }
        void main(){complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(CallExpr(Id("foo"),[])))
        self.assertTrue(TestChecker.test(inp,out,474))

    def test_75(self):
        inp = """
        int a[10],c;
        string[] foo(){
            string a[1];
            return a;
        }
        int[] complex(){
            int size;
            string arr[10];
            float j[10];
            boolean isTrue[10];
            int i;
            return foo();
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(CallExpr(Id("foo"),[])))
        self.assertTrue(TestChecker.test(inp,out,475))

    def test_76(self):
        inp = """int a[10],c;
        string[] foo(){
            string a[1];
            return a;
        }
        int complex(){
            int size;
            string arr[10];
            float j[10];
            boolean isTrue[10];
            int i;
            return foo();
        }
        void main(){ complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(CallExpr(Id("foo"),[])))
        self.assertTrue(TestChecker.test(inp,out,476))

    def test_77(self):
        inp = """
        int a[10],c;
        int[] foo(){
            int a[1];
            return a;
        }
        int complex(){
            int size;
            string arr[10];
            float j[10];
            boolean isTrue[10];
            int i;
            return foo();
        }
        void main(){complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(CallExpr(Id("foo"),[])))
        self.assertTrue(TestChecker.test(inp,out,477))

    def test_78(self):
        inp = """
        int a[10],c;
        float[] foo(){
            float h[10];
            return h;
        }
        float complex(){
            int size;
            string arr[10];
            float j[10];
            boolean isTrue[10];
            int i;
            return foo();
        }
        void main(){complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(CallExpr(Id("foo"),[])))
        self.assertTrue(TestChecker.test(inp,out,478))

    def test_79(self):
        inp = """
        int a[10],c;
        string[] foo(){
            string a[3];
            return a;
        }

        string complex(){
            int size;
            string arr[10];
            float j[10];
            boolean isTrue[10];
            int i;
            return foo();
        }

        void main(){complex();}
        """
        out = "Type Mismatch In Statement: " + str(Return(CallExpr(Id("foo"),[])))
        self.assertTrue(TestChecker.test(inp,out,479))

    def test_80(self):
        inp = """
        int a[10],c;
        void main(){
            int arr[10];
            float fNum;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            arr[fNum];
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("arr"),Id("fNum")))
        self.assertTrue(TestChecker.test(inp,out,40))

    def test_81(self):
        inp = """
        int a[10],c;
        void main(){
            int arr[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            arr[isTrue];
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("arr"),Id("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,481))

    def test_82(self):
        inp = """
        int a[10],c;
        void main(){
            int arr[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            arr["isTrue"];
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("arr"),StringLiteral("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,482))

    def test_83(self):
        inp = """
        void main(){
            int arr[10];
            int b;
            arr[b];
        }
        """
        out = "[]"
        # out = "Type Mismatch In Expression: " + str(ArrayCell(Id("arr"),Id("b")))
        self.assertTrue(TestChecker.test(inp,out,483))

    def test_84(self):
        inp = """
        int a[10],c;
        int[] foo(){
            int a[10];
            return a;
        }
        void main(){
            int arr[10];
            int b[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            arr[foo()];
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("arr"),CallExpr(Id("foo"),[])))
        self.assertTrue(TestChecker.test(inp,out,484))

    def test_85(self):
        inp = """
        int a[10];
        void main(){
            int a;
            a[10];
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"),IntLiteral(10)))
        self.assertTrue(TestChecker.test(inp,out,485))

    def test_86(self):
        inp = """
        int a[10],c;
        int[] foo(){
            int a[10];
            return a;
        }
        void main(){
            string a;
            int arr[10];
            int b[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            a[10];
            foo();
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"),IntLiteral(10)))
        self.assertTrue(TestChecker.test(inp,out,486))

    def test_87(self):
        inp = """
        int a[10],c;
        int[] foo(){
            int a[10];
            return a;
        }
        void main(){
            float a;
            int arr[10];
            int b[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            a[10];
            foo();
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"),IntLiteral(10)))
        self.assertTrue(TestChecker.test(inp,out,487))

    def test_88(self):
        inp = """
        int a[10],c;
        int[] foo(){
            int a[10];
            return a;
        }
        void main(){
            boolean a;
            int arr[10];
            int b[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            a[10];
            foo();
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(Id("a"),IntLiteral(10)))
        self.assertTrue(TestChecker.test(inp,out,488))

    def test_89(self):
        inp = """
        int a[10],c;
        int foo(){
            int a;
            return a;
        }
        void main(){
            boolean a;
            int arr[10];
            int b[10];
            float fNum;
            boolean isTrue;
            fNum = 1;
            arr[1] = 1;
            arr[2] = arr[1];
            foo()[10];
        }
        """
        out = "Type Mismatch In Expression: " + str(ArrayCell(CallExpr(Id("foo"),[]),IntLiteral(10)))
        self.assertTrue(TestChecker.test(inp,out,489))

    def test_90(self):
        inp = """
        int a[10],b,arr;
        void main(){
            int iNum;
            float fNum;
            fNum = 1;
            iNum = fNum;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("=",Id("iNum"),Id("fNum")))
        self.assertTrue(TestChecker.test(inp,out,490))

    def test_91(self):
        inp =  """
        int a[10],b,arr;
        void main(){
            int iNum;
            float fNum;
            boolean isTrue;
            isTrue = true;
            fNum = isTrue;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("=",Id("fNum"),Id("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,491))

    def test_92(self):
        inp = """
        int a[10],b,arr;
        void main(){
            string str;
            int iNum;
            float fNum;
            boolean isTrue;
            isTrue = true;
            str = isTrue;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("=",Id("str"),Id("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,492))

    def test_93(self):
        inp = """
        int a[10],b,arr;
        void main(){
            string str;
            int iNum;
            int arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            a=arr;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("=",Id("a"),Id("arr")))
        self.assertTrue(TestChecker.test(inp,out,493))

    def test_94(self):
        inp = """
        int a[10],b,arr;
        void main(){
            string str;
            int iNum;
            int arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            arr = foo(iNum);
        }
        int[] foo(int a){
            int arr[10];
            return arr;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("=",Id("arr"),CallExpr(Id("foo"),[Id("iNum")])))
        self.assertTrue(TestChecker.test(inp,out,494))

    def test_95(self):
        inp = """
        int a[10],b,arr;
        void main(){
            string str;
            int iNum;
            int arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            foo(iNum) = arr;
        }
        int[] foo(int a){
            int arr[10];
            return arr;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("=",CallExpr(Id("foo"),[Id("iNum")]),Id("arr")))
        self.assertTrue(TestChecker.test(inp,out,495))

    def test_96(self):
        inp = """
        int a[10],b,arr;
        void main(){
            string str;
            int iNum;
            int arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            foo(iNum) = foo(iNum+1);
        }
        int[] foo(int a){
            int arr[10];
            return arr;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("=",CallExpr(Id("foo"),[Id("iNum")]),CallExpr(Id("foo"),[BinaryOp("+",Id("iNum"),IntLiteral(1))])))
        self.assertTrue(TestChecker.test(inp,out,496))

    def test_97(self):
        inp = """
        int a[10],b,arr;
        void main(){
            string str;
            int iNum;
            int arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            foo(fNum);
        }
        int foo(int a){
            int arr;
            return arr;
        }
        """
        out = "Type Mismatch In Expression: " + str(CallExpr(Id("foo"),[Id("fNum")]))
        self.assertTrue(TestChecker.test(inp,out,497))

    def test_98(self):
        inp = """
        int a[10],b,arr;
        void main(){
            string str;
            int iNum;
            int arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
        foo();
        }
        int foo(int a){
            int arr;
            return arr;
        }
        """
        out = "Type Mismatch In Expression: " + str(CallExpr(Id("foo"),[]))
        self.assertTrue(TestChecker.test(inp,out,498))

    def test_99(self):
        inp = """
        int a[10],b,arr;
        void main(){
            string str;
            int iNum;
            int arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            foo(iNum);
        }
        int foo(int a[]){
            int arr;
            return arr;
        }
        """
        out = "Type Mismatch In Expression: " + str(CallExpr(Id("foo"),[Id("iNum")]))
        self.assertTrue(TestChecker.test(inp,out,499))

    def test_100(self):
        inp = """
        int a[10],b;
        void main(){
            string str;
            int iNum;
            float arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            foo(arr);
        }
        int foo(int a[]){
            int arr;
            return arr;
        }
        """
        out = "Type Mismatch In Expression: " + str(CallExpr(Id("foo"),[Id("arr")]))
        self.assertTrue(TestChecker.test(inp,out,500))

    def test_101(self):
        inp = """
        void main(){
            int iNum;
            foo(complex(iNum));
        }
        int foo(int a[]){
            int arr;
            return arr;
        }
        float[] complex(int a){
            float frr[11];
            return frr;
        }
        """
        out = "Type Mismatch In Expression: " + str(CallExpr(Id("foo"),[CallExpr(Id("complex"),[Id("iNum")])]))
        self.assertTrue(TestChecker.test(inp,out,501))

    def test_102(self):
        inp = """
        int a[10],b;
        void main(){
            string str;
            int iNum;
            float arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            isTrue = !fNum;
        }
        """
        out = "Type Mismatch In Expression: " + str(UnaryOp("!",Id("fNum")))
        self.assertTrue(TestChecker.test(inp,out,502))

    def test_103(self):
        inp = """
        int a[10],b;
        void main(){
            string str;
            int iNum;
            float arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            isTrue = -str;
        }
        """
        out = "Type Mismatch In Expression: " + str(UnaryOp("-",Id("str")))
        self.assertTrue(TestChecker.test(inp,out,503))

    def test_104(self):
        inp = """
        int a[10],b;
        void main(){
            string str;
            int iNum;
            float arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            isTrue = -isTrue;
        }
        """
        out = "Type Mismatch In Expression: " + str(UnaryOp("-",Id("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,504))

    def test_105(self):
        inp = """
        int a[10],b;
        void main(){
            string str;
            int iNum;
            float arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            str + isTrue;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("+",Id("str"),Id("isTrue")))
        self.assertTrue(TestChecker.test(inp,out,505))

    def test_106(self):
        inp = """
        int a[10],b;
        void main(){
            string str;
            int iNum;
            float arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            isTrue <= true;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("<=",Id("isTrue"),BooleanLiteral(True)))
        self.assertTrue(TestChecker.test(inp,out,506))

    def test_107(self):
        inp = """
        int a[10],b;
        void main(){
            string str;
            int iNum;
            float arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            fNum = 15;
            fNum = fNum%10;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("%",Id("fNum"),IntLiteral(10)))
        self.assertTrue(TestChecker.test(inp,out,507))

    def test_108(self):
        inp = """
        int a[10],b;
        void main(){
            string str;
            int iNum;
            float arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            fNum = 15;
            fNum != 15;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("!=",Id("fNum"),IntLiteral(15)))
        self.assertTrue(TestChecker.test(inp,out,508))

    def test_109(self):
        inp = """
        int a[10],b;
        void main(){
            string str;
            int iNum;
            float arr[10];
            float fNum;
            boolean isTrue;
            isTrue = true;
            fNum = 15;
            iNum = 15;
            iNum && fNum;
        }
        """
        out = "Type Mismatch In Expression: " + str(BinaryOp("&&",Id("iNum"),Id("fNum")))
        self.assertTrue(TestChecker.test(inp,out,509))

    # break / cont
    def test_110(self):
        inp = """
        void main(){
            foo();
        }
        void foo(){
            do{
                2;
            } while (true);
            break;
        }
        """
        out = "Break Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,510))


    def test_111(self):
        inp = """
        void main(){
            for(1;true;1) 1;
            break;
            return;
        }"""
        out = "Break Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,511))

    def test_112(self):
        inp = """
        void main() {
            int i;
            for (i; i < 5; i = i + 2) {
              i = i + 1;
            }
            continue;
        }
        """
        out = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,512))

    def test_129(self):
        inp = """
        void main(){
            continue;
        }
        """
        out = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,529))

    def test_130(self):
        inp = """
        void main(){
            for(1;true;1){if(true) continue;}
            if(true) { 
                for(1;true;1){ 
                    if(true) break; 
                } 
                continue;
            } 
            else { }
        }
        """
        out = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,530))

    def test_131(self):
        inp = """
        void main(){
            if(true) { 
                for(1;true;1) { continue; } 
                if(false) { continue;} 
            }
        }
        """
        out = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,531))

    def test_132(self):
        inp = """
        void main(){
            for(1;true;1) { 
                if(true) continue; 
            }
            do 
                if(true) continue; 
                else { continue;} 
            while(true);
            if(false) {} 
            else continue;
        }
        """
        out = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,532))

    def test_133(self):
        inp = """
        void main(){
            for(1;true;1) {
                if(true) continue; 
                else { continue;} 
                "hihis";
            }
        }
        """
        out = "Unreachable statement: StringLiteral(hihis)"
        self.assertTrue(TestChecker.test(inp,out,533))

    def test_134(self):
        inp = """
        void main(){
            for(1;true;1) {
                if(true) continue; 
                else { break;} 
                "hihis";
            }
        }
        """
        out = "Unreachable statement: StringLiteral(hihis)"
        self.assertTrue(TestChecker.test(inp,out,534))

    def test_135(self):
        inp = """
        void main(){
            for(1;true;1) {
                if(true) return; 
                else { break;} 
                "hihis";
            }
        }
        """
        out = "Unreachable statement: StringLiteral(hihis)"
        self.assertTrue(TestChecker.test(inp,out,535))

    def test_136(self):
        inp = """
        void main(){
            for(1;true;1) { 
                do if(true) break; else {continue;} while(true); if(true) continue; }
                do if(true) continue; else {continue;} while(true);
                if(false) { } 
                else { { 
                    { 
                        { 
                            { int a; continue; } 
                        } 
                    } 
                } 
            }
        }
        """
        out = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,536))

    def test_137(self):
        inp = """
         void main(){
          do if(true) break; else {continue;} while(true);
          for(1;true;1) { if(true) continue; }
          do if(false) break; else {} while(true);
          continue;
        }
        """
        out = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(inp,out,537))

    





    # not return 
    def test_113(self):
        inp = """
        void main(){ foo(1); }
        int foo(int a){ }
        """
        out = "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,513))

    def test_114(self):
        inp = """
        void main(){ foo(1,1); }
        int foo(int a,float b){
            if(true){ } 
            else {
                return 2;
            } 
        }
        """
        out = "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,514))

    def test_122(self):
        inp = """
        void main(){ foo(); }
        int foo(){
            int x;
            do
                x=0;
            while(true);
        }
        """
        out = "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,522))
    
    def test_123(self):
        inp = """
        void main(){ foo(); }
        int foo(){
            if(true) return 1;
        }"""
        out = "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,523))

    def test_124(self):
        inp = """
        void main(){ foo(); }
        int foo(){
            if(true) 1; 
            else return 1;
        }"""
        out = "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,524))

    def test_125(self):
        inp = """
        void main(){ foo(); }
        int foo(){
            if(true) 1; 
            else 1;
        }"""
        out = "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,525))

    def test_126(self):
        inp = """
        void main(){ foo(3); }
        int foo(int b){
            for(1;true;1) return 1;
        }
        """
        out =  "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,526))

    def test_127(self):
        inp =  """
        void main(){ foo(2); }
        int foo(int a){
            a = 1;
        }
        """  
        out = "Function foo Not Return "
        self.assertTrue(TestChecker.test(inp,out,527))

    def test_128(self):
        inp = """
        string getString(){return "Abc";}
        void func(){ }
        void main(){
            func();
            getString();
            haha();
        }
        boolean haha(){ }
        """
        out = "Function haha Not Return "
        self.assertTrue(TestChecker.test(inp,out,528))





    # unreach
    def test_115(self):
        inp = """
        void main(){
            return;
            0;
        }
        """
        out = "Unreachable statement: " + str(IntLiteral(0))
        self.assertTrue(TestChecker.test(inp,out,515))

    def test_116(self):
        inp = """
        void main(){
            for(1;true;1){
                break;
                continue;
                2;
            }
            return;
        }"""
        out = "Unreachable statement: " + str(Continue())
        self.assertTrue(TestChecker.test(inp,out,516))

    def test_117(self):
        inp = """
        void main(){ }
        int static_void_main(){
            int a,b;
            float result;
            if(a>b) a;
            else return a;
            do
                continue;
                if(a>1) return a; 
                else return b;
            while (true);
            return 1;
        }
        """
        out = "Unreachable statement: " + str(If(BinaryOp(">",Id("a"),IntLiteral(1)),Return(Id("a")),Return(Id("b"))))
        self.assertTrue(TestChecker.test(inp,out,517))

    def test_118(self):
        inp = """
        void main(){
            do
                {continue;}
                {1;}
            while(true);
            return;
        }
        """
        out = "Unreachable statement: "+str(Block([],[IntLiteral(1)]))
        self.assertTrue(TestChecker.test(inp,out,518))

    def test_119(self):
        inp = """
        void main(){ }
        float f;
        int checkOddNumber(int n){
            if(n%2==0)
                return n;
            else
                return checkOddNumber(n+1);
            n=1%n;
        }
        """
        out = "Unreachable statement: "+str(BinaryOp("=",Id("n"),BinaryOp("%",IntLiteral(1),Id("n"))))
        self.assertTrue(TestChecker.test(inp,out,519))

    def test_120(self):
        inp = """
        void main(){
            do 
                return; 
            while(true); 
            "luan1508"; 
            return;
        }
        """
        out = "Unreachable statement: "+str(StringLiteral("luan1508"))
        self.assertTrue(TestChecker.test(inp,out,520))

    def test_121(self):
        inp = """
        void main(){
            int i; 
            if(i==5) return; 
            else return; 
            i=1+i;
        }
        """
        out = "Unreachable statement: "+str(BinaryOp("=",Id("i"),BinaryOp("+",IntLiteral(1),Id("i"))))
        self.assertTrue(TestChecker.test(inp,out,521))








    # no entry point
    def test_130(self):
        inp = "int m(){ }"
        out = "No entry point"
        self.assertTrue(TestChecker.test(inp,out,530))

    def test_138(self):
        inp = """
        int mn(){
            int i; 
            if(i==5) return 1; 
            else return 1; 
            i=1+i;
        }
        """
        out = "No entry point"
        self.assertTrue(TestChecker.test(inp,out,538))

    def test_142(self):
        inp = "float min(int a){ }"
        out = "No entry point"
        self.assertTrue(TestChecker.test(inp,out,542))

    def test_143(self):
        inp = "boolean man(int a, int b){ int c; man();}"
        out = "No entry point"
        self.assertTrue(TestChecker.test(inp,out,543))


    # unreachable function 
    def test_139(self):
        inp = """
        void foo(){ }
        void main(){ }
        """
        out = "Unreachable function: foo"
        self.assertTrue(TestChecker.test(inp,out,539))

    def test_140(self):
        inp = """
        void foo(){
            foo();
        }
        void main(){ }
        """
        out = "Unreachable function: foo"
        self.assertTrue(TestChecker.test(inp,out,540))

    def test_141(self):
        inp = """
        void foo(){
            foo();
        }

        void foo1(){
            foo();
        }
        void main(){ }
        """
        out = "Unreachable function: foo1"
        self.assertTrue(TestChecker.test(inp,out,541))

    def test_141(self):
        inp = """
        void foo(){
            foo1();
        }

        void foo1(){
            foo();
        }

        void foo2(){
            foo();
            foo1();
        }

        void main(){ }
        """
        out = "Unreachable function: foo2"
        self.assertTrue(TestChecker.test(inp,out,541))


    

    
