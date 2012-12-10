#define pre	pre1

Name:		luminance-hdr
Version:	2.2.0
Release:	%mkrel %{?pre:0.%{pre}.}1
Summary:	A graphical tool for creating and tone-mapping HDR images
Group:		Graphics
License:	GPLv2+
URL:		http://qtpfsgui.sourceforge.net/
Source0:	http://downloads.sourceforge.net/qtpfsgui/%{name}-%{version}%{?pre:-%pre}.tar.bz2
Patch0:		luminance-hdr-2.2.0-linkage.patch
Patch1:		luminance-hdr-2.2.0-desktop_file_fix.patch
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(QtWebKit)
BuildRequires:	OpenEXR-devel
BuildRequires:	libexiv-devel
BuildRequires:	fftw-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	gsl-devel
BuildRequires:	libraw-devel >= 0.11.2
BuildRequires:	lcms-devel
BuildRequires:	libgomp-devel
Obsoletes:	qtpfsgui
Provides:	qtpfsgui
Requires:	qt4-database-plugin-sqlite

%description
Luminance is a graphical program for assembling bracketed photos into High
Dynamic Range (HDR) images.  It also provides a number of tone-mapping
operators for creating low dynamic range versions of HDR images.

%prep
%setup -q -n %{name}-%{version}%{?pre:-%pre} -c
#setup -q -n LuminanceHDR-%{version}
%patch0 -p1 -b .linkage
%patch1 -p1 -b .desktop-fix

# fix inconsistant newlines
%__sed -i 's/\r//' Changelog

%build
%cmake
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

#icons
#%__install -Dpm644 images/luminance.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

%clean
%__rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS Changelog LICENSE README TODO
%{_bindir}/%{name}
%{_datadir}/luminance
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*


%changelog
* Tue Jan 31 2012 Andrey Bondrov <abondrov@mandriva.org> 2.2.0-1mdv2011.0
+ Revision: 769984
- New version 2.2.0, switch to cmake, rediff patches, update file list

* Tue Jan 24 2012 Andrey Bondrov <abondrov@mandriva.org> 2.1.0-1
+ Revision: 767916
- New version 2.1.0, add QtWebKit to BuildRequires, update patches (sync with Mageia)

* Sat May 07 2011 Jani Välimaa <wally@mandriva.org> 2.0.2-2
+ Revision: 672287
- rebuild against new libraw

* Sat Apr 30 2011 Jani Välimaa <wally@mandriva.org> 2.0.2-1
+ Revision: 661047
- new version 2.0.2
- rediff patches
- drop buildroot definition

* Thu Feb 24 2011 Jani Välimaa <wally@mandriva.org> 2.0.2-0.pre1.3
+ Revision: 639617
- tighten libraw-devel BR

* Thu Feb 24 2011 Jani Välimaa <wally@mandriva.org> 2.0.2-0.pre1.2
+ Revision: 639580
- rename .spec file
- obsolete and provide qtpfsgui

* Thu Feb 24 2011 Jani Välimaa <wally@mandriva.org> 2.0.2-0.pre1.1
+ Revision: 639557
- import luminance-hdr

