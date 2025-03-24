.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	iconst_4
	istore_1
	iload_1
	invokestatic MCClass/foo(I)F
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static foo(I)F
.var 0 is a I from Label0 to Label1
.var 1 is foo I from Label0 to Label1
Label0:
	iconst_5
	istore_1
	iload_1
	iload_0
	iadd
	i2f
	freturn
Label1:
.limit stack 2
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
