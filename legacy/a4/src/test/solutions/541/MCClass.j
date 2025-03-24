.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static fNum F
.field static str2 Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is isT Z from Label0 to Label1
.var 2 is isTrue Z from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_0
	istore_2
	iconst_1
	dup
	istore_2
	istore_1
	iload_1
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 5
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
