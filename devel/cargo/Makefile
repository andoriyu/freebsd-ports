

# $FreeBSD$
PORTNAME=	cargo
PORTVERSION= 1.0.0-pre
CATEGORIES=	devel

USE_GITHUB=	yes
GH_ACCOUNT=	rust-lang
GH_PROJECT=	cargo
GH_COMMIT = 19af88c21a

MAINTAINER=	andoriyu@gmail.com
COMMENT=	Reparent a running program to a new terminal
USES= cmake python:2 curl pkgconf


BUILD_DEPENDS=	rustc:${PORTSDIR}/lang/rust

ONLY_FOR_ARCHS=	amd64
MAKE_ARGS= ARCH=x86_64
ONLY_FOR_ARCHS_REASON= requires lang/rust that is amd64 only

.include <bsd.port.pre.mk>

.if ${OPSYS} == FreeBSD && ${OSVERSION} < 1000000
BROKEN= Only compiles on FreeBSD 10 and 11
.endif

.include <bsd.port.post.mk>
