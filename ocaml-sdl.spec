%define up_name		ocamlsdl
%define name		ocaml-sdl
%define version		0.7.2
%define release		%mkrel 10

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Wrapper around the cross platform Simple DirectMedia Layer game library
License:	LGPL
Source:		http://belnet.dl.sourceforge.net/sourceforge/ocamlsdl/%{up_name}-%{version}.tar.bz2
Patch0:		ocamlsdl-0.7.2.install-destdir.patch
Group:		Development/Other
URL:		http://ocamlsdl.sourceforge.net/
BuildRequires:	libSDL-devel
BuildRequires:	libSDL_image-devel
BuildRequires:	libSDL_mixer-devel
BuildRequires:	libSDL_ttf-devel
BuildRequires:	libpng-devel
BuildRequires:	libncurses-devel
BuildRequires:	ocaml
BuildRequires:	ocaml-lablgl-devel
BuildRequires:  findlib
Obsoletes:      ocaml-SDL
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%package -n %{name}-devel
Summary:	Wrapper around the cross platform Simple DirectMedia Layer game library
Group:		Development/Other
Requires:	libSDL-devel
Requires:	libSDL_image-devel
Requires:	libSDL_mixer-devel
Requires:	libSDL_ttf-devel
Requires:	libpng-devel
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
%patch -p1

%build
%configure2_5x --with-lablgldir=%{ocaml_sitelib}/lablgl
make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{ocaml_sitelib}
install -d %{buildroot}%{ocaml_sitelib}/stublibs
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{ocaml_sitelib}"
mkdir -p %{buildroot}/%{_infodir}
install doc/*.info* %{buildroot}/%{_infodir}

%clean
rm -rf %{buildroot}

%post devel
%_install_info ocamlsdl.info

%preun devel
%_remove_install_info ocamlsdl.info

%files
%defattr(-,root,root)
%doc README AUTHORS META NEWS doc/* 
%dir %{ocaml_sitelib}/sdl
%{ocaml_sitelib}/sdl/*.cmi
%{ocaml_sitelib}/stublibs/*

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/sdl/*
%exclude %{ocaml_sitelib}/sdl/*.cmi
%{_infodir}/*
