.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is isTrue Z from Label0 to Label1
Label0:
	iconst_1
	dup
	istore_1
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label6
	iconst_3
	dup
	istore_1
	iconst_3
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label10
	bipush 6
	dup
	istore_1
	iconst_5
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label14
	bipush 8
	dup
	istore_1
	bipush 8
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	istore_2
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 3
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
