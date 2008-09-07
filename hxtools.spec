
Name:		hxtools
Version:	20080820
Release:	0
Group:		System/Base
URL:		http://jengelh.medozas.de/projects/hxtools/
Summary:	Collection of day-to-day tools

Source:		%name-%version.tar.lzma
License:	GPL,PD
# freetype2, xorg-x11 for "bdftopcf"
BuildRequires:	libHX-devel >= 1.25, lzma, freetype2, libcap-devel
BuildRequires:	xorg-x11, pkg-config
BuildRoot:	%_tmppath/%name-%version-build
Recommends:	hxtools-data
Prefix:		/opt/hxtools

%description
A big tool collection.

%package data
Group:		System/Base
Summary:	Collection day-to-day tools (data)
Recommends:	hxtools

%description data
Architecture-indepent data for hxtools.

%debug_package
%prep
%setup

%build
%configure \
	--prefix=/opt/hxtools \
	--exec-prefix=/opt/hxtools \
	--with-keymapdir=%_datadir/kbd/keymaps \
	--with-vgafontdir=%_datadir/kbd/consolefonts \
	--with-x11fontdir=%_datadir/fonts
make %{?jobs:-j%jobs};

%install
b="%buildroot";
rm -Rf "$b";
mkdir "$b";
make install DESTDIR="$b";
install -dm0755 "$b/%_sysconfdir/openldap/schema" "$b/%_datadir/mc/syntax";
install -pm0644 cooledit/*.syntax "$b/%_datadir/mc/syntax/";
install -pm0644 data/rfc2307bis-utf8.schema "$b/%_sysconfdir/openldap/schema/";

%clean
rm -Rf "%buildroot";

%files
%defattr(-,root,root)
/opt/hxtools

%files data
%defattr(-,root,root)
%_sysconfdir/openldap/schema/*
%_datadir/kbd/consolefonts/*
%_datadir/kbd/keymaps/i386/*/*
%_datadir/fonts/misc/*
%_datadir/mc/syntax/*
%doc doc/*
