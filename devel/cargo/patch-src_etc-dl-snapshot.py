--- src/etc/dl-snapshot.py.orig	2015-06-27 14:34:09.812696113 -0700
+++ src/etc/dl-snapshot.py	2015-06-27 14:32:21.832703631 -0700
@@ -39,6 +39,8 @@
 
 if (arch == 'i586') or (arch == 'i386'):
     arch = 'i686'
+if (arch == 'amd64'):
+    arch = 'x86_64'
 
 if len(ts) == 2:
     vendor = 'unknown'
@@ -55,6 +57,8 @@
     plat_os = 'winnt'
 elif (target_os == 'darwin'):
     plat_os = 'macos'
+elif (target_os == 'freebsd10.1'):
+    plat_os = 'freebsd'
 platform = "%s-%s" % (plat_os, plat_arch)
 if platform not in snaps[date]:
     raise Exception("no snapshot for the triple '%s'" % triple)
@@ -68,6 +72,9 @@
 elif target_os == 'windows':
     vendor = 'pc'
     target_os = 'windows-gnu'
+elif (target_os == 'freebsd10.1'):
+    vendor = 'unknown'
+    target_os = 'freebsd'
 triple = "%s-%s-%s" % (arch, vendor, target_os)
 hash = snaps[date][platform]
 
@@ -76,7 +83,6 @@
   (date.strip(), tarball)
 dl_path = "target/dl/" + tarball
 dst = "target/snapshot"
-
 if not os.path.isdir('target/dl'):
     os.makedirs('target/dl')
 
