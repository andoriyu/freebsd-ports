PORTNAME=       rust-extra
PORTVERSION=    0.1
CATEGORIES=     devel
MASTER_SITES=		https://s3.amazonaws.com/infinitycode-boxes/
EXTRACT_SUFX=		.tar.gz
DISTFILES=			rust-extra-0.1.tar.gz

MAINTAINER=     andoriyu@gmail.com
COMMENT=        Precompiled tools for rust development

LICENSE= 				MIT

NO_BUILD=       yes

WRKSRC=         ${WRKDIR}/${PORTNAME}
ONLY_FOR_ARCHS= amd64

RUN_DEPENDS= rustc:${PORTSDIR}/lang/rust
LIB_DEPENDS= libssh2.so:${PORTSDIR}/security/libssh2\
	libgit2.so:${PORTSDIR}/devel/libgit2\
	libssl:security/openssl\
	libcurl:ftp/curl\
	libclang:lang/clang36


do-install:
	cd ${WRKSRC} && ${COPYTREE_SHARE} \* ${STAGEDIR}${DATADIR}
	${CHMOD} ${BINMODE} ${STAGEDIR}${DATADIR}/bin/cargo
	${CHMOD} ${BINMODE} ${STAGEDIR}${DATADIR}/bin/bindgen
	${CHMOD} ${BINMODE} ${STAGEDIR}${DATADIR}/bin/racer

.include <bsd.port.mk>
