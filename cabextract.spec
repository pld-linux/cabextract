Summary:	A program to extract Microsoft Cabinet files
Summary(pl):	Program do rozpakowywania plików MS Cabinet
Name:		cabextract
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.kyz.uklinux.net/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	8fde8ad86f7144943b7e4e5a2da7eddb
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
