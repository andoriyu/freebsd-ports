--- xpra/client/gtk_base/start_new_command.py.orig	2018-07-19 22:43:57 UTC
+++ xpra/client/gtk_base/start_new_command.py
@@ -45,7 +45,6 @@ class StartNewCommand(object):
         self.window.set_default_size(400, 150)
         self.window.set_border_width(20)
         self.window.set_title("Start New Command")
-        self.window.modify_bg(STATE_NORMAL, gdk.Color(red=65535, green=65535, blue=65535))
 
         icon_pixbuf = self.get_icon("forward.png")
         if icon_pixbuf:
