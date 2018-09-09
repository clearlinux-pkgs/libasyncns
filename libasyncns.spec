#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libasyncns
Version  : 0.8
Release  : 1
URL      : http://0pointer.de/lennart/projects/libasyncns/libasyncns-0.8.tar.gz
Source0  : http://0pointer.de/lennart/projects/libasyncns/libasyncns-0.8.tar.gz
Summary  : Asynchronous Name Service
Group    : Development/Tools
License  : LGPL-2.1
Requires: libasyncns-lib
Requires: libasyncns-license

%description
libasyncns 0.8
de>
* [1]License
* [2]News
* [3]Overview
* [4]Current Status
* [5]Documentation
* [6]Requirements
* [7]Installation
* [8]Acknowledgements
* [9]Download

%package dev
Summary: dev components for the libasyncns package.
Group: Development
Requires: libasyncns-lib
Provides: libasyncns-devel

%description dev
dev components for the libasyncns package.


%package doc
Summary: doc components for the libasyncns package.
Group: Documentation

%description doc
doc components for the libasyncns package.


%package lib
Summary: lib components for the libasyncns package.
Group: Libraries
Requires: libasyncns-license

%description lib
lib components for the libasyncns package.


%package license
Summary: license components for the libasyncns package.
Group: Default

%description license
license components for the libasyncns package.


%prep
%setup -q -n libasyncns-0.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536451850
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1536451850
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libasyncns
cp LICENSE %{buildroot}/usr/share/doc/libasyncns/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libasyncns.so
/usr/lib64/pkgconfig/libasyncns.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libasyncns/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libasyncns.so.0
/usr/lib64/libasyncns.so.0.3.1

%files license
%defattr(-,root,root,-)
/usr/share/doc/libasyncns/LICENSE
