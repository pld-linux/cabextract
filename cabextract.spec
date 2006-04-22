Summary:	A program to extract Microsoft Cabinet files
Summary(pl):	Program do rozpakowywania plików MS Cabinet
Name:		cabextract
Version:	1.1
Release:	3
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.kyz.uklinux.net/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	f4b729c0be7d288660f4fc167de199a1
URL:		http://www.kyz.uklinux.net/cabextract.php3
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cabinet (.CAB) files are a form of archive, which Microsoft use to
distribute their software, and things like Windows Font Packs. The
cabextract program simply unpacks such files.

%description -l pl
Pliki Cabinet (.CAB) s± rodzajem archiwum, który Microsoft u¿ywa do
dystrybucji swojego oprogramowania i rzeczy typu Windows Font Pack.
cabextract mo¿e takie pliki rozpakowaæ.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D doc/ja/cabextract.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1*
