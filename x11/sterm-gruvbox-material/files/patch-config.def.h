--- config.def.h.orig	2018-04-04 17:53:36 UTC
+++ config.def.h
@@ -5,7 +5,7 @@
  *
  * font: see http://freedesktop.org/software/fontconfig/fontconfig-user.html
  */
-static char *font = "Liberation Mono:pixelsize=12:antialias=true:autohint=true";
+static char *font = "FuraMono Nerd Font:pixelsize=14:antialias=true:autohint=true";
 static int borderpx = 2;
 
 /*
@@ -63,7 +63,7 @@ static unsigned int cursorthickness = 2;
 static int bellvolume = 0;
 
 /* default TERM value */
-char *termname = "st-256color";
+char *termname = "xterm256color";
 
 /*
  * spaces per tab
@@ -84,31 +84,22 @@ unsigned int tabspaces = 8;
 
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
+	"#7c6f64", /* hard contrast: #1d2021 / soft contrast: #32302f */
+	"#ea6962",
+	"#a9b665",
+	"#e3a84e",
+	"#7daea3",
+	"#d3869b",
+	"#89b482",
+	"#a89984",
+	"#32302f",
+	"#ea6962",
+	"#a9b665",
+	"#e78a4e",
+	"#7daea3",
+	"#d3869b",
+	"#89b482",
+	"#dfbf8e",
 };
 
 
@@ -116,10 +107,10 @@ static const char *colorname[] = {
  * Default colors (colorname index)
  * foreground, background, cursor, reverse cursor
  */
-unsigned int defaultfg = 7;
+unsigned int defaultfg = 15;
 unsigned int defaultbg = 0;
-static unsigned int defaultcs = 256;
-static unsigned int defaultrcs = 257;
+static unsigned int defaultcs = 15;
+static unsigned int defaultrcs = 15;
 
 /*
  * Default shape of cursor
