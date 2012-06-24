Summary:	DJB DNS 
Summary(pl):	DJB DNS
Name:		djbdns
Version:	1.05
Release:	3
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://cr.yp.to/djbdns/%{name}-%{version}.tar.gz
Source1:	%{name}-doc.tar.gz
Patch0:		dnscache-1.05-multiple-ip.patch
URL:		http://cr.yp.to/djbdns.html
Requires:	daemontools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DJB DNS Tools.
This is DNS server with security in mind. If you find a security hole
you can get a prize.

%description -l pl
Narz�dzia DJB do obs�ugi DNS.
Jest to alternatywny server DNS'u, kt�rego g��wnym celem jest bezpiecze�stwo.
Za znalezienie dziury w tym programie zosta�a wyznaczona nawet nagroda.

%prep
%setup -q -a1
%patch0 -p1

cd doc
ln -s merge/djbdns/* .

%build
echo %{__cc} %{rpmcflags} >conf-cc
echo %{_prefix} > conf-home
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_sysconfdir}}

install dnsroots.global $RPM_BUILD_ROOT%{_sysconfdir}
install	axfr-get	$RPM_BUILD_ROOT%{_bindir}
install axfrdns		$RPM_BUILD_ROOT%{_bindir}
install axfrdns-conf	$RPM_BUILD_ROOT%{_bindir}
install cachetest	$RPM_BUILD_ROOT%{_bindir}
install dnscache	$RPM_BUILD_ROOT%{_bindir}
install dnscache-conf	$RPM_BUILD_ROOT%{_bindir}
install dnsfilter	$RPM_BUILD_ROOT%{_bindir}
install dnsip		$RPM_BUILD_ROOT%{_bindir}
install dnsipq		$RPM_BUILD_ROOT%{_bindir}
install dnsmx		$RPM_BUILD_ROOT%{_bindir}
install dnsname		$RPM_BUILD_ROOT%{_bindir}
install dnsq		$RPM_BUILD_ROOT%{_bindir}
install dnsqr		$RPM_BUILD_ROOT%{_bindir}
install dnstrace	$RPM_BUILD_ROOT%{_bindir}
install dnstxt		$RPM_BUILD_ROOT%{_bindir}
install pickdns		$RPM_BUILD_ROOT%{_bindir}
install pickdns-conf	$RPM_BUILD_ROOT%{_bindir}
install pickdns-data	$RPM_BUILD_ROOT%{_bindir}
install random-ip	$RPM_BUILD_ROOT%{_bindir}
install rbldns		$RPM_BUILD_ROOT%{_bindir}
install rbldns-conf	$RPM_BUILD_ROOT%{_bindir}
install rbldns-data	$RPM_BUILD_ROOT%{_bindir}
install rts		$RPM_BUILD_ROOT%{_bindir}
install tinydns		$RPM_BUILD_ROOT%{_bindir}
install tinydns-conf	$RPM_BUILD_ROOT%{_bindir}
install tinydns-data	$RPM_BUILD_ROOT%{_bindir}
install tinydns-edit	$RPM_BUILD_ROOT%{_bindir}
install tinydns-get	$RPM_BUILD_ROOT%{_bindir}
install walldns		$RPM_BUILD_ROOT%{_bindir}
install walldns-conf	$RPM_BUILD_ROOT%{_bindir}

gzip -9nf CHANGES TODO MULTIPLEIP TINYDNS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_sysconfdir}/*
