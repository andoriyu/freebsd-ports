--- chromiumcontent/chromiumcontent.gypi.orig	2015-09-12 20:04:24 UTC
+++ chromiumcontent/chromiumcontent.gypi
@@ -1,4 +1,4 @@
-{
+{p\
   'variables': {
     # Enalbe using proprietary codecs.
     'proprietary_codecs': 1,
@@ -19,21 +19,21 @@
         # On Chrome 41 this is disabled on Windows.
         'v8_use_external_startup_data': 1,
       }],
-      ['OS=="linux"', {
+      ['OS=="freebsd"', {
         # Enable high DPI support on Linux.
         'enable_hidpi': 1,
         # Use Dbus.
         'use_dbus': 1,
         # Make Linux build contain debug symbols, this flag will add '-g' to
         # cflags.
-        'linux_dump_symbols': 1,
+        'freebsd_dump_symbols': 1,
         # The Linux build of libchromiumcontent.so depends on, but doesn't
         # provide, tcmalloc by default.  Disabling tcmalloc here also prevents
         # any conflicts when linking to binaries or libraries that don't use
         # tcmalloc.
-        'linux_use_tcmalloc': 0,
+        'freebsd_use_tcmalloc': 0,
         # Force using gold linker.
-        'linux_use_bundled_gold': 1,
+        'freebsd_use_bundled_gold': 1,
         'conditions': [
           ['target_arch=="arm"', {
             'arm_version': 7,
@@ -82,7 +82,7 @@
       'U_STATIC_IMPLEMENTATION',
     ],
     'conditions': [
-      ['OS=="linux" and target_arch=="arm"', {
+      ['OS=="freebsd" and target_arch=="arm"', {
         # Work around ODR violations.
         'ldflags!': [
           '-Wl,--detect-odr-violations',
