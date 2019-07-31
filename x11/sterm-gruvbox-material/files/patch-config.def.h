--- config.def.h.orig	2019-07-31 03:21:03 UTC
+++ config.def.h
@@ -84,25 +84,21 @@ unsigned int tabspaces = 8;
 
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
+	"#32302f",
+	"#3c3836",
+	"#504945",
+	"#665c54",
+	"#7c6f64",
+	"#928374",
+	"#a89984",
+	"#dfbf8e",
+	"#ea6962",
+    "#e78a4e",
+	"#e3a84e",
+	"#a9b665",
+	"#89b482",
+	"#7daea3",
+	"#d3869b",
 
 	[255] = 0,
 
