%define up_name		ocamlsdl

Name:		ocaml-sdl
Version:	0.9.1
Release:	1
Summary:	Wrapper around the cross platform Simple DirectMedia Layer game library
License:	LGPL
Source:		https://sourceforge.net/projects/ocamlsdl/files/OCamlSDL/ocamlsdl-0.9.1/ocamlsdl-%{version}.tar.gz
Group:		Development/Other
URL:		https://ocamlsdl.sourceforge.net/
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	ocaml
BuildRequires:	ocaml-lablgl-devel
BuildRequires:  ocaml-findlib
Obsoletes:      ocaml-SDL

%package -n %{name}-devel
Summary:	Wrapper around the cross platform Simple DirectMedia Layer game library
Group:		Development/Other
Requires:	pkgconfig(sdl)
Requires:	pkgconfig(SDL_image)
Requires:	pkgconfig(SDL_mixer)
Requires:	pkgconfig(SDL_ttf)
Requires:	pkgconfig(libpng)
Obsoletes:  ocaml-SDL-devel
Requires:	%{name} = %{version}-%{release}

%description
Ocaml-SDL is a wrapper around the cross platform Simple Direct Layer game
library. Essentially it allows you to write cross platform games in ocaml,
using 2d (SDL), or 3d (OpenGL), or a combination of both if you wish.

%description -n %{name}-devel
Ocaml-SDL is a wrapper around the cross platform Simple Direct Layer game
library. Essentially it allows you to write cross platform games in ocaml,
using 2d (SDL), or 3d (OpenGL), or a combination of both if you wish.

%prep
%setup -q -n %{up_name}-%{version}

%build
%configure2_5x --with-lablgldir=%{_libdir}/ocaml/lablgl
make

%install
install -d %{buildroot}%{_libdir}/ocaml
install -d %{buildroot}%{_libdir}/ocaml/stublibs
make install OCAMLFIND_DESTDIR="%{buildroot}/%{_libdir}/ocaml"
mkdir -p %{buildroot}/%{_infodir}
install doc/*.info* %{buildroot}/%{_infodir}
install -d %{buildroot}%{_bindir}/
install -m 0755 ./xpm_to_ml %{buildroot}%{_bindir}/

%clean


%files
%doc COPYING README AUTHORS NEWS
%dir %{_libdir}/ocaml/sdl
%{_bindir}/xpm_to_ml
%{_libdir}/ocaml/sdl/*.cmi
%{_libdir}/ocaml/sdl/*.cma
%{_libdir}/ocaml/sdl/META
%{_libdir}/ocaml/stublibs/*

%files devel
%doc doc/*
%{_libdir}/ocaml/sdl/*.a
%{_libdir}/ocaml/sdl/*.cmxa
%{_libdir}/ocaml/sdl/*.cmx
%{_libdir}/ocaml/sdl/*.mli
%{_infodir}/*

