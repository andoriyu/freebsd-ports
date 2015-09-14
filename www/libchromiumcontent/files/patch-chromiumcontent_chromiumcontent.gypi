--- chromiumcontent/chromiumcontent.gypi.orig	2015-09-13 02:33:16 UTC
+++ chromiumcontent/chromiumcontent.gypi
@@ -19,7 +19,7 @@
         # On Chrome 41 this is disabled on Windows.
         'v8_use_external_startup_data': 1,
       }],
-      ['OS=="linux"', {
+      ['OS=="freebsd"', {
         # Enable high DPI support on Linux.
         'enable_hidpi': 1,
         # Use Dbus.
@@ -90,7 +90,7 @@
       }],
     ],
     'target_conditions': [
-      ['_type=="static_library" and _toolset=="target" and OS=="linux" and component=="static_library"', {
+      ['_type=="static_library" and _toolset=="target" and OS=="freebsd" and component=="static_library"', {
         'standalone_static_library': 1,
       }],
       ['_target_name in <(v8_libraries) + <(icu_libraries)', {
