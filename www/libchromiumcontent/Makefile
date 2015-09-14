PKGNAMEPREFIX=	libchromiumcontent-

MAINTAINER=	pusateri at bangj.com
COMMENT=	Shared library build of Chromium's Content module
#' <--- vim

USE_GITHUB=	nodefault
GH_PROJECT=	libchromiumcontent:libchromiumcontent python-patch:python_patch

GH_ACCOUNT=	atom:libchromiumcontent svn2github:python_patch

GH_TAGNAME=	v44.0.2403.125-atom:libchromiumcontent a336a45801:python_patch

MASTERDIR=	${.CURDIR}/../chromium44
DESCR=		${.CURDIR}/pkg-descr
DISTINFO_FILE=	${.CURDIR}/distinfo


#WRKSRC= ${WRKSRC_libchromiumcontent}
#BUILD_WRKSRC= ${WRKSRC_libchromiumcontent}
#CONFIGURE_WRKSRC= ${WRKSRC_libchromiumcontent}


GYP_DEFINES+= component=shared_library \
							clang=1

ALL_TARGET= chromiumcontent_all

post-extract:
	${CP} -r ${WRKSRC_libchromiumcontent}/chromiumcontent ${WRKSRC}/chromiumcontent
	@echo '44.0.2403.125' > ${WRKSRC}/.version
	${LN} -sf ${WRKSRC} ${WRKSRC_libchromiumcontent}/vendor/chromium/src
	${LN} -sf ${LOCALBASE}/bin/ninja ${WRKSRC_libchromiumcontent}/vendor/depot_tools/ninja
	${RM} -r ${WRKSRC_libchromiumcontent}/vendor/python-patch
	${LN} -sf ${WRKSRC_python_patch} ${WRKSRC_libchromiumcontent}/vendor/python-patch

ddo-configure:
	cd ${WRKSRC} && ${SETENV} ${CONFIGURE_ENV} ${PYTHON_CMD} \
		./build/gyp_chromium -I chromiumcontent/chromiumcontent.gypi chromiumcontent/chromiumcontent.gyp --depth .

# Apply port patches if any from slave
.if exists(${.CURDIR}/files)
EXTRA_PATCHES+=	${.CURDIR}/files/patch-*
.endif

.include "${MASTERDIR}/Makefile"
