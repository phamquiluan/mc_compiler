.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I
.field static arr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is iNum I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
Label0:
	getstatic MCClass.arr [I
	iconst_0
	iconst_0
	iastore
	getstatic MCClass.arr [I
	iconst_1
	iconst_1
	iastore
	getstatic MCClass.arr [I
	iconst_2
	iconst_2
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
	getstatic MCClass.arr [I
	iconst_0
	iaload
	getstatic MCClass.c I
	iadd
	getstatic MCClass.arr [I
	iconst_1
	iaload
	getstatic MCClass.b I
	isub
	iadd
	getstatic MCClass.arr [I
	iconst_2
	iaload
	getstatic MCClass.arr [I
	iconst_0
	iaload
	isub
	isub
	istore_1
	iload_1
	getstatic MCClass.arr [I
	iconst_0
	iaload
	isub
	getstatic MCClass.arr [I
	iconst_1
	iaload
	iadd
	getstatic MCClass.arr [I
	iconst_2
	iaload
	isub
	getstatic MCClass.c I
	isub
	istore_2
	iload_1
	iload_2
	isub
	bipush 11
	iadd
	istore_3
	iload_3
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 4
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
	iconst_3
	newarray int
	putstatic MCClass.arr [I
	return
.end method
