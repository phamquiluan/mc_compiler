.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is fNum F from Label0 to Label1
.var 2 is i F from Label0 to Label1
.var 3 is j F from Label0 to Label1
Label0:
	getstatic MCClass.arr [F
	iconst_0
	getstatic MCClass.arr [F
	iconst_1
	ldc 11.5
	dup_x2
	fastore
	fastore
	getstatic MCClass.arr [F
	iconst_2
	ldc 8.5
	fastore
	getstatic MCClass.arr [F
	iconst_0
	faload
	fneg
	getstatic MCClass.arr [F
	iconst_1
	faload
	fneg
	fadd
	fstore_2
	getstatic MCClass.arr [F
	iconst_2
	faload
	fneg
	iconst_3
	i2f
	fmul
	fstore_3
	fload_2
	fload_3
	fadd
	fstore_1
	fload_1
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 6
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
	putstatic MCClass.arr [F
	return
.end method
