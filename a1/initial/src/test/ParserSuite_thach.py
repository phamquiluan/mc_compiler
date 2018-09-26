import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    def test_simple_void_func(self):
        """Source: void main() {} """
        input = """void main(int a, float a[]) {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_simple_string_func(self):
        """Source: string _main() {} """
        input = """string _main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_simple_int_func(self):
        """Source: int main_() {} """
        input = """int main_() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_simple_bool_func(self):
        """Source: bool main12() {} """
        input = """bool main12() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_simple_float_func(self):
        """Source: float __main__2() {} """
        input = """float __main__2() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_func_one_param(self):
        """Source: void setName(string name, int a[]) {} """
        input = """void setName(string name, int a[]) {} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_var(self):
        """Source: int a ; """
        input = """int a ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_array_var(self):
        """Source: float _b[4] ; """
        input = """float _b[4] ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_var_list(self):
        """Source: int a, float _b[4] ; """
        input = """int a;
                float _b[4];
                string name, names[10] ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_complex_function(self):
        """Source: int main() {
            int a = 0 ;
        }"""
        input = """int main() {
            int a;
            a = 0;
            if (a > 0) {
                age = 1000 ;
            }
            if(a > b) {
                b = 10 ;
            }
            else {
                c = 100 ;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_if_stmt(self):
        """Source: int main() {
            if (a > 10) {
                a = a + 1 ;
            }
        } """
        input = """int main() {
            if (a > 10) {
                a = a + 1 ;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_expr_1(self):
        """Source: string funcname(int a, string b, float c[]){
            a = (b + c) * (c + d) ;
            a = a + c[a + (b * c)];
        }"""
        input = """string funcname(int a, string b, float c[]){
            a = (b + c) * (c + d) ;
            a = a + c > [a + (b * c)];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))
    
    def test_expr_2(self):
        """Source: int __test(int a, int b[]){
            a > 10 + b[a + 50];
        } """
        input = """int __test(int a, int b[]){
            a > 10 + b[a + 50];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_expr_3(self):
        """Source: void onlytest(int m, string name, int a___){
            10 + 4 * s * (1 + 1 + a * 2) / 10 - [a + a[10] * 14 + 10/2] * (3 % [2 && (13 * 2)]);
        }"""
        input = """void onlytest(int m, string name, int a___){
            10 + 4 * s * (1 + 1 + a * 2) / 10 - [a + a[10] * 14 + 10/2] * (3 % [2 && (13 * 2)]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_expr_4(self):
        """Source: a * b ;"""
        input = """
            int mult(int a, int b){
            a * b ;
            10 = 2 + a * (1 + 1) ;
            10 = 2 + a * (1 + 1) ;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_parser_1(self):
         """Source: bool[] main12() {} """
         input = """bool[] main12() {}"""
         expect = "successful"
         self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_for_stmt(self):
        """Source: string test(){
            for(i = 1; i < n; i = i + 1){
                if(i > 3) 
                    i = 1;
            }
        } """
        input = """string test(){
            for(i = 1; i < n; i = i + 1){
                if(i > 3) 
                    i = 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_do_while(self):
        """Source: void dowhile(){
            do {
                return a ;
            }while (a > 10);
        } """
        input = """void dowhile(){
            do {
                return a ;
            }while (a > 10);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_1(self):
        """Source: void dowhile(){
            do {
                return dd(10) ;
            }while (a > 10);
        } """
        input = """void dowhile(){
            do {
                return dd(10) ;
            }while (a > 10);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_2(self):
        """Source: void dowhile(){
            do {
                return dd(a) ;
            }while (a > 10);
        } """
        input = """void dowhile(){
            do {
                return dd(a) ;
            }while (a > 10);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_3_2(self):
        """Source: void dowhile(){
            do {
                return r(a + b) ;
            }while (a > 10);
        } """
        input = """void dowhile(){
            do {
                return r(a + b) ;
            }while (a > 10);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_3_4(self):
        """Source: void dowhile(){
            foo(2)[3+x] = a[b[2]] +3;
        } """
        input = """void dowhile(){
            foo(2)[3+x] = a[b[2]] +3;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_12(self):
        """Source: void todo(){
            foo(4);
            return 10;
            return ;
            return f(a[10]);
        } """
        input = """void todo(){
            foo(4);
            return 10;
            return ;
            return f(a[10]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_12__2(self):
        """Source: int [] foo(int b[]) {
            int a [1] ;
            if () return a ; 
            else  return b ;
        } """
        input = """void todo(){
            foo(4);
            return 10;
            return ;
            return f(a[10]);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    
    def test_100(self):
        """Source:
        void main(){
            return 0;
        }
        bool test(){
            return true;
        } """
        input = """
        void main(){
            return 0;
        }
        bool test(){
            return true;
        } """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_99(self):
        """Source:
        int i[1];"""
        input = """
        int i[1]; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_12a(self):
        input = """
                  int i,i,j, a[1];
                  bool a[1];
                  string abc;
                  float x;
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_12aaa(self):
        input = """
        string abc(){}
        bool _abc(){}
        void A_(){}
        int A_bc (){}
        float A_AB(){}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_12s_a(self):
        input ="""
        int main(int a[], float b[]){
                if (a>v) 1
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_test(self):
        input ="""
        int main(int a[], float b[]){
                do 1 while 1;
        }

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_test_1(self):
        input ="""
        int main(int a[], float b[]){
            for (1;2;1) if (a>v) 1 else 1
                break;
        }

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_test_a(self):
        input ="""
        int main(int a[], float b[]){
            for (1;2;1){
                int a , b , c ;
                float f [ 5 ] ;
            }
        return 0;
        }

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_test_12a(self):
        input ="""
        int main(int a[], float b[]){
            for (1;2;1){ if (c>b) 1 else 1
                continue;
                }

        }

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_test_sda__a1(self):
        input ="""
        int main(int a[], float b[]){
                if(a>b){
                int a;
                int a[2];
                int  a[2];
                int  a[2];
                boolean a[5];
                {
                int i ; // l o c a l i n t v a r i a b l e
                i =3;
                if ( i >0) putInt ( i ) ;
                }
            }
        }

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_todo1(self):
        input ="""
        int _Abc(int a[], float b[]){
            int a,b;
            foo(2)[3+x] = a[b[2]] + 3;
            a + b = c;
            return 0;
        }
        void Main(int main){
            int c;
            c = 11 + 12 + 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_todo122(self):
        input ="""
        void Main(int main){
            int c[4], x;
            x = 1;
            c[0] = 11 + 12 + 1;
            c[1] = 3;
            c[2] = foo(x)+3+x;

        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_todo_2(self):
        input ="""
        void foo ( float a [ ] ) {}
        void goo ( float x [ ] ) {
        float y[10] ;
        int z[10] ;
        foo ( x ) ;
        foo ( y ) ;
        foo ( z ) ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_todo_123(self):
        input ="""
        int foo( int b [] ) {
            for(a > 1 ; s > j; c-c) a = b + c;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_todo_more(self):
        input ="""
        void main ( ) {
        int main ;
        main = f ( ) ;
        putIntLn ( i ) ;
        {
        int i ;
        int main ;
        int f ;
        main = f = i = 100;
        putIntLn ( i ) ;
        putIntLn ( main ) ;
        putIntLn ( f ) ;
        }
        putIntLn ( main ) ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_todo_more_01(self):
        input ="""
        float foo( int b [] ) {
                    {
                int a , b , c ;
                float f [5] ;

                a=b=2;
                if (a=b) f[0] = 1.0 ;

                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))
    
    def test_todo_more_100(self):
        input ="""int main()
        {
         bool b ;
         int i ;
         i =3;
         if ( i >0) putInt( i ) ;
         }

        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))
    
    def test_513_1(self):
        input ="""bool[] main(){}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_513_2(self):
        input ="""string[] main(int a, float b[]){}
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_513_3(self):
        input ="""int[] main(){
            return fun(i) ;
            return(a);
            continue ;
            break ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))
        
    def test_513_4(self):
        input ="""int[] main(){
            return fun(i) ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_513_5(self):
        input ="""int[] main(int a){
            break;
            return fun(i) ;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_513_6(self):
        input = """void setName(string name, int a[]) {} """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_513_7(self):
        input = """string funcname(int a, string b, float c[]){
            a = (b + c) * (c + d) ;
            a = a + c > [a + (b * c)];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_513_8(self):
        input = """void dowhile(){
            foo(2)[3+x] = a[b[2]] +3;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_513_9(self):
        input ="""
        int main(int a[], float b[]){
            for (1;2;1){
                int a , b , c ;
                float f [ 5 ] ;
            }
        return 0;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))