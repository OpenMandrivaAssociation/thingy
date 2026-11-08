Name:		thingy
Version:	1.2.7
Release:	3
Summary:	Document Manager
License:        GPL-3+
URL:            https://github.com/linuxmint/thingy
Source0:	https://github.com/linuxmint/thingy/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Group:		Graphical desktop/Other

BuildRequires:  make
BuildRequires:  gettext
BuildRequires:	python

Requires:       python
Requires:       python-gi
Requires:       python-setproctitle
Requires:	typelib(GnomeDesktop) = 3.0	
Requires:	typelib(XApp)
Requires:       xreader
Requires:       libgsf

%description
Document Manager

%prep
%autosetup -p1

%build
%make_build

%install
cp -a usr %{buildroot}/
install -d %{buildroot}/usr/lib64
mv %{buildroot}/usr/lib/thingy %{buildroot}/usr/lib64/thingy
find %{buildroot}/usr/bin %{buildroot}/usr/lib64 %{buildroot}/usr/share -type f -exec sed -i 's|/usr/lib/thingy|/usr/lib64/thingy|g' {} +
find %{buildroot} -type f -exec sed -i -e "s/__DEB_VERSION__/%{version}/g" {} +

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%{_datadir}/applications/thingy.desktop
%{_datadir}/glib-2.0/schemas/org.x.thingy.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/thingy.svg
%{_datadir}/thingy/*
/usr/lib64/thingy/*
%{_bindir}/thingy
