.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Z from Label0 to Label1
.var 2 is b Z from Label0 to Label1
.var 3 is isTrue Z from Label0 to Label1
.var 4 is arr [Z from Label0 to Label1
Label0:
	iconst_3
	newarray boolean
	astore 4
	iconst_1
	istore_1
	iconst_1
	ifne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_2
	aload 4
	iconst_0
	iload_1
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	bastore
	aload 4
	iconst_1
	iload_2
	ifne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	bastore
	aload 4
	iconst_0
	baload
	ifle Label10
	aload 4
	iconst_1
	baload
	ifle Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	istore_3
	iload_3
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 9
.limit locals 5
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
