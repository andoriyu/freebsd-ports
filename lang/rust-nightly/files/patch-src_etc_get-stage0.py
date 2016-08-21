--- src/etc/get-stage0.py.orig	2016-08-20 14:09:53 UTC
+++ src/etc/get-stage0.py
@@ -31,7 +31,8 @@ def main(triple):
     filename = 'rustc-{}-{}.tar.gz'.format(channel, triple)
     url = 'https://static.rust-lang.org/dist/{}/{}'.format(date, filename)
     dst = dl_dir + '/' + filename
-    bootstrap.get(url, dst)
+    if not os.path.exists(dst):
+        bootstrap.get(url, dst)
 
     stage0_dst = triple + '/stage0'
     if os.path.exists(stage0_dst):
