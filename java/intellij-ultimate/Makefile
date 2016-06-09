# Created by: Tobias Kortkamp <t@tobik.me>
# $FreeBSD: head/java/intellij/Makefile 412347 2016-04-01 14:08:37Z mat $

# Based on the devel/intellij port from OpenBSD by
# Vadim Zhukov <zhuk@openbsd.org>

PORTNAME=	intellij
PORTVERSION=	2016.1.2
CATEGORIES=	java devel
MASTER_SITES=	https://download.jetbrains.com/idea/ \
		http://download.jetbrains.com/idea/
DISTNAME=	ideaIU-${PORTVERSION}

MAINTAINER=	t@tobik.me
COMMENT=	IntelliJ IDEA Community Edition

LICENSE=	APACHE20

RUN_DEPENDS=	intellij-fsnotifier>0:java/intellij-fsnotifier \
		intellij-pty4j>0:java/intellij-pty4j

USE_JAVA=	yes
JAVA_VERSION=	1.8+

NO_ARCH=	yes
NO_BUILD=	yes

WRKDIST=	${WRKDIR}/idea-IU-145.971.21

.include "common.mk"

PLIST_SUB+=	IDEA_HOME=${IDEA_HOME}
SUB_FILES+=	idea idea.desktop pkg-message
SUB_LIST+=	IDEA_HOME=${IDEA_HOME}

do-install:
	${MKDIR} ${STAGEDIR}${IDEA_HOME}
	@${TAR} -czf - -C ${WRKDIST} . | ${TAR} xzf - -C ${STAGEDIR}${IDEA_HOME}
# Linux/Windows/OS X only so remove them
	@${RM} ${STAGEDIR}${IDEA_HOME}/bin/fsnotifier \
		${STAGEDIR}${IDEA_HOME}/bin/fsnotifier-arm \
		${STAGEDIR}${IDEA_HOME}/bin/fsnotifier64 \
		${STAGEDIR}${IDEA_HOME}/bin/libbreakgen.so \
		${STAGEDIR}${IDEA_HOME}/bin/libbreakgen64.so \
		${STAGEDIR}${IDEA_HOME}/plugins/gradle/lib/native-platform-linux-amd64-0.10.jar \
		${STAGEDIR}${IDEA_HOME}/plugins/gradle/lib/native-platform-linux-i386-0.10.jar \
		${STAGEDIR}${IDEA_HOME}/plugins/gradle/lib/native-platform-osx-amd64-0.10.jar \
		${STAGEDIR}${IDEA_HOME}/plugins/gradle/lib/native-platform-osx-i386-0.10.jar \
		${STAGEDIR}${IDEA_HOME}/plugins/gradle/lib/native-platform-windows-amd64-0.10.jar \
		${STAGEDIR}${IDEA_HOME}/plugins/gradle/lib/native-platform-windows-i386-0.10.jar
	@${RM} -r ${STAGEDIR}${IDEA_HOME}/plugins/tfsIntegration/lib/native/hpux/ \
		${STAGEDIR}${IDEA_HOME}/plugins/tfsIntegration/lib/native/linux/ \
		${STAGEDIR}${IDEA_HOME}/plugins/tfsIntegration/lib/native/macosx/ \
		${STAGEDIR}${IDEA_HOME}/plugins/tfsIntegration/lib/native/solaris/ \
		${STAGEDIR}${IDEA_HOME}/plugins/tfsIntegration/lib/native/win32/ \
		${STAGEDIR}${IDEA_HOME}/plugins/tfsIntegration/lib/native/aix/

# Remove the bundled native Pty4J support libraries, they are replaced
# by java/intellij-pty4j
	@${RM} -r ${STAGEDIR}${IDEA_HOME}/lib/libpty
	@${RM} ${STAGEDIR}${IDEA_HOME}/lib/pty4j-0.5.jar
	${INSTALL_SCRIPT} ${WRKDIR}/idea ${STAGEDIR}${PREFIX}/bin/idea
	${INSTALL_MAN} ${FILESDIR}/idea.1 ${STAGEDIR}${PREFIX}/man/man1
	${INSTALL_DATA} ${WRKDIR}/idea.desktop ${STAGEDIR}${PREFIX}/share/applications/
	cd ${WRKDIST}/lib && ${JAVA_HOME}/bin/jar xf icons.jar
	${INSTALL_DATA} ${WRKDIST}/lib/icon.png ${STAGEDIR}${IDEA_HOME}/idea.png
# TODO: Remove and enable fsnotifier when devel/libinotify is fixed
# Disable filewatcher warning message on IDEA startup
	${ECHO} "idea.filewatcher.disabled=true" >> ${STAGEDIR}${IDEA_HOME}/bin/idea.properties
# Use fsnotifier replacement provided by java/intellij-fsnotifier
#	${ECHO} "idea.filewatcher.executable.path=${IDEA_HOME}/bin/fsnotifier" >> ${STAGEDIR}${IDEA_HOME}/bin/idea.properties

.include <bsd.port.mk>
