
B = $(realpath .)
s = $T/scripts

upstream_tag = $T/tags/$1.tag
milestone_tag = tags/$1.tag

include $T/upstream/autoconf-v2.64.makefile
include $T/upstream/autoconf-v2.69.makefile
include $T/upstream/automake-v1.11.makefile
include $T/upstream/libtool.makefile
include $T/upstream/protobuf.makefile
include $T/upstream/managarm.makefile
include $T/upstream/mlibc.makefile
include $T/upstream/binutils.makefile
include $T/upstream/gcc.makefile

# milestones that build host tools.
include $T/milestone/cross-autoconf-v2.64.makefile
include $T/milestone/host-autoconf-v2.69.makefile
include $T/milestone/cross-automake-v1.11.makefile
include $T/milestone/cross-libtool.makefile
include $T/milestone/host-protoc.makefile
include $T/milestone/host-frigg_pb.makefile

# milestones that build the kernel toolchain and kernel.
include $T/milestone/kernel-gcc.makefile
include $T/milestone/kernel-libgcc.makefile
include $T/milestone/kernel-libstdc++.makefile
include $T/milestone/managarm-bundle.makefile
include $T/milestone/managarm-kernel.makefile

# milestones that build the system toolchain and actual system.
include $T/milestone/sys-headers.makefile
include $T/milestone/cross-binutils.makefile
include $T/milestone/system-gcc.makefile
include $T/milestone/rtdl.makefile
include $T/milestone/sys-mlibc.makefile
include $T/milestone/libgcc.makefile
include $T/milestone/libstdc++.makefile
include $T/milestone/helix.makefile
include $T/milestone/libarch.makefile

