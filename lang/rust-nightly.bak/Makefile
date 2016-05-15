# Created by: Jean-Sébastien Pédron <dumbbell@FreeBSD.org>
# $FreeBSD: head/lang/rust-nightly/Makefile 392106 2015-07-14 22:36:53Z dumbbell $

PORTNAME=	rust-nightly
PORTVERSION=	1.10.0.20160423
CATEGORIES=	lang
MASTER_SITES=	 https://static.rust-lang.org/dist/2016-04-13/:bootstrap
DISTFILES=	${RUST_BOOT}:bootstrap
EXTRACT_ONLY=	${DISTNAME}${_GITHUB_EXTRACT_SUFX} \
		${DISTFILE_compiler_rt} \
		${DISTFILE_hoedown} \
		${DISTFILE_jemalloc} \
		${DISTFILE_rust_installer} \
    ${DISTFILE_liblibc} \
		${DISTFILE_llvm}

MAINTAINER=	dumbbell@FreeBSD.org
COMMENT=	Language with a focus on memory safety and concurrency

LICENSE=	APACHE20 \
		MIT
LICENSE_COMB=	dual
LICENSE_FILE=	${WRKSRC}/LICENSE-APACHE \
		${WRKSRC}/LICENSE-MIT

USE_GITHUB=	yes
GH_ACCOUNT=	rust-lang
GH_PROJECT=	rust \
		compiler-rt:compiler_rt \
		hoedown:hoedown \
		jemalloc:jemalloc \
		rust-installer:rust_installer \
		libc:liblibc \
		llvm:llvm
GH_TAGNAME= 8d0dd7876e733555b0284e9b6cbf0f33ed792b67 \
		57315f7:compiler_rt \
		238c4d5:hoedown \
		aab1c0a:jemalloc \
		c37d374:rust_installer \
		7265c17:liblibc \
		25c7dc3:llvm

ONLY_FOR_ARCHS=	amd64
ONLY_FOR_ARCHS_REASON=	requires prebuilt bootstrap compiler

RUST_PLATFORM=        ${OPSYS:tl}
RUST_ARCH=        ${ARCH:C/amd64/x86_64/}

#ALL_TARGET=snap-stage3
# FIXME: The bootstrapped rustc adds -L/usr/local/lib in front of
# the LDFLAGS. When stage0's rustc is linked, it picks the installed
# librust*so and fails.
CONFLICTS_BUILD=	rust \
			rust-nightly
CONFLICTS_INSTALL=	rust-nightly

RUST_BOOT=	rustc-beta-x86_64-unknown-freebsd.tar.gz

# Rust's libraries are named librustc_${component}-${RUST_VSN_HASH}.so.
# The hash depends on Rust version and channel. See
# $(CFG_FILENAME_EXTRA) definition in src/main.mk.
RUST_VSN=	${PORTVERSION:R}
RUST_CHANNEL=	${PORTNAME:S/^rust-//}
RUST_VSN_HASH!=	/usr/bin/printf '%s' ${RUST_VSN}-${RUST_CHANNEL} | /sbin/md5 -q | cut -c 1-8

PLIST_SUB+=	RUST_VSN_HASH=${RUST_VSN_HASH}
PLIST_SUB+= RUST_TARGET=${RUST_ARCH}-unknown-${RUST_PLATFORM}

USES=		gmake python:2,build
HAS_CONFIGURE=	yes
CONFIGURE_ARGS=	--disable-valgrind --disable-docs \
		--enable-clang --mandir=${MANPREFIX}/man \
		--release-channel=${RUST_CHANNEL}

 Use LLVM from ports, instead of the copy shipped with rust.
LLVM_VER=	37
BUILD_DEPENDS+=	llvm${LLVM_VER}>=0:${PORTSDIR}/devel/llvm${LLVM_VER}
CONFIGURE_ARGS+=--llvm-root=${LOCALBASE}/llvm${LLVM_VER}

MAKE_ARGS+=	VERBOSE=1

OPTIONS_DEFINE=		LLNEXTGEN
LLNEXTGEN_DESC=		Build with grammar verification

LLNEXTGEN_BUILD_DEPENDS=	LLnextgen:${PORTSDIR}/devel/llnextgen

.include <bsd.port.options.mk>

.if ${OPSYS} == FreeBSD && ${OSVERSION} < 1000000
BROKEN=		Only compiles on FreeBSD 10 and 11
.endif

.if ${OPSYS} == DragonFly
IGNORE=		please use lang/rust-dragonfly instead
.endif

post-extract:
	@(${RMDIR} ${WRKSRC}/src/compiler-rt && \
	  ${MV} ${WRKSRC_compiler_rt} ${WRKSRC}/src/compiler-rt)
	@(${RMDIR} ${WRKSRC}/src/rt/hoedown && \
	  ${MV} ${WRKSRC_hoedown} ${WRKSRC}/src/rt/hoedown)
	@(${RMDIR} ${WRKSRC}/src/jemalloc && \
	  ${MV} ${WRKSRC_jemalloc} ${WRKSRC}/src/jemalloc)
	@(${RMDIR} ${WRKSRC}/src/rust-installer && \
	  ${MV} ${WRKSRC_rust_installer} ${WRKSRC}/src/rust-installer)
	@(${RMDIR} ${WRKSRC}/src/liblibc && \
	  ${MV} ${WRKSRC_liblibc} ${WRKSRC}/src/liblibc)
	@(${RMDIR} ${WRKSRC}/src/llvm && \
	  ${MV} ${WRKSRC_llvm} ${WRKSRC}/src/llvm)
	@${MKDIR} ${WRKSRC}/dl
	${LN} -sf ${DISTDIR}/${RUST_BOOT} ${WRKSRC}/dl
	(cd ${WRKSRC} && ${FIND} . -type d -exec ${CHMOD} 0755 {} \;)

post-patch:
	@${REINPLACE_CMD} -e 's|%%LOCALBASE%%|${LOCALBASE}|' \
		${WRKSRC}/mk/main.mk
	@${REINPLACE_CMD} -e 's|gdb|${LOCALBASE}/bin/gdb|' \
		${WRKSRC}/src/etc/rust-gdb

# In case the previous "make stage" failed, this ensures rust's
# install.sh won't backup previously staged files before reinstalling
# new ones. Otherwise, the staging directory is polluted with unneeded
# files.
pre-install:
	@if test -f ${STAGEDIR}${PREFIX}/lib/rustlib/manifest-rustc; then \
		${SED} -E -e 's,^(dir|file:),${STAGEDIR},' \
		< ${STAGEDIR}${PREFIX}/lib/rustlib/manifest-rustc \
		| ${XARGS} ${RM}; \
	fi
	@if test -f ${STAGEDIR}${PREFIX}/lib/rustlib/manifest-rust-std-x86_64-unknown-freebsd; then \
		${SED} -E -e 's,^(dir|file:),${STAGEDIR},' \
		< ${STAGEDIR}${PREFIX}/lib/rustlib/manifest-rustc \
		| ${XARGS} ${RM}; \
	fi
	@${RM} \
		${STAGEDIR}${PREFIX}/lib/rustlib/components \
		${STAGEDIR}${PREFIX}/lib/rustlib/manifest-rustc \
		${STAGEDIR}${PREFIX}/lib/rustlib/rust-installer-version \
		${STAGEDIR}${PREFIX}/lib/rustlib/uninstall.sh \
		${STAGEDIR}${PREFIX}/lib/rustlib/manifest-rust-std-x86_64-unknown-freebsd

post-install:
	@${RM} ${STAGEDIR}${PREFIX}/lib/rustlib/install.log
	@${REINPLACE_CMD} -e 's|${STAGEDIR}||' \
		${STAGEDIR}${PREFIX}/lib/rustlib/manifest-rustc
	@${RM} ${STAGEDIR}${PREFIX}/lib/rustlib/manifest-rustc.bak
	@${REINPLACE_CMD} -e 's|${STAGEDIR}||' \
		${STAGEDIR}${PREFIX}/lib/rustlib/manifest-rust-std-x86_64-unknown-freebsd
	@${RM} ${STAGEDIR}${PREFIX}/lib/rustlib/manifest-rust-std-x86_64-unknown-freebsd.bak
	@${STRIP_CMD} \
		${STAGEDIR}${PREFIX}/bin/rustc \
		${STAGEDIR}${PREFIX}/bin/rustdoc \
		${STAGEDIR}${PREFIX}/lib/*.so \
		${STAGEDIR}${PREFIX}/lib/rustlib/*/lib/*.so
.if ${PORT_OPTIONS:MDOCS}
	@${MV} ${STAGEDIR}${PREFIX}/share/doc/rust ${STAGEDIR}${DOCSDIR}
.endif

.include <bsd.port.mk>
