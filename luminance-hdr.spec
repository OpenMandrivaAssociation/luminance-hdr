Summary:	A graphical tool for creating and tone-mapping HDR images
Name:		luminance-hdr
Version:	2.6.1.1
Release:	4
License:	GPLv2+
Group:		Graphics
Url:		http://qtpfsgui.sourceforge.net/
Source0:	http://downloads.sourceforge.net/qtpfsgui/%{name}-%{version}.tar.bz2
Patch0:		luminance-hdr-2.6.1.1-exiv2-0.28.patch
# Source mirror: https://github.com/LuminanceHDR/LuminanceHDR
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	boost-devel
BuildRequires:  boost-static-devel
BuildRequires:	gomp-devel
BuildRequires:	imagemagick
BuildRequires:	jpeg-devel
BuildRequires:  qt5-qttools
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(Qt5Concurrent) 
BuildRequires:  cmake(Qt5Core) 
BuildRequires:  cmake(Qt5Gui) 
BuildRequires:	cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Network) 
BuildRequires:  cmake(Qt5PrintSupport) 
BuildRequires:	cmake(Qt5Help)
BuildRequires:  cmake(Qt5Sql) 
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebEngineCore) 
BuildRequires:  cmake(Qt5WebEngineWidgets) 
BuildRequires:  cmake(Qt5Widgets) 
BuildRequires:  cmake(Qt5Xml)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:	pkgconfig(cfitsio)
BuildRequires:	pkgconfig(IlmBase)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(OpenEXR)
#BuildRequires:	pkgconfig(QtWebKit)
BuildRequires:	pkgconfig(zlib)

Provides:	qtpfsgui
Requires:	qt5-database-plugin-sqlite
Recommends:	hugin


%description
Luminance is a graphical program for assembling bracketed photos into High
Dynamic Range (HDR) images. It also provides a number of tone-mapping
operators for creating low dynamic range versions of HDR images.

%files
%doc AUTHORS Changelog LICENSE README.md TODO
%{_bindir}/%{name}
%{_bindir}/%{name}-cli
%{_datadir}/%{name}
%{_datadir}/applications/net.sourceforge.qtpfsgui.LuminanceHDR.desktop
 %{_iconsdir}/hicolor/*/apps/%{name}.*
%{_datadir}/appdata/net.sourceforge.qtpfsgui.LuminanceHDR.appdata.xml

#----------------------------------------------------------------------------

%prep
%autosetup -p1

# fix inconsistant newlines
sed -i 's/\r//' Changelog

%cmake_qt5 \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
