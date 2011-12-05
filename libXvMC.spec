Summary: X.Org X11 libXvMC runtime library
Name: libXvMC
Version: 1.0.4
Release: 8.1%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0: ftp://ftp.x.org/pub/individual/lib/%{name}-%{version}.tar.bz2

BuildRequires: pkgconfig
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXv-devel

%description
X.Org X11 libXvMC runtime library

%package devel
Summary: X.Org X11 libXvMC development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXvMC development package

%prep
%setup -q

# Disable static library creation by default.
%define with_static 0

%build
%configure \
%if ! %{with_static}
	--disable-static
%endif
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# Touch XvMCConfig for rpm to package the ghost file. (#192254)
{
    mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11
    touch $RPM_BUILD_ROOT%{_sysconfdir}/X11/XvMCConfig
}

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXvMC.so.1
%{_libdir}/libXvMC.so.1.0.0
%{_libdir}/libXvMCW.so.1
%{_libdir}/libXvMCW.so.1.0.0
%ghost %config(missingok,noreplace) %verify (not md5 size mtime) %{_sysconfdir}/X11/XvMCConfig

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/XvMClib.h
%if %{with_static}
%{_libdir}/libXvMC.a
%{_libdir}/libXvMCW.a
%endif
%{_libdir}/libXvMC.so
%{_libdir}/libXvMCW.so
%{_libdir}/pkgconfig/xvmc.pc

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0.4-8.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Adam Jackson <ajax@redhat.com> 1.0.4-7
- Un-require xorg-x11-filesystem
- Remove useless %%dir

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 1.0.4-5
- Fix license tag.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.4-4
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Adam Jackson <ajax@redhat.com> - 1.0.4-3
- Rebuild for build id

* Sat Apr 21 2007 Matthias Clasen <mclasen@redhat.com> 1.0.4-2
- Don't install INSTALL

* Fri Jan 05 2007 Adam Jackson <ajax@redhat.com> 1.0.4-1
- Update to 1.0.4

* Mon Nov 20 2006 Adam Jackson <ajax@redhat.com> 1.0.3-1
- Update to 1.0.3

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 1.0.2-2.1
- rebuild

* Mon Jun 05 2006 Mike A. Harris <mharris@redhat.com> 1.0.2-2
- Added "BuildRequires: pkgconfig" for (#193506)
- Replace "makeinstall" with "make install DESTDIR=..."
- Touch XvMCConfig during install phase, and add to file manifest as a ghost
  file, so that it is owned by the package if the user creates it. (#192254)

* Thu Apr 27 2006 Adam Jackson <ajackson@redhat.com> 1.0.2-1
- Update to 1.0.2.  Drop #180902 patch, already fixed upstream.

* Tue Feb 21 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-3
- Added libXvMC-1.0.1-libXvMC-XConfigDir-fix-bug180902.patch to fix (#180902)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-2
- Added "Requires: libXv-devel, xorg-x11-proto-devel" to fix (#176862)

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.1-1
- Updated libXvMC to version 1.0.1 from X11R7.0

* Fri Dec 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-1
- Updated libXvMC to version 1.0.0 from X11R7 RC4

* Tue Dec 13 2005 Mike A. Harris <mharris@redhat.com> 0.99.2-1
- Updated libXvMC to version 0.99.2 from X11R7 RC3
- Added "Requires(pre): xorg-x11-filesystem >= 0.99.2-3", to ensure
  that /usr/lib/X11 and /usr/include/X11 pre-exist.
- Removed 'x' suffix from manpage directories to match RC3 upstream.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 11 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-2
- Changed 'Conflicts: XFree86-devel, xorg-x11-devel' to 'Obsoletes'
- Changed 'Conflicts: XFree86-libs, xorg-x11-libs' to 'Obsoletes'

* Mon Oct 24 2005 Mike A. Harris <mharris@redhat.com> 0.99.1-1
- Updated libXvMC to version 0.99.1 from X11R7 RC1

* Thu Sep 29 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-3
- Renamed package to remove xorg-x11 from the name due to unanimous decision
  between developers.
- Use Fedora Extras style BuildRoot tag.
- Disable static library creation by default.
- Add missing defattr to devel subpackage
- Add missing documentation files to doc macro

* Tue Aug 23 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-2
- Renamed package to prepend "xorg-x11" to the name for consistency with
  the rest of the X11R7 packages.
- Added "Requires: %%{name} = %%{version}-%%{release}" dependency to devel
  subpackage to ensure the devel package matches the installed shared libs.
- Added virtual "Provides: lib<name>" and "Provides: lib<name>-devel" to
  allow applications to use implementation agnostic dependencies.
- Added post/postun scripts which call ldconfig.
- Added Conflicts with XFree86-libs and xorg-x11-libs to runtime package,
  and Conflicts with XFree86-devel and xorg-x11-devel to devel package.

* Mon Aug 22 2005 Mike A. Harris <mharris@redhat.com> 0.99.0-1
- Initial build.
