--- mk/install.mk.orig	2015-06-26 18:12:36.460747505 -0700
+++ mk/install.mk	2015-06-26 18:12:54.951746525 -0700
@@ -9,12 +9,7 @@
 # except according to those terms.
 
 install:
-ifeq (root user, $(USER) $(patsubst %,user,$(SUDO_USER)))
-# Build the dist as the original user
-	$(Q)sudo -u "$$SUDO_USER" $(MAKE) prepare_install
-else
 	$(Q)$(MAKE) prepare_install
-endif
 ifeq ($(CFG_DISABLE_DOCS),)
 	$(Q)cd tmp/empty_dir && sh ../../tmp/dist/$(DOC_PKG_NAME)-$(CFG_BUILD)/install.sh --prefix="$(DESTDIR)$(CFG_PREFIX)" --libdir="$(DESTDIR)$(CFG_LIBDIR)" --mandir="$(DESTDIR)$(CFG_MANDIR)"
 endif
@@ -25,12 +20,7 @@
 prepare_install: dist-tar-bins | tmp/empty_dir
 
 uninstall:
-ifeq (root user, $(USER) $(patsubst %,user,$(SUDO_USER)))
-# Build the dist as the original user
-	$(Q)sudo -u "$$SUDO_USER" $(MAKE) prepare_uninstall
-else
 	$(Q)$(MAKE) prepare_uninstall
-endif
 ifeq ($(CFG_DISABLE_DOCS),)
 	$(Q)cd tmp/empty_dir && sh ../../tmp/dist/$(DOC_PKG_NAME)-$(CFG_BUILD)/install.sh --uninstall --prefix="$(DESTDIR)$(CFG_PREFIX)" --libdir="$(DESTDIR)$(CFG_LIBDIR)" --mandir="$(DESTDIR)$(CFG_MANDIR)"
 endif
