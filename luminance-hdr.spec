Summary:	A graphical tool for creating and tone-mapping HDR images
Name:		luminance-hdr
Version:	2.5.1
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		http://qtpfsgui.sourceforge.net/
Source0:	http://downloads.sourceforge.net/qtpfsgui/%{name}-%{version}%{?pre:-%pre}.tar.bz2
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	gomp-devel
BuildRequires:	jpeg-devel
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(Qt5Concurrent) cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5Network) cmake(Qt5PrintSupport) cmake(Qt5Sql) cmake(Qt5WebEngineCore) cmake(Qt5WebEngineWidgets) cmake(Qt5Widgets) cmake(Qt5Xml)
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
Requires:	qt5-database-plugin-sqlite


%description
Luminance is a graphical program for assembling bracketed photos into High
Dynamic Range (HDR) images. It also provides a number of tone-mapping
operators for creating low dynamic range versions of HDR images.

%files
%doc AUTHORS Changelog LICENSE README.md TODO
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/appdata/%{name}.appdata.xml

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

# fix inconsistant newlines
sed -i 's/\r//' Changelog

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build


