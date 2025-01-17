Name:		flaw
Version:	1.3.2
Release:	3
Summary:	F.L.A.W. is a fighting game between magicians
License:	GPLv3+
Group:		Games/Arcade
URL:		https://flaw.sourceforge.net/index.php
Source:		%{name}-%{version}.tar.gz
# Buffer is too small and sprintf causes segfault with buffer overflaw
Patch0:		flaw-1.3.2-buffer.patch
BuildRequires:	boost-devel
BuildRequires:	intltool
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_gfx-devel
Requires:	freetype
Requires:	fonts-ttf-freefont

%description
F.L.A.W. is a free top-down wizard fighting game that can be played by
up to 5 players. The goal of the game is to survive as long as possible
while more and more fireballs appear in the arena.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --with-fontpath=%{_datadir}/fonts/TTF/
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/locale/*

