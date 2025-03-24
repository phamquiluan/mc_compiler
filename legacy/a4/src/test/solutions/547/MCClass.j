.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a F
.field static b F
.field static gArr [F

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
	istore_2
	iconst_3
	dup
	istore_3
	istore_2
	iload_2
	i2f
	putstatic MCClass.a F
	iconst_4
	dup
	istore_3
	i2f
	putstatic MCClass.b F
	aload_1
	iconst_0
	iconst_5
	iastore
	getstatic MCClass.gArr [F
	iconst_0
	aload_1
	iconst_0
	bipush 11
	dup_x2
	iastore
	i2f
	fastore
	getstatic MCClass.gArr [F
	iconst_1
	getstatic MCClass.gArr [F
	iconst_2
	aload_1
	iconst_2
	iload_2
	dup_x2
	iastore
	i2f
	dup_x2
	fastore
	fastore
	getstatic MCClass.gArr [F
	iconst_2
	faload
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 8
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
	newarray float
	putstatic MCClass.gArr [F
	return
.end method
