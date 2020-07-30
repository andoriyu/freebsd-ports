# Created by: Andrey Cherkashin <andoriyu@gmail.com>
# $FreeBSD: head/sysutils/reptyr/Makefile 407349 2016-01-27 10:30:42Z rakuco $

PORTNAME=	reptyr
PORTVERSION=	0.7.0
DISTVERSIONPREFIX=	reptyr-
CATEGORIES=	sysutils

MAINTAINER=	andoriyu@gmail.com
COMMENT=	Reparent a running program to a new terminal

LICENSE=	MIT

USE_GITHUB=	yes
GH_ACCOUNT=	nelhage

MAKE_ARGS=	BASHCOMPDIR=${PREFIX}/share/bash-completion/completions \
		MANDIR=${MANPREFIX}/man
USES=		gmake

ONLY_FOR_ARCHS=	i386 amd64

post-install:
	${STRIP_CMD} ${STAGEDIR}${PREFIX}/bin/reptyr

.include <bsd.port.mk>
