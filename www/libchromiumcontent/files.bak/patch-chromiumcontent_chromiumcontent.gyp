--- chromiumcontent/chromiumcontent.gyp.orig	2015-09-12 20:04:13 UTC
+++ chromiumcontent/chromiumcontent.gyp
@@ -8,7 +8,7 @@
         '<(DEPTH)/chrome/chrome.gyp:chromedriver',
       ],
       'conditions': [
-        ['OS=="linux"', {
+        ['OS=="freebsd"', {
           'dependencies': [
             'chromiumviews',
             '<(DEPTH)/build/linux/system.gyp:libspeechd',
@@ -53,7 +53,7 @@
     },
   ],
   'conditions': [
-    ['OS in ["win", "linux"]', {
+    ['OS in ["win", "freebsd"]', {
       'targets': [
         {
           'target_name': 'chromiumviews',
@@ -67,11 +67,11 @@
             '<(DEPTH)/ui/wm/wm.gyp:wm',
           ],
           'conditions': [
-            ['OS=="linux"', {
+            ['OS=="freebsd"', {
               'dependencies': [
                 '<(DEPTH)/chrome/browser/ui/libgtk2ui/libgtk2ui.gyp:gtk2ui',
               ],
-            }],  # OS=="linux"
+            }],  # OS=="freebsd"
           ],
         },
       ],
