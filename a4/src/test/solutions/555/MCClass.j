.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I
.field static arr [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
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
	bipush 19
	putstatic MCClass.a I
	getstatic MCClass.a I
	getstatic MCClass.a I
	getstatic MCClass.arr [I
	iconst_0
	iaload
	irem
	iadd
	putstatic MCClass.b I
	getstatic MCClass.b I
	getstatic MCClass.a I
	irem
	getstatic MCClass.arr [I
	iconst_0
	iaload
	getstatic MCClass.arr [I
	iconst_1
	iaload
	imul
	iadd
	putstatic MCClass.c I
	getstatic MCClass.arr [I
	iconst_2
	getstatic MCClass.c I
	getstatic MCClass.a I
	imul
	getstatic MCClass.b I
	irem
	iastore
	getstatic MCClass.arr [I
	iconst_2
	iaload
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 8
.limit locals 1
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
