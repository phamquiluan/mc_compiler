.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static fNum F
.field static str2 Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is iNum I from Label0 to Label1
Label0:
	bipush 14
	istore_1
	iload_1
	i2f
	putstatic MCClass.fNum F
	getstatic MCClass.fNum F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 1
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
