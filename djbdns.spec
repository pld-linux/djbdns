Summary:	DJB DNS 
Summary(pl):	DJB DNS
Name:		djbdns
Version:	1.05
Release:	4
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://cr.yp.to/djbdns/%{name}-%{version}.tar.gz
Source1:	%{name}-doc.tar.gz
Patch0:		dnscache-1.05-multiple-ip.patch
URL:		http://cr.yp.to/djbdns.html
Prereq:		shadow
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of DNS servers with security in mind. If you find a
security hole you can get a prize.

This package contains some basic DNS debugging tools and some
documentation. If you need a DNS server install one of the following
packages:

 - dnscache - a local DNS cache
 - tinydns - a DNS server
 - pickdns - a DNS load-balancing server
 - walldns - a reverse DNS wall
 - rbldns - an IP-address-listing DNS server
 - axfrdns - a DNS zone transfer server

%description -l de
Dies ist ein Satz von auf Sicherheit zielenden DNS-Servers. Man kriegt
ein Preis, wenn man ein Sicherheitsloch findet.

Dieses Paket enthält ein paar DNS-Werkzeugen und etwas Dokumentation.
Wenn du einen DNS-Server braucht, installe ein von den folgenden
Paketen:

 - dnscache - ein lokaler DNS-Cache
 - tinydns - ein DNS-Server
 - pickdns - ein Belastung ausgleichender DNS-Server
 - walldns - eine Wand Rückgekehrten DNSs
 - rbldns - ein IP-Adressen-Listen-DNS-Server
 - axfrdns - ein DNS-Zonen-Transfer-Server

%description -l pl
Jest to alternatywny zestaw serwerów DNS'u, którego g³ównym celem jest
bezpieczeñstwo. Za znalezienie dziury w tym systemie zosta³a
wyznaczona nawet nagroda.

Ten pakiet zawiera kilka podstawowych narzêdzi DNS oraz trochê
dokumentacji. Je¶li potrzebujesz serwera DNS zainstaluj jeden z
nastêpuj±cych pakietów:

 - dnscache - lokalny cache DNS
 - tinydns - serwer DNS
 - pickdns - serwer DNS do równowa¿enia obci±¿eñ
 - walldns - ¶ciana dla odwrotnych zapytañ DNS
 - rbldns - serwer DNS list adresów IP
 - axfrdns - serwer transferów stref DNS

%package -n dnscache
Summary:	DJB's local DNS cache
Summary(de):	DJBs lokaler DNS-Cache
Summary(pl):	Lokalny cache DNS od DJB
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Requires:	%{name} = %{version}
Requires:	daemontools
Prereq:		fileutils
Prereq:		shadow

%description -n dnscache
dnscache is a local DNS cache from the djbdns package. It accepts
recursive DNS queries from local clients such as web browsers and mail
transfer agents. It collects responses from remote DNS servers. It
caches the responses to save time later.

%description -n dnscache -l de
dnscache ist ein lokaler DNS-Cache aus dem djbdns-Paket. Es empfängt
rekursive DNS-Fragen von den lokalen Klienten, zum Beispiel
Web-Browsers und Mail-Transfer-Agenten. Es sammelt die Antworten von
den Fern-DNS-Servers. Es merkt sich die Antworten, um die Zeit später
zu sparen.

%description -n dnscache -l pl
dnscache jest lokalnym cachem DNS z pakietu djbdns. Przyjmuje on
rekursywne zapytania DNS od lokalnych klientów takich, jak
przegl±darki WWW i agenci transferu poczty (MTA). Zbiera on odpowiedzi
od zdalnych serwerów DNS. Zapamiêtuje on odpowiedzi, ¿eby pó¼niej
oszczêdziæ czas.

%package -n tinydns
Summary:	DJB's DNS server
Summary(de):	DJBs DNS-Server
Summary(pl):	Serwer DNS od DJB
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Requires:	%{name} = %{version}
Requires:	daemontools
Requires:	make
Prereq:		shadow

%description -n tinydns
tinydns is a DNS server from the djbdns package. It accepts iterative
DNS queries from hosts around the Internet and responds with
locally-configured information.

%description -n tinydns -l de
tinydns ist ein DNS-Server aus dem djbdns-Paket. Es empfängt iterative
DNS-Fragen von dem Hosts aus allem Internet und antwortet mit den
lokal-konfigurierten Informationen.

%description -n tinydns -l pl
tinydns jest serwerem DNS z pakietu djbdns. Przyjmuje on iteracyjne
zapytania DNS od komputerów z ca³ego Internetu i odpowiada przy u¿yciu
lokalnie skonfigurowanych informacji.

%package -n pickdns
Summary:	DJB's load-balancing DNS server
Summary(de):	DJBs Belastung ausgleichender DNS-Server
Summary(pl):	Serwer DNS równowa¿±cy obci±¿enie od DJB
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Requires:	%{name} = %{version}
Requires:	daemontools
Requires:	make
Prereq:		shadow

%description -n pickdns
pickdns is a DNS load-balancing server from the djbdns package. It
accepts iterative DNS queries from hosts around the Internet and
responds with a dynamic selection of locally configured IP addresses
with 5-second TTLs.

%description -n pickdns -l de
pickdns ist ein Belastung ausgleichender DNS-Server aus dem
djbdns-Paket. Es empfängt iterative DNS-Fragen von den Hosts aus allem
Internet und antwortet mit eine dynamische Auswahl von den
lokal-konfigurierten IP-Adressen mit 5-Sekunden-TTLs.

%description -n pickdns -l pl
pickdns jest równowa¿±cym obci±¿enie serwerem DNS z pakietu djbdns.
Odbiera on iteracyjne zapytania DNS od komputerów z ca³ego internetu i
odpowiada dynamicznym wyborem lokalnie skonfigurowanych adresów IP z
5-sekundowymi TTLami.

%package -n walldns
Summary:	DJB's reverse DNS wall
Summary(de):	DJBs Wand rückgekehrten DNSs
Summary(pl):	¦ciana dla odwrotnych zapytañ DNS od DJB
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Requires:	%{name} = %{version}
Requires:	daemontools
Prereq:		shadow

%description -n walldns
walldns is a reverse DNS wall from the djbdns package. It accepts
iterative DNS queries for in-addr.arpa domains from hosts around the
Internet and supplies generic responses that avoid revealing local
host information.

%description -n walldns -l de
walldns ist ein Wand rückgekehrten DNSs aus dem djbdns-Paket. Es
empfängt iterative DNS-Fragen für den in-addr.arpa-Domänen von den
Hosts aus allem Internet und liefert Antworte, die vermeiden
Informationen über die lokalen Hosts zu aufzudecken.

%description -n walldns -l pl
walldns jest ¶cian± dla odwrotnych zapytañ DNS z pakietu djbdns.
Przyjmuje ona iteracyjne zapytania DNS dla domen in-addr.arpa od
komputerów z ca³ego Internetu i dostarcza odpowiedzi, które unikaj±
ujawniania informacji o lokalnych komputerach.

%package -n rbldns
Summary:	DJB's IP-address-listing DNS server
Summary(de):	DJBs IP-Adressen-Listen-DNS-Server
Summary(pl):	Serwer DNS list adresów IP od DJB
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Requires:	%{name} = %{version}
Requires:	daemontools
Requires:	make
Prereq:		shadow

%description -n rbldns
rbldns is an IP-address-listing DNS server from the djbdns package. It
accepts iterative DNS queries from hosts around the Internet asking
about various IP addresses. It provides responses showing whether the
addresses are on a locally configured list, such as RBL or DUL.

%description -n rbldns -l de
rbldns ist ein IP-Adressen-Listen-DNS-Server aus dem djbdns-Paket. Es
empfängt iterative DNS-Fragen von den Hosts aus allem Internet
fragende nach verschiedene IP-Adresse. Es liefert Antworte, die zeugen
ob die Adresse sich auf einer lokal-konfigurierten Liste befinden, zum
Beispiel RBL oder DUL.

%description -n rbldns -l pl
rbldns jest serwerem DNS list adresów z pakietu djbdns. Przyjmuje on
iteracyjne zapytania DNS od komputerów z ca³ego Internetu pytaj±ce o
ró¿ne adresy IP. Dostarcza on odpowiedzi pokazuj±cych, czy adresy te
s± na lokalnie skonfigurowanej li¶cie takiej, jak RBL lub DUL.

%package -n axfrdns
Summary:	DJB's DNS zone-transfer server
Summary(de):	DJBs DNS-Zonen-Transfer-Server
Summary(pl):	Serwer transferów stref DNS od DJB
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Requires:	%{name} = %{version}
Requires:	tinydns = %{version}
Requires:	daemontools
Requires:	ucspi-tcp
Requires:	make
Prereq:		shadow

%description -n axfrdns
axfrdns is a DNS zone transfer server from the djbdns package. It
reads a zone-transfer request in DNS-over-TCP format from its standard
input and responds with locally configured information.

%description -n axfrdns -l de
axfrdns ist ein DNS-Zonen-Transfer-Server aus dem djbdns-Paket. Es
liest ein Zonen-Transfer-Ersuchen im DNS-over-TCP-Format von seinem
standarden Eingabe und antwortet mit den lokal-konfigurierten
Informationen.

%description -n axfrdns -l pl
axfrdns jest serwerem transferów stref DNS z pakietu djbdns. Wczytuje
on ze standardowego wej¶cia pro¶bê o transfer strefy w formacie
DNS-over-TCP i odpowiada przy u¿yciu lokalnie skonfigurowanych
informacji.

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

##### DNSCACHE #####

mkdir $RPM_BUILD_ROOT%{_sysconfdir}/dnscache
cd $RPM_BUILD_ROOT%{_sysconfdir}/dnscache
mkdir log
mkdir log/main
touch log/status
mkdir env
echo %{_sysconfdir}/dnscache/root>env/ROOT
echo 127.0.0.1                   >env/IP
echo 0.0.0.0                     >env/IPSEND
echo 1000000                     >env/CACHESIZE
echo 3000000                     >env/DATALIMIT
cat>run<<___
#!/bin/sh
exec 2>&1
exec <seed
exec envdir ./env sh -c '
  exec envuidgid dnscache softlimit -o250 -d "\$DATALIMIT" %{_bindir}/dnscache
'
___
cat>log/run<<___
#!/bin/sh
exec setuidgid dnslog multilog t ./main
___
mkdir root
mkdir root/ip
touch root/ip/127.0.0.1
mkdir root/servers
ln $RPM_BUILD_ROOT%{_sysconfdir}/dnsroots.global root/servers/\@
dd if=/dev/zero of=seed bs=128c count=1

##### TINYDNS #####

mkdir $RPM_BUILD_ROOT%{_sysconfdir}/tinydns
cd $RPM_BUILD_ROOT%{_sysconfdir}/tinydns
mkdir log
mkdir log/main
touch log/status
cat>log/run<<___
#!/bin/sh
exec setuidgid dnslog multilog t ./main
___
mkdir env
echo %{_sysconfdir}/tinydns/root>env/ROOT
echo 127.0.0.1                  >env/IP
cat>run<<___
#!/bin/sh
exec 2>&1
exec envuidgid tinydns envdir ./env softlimit -d300000 %{_bindir}/tinydns
___
mkdir root
touch root/data
cat>root/add-ns<<___
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add ns \${1+"\$@"}
___
cat>root/add-childns<<___
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add childns \${1+"\$@"}
___
cat>root/add-host<<___
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add host \${1+"\$@"}
___
cat>root/add-alias<<___
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add alias \${1+"\$@"}
___
cat>root/add-mx<<___
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add mx \${1+"\$@"}
___
cat>root/Makefile<<___
data.cdb: data
        %{_bindir}/tinydns-data
___

##### PICKDNS #####

mkdir $RPM_BUILD_ROOT%{_sysconfdir}/pickdns
cd $RPM_BUILD_ROOT%{_sysconfdir}/pickdns
mkdir log
mkdir log/main
touch log/status
cat>log/run<<___
#!/bin/sh
exec setuidgid dnslog multilog t ./main
___
mkdir env
echo %{_sysconfdir}/pickdns/root>env/ROOT
echo 127.0.0.1                  >env/IP
cat>run<<___
#!/bin/sh
exec 2>&1
exec envuidgid pickdns envdir ./env softlimit -d250000 %{_bindir}/pickdns
___
mkdir root
touch root/data
cat>root/Makefile<<___
data.cdb: data
        %{_bindir}/pickdns-data
___

##### WALLDNS #####
mkdir $RPM_BUILD_ROOT%{_sysconfdir}/walldns
cd $RPM_BUILD_ROOT%{_sysconfdir}/walldns
mkdir log
mkdir log/main
touch log/status
cat>log/run<<___
#!/bin/sh
exec setuidgid dnslog multilog t ./main
___
mkdir env
echo %{_sysconfdir}/walldns/root>env/ROOT
echo 127.0.0.1                  >env/IP
cat>run<<___
#!/bin/sh
exec 2>&1
exec envuidgid walldns envdir ./env softlimit -d250000 %{_bindir}/walldns
___
mkdir root

##### RBLDNS #####

mkdir $RPM_BUILD_ROOT%{_sysconfdir}/rbldns
cd $RPM_BUILD_ROOT%{_sysconfdir}/rbldns
mkdir log
mkdir log/main
touch log/status
cat>log/run<<___
#!/bin/sh
exec setuidgid dnslog multilog t ./main
___
mkdir env
echo %{_sysconfdir}/rbldns/root>env/ROOT
echo 127.0.0.1                 >env/IP
echo in-addr.arpa              >env/BASE
cat>run<<___
#!/bin/sh
exec 2>&1
exec envuidgid rbldns envdir ./env softlimit -d250000 %{_bindir}/rbldns
___
mkdir root
touch root/data
cat>root/Makefile<<___
data.cdb: data
        %{_bindir}/rbldns-data
___

##### AXFRDNS #####

mkdir $RPM_BUILD_ROOT%{_sysconfdir}/axfrdns
cd $RPM_BUILD_ROOT%{_sysconfdir}/axfrdns
mkdir log
mkdir log/main
touch log/status
cat>log/run<<___
#!/bin/sh
exec setuidgid dnslog multilog t ./main
___
mkdir env
echo %{_sysconfdir}/tinydns/root>env/ROOT
echo 127.0.0.1                  >env/IP
cat>run<<___
#!/bin/sh
exec 2>&1
exec envdir ./env sh -c '
  exec envuidgid axfrdns softlimit -d300000 tcpserver -vDRHl0 -x tcp.cdb -- "\$IP" 53 %{_bindir}/axfrdns
'
___
cat>Makefile<<___
tcp.cdb: tcp
        tcprules tcp.cdb tcp.tmp < tcp
___
cat>tcp<<___
# sample line:  1.2.3.4:allow,AXFR="heaven.af.mil/3.2.1.in-addr.arpa"
:deny
___

##### daemontools symlinks #####
install -d $RPM_BUILD_ROOT/var/run/service
cd $RPM_BUILD_ROOT/var/run/service
ln -s ../../..%{_sysconfdir}/dnscache
ln -s ../../..%{_sysconfdir}/tinydns
ln -s ../../..%{_sysconfdir}/pickdns
ln -s ../../..%{_sysconfdir}/walldns
ln -s ../../..%{_sysconfdir}/rbldns
ln -s ../../..%{_sysconfdir}/axfrdns

%pre
if [ -n "`getgid djbdns`" ]; then
	if [ "`getgid djbdns`" != "32" ]; then
		echo "Warning: the group djbdns doesn't have gid=32. Correct this before installing djbdns" 1>&2
		exit 1
	fi
else
	%{_sbindir}/groupadd -g 32 -r -f djbdns
fi
if [ -n "`id -u dnslog 2>/dev/null`" ]; then
	if [ "`id -u dnslog`" != "32" ]; then
		echo "Warning: the user dnslog doesn't have uid=32. Correct this before installing djbdns" 1>&2
		exit 1
	fi
else
	%{_sbindir}/useradd -u 32 -r -d / -s /bin/false -c "djbdns User" -g djbdns dnslog 1>&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/userdel dnslog
	/usr/sbin/groupdel djbdns
fi

%pre -n dnscache
if [ -n "`id -u dnscache 2>/dev/null`" ]; then
	if [ "`id -u dnscache`" != "33" ]; then
		echo "Warning: the user dnscache doesn't have uid=33. Correct this before installing dnscache" 1>&2
		exit 1
	fi
else
	%{_sbindir}/useradd -u 33 -r -d /etc/dnscache -s /bin/false -c "djbdns User" -g djbdns dnscache 1>&2
fi
dd if=/dev/urandom of=seed bs=128c count=1

%postun -n dnscache
if [ "$1" = "0" ]; then
	/usr/sbin/userdel dnscache
fi

%pre -n tinydns
if [ -n "`id -u tinydns 2>/dev/null`" ]; then
	if [ "`id -u tinydns`" != "34" ]; then
		echo "Warning: the user tinydns doesn't have uid=34. Correct this before installing tinydns" 1>&2
		exit 1
	fi
else
	%{_sbindir}/useradd -u 34 -r -d /etc/tinydns -s /bin/false -c "djbdns User" -g djbdns tinydns 1>&2
fi

%postun -n tinydns
if [ "$1" = "0" ]; then
	/usr/sbin/userdel tinydns
fi

%pre -n pickdns
if [ -n "`id -u pickdns 2>/dev/null`" ]; then
	if [ "`id -u pickdns`" != "35" ]; then
		echo "Warning: the user pickdns doesn't have uid=35. Correct this before installing pickdns" 1>&2
		exit 1
	fi
else
	%{_sbindir}/useradd -u 35 -r -d /etc/pickdns -s /bin/false -c "djbdns User" -g djbdns pickdns 1>&2
fi

%postun -n pickdns
if [ "$1" = "0" ]; then
	/usr/sbin/userdel pickdns
fi

%pre -n walldns
if [ -n "`id -u walldns 2>/dev/null`" ]; then
	if [ "`id -u walldns`" != "36" ]; then
		echo "Warning: the user walldns doesn't have uid=36. Correct this before installing walldns" 1>&2
		exit 1
	fi
else
	%{_sbindir}/useradd -u 36 -r -d /etc/walldns -s /bin/false -c "djbdns User" -g djbdns walldns 1>&2
fi

%postun -n walldns
if [ "$1" = "0" ]; then
	/usr/sbin/userdel walldns
fi

%pre -n rbldns
if [ -n "`id -u rbldns 2>/dev/null`" ]; then
	if [ "`id -u rbldns`" != "37" ]; then
		echo "Warning: the user rbldns doesn't have uid=37. Correct this before installing rbldns" 1>&2
		exit 1
	fi
else
	%{_sbindir}/useradd -u 37 -r -d /etc/rbldns -s /bin/false -c "djbdns User" -g djbdns rbldns 1>&2
fi

%postun -n rbldns
if [ "$1" = "0" ]; then
	/usr/sbin/userdel rbldns
fi

%pre -n axfrdns
if [ -n "`id -u axfrdns 2>/dev/null`" ]; then
	if [ "`id -u axfrdns`" != "38" ]; then
		echo "Warning: the user axfrdns doesn't have uid=38. Correct this before installing axfrdns" 1>&2
		exit 1
	fi
else
	%{_sbindir}/useradd -u 38 -r -d /etc/axfrdns -s /bin/false -c "djbdns User" -g djbdns axfrdns 1>&2
fi

%postun -n axfrdns
if [ "$1" = "0" ]; then
	/usr/sbin/userdel axfrdns
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*
%attr(755,root,root) %{_bindir}/cachetest
%attr(755,root,root) %{_bindir}/dns[f-t]*

%files -n dnscache
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dnscache*
%config %attr(644,root,root) %{_sysconfdir}/dnsroots.global
%dir %attr(3755,root,root) %{_sysconfdir}/dnscache
%dir %attr(2755,root,root) %{_sysconfdir}/dnscache/log
%dir %attr(2755,dnslog,djbdns) %{_sysconfdir}/dnscache/log/main
%attr(644,dnslog,djbdns) %{_sysconfdir}/dnscache/log/status
%dir %attr(2755,root,root) %{_sysconfdir}/dnscache/env
%config %attr(644,root,root) %{_sysconfdir}/dnscache/env/*
%attr(755,root,root) %{_sysconfdir}/dnscache/run
%attr(755,root,root) %{_sysconfdir}/dnscache/log/run
%dir %attr(2755,root,root) %{_sysconfdir}/dnscache/root
%dir %attr(2755,root,root) %{_sysconfdir}/dnscache/root/*
%config %attr(600,root,root) %{_sysconfdir}/dnscache/root/ip/*
%config %attr(644,root,root) %{_sysconfdir}/dnscache/root/servers/*
%ghost %attr(600,root,root) %{_sysconfdir}/dnscache/seed
/var/run/service/dnscache

%files -n tinydns
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tinydns*
%dir %attr(3755,root,root) %{_sysconfdir}/tinydns
%dir %attr(2755,root,root) %{_sysconfdir}/tinydns/log
%dir %attr(2755,dnslog,djbdns) %{_sysconfdir}/tinydns/log/main
%attr(644,dnslog,djbdns) %{_sysconfdir}/tinydns/log/status
%attr(755,root,root) %{_sysconfdir}/tinydns/log/run
%dir %attr(2755,root,root) %{_sysconfdir}/tinydns/env
%config %attr(644,root,root) %{_sysconfdir}/tinydns/env/*
%attr(755,root,root) %{_sysconfdir}/tinydns/run
%dir %attr(2755,root,root) %{_sysconfdir}/tinydns/root
%attr(644,root,root) %{_sysconfdir}/tinydns/root/Makefile
%config %attr(644,root,root) %{_sysconfdir}/tinydns/root/data
%attr(755,root,root) %{_sysconfdir}/tinydns/root/add-*
/var/run/service/tinydns

%files -n pickdns
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pickdns*
%dir %attr(3755,root,root) %{_sysconfdir}/pickdns
%dir %attr(2755,root,root) %{_sysconfdir}/pickdns/log
%dir %attr(2755,dnslog,djbdns) %{_sysconfdir}/pickdns/log/main
%attr(644,dnslog,djbdns) %{_sysconfdir}/pickdns/log/status
%attr(755,root,root) %{_sysconfdir}/pickdns/log/run
%dir %attr(2755,root,root) %{_sysconfdir}/pickdns/env
%config %attr(644,root,root) %{_sysconfdir}/pickdns/env/*
%attr(755,root,root) %{_sysconfdir}/pickdns/run
%dir %attr(2755,root,root) %{_sysconfdir}/pickdns/root
%attr(644,root,root) %{_sysconfdir}/pickdns/root/Makefile
%config %attr(644,root,root) %{_sysconfdir}/pickdns/root/data
/var/run/service/pickdns

%files -n walldns
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/walldns*
%dir %attr(3755,root,root) %{_sysconfdir}/walldns
%dir %attr(2755,root,root) %{_sysconfdir}/walldns/log
%dir %attr(2755,dnslog,djbdns) %{_sysconfdir}/walldns/log/main
%attr(644,dnslog,djbdns) %{_sysconfdir}/walldns/log/status
%attr(755,root,root) %{_sysconfdir}/walldns/log/run
%dir %attr(2755,root,root) %{_sysconfdir}/walldns/env
%config %attr(644,root,root) %{_sysconfdir}/walldns/env/*
%attr(755,root,root) %{_sysconfdir}/walldns/run
%dir %attr(2755,root,root) %{_sysconfdir}/walldns/root
/var/run/service/walldns

%files -n rbldns
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rbldns*
%dir %attr(3755,root,root) %{_sysconfdir}/rbldns
%dir %attr(2755,root,root) %{_sysconfdir}/rbldns/log
%dir %attr(2755,dnslog,djbdns) %{_sysconfdir}/rbldns/log/main
%attr(644,dnslog,djbdns) %{_sysconfdir}/rbldns/log/status
%attr(755,root,root) %{_sysconfdir}/rbldns/log/run
%dir %attr(2755,root,root) %{_sysconfdir}/rbldns/env
%config %attr(644,root,root) %{_sysconfdir}/rbldns/env/*
%attr(755,root,root) %{_sysconfdir}/rbldns/run
%dir %attr(2755,root,root) %{_sysconfdir}/rbldns/root
%attr(644,root,root) %{_sysconfdir}/rbldns/root/Makefile
%config %attr(644,root,root) %{_sysconfdir}/rbldns/root/data
/var/run/service/rbldns

%files -n axfrdns
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/axfrdns*
%dir %attr(3755,root,root) %{_sysconfdir}/axfrdns
%dir %attr(2755,root,root) %{_sysconfdir}/axfrdns/log
%dir %attr(2755,dnslog,djbdns) %{_sysconfdir}/axfrdns/log/main
%attr(644,dnslog,djbdns) %{_sysconfdir}/axfrdns/log/status
%attr(755,root,root) %{_sysconfdir}/axfrdns/log/run
%dir %attr(2755,root,root) %{_sysconfdir}/axfrdns/env
%config %attr(644,root,root) %{_sysconfdir}/axfrdns/env/*
%attr(755,root,root) %{_sysconfdir}/axfrdns/run
%attr(644,root,root) %{_sysconfdir}/axfrdns/Makefile
%config %attr(644,root,root) %{_sysconfdir}/axfrdns/tcp
/var/run/service/axfrdns
