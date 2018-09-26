.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [F from Label0 to Label1
Label0:
	iconst_5
	newarray float
	astore_1
	aload_1
	iconst_0
	ldc 111.2
	fastore
	aload_1
	iconst_0
	faload
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 3
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
