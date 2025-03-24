.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
.var 3 is k I from Label0 to Label1
Label0:
	iconst_1
	istore_1
Label2:
	iload_1
	bipush 7
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifeq Label4
Label7:
	iconst_1
	istore_2
Label9:
	iload_2
	iload_1
	if_icmpgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifeq Label11
	iload_2
	invokestatic io/putInt(I)V
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label9
Label11:
	bipush 7
	iload_1
	isub
	istore_3
Label14:
	iload_3
	iconst_1
	if_icmplt Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifeq Label16
	ldc "*"
	invokestatic io/putString(Ljava/lang/String;)V
Label15:
	iload_3
	iconst_1
	isub
	istore_3
	goto Label14
Label16:
	ldc ""
	invokestatic io/putString(Ljava/lang/String;)V
Label8:
Label3:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label4:
	ldc ""
	invokestatic io/putString(Ljava/lang/String;)V
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
