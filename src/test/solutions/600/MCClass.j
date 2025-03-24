.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	anewarray java/lang/String
	astore_1
	aload_1
	iconst_2
	ldc "stringMain"
	aastore
	aload_1
	iconst_2
	aload_1
	invokestatic MCClass/foo([Ljava/lang/String;)[Ljava/lang/String;
	iconst_2
	aaload
	aastore
	aload_1
	iconst_2
	aaload
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
.limit locals 2
.end method

.method public static foo([Ljava/lang/String;)[Ljava/lang/String;
.var 0 is x [Ljava/lang/String; from Label0 to Label1
Label0:
	aload_0
	iconst_2
	ldc "stringFoo"
	aastore
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
