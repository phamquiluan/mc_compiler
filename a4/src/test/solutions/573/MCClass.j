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
Label0:
	iconst_1
	putstatic MCClass.a I
	getstatic MCClass.a I
	iconst_1
	iadd
	putstatic MCClass.b I
	getstatic MCClass.b I
	iconst_1
	irem
	putstatic MCClass.c I
	getstatic MCClass.a I
	getstatic MCClass.b I
	iadd
	getstatic MCClass.c I
	getstatic MCClass.a I
	iadd
	idiv
	i2f
	putstatic MCClass.fa F
	getstatic MCClass.fa F
	getstatic MCClass.a I
	i2f
	fadd
	getstatic MCClass.c I
	getstatic MCClass.b I
	iadd
	i2f
	fdiv
	putstatic MCClass.fb F
	getstatic MCClass.fa F
	getstatic MCClass.fb F
	fmul
	getstatic MCClass.c I
	i2f
	fdiv
	putstatic MCClass.fc F
	getstatic MCClass.fa F
	getstatic MCClass.fb F
	fcmpl
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_1
	iload_1
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 3
.limit locals 2
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
