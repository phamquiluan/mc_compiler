.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is res I from Label0 to Label1
Label0:
	bipush 11
	istore_1
	bipush 12
	istore_2
	iload_1
	iload_2
	invokestatic MCClass/foo(II)I
	istore_3
	iload_3
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method

.method public static foo(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label6:
	iload_0
	iconst_1
	if_icmpeq Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
Label12:
	iload_0
	iconst_1
	iadd
	istore_0
Label13:
	goto Label11
Label10:
Label14:
	iload_1
	iconst_1
	if_icmpne Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
Label20:
	iconst_1
	ireturn
Label21:
	goto Label19
Label18:
Label22:
	iload_0
	iconst_3
	iadd
	istore_0
Label23:
Label19:
Label15:
Label11:
	iload_0
	ireturn
Label7:
	goto Label5
Label4:
Label24:
	iconst_0
	ireturn
Label25:
Label5:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static complex(III)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label6:
	iload_0
	ireturn
Label7:
	goto Label5
Label4:
Label8:
	iload_2
	iload_1
	if_icmpne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label12
Label14:
	iload_2
	ireturn
Label15:
	goto Label13
Label12:
Label16:
	iload_1
	ireturn
Label17:
Label13:
Label9:
Label5:
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
