.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static str1 Ljava/lang/String;
.field static str2 Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "strDemo"
	putstatic MCClass.str1 Ljava/lang/String;
	getstatic MCClass.str1 Ljava/lang/String;
	putstatic MCClass.str2 Ljava/lang/String;
	getstatic MCClass.str2 Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
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
