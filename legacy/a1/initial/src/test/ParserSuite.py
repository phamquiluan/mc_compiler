import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test_group(self):
    #     """Simple program: int main() {} """
    #     input =  """ void foo(){ str =\"natsu\\g\"}"""
    #     expect = "Iilegal escape in string: natsu\\"
    #     self.assertTrue(TestParser.checkParser(input,expect,1000))

    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    
    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """int main( {}"""
        expect = "Error on line 1 col 10: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    # def test_201(self):
    #     inp=
    #     out= 
    #     self.assertTrue(TestParser.checkParser(inp,out,201))

    # def test_202(self):
    #     inp=
    #     out= 
    #     self.assertTrue(TestParser.checkParser(inp,out,202))

    # def test_203(self):
    #     inp=
    #     out= 
    #     self.assertTrue(TestParser.checkParser(inp,out,203))

    def test_204(self):
        inp="""int abc[3];
  void main() {}"""
        out= "successful"
        self.assertTrue(TestParser.checkParser(inp,out,204))

    def test_205(self):
        inp="""int variable1;
  void main() {}"""
        out= "successful"
        self.assertTrue(TestParser.checkParser(inp,out,205))

    def test_206(self):
        inp="} int main {"
        out="Error on line 1 col 0: }"
        self.assertTrue(TestParser.checkParser(inp,out,206))

    def test_207(self):
        inp="""int variable1, variable2[3];
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,207))

    def test_208(self):
        inp="int variable1, variable2[];"
        out="Error on line 1 col 25: ]"
        self.assertTrue(TestParser.checkParser(inp,out,208))

    def test_209(self):
        inp="int variable1, variable2[6;"
        out="Error on line 1 col 26: ;"
        self.assertTrue(TestParser.checkParser(inp,out,209))

    def test_210(self):
        inp="int variable = 1;"
        out="Error on line 1 col 13: ="
        self.assertTrue(TestParser.checkParser(inp,out,210))

    def test_211(self):
        inp="int abc, variable = 1;"
        out="Error on line 1 col 18: ="
        self.assertTrue(TestParser.checkParser(inp,out,211))

    def test_212(self):
        inp="""float func() {}
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,212))

    def test_213(self):
        inp="""void func() {}
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,213))

    def test_214(self):
        inp="void func( {}"
        out="Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(inp,out,214))

    def test_215(self):
        inp="""int func(int par1){}
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,215))

    def test_216(self):
        inp="""int func(int par1, float par2){}
  void main() {}"""
        out="successful" 
        self.assertTrue(TestParser.checkParser(inp,out,216))

    def test_217(self):
        inp="int func(void par1){}"
        out="Error on line 1 col 9: void"
        self.assertTrue(TestParser.checkParser(inp,out,217))

    def test_218(self):
        inp="int func(int par1, void par2){}"
        out="Error on line 1 col 19: void"
        self.assertTrue(TestParser.checkParser(inp,out,218))

    def test_219(self):
        inp="""void func() { float abc;}
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,219))

    def test_220(self):
        inp="""int[] func(boolean abc, float xyz) {int x1; float x2;}
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,220))

    def test_221(self):
        inp="""void[] func(boolean abc, float xyz) {
    int x1;
    float x2;
    }"""
        out="Error on line 1 col 4: ["
        self.assertTrue(TestParser.checkParser(inp,out,221))

    def test_222(self):
        inp="""void func() {
  break;
  }
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,222))

    def test_223(self):
        inp="""int func() {
  float abc;
  continue;
  }
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,223))

    def test_224(self):
        inp="""int func() {
  float abc;
  abc = 1;
  }
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,224))

    def test_225(self):
        inp="""int func(int par1, float par2){
  if (a != 1)
  continue;
  }
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,225))

    def test_226(self):
        inp="""int func(int par1, float par2){
  if (a != 1)
    continue;
  else
    break;
  return a;
  }
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,226))

    def test_227(self):
        inp="""int func(int par1, float par2){
  for(a = 10; a < 20; a = a + 1 )
      i = i + 1;
  }
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,227))

    def test_228(self):
        inp="""int func(int par1, float par2){
  do a = 1; while a = 1;
    continue;
  }
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,228))

    def test_229(self):
        inp="""int func(int par1, float par2){
  do a = 1; while a = 1;
    return a = 1;
  }
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,229))

    def test_230(self):
        inp="""int func(int par1, float par2){
  abc = a[b[2]] + 3;
    return a = 1;
  }
  void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,230))

    def test_231(self):
        inp="""void main() {}"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,231))

    def test_232(self):
        inp="""void main() {
  int abc;
  continue;
  putInt(i);
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,232))

    def test_233(self):
        inp="""void[] main() {
  int abc;
  continue;
  }"""
        out="Error on line 1 col 4: ["
        self.assertTrue(TestParser.checkParser(inp,out,233))

    def test_234(self):
        inp="""void foo ( int i ) {
    int i,j,k[5];
    // ABC XYZ
  }
  void main() {
    int abc;
    continue;
    putInt(i);
  }
  """
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,234))

    def test_235(self):
        inp="""void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[5]) + 123123;
  }
  void main() {
    int abc;
    continue;
    putFloat(i);
  }"""
        out="successful" 
        self.assertTrue(TestParser.checkParser(inp,out,235))

    def test_236(self):
        inp="""void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[5]) + a;
  }
  void main() {
    int abc;
    continue;
    putFloat(i);
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,236))

    def test_237(self):
        inp="""void foo ( int i ) {
    int i,j,k[5];
    float arr[10];
    i = (j + i) /(j + k[arr[1]]) + 123123;
  }
  void main() {
    int abc;
    continue;
    putFloat(i);
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,237))

    def test_238(self):
        inp="""float arr[10];
  int func(int par1, float par2){
    if (a != 1)
    continue;
  }
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + 123123;
  }
  void main() {
    int abc;
    if (arr[arr[2]] == arr[arr[3]])
      i = j;
    else
      break;
    return ;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,238))

    def test_239(self):
        inp="""float arr[10];
  int func(int par1, float par2){
    if (a != 1)
    continue;
  }
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + 123123;
  }
  void main() {
    int abc;
    if (arr[arr[2]] == arr[arr[3]])
      i = j;
    else
      break;
    return ;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,239))

    def test_240(self):
        inp="""float arr[10];
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + 123123;
  }
  void main() {
    int abc;
    for(a = 10; a < 20; a = a + 1 )
        continue;
    return ;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,240))

    def test_241(self):
        inp="""float arr[10];
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + 123123;
  }
  void main() {
    int abc;
    do a = 1;
    while arr[arr[2]] == arr[arr[3]];
    return ;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,241))

    def test_242(self):
        inp="""float arr[10];
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + 123123;
  }
  void main() {
    int abc;
    if (a != 1)
      continue;

    if (arr[arr[2]] == arr[arr[3]])
      i = j;
    else
      break;

    for(a = 10; a < 20; a = a + 1 )
        continue;

    do a = 1;
    while arr[arr[2]] == arr[arr[3]];
    return ;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,242))

    def test_243(self):
        inp="""void main() {
  int abc;
  void func(float abc) {
    boolean xyz;
    xyz = false;
  }
  return 0;
  }"""
        out="Error on line 3 col 2: void"
        self.assertTrue(TestParser.checkParser(inp,out,243))

    def test_244(self):
        inp="""void func(float abc) {
    boolean xyz;
    xyz = false;
    int subFunc(boolean bl) {
      if(bl = false)
        xyz = true;
      else
        xyz = false;
      return 0;
    }
  }
  void main() {
  int abc;
  return 0;
  }"""
        out= "Error on line 4 col 4: int"
        self.assertTrue(TestParser.checkParser(inp,out,244))

    def test_245(self):
        inp="""boolean xyz;
  int subFunc(boolean bl) {
    xyz = false;
    if(bl = false)
      xyz = true;
    else
      xyz = false;
    return 0;
  }
  void main() {
  int abc;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,245))

    def test_246(self):
        inp="""boolean xyz;
  int subFunc(boolean bl) {
    xyz = false;
    if(bl = false)
      xyz = true;
    else
      xyz = false;
    return 0;
  }
  float arr[10];
  int func(int par1, float par2){
    if (a != 1)
    continue;
  }
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + 123123;
  }
  void main() {
  int abc;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,246))

    def test_247(self):
        inp="""boolean xyz;
  int abc[3], xyz[3], XYZ[3];
  int subFunc(boolean bl) {
    xyz = false;
    if(bl = false)
      xyz = true;
    else
      xyz = false;
    return 0;
  }
  float arr[10];
  int func(int par1, float par2){
    if (a != 1)
    continue;
  }
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + 123123;
  }
  void main() {
  int abc;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,247))

    def test_248(self):
        inp="""boolean xyz;
  int abc[3], xyz[3], XYZ[3];
  int subFunc(boolean bl) {
    xyz = false;
    if(bl = false)
      xyz = true;
    else
      xyz = false;
    return 0;
  }
  float arr[10];
  int func(int par1, float par2){
    if (a != 1)
    continue;
  }
  void main() {
  int abc;
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + 123123;
  }
  return 0;
  }"""
        out="Error on line 18 col 2: void"
        self.assertTrue(TestParser.checkParser(inp,out,248))

    def test_249(self):
        inp="""boolean xyz;
  int subFunc(boolean bl) {
    xyz = false;
    if(bl = false)
      xyz = true;
    else
      xyz = false;
    return 0;
  }
  void main() {
    int abc;
    putInt(i);
    return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,249))

    def test_250(self):
        inp="""int func(int par1, float par2){
    abc = a[b[2]] + 3;
      return a = 1;
  }
  void main() {
  int abc;
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + 123123;
  }
  return 0;
  }"""
        out= "Error on line 7 col 2: void"
        self.assertTrue(TestParser.checkParser(inp,out,250))

    def test_251(self):
        inp="""boolean xyz;
  int abc;
  int subFunc(boolean bl) {
    xyz = false;
    for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        abc = 1;
    return 0;
  }
  void main() {
  int abc;
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + 123123;
  }
  return 0;
  }"""
        out="Error on line 14 col 2: void"
        self.assertTrue(TestParser.checkParser(inp,out,251))

    def test_252(self):
        inp="""boolean xyz;
  int abc;
  int subFunc(boolean bl) {
    xyz = false;
    do abc = abc + 1;
    while xyz != false;
    return 0;
  }
  void main() {
  int abc;
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + ASDASDASDA;
  }
  return 0;
  }"""
        out="Error on line 11 col 2: void"
        self.assertTrue(TestParser.checkParser(inp,out,252))

    def test_253(self):
        inp="""void main() {
    continue;
  }
  int abc"""
        out="Error on line 4 col 9: <EOF>"
        self.assertTrue(TestParser.checkParser(inp,out,253))

    def test_254(self):
        inp="""boolean xyz;
  void main() {
    int abc;
    xyz = false;
    abc = false;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,254))

    def test_255(self):
        inp="""boolean xyz;
  int abc;
  void main() {
  int abc;
  do abc = abc + 1;
  while xyz != false;
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + ASDASDASDA;
  }
  return 0;
  }"""
        out="Error on line 7 col 2: void"
        self.assertTrue(TestParser.checkParser(inp,out,255))

    def test_256(self):
        inp="""boolean xyz;
  int abc;
  void main() {
  int abc;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        abc = 1;
  do abc = abc + 1;
  while xyz != false;
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + ASDASDASDA;
  }
  return 0;
  }"""
        out="Error on line 12 col 2: void"
        self.assertTrue(TestParser.checkParser(inp,out,256))

    def test_257(self):
        inp="""boolean xyz;
  int abc;
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + ASDASDASDA;
  }
  return 0;
  }"""
        out="Error on line 12 col 2: void"
        self.assertTrue(TestParser.checkParser(inp,out,257))

    def test_258(self):
        inp="""boolean xyz;
  int abc;
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + ASDASDASDA;
  }
  return 0;
  }"""
        out="Error on line 12 col 2: void"
        self.assertTrue(TestParser.checkParser(inp,out,258))

    def test_259(self):
        inp="""boolean xyz;
  int abc;
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  string foo(){return x;}
  return 0;
  }"""
        out="Error on line 12 col 2: string"
        self.assertTrue(TestParser.checkParser(inp,out,259))

    def test_260(self):
        inp="""float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,260))

    def test_261(self):
        inp="""int [ ] foo ( int b [ ] ) {
    int a [ 1 ] ;
    if (ABC ) return a ;
    else return b ;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,261))

    def test_262(self):
        inp="""float foo(){
    i=2;
    foo(1.2);
    foo(3*4);
    100;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,262))

    def test_263(self):
        inp="""float foo(){
    return x;
  }
  float foo(){
    y=y*13;
    return y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out= "successful"
        self.assertTrue(TestParser.checkParser(inp,out,263))

    def test_264(self):
        inp="""float foo(){
    foo(x);
    return x;
    }
  float foo(){
    return y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,264))

    def test_265(self):
        inp="""float foo(){
    return x;
  }
  int foo(){
    return y;
  }
  void main() {
  int abc;
  int x,y;
  float ft;
  ft = foo();
  abc = foo();
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  string foo(){return x;}
  return 0;
  }"""
        out="Error on line 19 col 2: string"
        self.assertTrue(TestParser.checkParser(inp,out,265))

    def test_266(self):
        inp="""float foo(float x, float y){
    x=x+y;
    x = x + foo(x+y);
  }
  void main() {
  int abc;
  int x,y;
  float ft;
  ft = foo();
  abc = foo();
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,266))

    def test_267(self):
        inp="""float foo(){
    int x, arr[3];
    x=1;
    arr[0] = arr[1 + arr[2] + x];
  }
  void main() {
  int abc;
  int x,y;
  float ft;
  ft = foo();
  abc = foo();
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,267))

    def test_268(self):
        inp="""boolean xyz;
  int abc[3], xyz[3], XYZ[3];
  int subFunc(boolean bl) {
    xyz = false;
    if(bl = false)
      xyz = true;
    else
      xyz = false;
    return 0;
  }
  float foo(){
    int x, arr[3];
    x=1;
    arr[0] = arr[1 + arr[2] + x];
  }
  void main() {
  int abc;
  int x,y;
  float ft;
  ft = foo();
  abc = foo();
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,268))

    def test_269(self):
        inp="""float foo(){
    for ( i=0;i<n;i=i+1)
      if(a<b)
        a=a+1;
      else
        a=a-1;
  }
  void main() {
  int abc;
  int x,y;
  float ft;
  ft = foo();
  abc = foo();
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out= "successful"
        self.assertTrue(TestParser.checkParser(inp,out,269))

    def test_270(self):
        inp="""float foo(){
    for ( i=0;i<n;i=i+1)
      if(a<b)
        a=a+1;
      else
        a=a-1;
  }
  void func( int i ) {
    int i,j,k[5];
    float arr[10];
    i = (j + i) /(j + k[arr[1]]) + 123123;
    j = foo() + k[2];
  }
  void main() {
    int abc;
    continue;
    putFloat(i);
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,270))

    def test_271(self):
        inp="""boolean xyz;
  int abc[3], xyz[3], XYZ[3];
  int subFunc(boolean bl) {
    xyz = false;
    if(bl = false)
      xyz = true;
    else
      xyz = false;
    return 0;
  }
  int func(int par1, float par2){
    if (a != 1)
    continue;
  }
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + 123123;
    i = i + subFunc(true);
  }
  void main() {
  int abc;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,271))

    def test_272(self):
        inp="""boolean xyz;
  int abc[3], xyz[3], XYZ[3];
  int subFunc(boolean bl) {
    xyz = false;
    if(bl = false)
      xyz = true;
    else
      xyz = false;
    return 0;
  }
  int func(int par1, float par2){
    if (a != 1)
      continue;
    else
      break;
  }
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + 123123;
    i = i + subFunc(true);
  }
  void main() {
  int abc;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,272))

    def test_273(self):
        inp="""boolean xyz;
  int abc[3], xyz[3], XYZ[3];
  int subFunc(boolean bl) {
    xyz = false;
    if(bl = false)
      xyz = true;
    else
      xyz = false;
    return 0;
  }
  int func(int par1, float par2){
    for(a = 10; a < 20; a = a + 1 )
      i = i + 1;
  }
  void foo ( int i ) {
    int i,j,k[5];
    i = (j + i) /(j + k[arr[1]]) + 123123;
    i = i + subFunc(true);
  }
  void main() {
  int abc;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,273))

    def test_274(self):
        inp="""int subFunc(boolean bl) {
    xyz = false;
    if(bl = false)
      xyz = true;
    else
      xyz = false;
    return 0;
  }
  void foo ( int i ) {
    int i,j,k[5];
    float arr[10];
    i = (j + i) /(j + k[arr[1]]) + 123123 + subFunc(true);
  }
  void[] main() {
  int abc;
  continue;

  }"""
        out="Error on line 14 col 6: ["
        self.assertTrue(TestParser.checkParser(inp,out,274))

    def test_275(self):
        inp="""
  int[] func(boolean abc, float xyz) {int x1; float x2;}
  void main() {int abc;
  continue;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,275))

    def test_276(self):
        inp="""int[] func(boolean abc, float xyz) {
    int x1;
    float x2;
    for(a = 10; a < 20; a = a + 1 )
         i = i + 1;
  }
  void main() {int abc;
  continue;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,276))

    def test_277(self):
        inp="""int[] func(boolean abc, float xyz) {
    int x1;
    float x2;
    for(a = 10; a < 20; a = a + 1 )
         i = i + 1;
    if (a != 1)
      continue;
    else
      break;
  }
  void main() {int abc;
  continue;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,277))

    def test_278(self):
        inp="""int func(boolean abc, float xyz) {
  int x1;
  float x2;
  if (a != 1)
    for(a = 10; a < 20; a = a + 1 )
       i = i + 1;
  else
    break;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      return x;
  }
  void main() {int abc;
  continue;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,278))

    def test_279(self):
        inp="""float foo(){
    if (a<b)
      a=a+1;
    else
      a-1;
    }
  boolean check(){
    if(a>x)
      return a;
    else
      return x;
  }
  void main() {int abc;
  continue;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,279))

    def test_280(self):
        inp="""boolean check(){
    if(a>x)
      return a;
    else
      return x;
  }
  void main() {int abc;
  continue;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,280))

    def test_281(self):
        inp="""int[] func(boolean abc, float xyz) {
  int x1;
  float x2;
  for(a = 10; a < 20; a = a + 1 )
       i = i + 1;
  if (a != 1)
    continue;
  else
    break;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      return x;
  }
  void main() {int abc;
  continue;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,281))

    def test_282(self):
        inp="""int func(boolean abc, float xyz) {
  int x1;
  float x2;
  for(a = 10; a < 20; a = a + 1 )
       i = i + 1;
  if (a != 1)
    continue;
  else
    break;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      return x;
  }
  void main() {int abc;
  continue;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,282))

    def test_283(self):
        inp="""int[] func(boolean abc, float xyz) {
  int x1;
  float x2;
  for(a = 10; a < 20; a = a + 1 )
       i = i + 1;
  if (a != 1)
    continue;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      return x;
  }
  void main() {int abc;
  continue;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,283))

    def test_284(self):
        inp="""int[] func(boolean abc, float xyz) {
  int x1;
  float x2;
  if (a != 1)
    for(a = 10; a < 20; a = a + 1 )
       i = i + 1;
  else
    break;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      return x;
  }
  void main() {int abc;
  continue;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,284))

    def test_285(self):
        inp="""float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        break;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,285))

    def test_286(self):
        inp="""float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        x;
    foo(x+y);
    y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,286))

    def test_287(self):
        inp="""float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        x;
    foo(x+y);
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,287))

    def test_288(self):
        inp="""
  float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        foo(x+y);
    y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,288))

    def test_289(self):
        inp="""float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        foo(x+y);
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,289))

    def test_290(self):
        inp="""float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        x;
    y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,290))

    def test_291(self):
        inp="""float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        x;
    y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,291))

    def test_292(self):
        inp="""boolean xyz;
  int abc;
  int subFunc(boolean bl) {
    xyz = false;
    do abc = abc + 1;
    while xyz != false;
    return 0;
  }
  float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        foo(x+y);
    y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,292))

    def test_293(self):
        inp="""boolean xyz;
  int subFunc(boolean bl) {
    xyz = false;
    do abc = abc + 1;
    while xyz != false;
    return 0;
  }
  float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        foo(x+y);
    y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,293))

    def test_294(self):
        inp="""boolean xyz;
  int abc;
  int subFunc(boolean bl) {
    xyz = false;
    do abc = abc + 1;
    while xyz != false;
    return 0;
  }
  float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        foo(x+y);
    y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }
  void[] main() {
  int abc;
  continue;

  }"""
        out="Error on line 36 col 6: ["
        self.assertTrue(TestParser.checkParser(inp,out,294))

    def test_295(self):
        inp="""int abc, xyz;
  int subFunc(boolean bl) {
    xyz = false;
    do abc = abc + 1;
    while xyz != false;
    return 0;
  }
  float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        foo(x+y);
    y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,295))

    def test_296(self):
        inp="""int subFunc(boolean bl) {
    boolean xyz;
    int abc;
    xyz = false;
    do abc = abc + 1;
    while xyz != false;
    return 0;
  }
  float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        foo(x+y);
    y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,296))

    def test_297(self):
        inp="""int abc, xyz;
  int subFunc(boolean bl) {
    xyz = false;
    do abc = abc + 1;
    while xyz != false;
    return 0;
  }
  float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
    y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,297))

    def test_298(self):
        inp="""int abc, xyz;
  int subFunc(boolean bl) {
    xyz = false;
    do abc = abc + 1;
    while xyz != false;
    return 0;
  }
  float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,298))

    def test_299(self):
        inp="""int abc, xyz;
  int subFunc(boolean bl) {
    xyz = false;
    do abc = abc + 1;
    while xyz != false;
    return 0;
  }
  float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        do abc = abc + 1;
        while xyz != false;
    y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,299))

    def test_300(self):
        inp="""int abc, xyz;
  int subFunc(boolean bl) {
    xyz = false;
    do abc = abc + 1;
    while xyz != false;
    return 0;
  }
  float foo(float x, float y){
    x;
    foo(x+y);
    y;
  }
  boolean check(){
    if(a>x)
      return a;
    else
      if (a != 1)
        for(a = 10; a < 20; a = a + 1 )
            i = i + 1;
      else
        for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        do abc = abc + 1;
        while xyz != false;
      else
        abc = 0;
    y;
  }
  void main() {
  int abc;
  int x,y;
  for( abc = 1; xyz == true; abc = abc + 1)
      if(abc == 1)
        abc = 0;
      else
        do abc = abc + 1;
        while xyz != false;
  return 0;
  }"""
        out="successful"
        self.assertTrue(TestParser.checkParser(inp,out,300))















