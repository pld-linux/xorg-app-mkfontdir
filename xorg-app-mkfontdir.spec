Summary:	mkfontdir application - create an index of X font files in a directory
Summary(pl.UTF-8):	Aplikacja mkfontdir - tworzenie indeksu plików fontów X w katalogu
Name:		xorg-app-mkfontdir
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/mkfontdir-%{version}.tar.bz2
# Source0-md5:	9365ac66d19186eaf030482d312fca06
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-app-mkfontscale
#BuildArch:	noarch but automake doesn't like it
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
For each directory argument, mkfontdir reads all of the font files in
the directory searching for properties named "FONT", or (failing that)
the name of the file stripped of its suffix. These are converted to
lower case and used as font names, and, along with the name of the
font file, are written out to the file "fonts.dir" in the directory.
The X server and font server use "fonts.dir" to find font files.

%description -l pl.UTF-8
mkfontdir dla każdego argumentu będącego katalogiem odczytuje
wszystkie pliki fontów z tego katalogu wyszukując właściwości o nazwie
"FONT" lub (jeśli to się nie uda) nazwy plików po usunięciu
przyrostka. Te nazwy są przekształcane do małych liter i używane jako
nazwy fontów, a następnie, wraz z nazwami plików fontów, zapisywane do
pliku "fonts.dir" w katalogu. Serwer X oraz serwer fontów wykorzystują
pliki "fonts.dir" do odnalezienia plików fontów.

%prep
%setup -q -n mkfontdir-%{version}

%build
%{__aclocal}
%{__autoconf}
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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/mkfontdir
%{_mandir}/man1/mkfontdir.1x*
