--- mk/main.mk.orig	2016-09-13 17:54:55 UTC
+++ mk/main.mk
@@ -135,7 +135,7 @@ ifneq ($(wildcard $(NON_BUILD_TARGET)),)
 CFG_INFO := $(info cfg: non-build target triples $(NON_BUILD_TARGET))
 endif
 
-CFG_RUSTC_FLAGS := $(RUSTFLAGS)
+CFG_RUSTC_FLAGS := $(RUSTFLAGS) -L/usr/local/lib
 CFG_GCCISH_CFLAGS :=
 CFG_GCCISH_LINK_FLAGS :=
 
