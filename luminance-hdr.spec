Summary:	A graphical tool for creating and tone-mapping HDR images
Name:		luminance-hdr
Version:	2.3.1
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		http://qtpfsgui.sourceforge.net/
Source0:	http://downloads.sourceforge.net/qtpfsgui/%{name}-%{version}%{?pre:-%pre}.tar.bz2
Patch0:		luminance-hdr-2.3.1-desktop_file_fix.patch
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	gomp-devel
BuildRequires:	jpeg-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(OpenEXR)
BuildRequires:	pkgconfig(QtWebKit)
BuildRequires:	pkgconfig(zlib)
Requires:	qt4-database-plugin-sqlite

%description
Luminance is a graphical program for assembling bracketed photos into High
Dynamic Range (HDR) images. It also provides a number of tone-mapping
operators for creating low dynamic range versions of HDR images.

%files
%doc AUTHORS Changelog LICENSE README TODO
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

#----------------------------------------------------------------------------

%prep
%setup -q -c
%patch0 -p1 -b .desktop-fix

# fix inconsistant newlines
sed -i 's/\r//' Changelog

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build


