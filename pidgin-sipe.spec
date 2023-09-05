#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pidgin-sipe
Version  : 1.25.0
Release  : 27
URL      : https://github.com/tieto/sipe/archive/1.25.0/sipe-1.25.0.tar.gz
Source0  : https://github.com/tieto/sipe/archive/1.25.0/sipe-1.25.0.tar.gz
Summary  : Pidgin protocol plugin to connect to MS Office Communicator
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: pidgin-sipe-data = %{version}-%{release}
Requires: pidgin-sipe-lib = %{version}-%{release}
Requires: pidgin-sipe-license = %{version}-%{release}
Requires: pidgin-sipe-locales = %{version}-%{release}
Requires: appstream
BuildRequires : appstream
BuildRequires : e2fsprogs-dev
BuildRequires : farstream-dev
BuildRequires : flex
BuildRequires : gettext
BuildRequires : gst-plugins-base
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : krb5-dev
BuildRequires : libnice-dev
BuildRequires : libtool
BuildRequires : openssl
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : pidgin-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(freerdp-shadow2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmime-3.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-rtp-1.0)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(winpr2)
BuildRequires : util-linux

%description
A third-party plugin for the Pidgin multi-protocol instant messenger.
It implements the extended version of SIP/SIMPLE used by various products:

    * Skype for Business
    * Microsoft Office 365
    * Microsoft Business Productivity Online Suite (BPOS)
    * Microsoft Lync Server
    * Microsoft Office Communications Server (OCS 2007/2007 R2)
    * Microsoft Live Communications Server (LCS 2003/2005)

With this plugin you should be able to replace your Microsoft Office
Communicator client with Pidgin.

This package provides the icon set for Pidgin.

%package data
Summary: data components for the pidgin-sipe package.
Group: Data

%description data
data components for the pidgin-sipe package.


%package lib
Summary: lib components for the pidgin-sipe package.
Group: Libraries
Requires: pidgin-sipe-data = %{version}-%{release}
Requires: pidgin-sipe-license = %{version}-%{release}

%description lib
lib components for the pidgin-sipe package.


%package license
Summary: license components for the pidgin-sipe package.
Group: Default

%description license
license components for the pidgin-sipe package.


%package locales
Summary: locales components for the pidgin-sipe package.
Group: Default

%description locales
locales components for the pidgin-sipe package.


%prep
%setup -q -n sipe-1.25.0
cd %{_builddir}/sipe-1.25.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594620421
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static --disable-telepathy --enable-purple --with-krb5 --with-vv --with-dbus
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1594620421
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pidgin-sipe
cp %{_builddir}/sipe-1.25.0/COPYING %{buildroot}/usr/share/package-licenses/pidgin-sipe/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
%make_install
%find_lang pidgin-sipe

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/metainfo/pidgin-sipe.metainfo.xml
/usr/share/pixmaps/pidgin/protocols/16/sipe.png
/usr/share/pixmaps/pidgin/protocols/22/sipe.png
/usr/share/pixmaps/pidgin/protocols/24/sipe.png
/usr/share/pixmaps/pidgin/protocols/32/sipe.png
/usr/share/pixmaps/pidgin/protocols/48/sipe.png
/usr/share/pixmaps/pidgin/protocols/scalable/sipe.svg

%files lib
%defattr(-,root,root,-)
/usr/lib64/purple-2/libsipe.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pidgin-sipe/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files locales -f pidgin-sipe.lang
%defattr(-,root,root,-)

