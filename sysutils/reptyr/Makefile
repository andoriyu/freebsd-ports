# $FreeBSD$
PORTNAME=	influxdb
PORTVERSION= 0.9.0-rc33
CATEGORIES=	databases

USE_GITHUB=	yes
GH_ACCOUNT=	influx
GH_PROJECT=	influx
GH_TAGNAME=	v0.9.0-rc33

MAINTAINER=	andoriyu@gmail.com
COMMENT=	Reparent a running program to a new terminal


OPTIONS_DEFINE=	BASH
OPTIONS_SUB=	yes


ONLY_FOR_ARCHS=	i386 amd64

.include <bsd.port.pre.mk>
.include "${PORTSDIR}/lang/go/files/bsd.go.mk"
.include <bsd.port.post.mk>
