.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I
.field static b F
.field static frr [F
.field static arr [I
.field static aStr [Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b F from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 3
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
	iconst_5
	newarray int
	putstatic MCClass.arr [I
	iconst_4
	anewarray java/lang/String
	putstatic MCClass.aStr [Ljava/lang/String;
	return
.end method
