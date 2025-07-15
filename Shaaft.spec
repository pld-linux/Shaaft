Summary:	Falling block game resembling Blockout
Summary(pl.UTF-8):	Gra w spadające klocki przypominająca Blockout
Name:		Shaaft
Version:	0.5.0
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/criticalmass/%{name}-%{version}.tar.bz2
# Source0-md5:	c86524f286c60e3fd45b10d023a92db2
Patch0:		%{name}-types.patch
URL:		http://criticalmass.sourceforge.net/shaaft.php
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Shaaft is a falling block game resembling Blockout. It is a 3D Tetris
clone.

%description -l pl.UTF-8
Shaaft to gra w spadające klocki przypominająca Blockout. To
trójwymiarowy klon Tetrisa.

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__automake} --include-deps
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# this one gets installed by author's mistake
rm -f $RPM_BUILD_ROOT%{_bindir}/Packer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/Shaaft
%{_mandir}/man6/*
