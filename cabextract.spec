Summary:	A program to extract Microsoft Cabinet files
Summary(pl.UTF-8):	Program do rozpakowywania plików MS Cabinet
Name:		cabextract
Version:	1.8
Release:	1
License:	GPL v2+
Group:		Applications/Archiving
Source0:	http://www.cabextract.org.uk/%{name}-%{version}.tar.gz
# Source0-md5:	e16660a9769423bf438233f87a6667a2
URL:		http://www.cabextract.org.uk/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libmspack-devel >= 0.8alpha-3
Requires:	libmspack >= 0.8alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cabinet (.CAB) files are a form of archive, which Microsoft use to
distribute their software, and things like Windows Font Packs. The
cabextract program simply unpacks such files.

%description -l pl.UTF-8
Pliki Cabinet (.CAB) są rodzajem archiwum, który Microsoft używa do
dystrybucji swojego oprogramowania i rzeczy typu Windows Font Pack.
cabextract może takie pliki rozpakować.

%prep
%setup -q
# make sure we use system libmspack
rm -rf mspack

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/mspack" \
	--with-external-libmspack
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D doc/ja/cabextract.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1/cabextract.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/cabextract
%{_mandir}/man1/cabextract.1*
%lang(ja) %{_mandir}/ja/man1/cabextract.1*
