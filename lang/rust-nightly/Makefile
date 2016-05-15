# Created by: Jean-Sébastien Pédron <dumbbell@FreeBSD.org>
# $FreeBSD: head/lang/rust-nightly/Makefile 412409 2016-04-02 15:11:59Z jbeich $

PORTVERSION=	1.10.0.20160509
PKGNAMESUFFIX=	-nightly
DISTNAME=	#
DISTFILES=	#

MAINTAINER=	dumbbell@FreeBSD.org

ONLY_FOR_ARCHS=	amd64

MASTERDIR=	${.CURDIR}/../rust
PATCHDIR=	${.CURDIR}/files
DISTINFO_FILE=	${.CURDIR}/distinfo
PLIST=		${.CURDIR}/pkg-plist

USE_GITHUB=	yes
GH_ACCOUNT=	rust-lang
GH_PROJECT=	rust \
		compiler-rt:compiler_rt \
		hoedown:hoedown \
		jemalloc:jemalloc \
		libc:liblibc \
		rust-installer:rust_installer
GH_TAGNAME= 0e7cb8b \
		57315f7:compiler_rt \
		238c4d5:hoedown \
		aab1c0a:jemalloc \
		c37d374:rust_installer \
		7265c17:liblibc

CONFLICTS_BUILD=	rust # see FIXME in lang/rust
CONFLICTS_INSTALL=	rust


RUST_BOOT=	rustc-beta-x86_64-unknown-freebsd.tar.gz

PORT_LLVM_EXTRACT_ONLY_OFF=	${DISTFILE_llvm}
PORT_LLVM_GH_PROJECT_OFF=	llvm:llvm
PORT_LLVM_GH_TAGNAME_OFF=	7513452:llvm
PORT_LLVM_VARS_OFF=		NOPRECIOUSMAKEVARS=1 # ARCH

post-extract:	slave-post-extract
slave-post-extract:
	@(${RMDIR} ${WRKSRC}/src/compiler-rt && \
	  ${MV} ${WRKSRC_compiler_rt} ${WRKSRC}/src/compiler-rt)
	@(${RMDIR} ${WRKSRC}/src/rt/hoedown && \
	  ${MV} ${WRKSRC_hoedown} ${WRKSRC}/src/rt/hoedown)
	@(${RMDIR} ${WRKSRC}/src/jemalloc && \
	  ${MV} ${WRKSRC_jemalloc} ${WRKSRC}/src/jemalloc)
	@(${RMDIR} ${WRKSRC}/src/liblibc && \
	  ${MV} ${WRKSRC_liblibc} ${WRKSRC}/src/liblibc)
	@(${RMDIR} ${WRKSRC}/src/rust-installer && \
	  ${MV} ${WRKSRC_rust_installer} ${WRKSRC}/src/rust-installer)

post-extract-PORT_LLVM-off:
	@(${RMDIR} ${WRKSRC}/src/llvm && \
	  ${MV} ${WRKSRC_llvm} ${WRKSRC}/src/llvm)

.include "${MASTERDIR}/Makefile"
