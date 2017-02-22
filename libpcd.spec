Name:         libpcd
License:      GPLv2+
Version:      1.0.1
Release:      1%{?dist}
Summary:      PhotoCD decoding library
Group:        System Environment/Libraries
URL:          http://www.kraxel.org/blog/linux/%{name}/
Source:       http://www.kraxel.org/releases/%{name}/%{name}_%{version}.tar.gz

%description
PhotoCD decoding library

%package devel
Summary: PhotoCD decoding library devel files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
%description devel
PhotoCD decoding library devel files

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make prefix=/usr

%install
make    prefix=/usr DESTDIR=%{buildroot} \
        libdir=%{buildroot}%{_libdir} \
        install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libpcd*.so.*

%files devel
%doc *.html *.css
%{_libdir}/libpcd*.a
%{_libdir}/libpcd*.so
%{_includedir}/pcd.h

%changelog
