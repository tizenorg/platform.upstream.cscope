Name:           cscope
Version:        15.8a
Release:        0
License:        BSD-3-Clause
Summary:        An interactive, screen-oriented tool for browsing source code
Url:            http://cscope.sourceforge.net
Group:          Development/Tools
Source:         %{name}-%{version}.tar.gz
Source1001: 	cscope.manifest
BuildRequires:  ncurses-devel

%description
cscope is an interactive, screen-oriented tool that allows the user to browse
through C source files for specified elements of code.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%docs_package

%files
%manifest %{name}.manifest
%license COPYING
%{_bindir}/*
