--- st.c.orig	2020-10-31 19:55:58 UTC
+++ st.c
@@ -2581,7 +2581,8 @@ draw(void)
 
 	drawregion(0, 0, term.col, term.row);
 	xdrawcursor(cx, term.c.y, term.line[term.c.y][cx],
-			term.ocx, term.ocy, term.line[term.ocy][term.ocx]);
+			term.ocx, term.ocy, term.line[term.ocy][term.ocx],
+			term.line[term.ocy], term.col);
 	term.ocx = cx;
 	term.ocy = term.c.y;
 	xfinishdraw();
