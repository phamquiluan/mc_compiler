.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I
.field static j I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is iSum I from Label0 to Label1
Label0:
	bipush 10
	putstatic MCClass.i I
.var 4 is i F from Label2 to Label3
Label2:
	ldc 11.8
	fstore 4
	fload 4
	invokestatic io/putFloat(F)V
Label3:
Label4:
	bipush 11
	putstatic MCClass.i I
Label5:
	getstatic MCClass.i I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 1
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
