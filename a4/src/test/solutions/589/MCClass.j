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
	iload_2
	bipush 10
	if_icmple Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label14
	goto Label9
Label14:
	iload_2
	iconst_2
	irem
	iconst_1
	if_icmpne Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifle Label17
	goto Label8
Label17:
	iload_3
	iload_2
	iadd
	istore_3
Label11:
Label8:
	iload_2
	iload_1
	if_icmpge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifeq Label9
	goto Label7
Label9:
	iload_1
	iload_2
	irem
	iconst_0
	if_icmpne Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label22
	goto Label3
Label22:
	iload_1
	iload_2
	iadd
	bipush 40
	if_icmple Label23
	iconst_1
	goto Label24
Label23:
	iconst_0
Label24:
	ifle Label25
	goto Label4
Label25:
	iload_3
	iload_1
	iadd
	istore_3
Label6:
Label3:
	iload_1
	bipush 20
	if_icmpge Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifeq Label4
	goto Label2
Label4:
	iload_3
	invokestatic io/putIntLn(I)V
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
