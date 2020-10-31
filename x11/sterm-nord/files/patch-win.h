--- win.h.orig	2020-10-31 19:58:22 UTC
+++ win.h
@@ -25,7 +25,7 @@ enum win_mode {
 
 void xbell(void);
 void xclipcopy(void);
-void xdrawcursor(int, int, Glyph, int, int, Glyph);
+void xdrawcursor(int, int, Glyph, int, int, Glyph, Line, int);
 void xdrawline(Line, int, int, int);
 void xfinishdraw(void);
 void xloadcols(void);
