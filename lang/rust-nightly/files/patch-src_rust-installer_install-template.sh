--- src/rust-installer/install-template.sh.orig	2016-09-14 00:27:24 UTC
+++ src/rust-installer/install-template.sh
@@ -834,6 +834,7 @@ valopt components "" "comma-separated li
 flag list-components "list available components"
 valopt libdir "$CFG_DESTDIR_PREFIX/lib" "install libraries"
 valopt mandir "$CFG_DESTDIR_PREFIX/share/man" "install man pages in PATH"
+valopt docdir "$CFG_DESTDIR_PREFIX/share/doc/rust" "install documentation in PATH"
 opt ldconfig 1 "run ldconfig after installation (Linux only)"
 opt verify 1 "obsolete"
 flag verbose "run with verbose output"
