.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a Ljava/lang/String;
.field static b Ljava/lang/String;
.field static gArr [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [Ljava/lang/String; from Label0 to Label1
.var 2 is c Ljava/lang/String; from Label0 to Label1
.var 3 is d Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_4
	anewarray java/lang/String
	astore_1
	ldc "ccc"
	astore_2
	ldc "cd"
	dup
	astore_3
	astore_2
	aload_2
	putstatic MCClass.a Ljava/lang/String;
	ldc "string"
	dup
	astore_3
	putstatic MCClass.b Ljava/lang/String;
	aload_1
	iconst_0
	ldc "strDemo"
	aastore
	getstatic MCClass.gArr [Ljava/lang/String;
	iconst_0
	aload_1
	iconst_0
	ldc "stringDemo"
	dup_x2
	aastore
	aastore
	getstatic MCClass.gArr [Ljava/lang/String;
	iconst_1
	getstatic MCClass.gArr [Ljava/lang/String;
	iconst_2
	aload_1
	iconst_2
	aload_1
	iconst_0
	aaload
	dup_x2
	aastore
	dup_x2
	aastore
	aastore
	getstatic MCClass.gArr [Ljava/lang/String;
	iconst_1
	aaload
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label1:
	return
.limit stack 8
.limit locals 4
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
	putstatic MCClass.gArr [Ljava/lang/String;
	return
.end method
