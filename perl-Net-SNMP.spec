#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	SNMP
Summary:	Net::SNMP - object oriented interface to SNMP
Summary(pl):	Net::SNMP - zorientowany obiektowo interfejs do SNMP
Name:		perl-Net-SNMP
Version:	4.1.2
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e6b761db6115b0b1fe5446e220abaa4a
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Crypt-DES >= 2.0.3
BuildRequires:	perl-Digest-HMAC
BuildRequires:	perl-Digest-SHA1
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Crypt-DES >= 2.0.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::SNMP Perl module implements an object oriented interface to
the Simple Network Management Protocol.  Perl applications can use the
module to retrieve or update information on a remote host using the
SNMP protocol.  The module supports SNMP version-1, SNMP version-2c
(Community-Based SNMPv2), and SNMP version-3.  The Net::SNMP module
assumes that the user has a basic understanding of the Simple Network
Management Protocol and related network management concepts.

%description -l pl
Modu³ Perla Net::SNMP stanowi zorientowan± obiektowo implementacjê
interfejsu do protoko³u SNMP (Simple Network Management Protocol).
Programy perlowe mog± korzystaæ z tego modu³u do pobierania i
aktualizacji informacji na zdalnych hostach u¿ywaj±c protoko³u SNMP.
Modu³ ten obs³uguje wersje protoko³u SNMP: 1, 2c (Community-Based
SNMPv2) oraz 3. Modu³ Net::SNMP zak³ada, ¿e u¿ytkownik rozumie w
podstawowym zakresie protokó³ SNMP i zwi±zane z nim idee zarz±dzania
sieciowego.

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
%doc README* Changes
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Net/*.pm
%{perl_vendorlib}/Net/SNMP
%{_mandir}/man?/*
