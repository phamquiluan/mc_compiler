.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is iNum I from Label0 to Label1
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
Label0:
	getstatic MCClass.arr [I
	iconst_0
	getstatic MCClass.arr [I
	iconst_1
	getstatic MCClass.arr [I
	iconst_2
	bipush 10
	dup_x2
	iastore
	dup_x2
	iastore
	iastore
	getstatic MCClass.arr [I
	iconst_0
	iaload
	ineg
	istore_2
	getstatic MCClass.arr [I
	iconst_1
	iaload
	ineg
	istore_3
	iload_2
	iload_3
	iadd
	istore_1
	iload_1
	invokestatic io/putIntLn(I)V
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
	newarray int
	putstatic MCClass.arr [I
	return
.end method
