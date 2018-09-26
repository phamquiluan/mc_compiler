.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static fNum F
.field static str [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass.str [Ljava/lang/String;
	iconst_0
	ldc "null"
	aastore
	getstatic MCClass.str [Ljava/lang/String;
	iconst_1
	ldc "text"
	aastore
	getstatic MCClass.str [Ljava/lang/String;
	iconst_2
	ldc "notNull"
	aastore
	getstatic MCClass.str [Ljava/lang/String;
	iconst_0
	getstatic MCClass.str [Ljava/lang/String;
	iconst_1
	ldc "final"
	dup_x2
	aastore
	aastore
	getstatic MCClass.str [Ljava/lang/String;
	iconst_0
	aaload
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
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

.method public static <clinit>()V
.limit stack 1
.limit locals 0
	iconst_4
	anewarray java/lang/String
	putstatic MCClass.str [Ljava/lang/String;
	return
.end method
