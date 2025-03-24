.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is iSum I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_0
	istore_2
Label2:
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	bipush 17
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
	goto Label4
Label9:
	iload_2
	iload_1
	iadd
	istore_2
Label6:
Label3:
	iload_1
	bipush 20
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifeq Label4
	goto Label2
Label4:
	iload_2
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 3
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
