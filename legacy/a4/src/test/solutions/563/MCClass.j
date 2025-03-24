.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is isTrue Z from Label0 to Label1
.var 2 is a I from Label0 to Label1
.var 3 is b I from Label0 to Label1
.var 4 is arr [I from Label0 to Label1
Label0:
	iconst_2
	newarray int
	astore 4
	iconst_0
	istore_1
	bipush 14
	istore_2
	bipush 12
	istore_3
	aload 4
	iconst_0
	bipush 14
	iastore
	aload 4
	iconst_0
	iaload
	iload_2
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_1
	iload_1
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 4
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

.method public static <clinit>()V
.limit stack 1
.limit locals 0
	iconst_4
	newarray float
	putstatic MCClass.arr [F
	return
.end method
