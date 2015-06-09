# $FreeBSD$
PORTNAME=	reptyr
PORTVERSION=	0.6.3a
CATEGORIES=	sysutils

USE_GITHUB=	yes
GH_ACCOUNT=	nelhage
GH_PROJECT=	reptyr
GH_TAGNAME=	6fb15adb4552e170bcd5e648803da83dba57283b

MAINTAINER=	andoriyu@gmail.com
COMMENT=	Reparent a running program to a new terminal


USES=gmake

OPTIONS_DEFINE=	BASH
OPTIONS_SUB=	yes


ONLY_FOR_ARCHS=	i386 amd64

.include <bsd.port.pre.mk>
.if ${OSVERSION} < 1000000
BROKEN=	does not supported on FreeBSD older than 10.0
.endif

.include <bsd.port.post.mk>
