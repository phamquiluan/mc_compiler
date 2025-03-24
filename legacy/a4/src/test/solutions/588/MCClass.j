.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is iSum I from Label0 to Label1
Label0:
	iconst_0
	istore_1
	iconst_0
	istore_2
	iconst_0
	istore_3
Label2:
Label5:
	iconst_0
	istore_2
	iload_1
	iconst_1
	iadd
	istore_1
Label7:
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
	iload_3
	iload_2
	iadd
	istore_3
Label11:
Label8:
	iload_2
	iload_1
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifeq Label9
	goto Label7
Label9:
	iload_3
	iload_1
	iadd
	istore_3
Label6:
Label3:
	iload_1
	bipush 20
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifeq Label4
	goto Label2
Label4:
	iload_3
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
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
