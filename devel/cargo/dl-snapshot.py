import distutils.spawn
import hashlib
import os
import subprocess
import sys
import tarfile
import shutil
import contextlib
import re

datere = re.compile('^\d{4}-\d{2}-\d{2}')
cksumre = re.compile('^  ([^ ]+) ([^$]+)$')

current = None
snaps = {}
with open('src/snapshots.txt') as f:
    for line in iter(f):
        line = line.rstrip()
        m = datere.match(line)
        if m:
            current = m.group()
            snaps[current] = {}
            continue

        m = cksumre.match(line)
        if m:
            snaps[current][m.group(1)] = m.group(2)
            continue

        # This script currently doesn't look at older snapshots, so there is
        # no need to look past the first section.
        break

date = current
triple = sys.argv[1]

ts = triple.split('-')
arch = ts[0]

if (arch == 'i586') or (arch == 'i386'):
    arch = 'i686'
if (arch == 'amd64'):
    arch = 'x86_64'

if len(ts) == 2:
    vendor = 'unknown'
    target_os = ts[1]
else:
    vendor = ts[1]
    target_os = ts[2]

# NB: The platform format differs from the triple format, to support
#     bootstrapping multiple triples from the same snapshot.
plat_arch = arch if (arch != 'i686') else 'i386'
plat_os = target_os
if (target_os == 'windows'):
    plat_os = 'winnt'
elif (target_os == 'darwin'):
    plat_os = 'macos'
elif (target_os == 'freebsd10.1'):
    plat_os = 'freebsd'
platform = "%s-%s" % (plat_os, plat_arch)
if platform not in snaps[date]:
    raise Exception("no snapshot for the triple '%s'" % triple)

# Reconstitute triple with any applicable changes.  For historical reasons
# this differs from the snapshots.txt platform name.
if target_os == 'linux':
    target_os = 'linux-gnu'
elif target_os == 'darwin':
    vendor = 'apple'
elif target_os == 'windows':
    vendor = 'pc'
    target_os = 'windows-gnu'
elif (target_os == 'freebsd10.1'):
    vendor = 'unknown'
    target_os = 'freebsd'
triple = "%s-%s-%s" % (arch, vendor, target_os)
hash = snaps[date][platform]

tarball = 'cargo-nightly-' + triple + '.tar.gz'
url = 'https://static.rust-lang.org/cargo-dist/%s/%s' % \
  (date.strip(), tarball)
dl_path = "target/dl/" + tarball
dst = "target/snapshot"
if not os.path.isdir('target/dl'):
    os.makedirs('target/dl')

if os.path.isdir(dst):
    shutil.rmtree(dst)

exists = False
if os.path.exists(dl_path):
    h = hashlib.sha1(open(dl_path, 'rb').read()).hexdigest()
    if h == hash:
        print("file already present %s (%s)" % (dl_path, hash,))
        exists = True

if not exists:
    ret = subprocess.call(["curl", "-o", dl_path, url])
    if ret != 0:
        raise Exception("failed to fetch url")
    h = hashlib.sha1(open(dl_path, 'rb').read()).hexdigest()
    if h != hash:
        raise Exception("failed to verify the checksum of the snapshot")

with contextlib.closing(tarfile.open(dl_path)) as tar:
    for p in tar.getnames():
        name = p.replace("cargo-nightly-" + triple + "/", "", 1)
        fp = os.path.join(dst, name)
        print("extracting " + p)
        tar.extract(p, dst)
        tp = os.path.join(dst, p)
        if os.path.isdir(tp) and os.path.exists(fp):
            continue
        shutil.move(tp, fp)
shutil.rmtree(os.path.join(dst, 'cargo-nightly-' + triple))