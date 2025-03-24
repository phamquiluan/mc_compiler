.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a Z
.field static b Z
.field static gArr [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [Z from Label0 to Label1
.var 2 is c Z from Label0 to Label1
.var 3 is d Z from Label0 to Label1
Label0:
	iconst_4
	newarray boolean
	astore_1
	iconst_1
	istore_2
	iconst_0
	dup
	istore_3
	istore_2
	iload_2
	putstatic MCClass.a Z
	iconst_0
	dup
	istore_3
	putstatic MCClass.b Z
	aload_1
	iconst_0
	iconst_1
	bastore
	getstatic MCClass.gArr [Z
	iconst_0
	aload_1
	iconst_0
	iconst_1
	dup_x2
	bastore
	bastore
	getstatic MCClass.gArr [Z
	iconst_1
	getstatic MCClass.gArr [Z
	iconst_2
	aload_1
	iconst_2
	iload_3
	dup_x2
	bastore
	dup_x2
	bastore
	bastore
	getstatic MCClass.gArr [Z
	iconst_1
	baload
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 13
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
	newarray boolean
	putstatic MCClass.gArr [Z
	return
.end method
