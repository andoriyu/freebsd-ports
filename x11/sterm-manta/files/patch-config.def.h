--- config.def.h.orig	2019-07-30 05:20:38 UTC
+++ config.def.h
@@ -84,31 +84,24 @@ unsigned int tabspaces = 8;
 
 /* Terminal colors (16 first used in escape sequence) */
 static const char *colorname[] = {
-	/* 8 normal colors */
-	"black",
-	"red3",
-	"green3",
-	"yellow3",
-	"blue2",
-	"magenta3",
-	"cyan3",
-	"gray90",
-
-	/* 8 bright colors */
-	"gray50",
-	"red",
-	"green",
-	"yellow",
-	"#5c5cff",
-	"magenta",
-	"cyan",
-	"white",
-
+    "#1E2541",
+    "#F0719B",
+    "#5AF7B0",
+    "#FFA56B",
+    "#57C7FF",
+    "#C792EA",
+    "#89DDFF",
+    "#EEFFFF",
+    "#354274",
+    "#F02E6E",
+    "#2CE592",
+    "#FF8537",
+    "#1DA0E2",
+    "#A742EA",
+    "#47BAE8",
+    "#DEE6E7",
+    "#2A335A",
 	[255] = 0,
-
-	/* more colors can be added after 255 to use with DefaultXX */
-	"#cccccc",
-	"#555555",
 };
 
 
@@ -118,8 +111,8 @@ static const char *colorname[] = {
  */
 unsigned int defaultfg = 7;
 unsigned int defaultbg = 0;
-static unsigned int defaultcs = 256;
-static unsigned int defaultrcs = 257;
+static unsigned int defaultcs = 7;
+static unsigned int defaultrcs = 0;
 
 /*
  * Default shape of cursor
