--- config.def.h.orig	2019-07-31 04:37:20 UTC
+++ config.def.h
@@ -84,31 +84,26 @@ unsigned int tabspaces = 8;
 
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
-	[255] = 0,
-
-	/* more colors can be added after 255 to use with DefaultXX */
-	"#cccccc",
-	"#555555",
+    "#3b4252", /*  0: nord1 */
+    "#bf616a", /*  1: nord11 */
+    "#a3be8c", /*  2: nord14 */
+    "#ebcb8b", /*  3: nord13 */
+    "#81a1c1", /*  4: nord9 */
+    "#b48ead", /*  5: nord15 */
+    "#88c0d0", /*  6: nord8 */
+    "#e5e9f0", /*  7: nord5 */
+    "#4c566a", /*  8: nord3 */
+    "#bf616a", /*  9: nord11 */
+    "#a3be8c", /* 10: nord14 */
+    "#ebcb8b", /* 11: nord3 */
+    "#81a1c1", /* 12: nord9 */
+    "#b48ead", /* 13: nord15 */
+    "#8fbcbb", /* 14: nord7 */
+    "#eceff4", /* 15: nord6 */
+    [255] = 0,
+    // defaults
+    [256] = "#d8dee9", /* 256: nord4 */
+    [257] = "#2e3440", /* 257: nord0 */
 };
 
 
@@ -116,10 +111,10 @@ static const char *colorname[] = {
  * Default colors (colorname index)
  * foreground, background, cursor, reverse cursor
  */
-unsigned int defaultfg = 7;
-unsigned int defaultbg = 0;
-static unsigned int defaultcs = 256;
-static unsigned int defaultrcs = 257;
+unsigned int defaultfg = 256; /* nord4 */
+unsigned int defaultbg = 257; /* nord0 */
+unsigned int defaultcs = 256; /* nord4 */
+unsigned int defaultrcs = 8;  /* nord3 */
 
 /*
  * Default shape of cursor
