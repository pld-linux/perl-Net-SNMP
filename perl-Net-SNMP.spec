%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	SNMP
Summary:	Object oriented interface to SNMP
Summary(pl):	Obiektowo zorientowany interfejs do SNMP
Name:		perl-Net-SNMP
Version:	4.0.3
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	88a1f361092bfb560b629e61db4f0da3
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Crypt-DES >= 2.0.3
BuildRequires:	perl-Digest-HMAC
BuildRequires:	perl-Digest-SHA1
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Crypt-DES >= 2.0.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Object oriented interface to SNMP.

%description -l pl
Obiektowo zorientowany interfejs do SNMP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* Changes
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Net/*.pm
%{perl_vendorlib}/Net/SNMP
%{_mandir}/man?/*
