#define pre	pre1

Name:		luminance-hdr
Version:	2.1.0
Release:	%mkrel %{?pre:0.%{pre}.}1
Summary:	A graphical tool for creating and tone-mapping HDR images
Group:		Graphics
License:	GPLv2+
URL:		http://qtpfsgui.sourceforge.net/
Source0:	http://downloads.sourceforge.net/qtpfsgui/%{name}-%{version}%{?pre:-%pre}.tar.gz
Patch0:		luminance-hdr-2.0.2-linkage.patch
Patch1:		luminance-hdr-2.1.0-desktop_file_fix.patch
Patch2:		luminance-hdr-2.1.0-libraw.patch
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
%setup -q -n %{name}-%{version}%{?pre:-%pre}
#setup -q -n LuminanceHDR-%{version}
%patch0 -p0 -b .linkage
%patch1 -p0 -b .desktop-fix
%patch2 -p1 -b .libraw-fix

# fix inconsistant newlines
%__sed -i 's/\r//' Changelog

%build
%qmake_qt4 \
	PREFIX=%{_prefix} \
	DOCDIR=%{_defaultdocdir}/%{name} \
	HTMLDIR=%{_datadir}/%{name}
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std INSTALL_ROOT=%{buildroot}

#icons
%__install -Dpm644 images/luminance.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

#for i in 16 24 48 64; do
#	mkdir -p %{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps
#	convert -scale $i images/%{name}.png %{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps/%{name}.png
#done

#handle docs in files section
%__mv %{buildroot}%{_defaultdocdir}/%{name} installed-docs

%clean
%__rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS Changelog LICENSE README TODO
%doc installed-docs/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
