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
.var 1 is isTrue Z from Label0 to Label1
.var 2 is isT Z from Label0 to Label1
.var 3 is isF Z from Label0 to Label1
Label0:
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
	getstatic MCClass.a I
	getstatic MCClass.b I
	imul
	getstatic MCClass.c I
	getstatic MCClass.a I
	idiv
	isub
	i2f
	putstatic MCClass.fa F
	getstatic MCClass.a I
	i2f
	getstatic MCClass.fa F
	getstatic MCClass.a I
	i2f
	fadd
	fmul
	getstatic MCClass.c I
	getstatic MCClass.b I
	isub
	i2f
	fmul
	putstatic MCClass.fb F
	getstatic MCClass.fa F
	getstatic MCClass.fb F
	fmul
	getstatic MCClass.c I
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
	istore_2
	getstatic MCClass.fb F
	getstatic MCClass.fa F
	fcmpl
	iflt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore_3
	iload_2
	iload_3
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	istore_1
	iload_1
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 3
.limit locals 4
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
