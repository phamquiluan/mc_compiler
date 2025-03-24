.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b I
.field static gArr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [I from Label0 to Label1
.var 2 is c I from Label0 to Label1
.var 3 is d I from Label0 to Label1
Label0:
	iconst_4
	newarray int
	astore_1
	iconst_1
	putstatic MCClass.a I
	iconst_1
	dup
	putstatic MCClass.a I
	putstatic MCClass.b I
	getstatic MCClass.a I
	istore_2
	getstatic MCClass.b I
	dup
	istore_2
	dup
	putstatic MCClass.a I
	putstatic MCClass.b I
	getstatic MCClass.gArr [I
	iconst_0
	aload_1
	iconst_0
	iconst_1
	dup_x2
	iastore
	iastore
	getstatic MCClass.gArr [I
	iconst_1
	getstatic MCClass.gArr [I
	iconst_0
	bipush 11
	dup_x2
	iastore
	iastore
	getstatic MCClass.gArr [I
	iconst_1
	aload_1
	iconst_3
	getstatic MCClass.gArr [I
	iconst_0
	getstatic MCClass.gArr [I
	iconst_2
	bipush 11
	dup
	putstatic MCClass.b I
	dup_x2
	iastore
	dup
	putstatic MCClass.a I
	dup_x2
	iastore
	dup_x2
	iastore
	dup_x2
	iastore
	istore_3
	getstatic MCClass.gArr [I
	iconst_1
	iaload
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 10
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

.method public static <clinit>()V
.limit stack 1
.limit locals 0
	iconst_4
	newarray int
	putstatic MCClass.gArr [I
	return
.end method
