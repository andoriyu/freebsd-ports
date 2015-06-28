# Created by: Andrey Cherkashin
# $FreeBSD$
PORTNAME=	cargo
PORTVERSION= 0.3.0n
CATEGORIES=	devel

USE_GITHUB=	yes
GH_ACCOUNT=	rust-lang
GH_PROJECT=	cargo \
						rust-installer:installer

INSTALLER_TAG=	8e4f8ea
GH_TAGNAME = c8c1624baf41f4bf8ae71ab537471f348fb33154 \
						 ${INSTALLER_TAG}:installer

CARGO_SOURCE= ${GH_ACCOUNT}-${GH_PROJECT}-${PORTVERSION}-${GH_TAGNAME}_GH0
DISTFILES+= ${CARGO_SOURCE} \
						${CARGO_BOOT}:bootstrap
CONFIGURE_TARGET= x86_64-unknown-freebsd
CARGO_BOOT=cargo-nightly-x86_64-unknown-freebsd.tar.gz
MASTER_SITES= ${GH} \
							https://static.rust-lang.org/cargo-dist/2015-04-02/:bootstrap

MAINTAINER=	andoriyu@gmail.com
COMMENT=	Reparent a running program to a new terminal
USES= gmake python:2
GNU_CONFIGURE= yes
USE_BINUTILS=	yes
CONFIGURE_ARGS= --local-rust-root=${LOCALBASE}
BUILD_DEPENDS=	rustc:${PORTSDIR}/lang/rust-nightly \
	curl:${PORTSDIR}/ftp/curl \
	pkg-config:${PORTSDIR}/devel/pkgconf \
	cmake:${PORTSDIR}/devel/cmake \
	git:${PORTSDIR}/devel/git 

ONLY_FOR_ARCHS=	amd64
MAKE_ARGS= ARCH=x86_64
ONLY_FOR_ARCHS_REASON= requires lang/rust that is amd64 only
.include <bsd.port.pre.mk>
pre-install:
	@if test -f ${STAGEDIR}${PREFIX}/lib/rustlib/manifest-cargo; then \
		${SED} -E -e 's,^(dir|file:),${STAGEDIR},' \
		< ${STAGEDIR}${PREFIX}/lib/rustlib/manifest-cargo \
		| ${XARGS} ${RM}; \
	fi
	${RM} \
		${STAGEDIR}${PREFIX}/lib/rustlib/install.log \
		${STAGEDIR}${PREFIX}/lib/rustlib/components \
		${STAGEDIR}${PREFIX}/lib/rustlib/manifest-cargo \
		${STAGEDIR}${PREFIX}/lib/rustlib/rust-installer-version \
		${STAGEDIR}${PREFIX}/lib/rustlib/uninstall.sh
	${RMDIR} ${STAGEDIR}${PREFIX}/lib/rustlib

post-extract:
	${MKDIR} ${WRKSRC}/target/dl
	${LN} -sf ${DISTDIR}/${CARGO_BOOT} ${WRKSRC}/target/dl
	(cd ${WRKSRC} && find . -type d -exec chmod 0755 {} \;)
	${CHMOD} 755 ${WRKSRC}/src/etc/dl-snapshot.py
	${RMDIR} ${WRKSRC}/src/rust-installer
	${LN} -sf ${WRKSRC}/../rust-installer-${INSTALLER_TAG} ${WRKSRC}/src/rust-installer

.if ${OPSYS} == FreeBSD && ${OSVERSION} < 1000000
BROKEN= Only compiles on FreeBSD 10 and 11
.endif

.include <bsd.port.post.mk>
