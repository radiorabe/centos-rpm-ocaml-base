Name:           ocaml-base
Version:        0.12.2
Release:        0.0%{?dist}
Summary:        Standard library for OCaml

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:        MIT
URL:            https://github.com/janestreet/base/
Source0:        https://github.com/janestreet/base/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-sexplib0-devel
BuildRequires:  ocaml-dune-devel

%description
A Part of Jane Street's Core library The Core suite of libraries is
an industrial strength alternative to OCaml's standard library that
was developed by Jane Street.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n %{libname}-%{version}

%build
%make_build

%install
# Currently base installs itself with ocamlfind.
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
dune install --prefix=$OCAMLFIND_DESTDIR --libdir=$OCAMLFIND_DESTDIR

%files
%doc README.org
%doc %{_libdir}/ocaml/doc/%{libname}
%license LICENSE.md
%{_libdir}/ocaml/%{libname}
%{_libdir}/ocaml/stublibs/dll%{libname}_stubs.so
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.ml
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license LICENSE.md
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Fri Dec 13 2019 Lucas Bickel <hairmare@rabe.ch> - 0.12.2-0.0
- Bump to 0.12.2
- Switch to MIT license

* Sun Dec  8 2019 Lucas Bickel <hairmare@rabe.ch> - 0.11.1-0.2
- Fix libdir env variable
- Use ocaml-dune instead of jbuilder

* Sat Aug  3 2019 Lucas Bickel <hairmare@rabe.ch> - 0.11.1-0.1
- Fix building with dune vs. jbuilder

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.11.1-0.0
- Initial build for pcre-ocaml package bump
