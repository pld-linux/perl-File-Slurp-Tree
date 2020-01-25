#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	File
%define		pnam	Slurp-Tree
Summary:	File::Slurp::Tree - slurp and emit file trees as nested hashes
Summary(pl.UTF-8):	File::Slurp::Tree - tworzenie z plików drzew jako zagnieżdżonych haszy
Name:		perl-File-Slurp-Tree
Version:	1.24
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3d4287dd9697fc8fe402399841a6c742
URL:		http://search.cpan.org/dist/File-Slurp-Tree/
%if %{with tests}
BuildRequires:	perl-File-Find-Rule
BuildRequires:	perl-File-Slurp
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::Slurp::Tree provides functions for slurping and emitting trees
of files and directories.

%description -l pl.UTF-8
File::Slurp::Tree dostarcza funkcje do odczytu i tworzenia drzew
plików i katalogów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/File/Slurp
%{perl_vendorlib}/File/Slurp/Tree.pm
%{_mandir}/man3/*
