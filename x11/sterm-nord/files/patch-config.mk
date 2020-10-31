--- config.mk.orig	2020-10-31 19:51:56 UTC
+++ config.mk
@@ -15,10 +15,12 @@ PKG_CONFIG = pkg-config
 # includes and libs
 INCS = -I$(X11INC) \
        `$(PKG_CONFIG) --cflags fontconfig` \
-       `$(PKG_CONFIG) --cflags freetype2`
+       `$(PKG_CONFIG) --cflags freetype2` \
+       `$(PKG_CONFIG) --cflags harfbuzz`
 LIBS = -L$(X11LIB) -lm -lrt -lX11 -lutil -lXft \
        `$(PKG_CONFIG) --libs fontconfig` \
-       `$(PKG_CONFIG) --libs freetype2`
+       `$(PKG_CONFIG) --libs freetype2` \
+       `$(PKG_CONFIG) --libs harfbuzz`
 
 # flags
 STCPPFLAGS = -DVERSION=\"$(VERSION)\" -D_XOPEN_SOURCE=600
