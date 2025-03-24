.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	iconst_2
	istore_1
	iload_1
	iconst_5
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label6:
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	iload_1
	iconst_2
	imul
	istore_1
Label10:
Label7:
	goto Label5
Label4:
Label11:
	bipush 11
	istore_1
	iload_1
	iconst_3
	irem
	iconst_0
	if_icmpeq Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label15
	iload_1
	iconst_3
	imul
	istore_1
Label15:
Label12:
Label5:
	iload_1
	invokestatic io/putInt(I)V
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
