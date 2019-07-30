--- xpra/client/gtk_base/client_launcher.py.orig	2018-07-19 22:43:51 UTC
+++ xpra/client/gtk_base/client_launcher.py
@@ -165,7 +165,6 @@ class ApplicationWindow:
         self.window.set_default_size(400, 260)
         self.window.set_border_width(20)
         self.window.set_title("Xpra Launcher")
-        self.window.modify_bg(STATE_NORMAL, gdk.Color(red=65535, green=65535, blue=65535))
 
         self.window.set_position(WIN_POS_CENTER)
 
