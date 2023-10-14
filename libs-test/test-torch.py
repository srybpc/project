# PyTorch TEST
import torch
pyTorchVersion = torch.__version__
randomTestWithTensor  = torch.rand(5,3)
hypotCal = torch.hypot(torch.tensor([1.]), torch.tensor([1.]))
print('PyTorch version: ', pyTorchVersion)
print('Random metric test: ', randomTestWithTensor)
print('Random hypot calculation: ', hypotCal)

# TorchVision TEST
import torchvision as tv
torchvisionVersion = tv.__version__
print('TorchVision version: ', torchvisionVersion)

# INSTALLED PACKAGES RELATED TO PyTorch
'''
	=> PyTorch
	=> TorchVision
'''

# INSTALLATION LOGS (https://qengineering.eu/install-pytorch-on-raspberry-pi-4.html)
'''
birdscarekku@raspberrypi:~/dev $ uname -a
Linux raspberrypi 5.15.84-v8+ #1613 SMP PREEMPT Thu Jan 5 12:03:08 GMT 2023 aarch64 GNU/Linux

birdscarekku@raspberrypi:~/dev $ gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/aarch64-linux-gnu/10/lto-wrapper
Target: aarch64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Debian 10.2.1-6' 
				--with-bugurl=file:///usr/share/doc/gcc-10/README.Bugs 
				--enable-languages=c,ada,c++,go,d,fortran,objc,obj-c++,m2 
				--prefix=/usr --with-gcc-major-version-only 
				--program-suffix=-10 
				--program-prefix=aarch64-linux-gnu- 
				--enable-shared --enable-linker-build-id 
				--libexecdir=/usr/lib 
				--without-included-gettext 
				--enable-threads=posix 
				--libdir=/usr/lib --enable-nls 
				--enable-bootstrap 
				--enable-clocale=gnu 
				--enable-libstdcxx-debug 
				--enable-libstdcxx-time=yes 
				--with-default-libstdcxx-abi=new 
				--enable-gnu-unique-object 
				--disable-libquadmath 
				--disable-libquadmath-support 
				--enable-plugin 
				--enable-default-pie 
				--with-system-zlib 
				--enable-libphobos-checking=release 
				--with-target-system-zlib=auto 
				--enable-objc-gc=auto 
				--enable-multiarch 
				--enable-fix-cortex-a53-843419 
				--disable-werror 
				--enable-checking=release 
				--build=aarch64-linux-gnu 
				--host=aarch64-linux-gnu 
				--target=aarch64-linux-gnu 
				--with-build-config=bootstrap-lto-lean 
				--enable-link-mutex
Thread model: posix
Supported LTO compression algorithms: zlib zstd
gcc version 10.2.1 20210110 (Debian 10.2.1-6) 
birdscarekku@raspberrypi:~ $ free -m
               total        used        free      shared  buff/cache   available
Mem:            7812         500        6220         211        1091        6978
Swap:             99           0          99
birdscarekku@raspberrypi:~ $ cat /etc/os-release
PRETTY_NAME='Debian GNU/Linux 11 (bullseye)'
NAME='Debian GNU/Linux'
VERSION_ID='11'
VERSION='11 (bullseye)'
VERSION_CODENAME=bullseye
ID=debian
HOME_URL='https://www.debian.org/'
SUPPORT_URL='https://www.debian.org/support'
BUG_REPORT_URL='https://bugs.debian.org/'
birdscarekku@raspberrypi:~ $ python3 --version
Python 3.9.2
'''
