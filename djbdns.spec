Summary:     	DJB DNS 
Summary(pl): 	DJB DNS
Name:        	djbdns
Version:     	1.03
Release:     	1
Group:       	Networking/Daemons
Group(pl):   	Sieciowe/Serwery
Copyright:   	GPL
URL:         	http://cr.yp.to/djbdns.html
Source0:      	http://cr.yp.to/djbdns/%{name}-%{version}.tar.gz
Source1:	%{name}-doc.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DJB DNS Tools.

%description -l pl
Narzêdzia DJB do obs³ugi DNS.

%prep
tar zxf %{SOURCE1}
cd doc
ln -s merge/djbdns/* .

%setup -q
echo %{__cc} %{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS} >conf-cc
echo /usr >conf-home

%build
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}

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

gzip -9nf CHANGES README SYSDEPS TARGETS TODO VERSION

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz ../doc/
%attr(755,root,root) %{_bindir}/*
