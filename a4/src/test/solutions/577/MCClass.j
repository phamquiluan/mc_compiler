.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a F from Label0 to Label1
Label0:
	iconst_2
	invokestatic MCClass/ax(I)F
	fstore_1
	fload_1
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static ax(I)F
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_2
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	ldc 1.2
	freturn
Label4:
	ldc 2.0
	freturn
Label1:
.limit stack 2
.limit locals 1
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
