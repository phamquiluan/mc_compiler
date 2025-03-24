.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [F from Label0 to Label1
Label0:
	iconst_3
	newarray float
	astore_1
	aload_1
	iconst_2
	ldc 1.5
	fastore
	aload_1
	invokestatic MCClass/foo([F)[F
	pop
	aload_1
	iconst_2
	aload_1
	invokestatic MCClass/foo([F)[F
	iconst_2
	faload
	ldc 1.1
	fadd
	fastore
	aload_1
	iconst_2
	faload
	invokestatic io/putFloatLn(F)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static foo([F)[F
.var 0 is x [F from Label0 to Label1
Label0:
	aload_0
	iconst_2
	ldc 5.1
	fastore
	aload_0
	areturn
Label1:
.limit stack 3
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
