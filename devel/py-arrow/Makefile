# Created by: Andrey Cherkashin <andoriyu@gmail.com>
# $FreeBSD$


PORTNAME=	arrow
PORTVERSION=	0.6.0
CATEGORIES=	devel python
MASTER_SITES=	CHEESESHOP

MAINTAINER=	andoriyu@gmail.com
COMMENT=	Python library to work with dates and times

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}dateutil>2.0:${PORTSDIR}/devel/py-dateutil
TEST_DEPENDS=	${PYTHON_PKGNAMEPREFIX}nose>1.3.0:${PORTSDIR}/devel/py-nose \
							${PYTHON_PKGNAMEPREFIX}nose-cov>1.6:${PORTSDIR}/devel/py-nose-cov \
							${PYTHON_PKGNAMEPREFIX}chai>0.4.0:${PORTSDIR}/devel/py-chai \
							${PYTHON_PKGNAMEPREFIX}sphinx>1.2.0:${PORTSDIR}/textproc/py-sphinx \
							${PYTHON_PKGNAMEPREFIX}simplejson>3.6.0:${PORTSDIR}/devel/py-simplejson

OPTIONS_DEFINE= TESTS

TESTS_DESC=	Install test suit requirments
TESTS_BUILD_DEPENDS=	${RUN_DEPENDS} \
											${TEST_DEPENDS}

USES=	python
USE_PYTHON=	autoplist diskutils

NO_ARCH= yes

regression-test: build
	@cd ${WRKSRC} && ${PYTHON_CMD}

