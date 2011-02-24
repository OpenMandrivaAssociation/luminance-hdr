%define version	2.0.2
%define release	1
%define	pre	pre1

Name:		luminance-hdr
Version:	%{version}
Release:	%mkrel %{?pre:0.%{pre}.}%{release}
Summary:	A graphical tool for creating and tone-mapping HDR images
Group:		Graphics
License:	GPLv2+
URL:		http://qtpfsgui.sourceforge.net/
Source0:	http://downloads.sourceforge.net/qtpfsgui/%{name}-%{version}%{?pre:-%pre}.tar.gz
Patch0:		luminance-hdr-2.0.2-pre1-linkage.patch
Patch1:		luminance-hdr-2.0.2-pre1-desktop_file_fix.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:	libqt4-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	libexiv-devel
BuildRequires:	fftw-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	gsl-devel
BuildRequires:	libraw-devel
BuildRequires:	lcms-devel
BuildRequires:	libgomp-devel
Obsoletes:	qtpfsgui
Provides:	qtpfsgui

%description
Luminance is a graphical program for assembling bracketed photos into High
Dynamic Range (HDR) images.  It also provides a number of tone-mapping
operators for creating low dynamic range versions of HDR images.

%prep
%setup -q -n %{name}-%{version}%{?pre:-%pre}
%patch0 -p0 -b .linkage
%patch1 -p0 -b .desktop-fix

# fix inconsistant newlines
%{__sed} -i 's/\r//' Changelog

%build
%qmake_qt4 PREFIX=%{_prefix}
%make

%install
rm -rf %{buildroot}
%makeinstall_std INSTALL_ROOT=%{buildroot}

#icons
install -Dpm644 images/luminance.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg

#for i in 16 24 48 64; do
#	mkdir -p %{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps
#	convert -scale $i images/%{name}.png %{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps/%{name}.png
#done

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS Changelog LICENSE README TODO
%doc %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
