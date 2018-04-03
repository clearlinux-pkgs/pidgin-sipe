#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pidgin-sipe
Version  : 1.23.1
Release  : 6
URL      : https://github.com/tieto/sipe/archive/1.23.1.tar.gz
Source0  : https://github.com/tieto/sipe/archive/1.23.1.tar.gz
Summary  : Pidgin protocol plugin to connect to MS Office Communicator
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: pidgin-sipe-lib
Requires: pidgin-sipe-data
Requires: pidgin-sipe-locales
BuildRequires : FreeRDP-dev
BuildRequires : e2fsprogs-dev
BuildRequires : farstream-dev
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : krb5-dev
BuildRequires : libnice-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pidgin-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmime-3.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gstreamer-1.0)
BuildRequires : pkgconfig(gstreamer-rtp-1.0)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(valgrind)

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
Requires: pidgin-sipe-data

%description lib
lib components for the pidgin-sipe package.


%package locales
Summary: locales components for the pidgin-sipe package.
Group: Default

%description locales
locales components for the pidgin-sipe package.


%prep
%setup -q -n sipe-1.23.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522763210
%autogen --disable-static --disable-telepathy --enable-purple --with-krb5 --with-vv --with-dbus
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1522763210
rm -rf %{buildroot}
%make_install
%find_lang pidgin-sipe

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/appdata/pidgin-sipe.metainfo.xml
/usr/share/pixmaps/pidgin/protocols/16/sipe.png
/usr/share/pixmaps/pidgin/protocols/22/sipe.png
/usr/share/pixmaps/pidgin/protocols/24/sipe.png
/usr/share/pixmaps/pidgin/protocols/32/sipe.png
/usr/share/pixmaps/pidgin/protocols/48/sipe.png
/usr/share/pixmaps/pidgin/protocols/scalable/sipe.svg

%files lib
%defattr(-,root,root,-)
/usr/lib64/purple-2/libsipe.so

%files locales -f pidgin-sipe.lang
%defattr(-,root,root,-)

