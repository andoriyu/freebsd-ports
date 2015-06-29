# Created by: Jyun-Yan You <jyyou@cs.nctu.edu.tw>
# $FreeBSD: head/lang/rust/Makefile 390497 2015-06-24 17:09:27Z dumbbell $

PORTNAME=	rust-nightly
PORTVERSION=	1.2.0n
PORTREVISION=	2
CATEGORIES=	lang


USE_GITHUB=	yes

GH_ACCOUNT=	rust-lang \

GH_PROJECT= rust \
						compiler-rt:rt \
						jemalloc:jemalloc \
						rust-installer:installer \
						hoedown:hoedown

RT_TAG=					58ab642
JEMALLOC_TAG=		e24a1a0
INSTALLER_TAG=	8e4f8ea
HOEDOWN_TAG=		238c4d5
GH_TAGNAME= a973e4cda5191040ca219fb4a4f8041e9b560301 \
						${RT_TAG}:rt \
						${JEMALLOC_TAG}:jemalloc \
						${INSTALLER_TAG}:installer \
						${HOEDOWN_TAG}:hoedown
MASTER_SITES=	${GH} \
	http://static.rust-lang.org/stage0-snapshots/:bootstrap

RUST_SOURCE= ${GH_ACCOUNT}-${GH_PROJECT}-${PORTVERSION}-${GH_TAGNAME}_GH0
DISTFILES+= ${RUST_SOURCE} \
	${RUST_BOOT}:bootstrap

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Language with a focus on memory safety and concurrency

LICENSE=	APACHE20 \
		MIT
LICENSE_COMB=	dual
LICENSE_FILE=	${WRKSRC}/LICENSE-APACHE \
		${WRKSRC}/LICENSE-MIT

ONLY_FOR_ARCHS=	amd64
ONLY_FOR_ARCHS_REASON=	requires prebuilt bootstrap compiler

# FIXME: The bootstrapped rustc adds -L/usr/local/lib in front of
# the LDFLAGS. When stage0's rustc is linked, it picks the installed
# librust*so and fails.
CONFLICTS_BUILD=	rust \
			rust-nightly
CONFLICTS_INSTALL=	rust

RUST_SOURCE=	${DISTNAME}-src${EXTRACT_SUFX}
RUST_BOOT=	rust-stage0-${RUST_BOOT_SIG}.tar.bz2
#RUST_BOOT_SIG=	2015-04-27-857ef6e-freebsd-x86_64-18925db56f6298cc190d1f41615ab5871de1dda0

RUST_BOOT_SIG=	2015-05-24-ba0e1cd-freebsd-x86_64-370db40613f5c08563ed7e38357826dd42d4e0f8
USES=		gmake python:2,build
HAS_CONFIGURE=	yes
CONFIGURE_ARGS=	--disable-valgrind --disable-docs \
		--enable-clang --mandir=${MANPREFIX}/man \
		--release-channel=nightly


MAKE_JOBS_UNSAFE=yes
# Use LLVM from ports, instead of the copy shipped with rust.
LLVM_VER=	36
BUILD_DEPENDS+=	llvm${LLVM_VER}>=0:${PORTSDIR}/devel/llvm${LLVM_VER}
CONFIGURE_ARGS+=--llvm-root=${LOCALBASE}/llvm${LLVM_VER}

.if defined(BATCH) || defined(PACKAGE_BUILDING)
MAKE_ARGS+=	VERBOSE=1
.endif

OPTIONS_DEFINE=		LLNEXTGEN
LLNEXTGEN_DESC=		Build with grammar verification

LLNEXTGEN_BUILD_DEPENDS=	LLnextgen:${PORTSDIR}/devel/llnextgen

.include <bsd.port.pre.mk>

.if ${OPSYS} == FreeBSD && ${OSVERSION} < 1000000
BROKEN=		Only compiles on FreeBSD 10 and 11
.endif

.if ${OPSYS} == DragonFly
IGNORE=		please use lang/rust-dragonfly instead
.endif

post-extract:
	@${MKDIR} ${WRKSRC}/dl
	@${LN} -sf ${DISTDIR}/${RUST_BOOT} ${WRKSRC}/dl
	@${RMDIR} ${WRKSRC}/src/compiler-rt
	@${LN} -sf ${WRKSRC}/../compiler-rt-${RT_TAG} ${WRKSRC}/src/compiler-rt
	@${RMDIR} ${WRKSRC}/src/jemalloc
	@${LN} -sf ${WRKSRC}/../jemalloc-${JEMALLOC_TAG} ${WRKSRC}/src/jemalloc
	@${RMDIR} ${WRKSRC}/src/rust-installer
	@${LN} -sf ${WRKSRC}/../rust-installer-${INSTALLER_TAG} ${WRKSRC}/src/rust-installer
	@${RMDIR} ${WRKSRC}/src/rt/hoedown
	@${LN} -sf ${WRKSRC}/../hoedown-${HOEDOWN_TAG} ${WRKSRC}/src/rt/hoedown
	@(cd ${WRKSRC} && find . -type d -exec chmod 0755 {} \;)

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
	@${RM} \
		${STAGEDIR}${PREFIX}/lib/rustlib/components \
		${STAGEDIR}${PREFIX}/lib/rustlib/manifest-rustc \
		${STAGEDIR}${PREFIX}/lib/rustlib/rust-installer-version \
		${STAGEDIR}${PREFIX}/lib/rustlib/uninstall.sh

post-install:
	@${RM} ${STAGEDIR}${PREFIX}/lib/rustlib/install.log
	@${REINPLACE_CMD} -e 's|${STAGEDIR}||' \
		${STAGEDIR}${PREFIX}/lib/rustlib/manifest-rustc
	@${RM} ${STAGEDIR}${PREFIX}/lib/rustlib/manifest-rustc.bak
	@${STRIP_CMD} \
		${STAGEDIR}${PREFIX}/bin/rustc \
		${STAGEDIR}${PREFIX}/bin/rustdoc \
		${STAGEDIR}${PREFIX}/lib/*.so \
		${STAGEDIR}${PREFIX}/lib/rustlib/*/lib/*.so
	@${RM} \
		${STAGEDIR}${PREFIX}/lib/rustlib/components \
		${STAGEDIR}${PREFIX}/lib/rustlib/manifest-rustc \
		${STAGEDIR}${PREFIX}/lib/rustlib/rust-installer-version \
		${STAGEDIR}${PREFIX}/lib/rustlib/uninstall.sh
	@${MKDIR} ${STAGEDIR}${DOCSDIR}
	@${MV} ${STAGEDIR}${PREFIX}/share/doc/rust/* ${STAGEDIR}${DOCSDIR}
	@${RMDIR} ${STAGEDIR}${PREFIX}/share/doc/rust
.include <bsd.port.post.mk>
