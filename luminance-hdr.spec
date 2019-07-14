Summary:	A graphical tool for creating and tone-mapping HDR images
Name:		luminance-hdr
Version:	2.6.0
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		http://qtpfsgui.sourceforge.net/
Source0:	http://downloads.sourceforge.net/qtpfsgui/%{name}-%{version}.tar.bz2
# Source mirror: https://github.com/LuminanceHDR/LuminanceHDR
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:    boost-static-devel
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
BuildRequires:	cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebEngineCore) 
BuildRequires:  cmake(Qt5WebEngineWidgets) 
BuildRequires:  cmake(Qt5Widgets) 
BuildRequires:  cmake(Qt5Xml)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:  pkgconfig(eigen3)
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
%setup -q
%apply_patches

# fix inconsistant newlines
sed -i 's/\r//' Changelog

%build
%cmake_qt5 \
      -DBUILD_SHARED_LIBS:BOOL=OFF
%make_build

%install
%make_install -C build


