#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	SNMP
Summary:	Net::SNMP - object oriented interface to SNMP
Summary(pl.UTF-8):	Net::SNMP - zorientowany obiektowo interfejs do SNMP
Name:		perl-Net-SNMP
Version:	5.2.0
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0e717723f843ab22a93248833f3ebff7
Patch0:		%{name}-kill_vstring.patch
BuildRequires:	perl-Crypt-DES >= 2.0.3
BuildRequires:	perl-Digest-HMAC
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Crypt-DES >= 2.0.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# optional (not required if not using v6)
%define		_noautoreq	perl(Socket6) perl(IO::Socket::INET6)

%description
The Net::SNMP Perl module implements an object oriented interface to
the Simple Network Management Protocol. Perl applications can use the
module to retrieve or update information on a remote host using the
SNMP protocol. The module supports SNMP version-1, SNMP version-2c
(Community-Based SNMPv2), and SNMP version-3. The Net::SNMP module
assumes that the user has a basic understanding of the Simple Network
Management Protocol and related network management concepts.

%description -l pl.UTF-8
Moduł Perla Net::SNMP stanowi zorientowaną obiektowo implementację
interfejsu do protokołu SNMP (Simple Network Management Protocol).
Programy perlowe mogą korzystać z tego modułu do pobierania i
aktualizacji informacji na zdalnych hostach używając protokołu SNMP.
Moduł ten obsługuje wersje protokołu SNMP: 1, 2c (Community-Based
SNMPv2) oraz 3. Moduł Net::SNMP zakłada, że użytkownik rozumie w
podstawowym zakresie protokół SNMP i związane z nim idee zarządzania
sieciowego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Net/*.pm
%{perl_vendorlib}/Net/SNMP
%{_mandir}/man?/*
%{_examplesdir}/%{name}-%{version}
