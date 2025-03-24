.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iconst_5
	istore_1
	iload_1
	invokestatic MCClass/foo(I)I
	pop
	iload_1
	invokestatic MCClass/foo(I)I
	i2f
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static foo(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iload_0
	imul
	ireturn
Label1:
.limit stack 2
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
