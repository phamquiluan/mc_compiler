.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static Fibonacci(I)I
.var 0 is i I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label5:
	iconst_0
	ireturn
Label6:
Label4:
	iload_0
	iconst_1
	if_icmpne Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
Label10:
	iconst_1
	ireturn
Label11:
Label9:
	iload_0
	iconst_1
	isub
	invokestatic MCClass/Fibonacci(I)I
	iload_0
	iconst_2
	isub
	invokestatic MCClass/Fibonacci(I)I
	iadd
	ireturn
Label1:
.limit stack 3
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_0
	istore_1
Label2:
	iload_1
	bipush 10
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifeq Label4
Label7:
	iload_1
	invokestatic MCClass/Fibonacci(I)I
	invokestatic io/putInt(I)V
Label8:
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
Label1:
	return
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
