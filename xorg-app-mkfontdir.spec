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
BuildRequires:	xorg-util-util-macros >= 1.3
Requires:	xorg-app-mkfontscale
#BuildArch:	noarch but automake doesn't like it
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mkfontdir creates the fonts.dir files needed by the legacy X server
core font system. The current implementation is a simple wrapper
script around the mkfontscale program, which must be installed first.

%description -l pl.UTF-8
mkfontdir tworzy pliki fonts.dir wymagane przez stary system fontów
serwera X. Aktualna implementacja to prosty skrypt obudowujący program
mkfontscale, który musi być wcześniej zainstalowany.

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/mkfontdir
%{_mandir}/man1/mkfontdir.1x*
