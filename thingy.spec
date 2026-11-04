Name:		thingy
Version:	1.2.7
Release:	1
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
Requires:	lib64gnome-desktop-gir3.0	
Requires:	lib64xapp-gir3.2
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
find %{buildroot} -type f -exec sed -i -e "s/__DEB_VERSION__/%{version}/g" {} +

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%{_datadir}/applications/thingy.desktop
%{_datadir}/glib-2.0/schemas/org.x.thingy.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/thingy.svg
%{_datadir}/thingy/*
/usr/lib/thingy/*
%{_bindir}/thingy
