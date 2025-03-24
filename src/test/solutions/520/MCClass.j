.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b F
.field static frr [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b F from Label0 to Label1
.var 3 is arr [I from Label0 to Label1
Label0:
	iconst_5
	newarray int
	astore_3
Label1:
	return
.limit stack 1
.limit locals 4
.end method

.method public static funcVoid(II)V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
.var 3 is d F from Label0 to Label1
.var 4 is e F from Label0 to Label1
.var 5 is f F from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 6
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

.method public static <clinit>()V
.limit stack 1
.limit locals 0
	iconst_4
	newarray float
	putstatic MCClass.frr [F
	return
.end method
