.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I
.field static arr [I
.field static fa F
.field static fb F
.field static fc F
.field static frr [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is fNum F from Label0 to Label1
Label0:
	getstatic MCClass.arr [I
	iconst_0
	getstatic MCClass.arr [I
	iconst_1
	getstatic MCClass.arr [I
	iconst_2
	iconst_3
	dup_x2
	iastore
	dup_x2
	iastore
	iastore
	iconst_3
	putstatic MCClass.a I
	getstatic MCClass.a I
	iconst_2
	iadd
	putstatic MCClass.b I
	getstatic MCClass.b I
	getstatic MCClass.a I
	iadd
	iconst_3
	iadd
	putstatic MCClass.c I
	getstatic MCClass.a I
	getstatic MCClass.b I
	iadd
	getstatic MCClass.arr [I
	iconst_0
	iaload
	iadd
	iconst_1
	isub
	i2f
	fstore_1
	fload_1
	getstatic MCClass.c I
	i2f
	fadd
	putstatic MCClass.fa F
	getstatic MCClass.fa F
	getstatic MCClass.a I
	i2f
	fadd
	putstatic MCClass.fb F
	getstatic MCClass.fb F
	getstatic MCClass.b I
	i2f
	fadd
	putstatic MCClass.fc F
	getstatic MCClass.frr [F
	iconst_0
	getstatic MCClass.fa F
	getstatic MCClass.fb F
	fadd
	getstatic MCClass.fc F
	fadd
	fastore
	getstatic MCClass.frr [F
	iconst_1
	getstatic MCClass.frr [F
	iconst_0
	faload
	getstatic MCClass.a I
	i2f
	fadd
	getstatic MCClass.b I
	i2f
	fadd
	getstatic MCClass.c I
	i2f
	fadd
	fastore
	getstatic MCClass.frr [F
	iconst_1
	faload
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 8
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

.method public static <clinit>()V
.limit stack 1
.limit locals 0
	iconst_3
	newarray int
	putstatic MCClass.arr [I
	iconst_4
	newarray float
	putstatic MCClass.frr [F
	return
.end method
