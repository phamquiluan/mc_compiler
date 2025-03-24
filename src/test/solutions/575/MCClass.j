.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I
.field static fa F
.field static fb F
.field static fc F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [I from Label0 to Label1
.var 2 is isTrue Z from Label0 to Label1
.var 3 is isT Z from Label0 to Label1
.var 4 is isF Z from Label0 to Label1
Label0:
	iconst_3
	newarray int
	astore_1
	bipush 10
	putstatic MCClass.a I
	getstatic MCClass.a I
	iconst_2
	imul
	putstatic MCClass.b I
	getstatic MCClass.b I
	bipush 7
	idiv
	putstatic MCClass.c I
	aload_1
	iconst_0
	getstatic MCClass.c I
	getstatic MCClass.b I
	iconst_2
	idiv
	iadd
	iastore
	aload_1
	iconst_1
	getstatic MCClass.a I
	iconst_2
	idiv
	getstatic MCClass.c I
	iconst_3
	idiv
	iadd
	iastore
	aload_1
	iconst_2
	getstatic MCClass.b I
	getstatic MCClass.a I
	imul
	iconst_4
	idiv
	getstatic MCClass.c I
	iconst_4
	idiv
	iadd
	iastore
	aload_1
	iconst_0
	iaload
	getstatic MCClass.b I
	imul
	getstatic MCClass.a I
	idiv
	getstatic MCClass.c I
	aload_1
	iconst_2
	iaload
	imul
	aload_1
	iconst_1
	iaload
	isub
	isub
	i2f
	putstatic MCClass.fa F
	getstatic MCClass.a I
	i2f
	getstatic MCClass.fa F
	aload_1
	iconst_2
	iaload
	i2f
	fadd
	fmul
	getstatic MCClass.c I
	aload_1
	iconst_1
	iaload
	isub
	i2f
	fmul
	putstatic MCClass.fb F
	getstatic MCClass.fa F
	getstatic MCClass.fb F
	fmul
	aload_1
	iconst_2
	iaload
	i2f
	fdiv
	putstatic MCClass.fc F
	getstatic MCClass.fa F
	getstatic MCClass.fc F
	fcmpl
	ifge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_3
	getstatic MCClass.fb F
	getstatic MCClass.fa F
	fcmpl
	iflt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore 4
	iload_3
	ifgt Label10
	iload 4
	ifle Label8
	getstatic MCClass.a I
	iconst_3
	iadd
	dup
	putstatic MCClass.a I
	bipush 17
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	iconst_0
	goto Label11
Label10:
	iconst_1
Label11:
	ifgt Label18
	getstatic MCClass.a I
	bipush 7
	iadd
	dup
	putstatic MCClass.c I
	bipush 19
	if_icmpeq Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label16
	aload_1
	iconst_2
	getstatic MCClass.b I
	getstatic MCClass.c I
	iadd
	dup_x2
	iastore
	bipush 11
	if_icmpeq Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifgt Label18
	iconst_0
	goto Label19
Label18:
	iconst_1
Label19:
	istore_2
	aload_1
	iconst_2
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 6
.limit locals 5
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
