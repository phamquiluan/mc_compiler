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
	istore_3
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
	iconst_0
	istore_2
Label9:
	iload_2
	iload_1
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifeq Label11
Label14:
	iload_1
	iload_2
	iadd
	bipush 17
	if_icmple Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
	goto Label11
Label18:
	iload_2
	iconst_2
	irem
	iconst_0
	if_icmpne Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label21
	goto Label10
Label21:
	iload_3
	iload_2
	iadd
	istore_3
Label15:
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label9
Label11:
	iload_3
	bipush 27
	if_icmple Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	ifle Label24
	goto Label4
Label24:
	iload_1
	iconst_3
	irem
	iconst_0
	if_icmpeq Label25
	iconst_1
	goto Label26
Label25:
	iconst_0
Label26:
	ifle Label27
	goto Label3
Label27:
	iload_3
	iload_1
	iadd
	istore_3
Label8:
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
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
