Summary:	DJB DNS
Summary(pl):	DJB DNS
Name:		djbdns
Version:	1.05
Release:	13
License:	http://cr.yp.to/distributors.html (free to use)
Group:		Networking/Daemons
Source0:	http://cr.yp.to/djbdns/%{name}-%{version}.tar.gz
Source1:	%{name}-doc.tar.gz
Source2:	ftp://ftp.innominate.org/gpa/djb/%{name}-%{version}-man.tar.gz
Patch0:		dnscache-1.05-multiple-ip.patch
Patch1:		http://www.fefe.de/dns/%{name}-1.05-ipv6.diff
#		based on http://www.ohse.de/uwe/patches/djbdns-1.05-multiip.diff
Patch2:		%{name}-1.05-multiip.diff
Patch3:		http://iksz.hu/package/djbdns-conf/djbdns-1.05-multi_tinydns_data.patch
Patch4:		%{name}-srv.patch
Patch5:		%{name}-glibc.patch
URL:		http://cr.yp.to/djbdns.html
Requires(pre):	/usr/bin/getgid
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/userdel
Requires(postun):	/usr/sbin/groupdel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of DNS servers with security in mind. If you find a
security hole you can get a prize.

This package contains some basic DNS debugging tools and some
documentation. If you need a DNS server install one of the following
packages:

 - djbdns-dnscache - a local DNS cache
 - djbdns-tinydns - a DNS server
 - djbdns-pickdns - a DNS load-balancing server
 - djbdns-walldns - a reverse DNS wall
 - djbdns-rbldns - an IP-address-listing DNS server
 - djbdns-axfrdns - a DNS zone transfer server

%description -l de
Dies ist ein Satz von auf Sicherheit zielenden DNS-Servers. Man kriegt
ein Preis, wenn man ein Sicherheitsloch findet.

Dieses Paket enthält ein paar DNS-Werkzeugen und etwas Dokumentation.
Wenn du einen DNS-Server braucht, installe ein von den folgenden
Paketen:

 - djbdns-dnscache - ein lokaler DNS-Cache
 - djbdns-tinydns - ein DNS-Server
 - djbdns-pickdns - ein Belastung ausgleichender DNS-Server
 - djbdns-walldns - eine Wand Rückgekehrten DNSs
 - djbdns-rbldns - ein IP-Adressen-Listen-DNS-Server
 - djbdns-axfrdns - ein DNS-Zonen-Transfer-Server

%description -l pl
Jest to alternatywny zestaw serwerów DNS'u, którego g³ównym celem jest
bezpieczeñstwo. Za znalezienie dziury w tym systemie zosta³a
wyznaczona nawet nagroda.

Ten pakiet zawiera kilka podstawowych narzêdzi DNS oraz trochê
dokumentacji. Je¶li potrzebujesz serwera DNS zainstaluj jeden z
nastêpuj±cych pakietów:

 - djbdns-dnscache - lokalny cache DNS
 - djbdns-tinydns - serwer DNS
 - djbdns-pickdns - serwer DNS do równowa¿enia obci±¿eñ
 - djbdns-walldns - ¶ciana dla odwrotnych zapytañ DNS
 - djbdns-rbldns - serwer DNS list adresów IP
 - djbdns-axfrdns - serwer transferów stref DNS

%package dnscache
Summary:	DJB's local DNS cache
Summary(de):	DJBs lokaler DNS-Cache
Summary(pl):	Lokalny cache DNS od DJB
Group:		Networking/Daemons
PreReq:		%{name} = %{version}
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/useradd
Requires(post):	diffutils
Requires(post):	fileutils
Requires(preun):	daemontools
Requires(postun):	/usr/sbin/userdel
Requires:	daemontools >= 0.70-5
Obsoletes:	dnscache

%description dnscache
dnscache is a local DNS cache from the djbdns package. It accepts
recursive DNS queries from local clients such as web browsers and mail
transfer agents. It collects responses from remote DNS servers. It
caches the responses to save time later.

%description dnscache -l de
dnscache ist ein lokaler DNS-Cache aus dem djbdns-Paket. Es empfängt
rekursive DNS-Fragen von den lokalen Klienten, zum Beispiel
Web-Browsers und Mail-Transfer-Agenten. Es sammelt die Antworten von
den Fern-DNS-Servers. Es merkt sich die Antworten, um die Zeit später
zu sparen.

%description dnscache -l pl
dnscache jest lokalnym cachem DNS z pakietu djbdns. Przyjmuje on
rekursywne zapytania DNS od lokalnych klientów takich, jak
przegl±darki WWW i agenci transferu poczty (MTA). Zbiera on odpowiedzi
od zdalnych serwerów DNS. Zapamiêtuje on odpowiedzi, ¿eby pó¼niej
oszczêdziæ czas.

%package tinydns
Summary:	DJB's DNS server
Summary(de):	DJBs DNS-Server
Summary(pl):	Serwer DNS od DJB
Group:		Networking/Daemons
PreReq:		%{name} = %{version}
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/useradd
Requires(post):	diffutils
Requires(preun):	daemontools
Requires(postun):	/usr/sbin/userdel
Requires:	daemontools >= 0.70-5
Requires:	make
Obsoletes:	tinydns

%description tinydns
tinydns is a DNS server from the djbdns package. It accepts iterative
DNS queries from hosts around the Internet and responds with
locally-configured information.

%description tinydns -l de
tinydns ist ein DNS-Server aus dem djbdns-Paket. Es empfängt iterative
DNS-Fragen von dem Hosts aus allem Internet und antwortet mit den
lokal-konfigurierten Informationen.

%description tinydns -l pl
tinydns jest serwerem DNS z pakietu djbdns. Przyjmuje on iteracyjne
zapytania DNS od komputerów z ca³ego Internetu i odpowiada przy u¿yciu
lokalnie skonfigurowanych informacji.

%package pickdns
Summary:	DJB's load-balancing DNS server
Summary(de):	DJBs Belastung ausgleichender DNS-Server
Summary(pl):	Serwer DNS równowa¿±cy obci±¿enie od DJB
Group:		Networking/Daemons
PreReq:		%{name} = %{version}
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/useradd
Requires(post):	diffutils
Requires(preun):	daemontools
Requires(postun):	/usr/sbin/userdel
Requires:	daemontools >= 0.70-5
Requires:	make
Obsoletes:	pickdns

%description pickdns
pickdns is a DNS load-balancing server from the djbdns package. It
accepts iterative DNS queries from hosts around the Internet and
responds with a dynamic selection of locally configured IP addresses
with 5-second TTLs.

%description pickdns -l de
pickdns ist ein Belastung ausgleichender DNS-Server aus dem
djbdns-Paket. Es empfängt iterative DNS-Fragen von den Hosts aus allem
Internet und antwortet mit eine dynamische Auswahl von den
lokal-konfigurierten IP-Adressen mit 5-Sekunden-TTLs.

%description pickdns -l pl
pickdns jest równowa¿±cym obci±¿enie serwerem DNS z pakietu djbdns.
Odbiera on iteracyjne zapytania DNS od komputerów z ca³ego internetu i
odpowiada dynamicznym wyborem lokalnie skonfigurowanych adresów IP z
5-sekundowymi TTLami.

%package walldns
Summary:	DJB's reverse DNS wall
Summary(de):	DJBs Wand rückgekehrten DNSs
Summary(pl):	¦ciana dla odwrotnych zapytañ DNS od DJB
Group:		Networking/Daemons
PreReq:		%{name} = %{version}
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/useradd
Requires(post):	diffutils
Requires(preun):	daemontools
Requires(postun):	/usr/sbin/userdel
Requires:	daemontools >= 0.70-5
Obsoletes:	walldns

%description walldns
walldns is a reverse DNS wall from the djbdns package. It accepts
iterative DNS queries for in-addr.arpa domains from hosts around the
Internet and supplies generic responses that avoid revealing local
host information.

%description walldns -l de
walldns ist ein Wand rückgekehrten DNSs aus dem djbdns-Paket. Es
empfängt iterative DNS-Fragen für den in-addr.arpa-Domänen von den
Hosts aus allem Internet und liefert Antworte, die vermeiden
Informationen über die lokalen Hosts zu aufzudecken.

%description walldns -l pl
walldns jest ¶cian± dla odwrotnych zapytañ DNS z pakietu djbdns.
Przyjmuje ona iteracyjne zapytania DNS dla domen in-addr.arpa od
komputerów z ca³ego Internetu i dostarcza odpowiedzi, które unikaj±
ujawniania informacji o lokalnych komputerach.

%package rbldns
Summary:	DJB's IP-address-listing DNS server
Summary(de):	DJBs IP-Adressen-Listen-DNS-Server
Summary(pl):	Serwer DNS list adresów IP od DJB
Group:		Networking/Daemons
PreReq:		%{name} = %{version}
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/useradd
Requires(post):	diffutils
Requires(preun):	daemontools
Requires(postun):	/usr/sbin/userdel
Requires:	daemontools >= 0.70-5
Requires:	make
Obsoletes:	rbldns

%description rbldns
rbldns is an IP-address-listing DNS server from the djbdns package. It
accepts iterative DNS queries from hosts around the Internet asking
about various IP addresses. It provides responses showing whether the
addresses are on a locally configured list, such as RBL or DUL.

%description rbldns -l de
rbldns ist ein IP-Adressen-Listen-DNS-Server aus dem djbdns-Paket. Es
empfängt iterative DNS-Fragen von den Hosts aus allem Internet
fragende nach verschiedene IP-Adresse. Es liefert Antworte, die zeugen
ob die Adresse sich auf einer lokal-konfigurierten Liste befinden, zum
Beispiel RBL oder DUL.

%description rbldns -l pl
rbldns jest serwerem DNS list adresów z pakietu djbdns. Przyjmuje on
iteracyjne zapytania DNS od komputerów z ca³ego Internetu pytaj±ce o
ró¿ne adresy IP. Dostarcza on odpowiedzi pokazuj±cych, czy adresy te
s± na lokalnie skonfigurowanej li¶cie takiej, jak RBL lub DUL.

%package axfrdns
Summary:	DJB's DNS zone-transfer server
Summary(de):	DJBs DNS-Zonen-Transfer-Server
Summary(pl):	Serwer transferów stref DNS od DJB
Group:		Networking/Daemons
PreReq:		%{name} = %{version}
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/useradd
Requires(preun):	daemontools
Requires(postun):	/usr/sbin/userdel
Requires:	%{name}-tinydns = %{version}
Requires:	daemontools >= 0.70-5
Requires:	make
Requires:	ucspi-tcp
Obsoletes:	axfrdns

%description axfrdns
axfrdns is a DNS zone transfer server from the djbdns package. It
reads a zone-transfer request in DNS-over-TCP format from its standard
input and responds with locally configured information.

%description axfrdns -l de
axfrdns ist ein DNS-Zonen-Transfer-Server aus dem djbdns-Paket. Es
liest ein Zonen-Transfer-Ersuchen im DNS-over-TCP-Format von seinem
standarden Eingabe und antwortet mit den lokal-konfigurierten
Informationen.

%description axfrdns -l pl
axfrdns jest serwerem transferów stref DNS z pakietu djbdns. Wczytuje
on ze standardowego wej¶cia pro¶bê o transfer strefy w formacie
DNS-over-TCP i odpowiada przy u¿yciu lokalnie skonfigurowanych
informacji.

%prep
%setup -q -a1 -a2

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5
cd doc
ln -s merge/djbdns/* .

%build
echo %{__cc} %{rpmcflags} >conf-cc
echo %{_prefix} > conf-home
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_sysconfdir}}
install -d $RPM_BUILD_ROOT%{_mandir}/{man1,man5,man8}

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
install djbdns-man/*.1	$RPM_BUILD_ROOT%{_mandir}/man1
install djbdns-man/*.5  $RPM_BUILD_ROOT%{_mandir}/man5
install djbdns-man/*.8  $RPM_BUILD_ROOT%{_mandir}/man8

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
cat>root/add-host6<<___
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add host6 \${1+"\$@"}
___
cat>root/add-alias<<___
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add alias \${1+"\$@"}
___
cat>root/add-alias6<<___
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add alias6 \${1+"\$@"}
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
install -d $RPM_BUILD_ROOT/service
cd $RPM_BUILD_ROOT/service
ln -s ..%{_sysconfdir}/dnscache
ln -s ..%{_sysconfdir}/tinydns
ln -s ..%{_sysconfdir}/pickdns
ln -s ..%{_sysconfdir}/walldns
ln -s ..%{_sysconfdir}/rbldns
ln -s ..%{_sysconfdir}/axfrdns

%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ -n "`getgid djbdns`" ]; then
	if [ "`getgid djbdns`" != "32" ]; then
		echo "Error: group djbdns doesn't have gid=32. Correct this before installing djbdns." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 32 -r -f djbdns
fi
if [ -n "`id -u dnslog 2>/dev/null`" ]; then
	if [ "`id -u dnslog`" != "32" ]; then
		echo "Error: user dnslog doesn't have uid=32. Correct this before installing djbdns." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 32 -r -d / -s /bin/false -c "djbdns User" -g djbdns dnslog 1>&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/userdel dnslog
	/usr/sbin/groupdel djbdns
fi

%pre dnscache
if [ -n "`id -u dnscache 2>/dev/null`" ]; then
	if [ "`id -u dnscache`" != "33" ]; then
		echo "Error: user dnscache doesn't have uid=33. Correct this before installing djbdns-dnscache." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 33 -r -d /etc/dnscache -s /bin/false -c "djbdns User" -g djbdns dnscache 1>&2
fi

%post dnscache
if [ \! -s /etc/dnscache/seed ]; then
	dd if=/dev/urandom of=/etc/dnscache/seed bs=128c count=1
fi
if diff -u /etc/{dnscache,pickdns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and pickdns can't work on the same"
	echo "IP address. You have to edit either /etc/dnscache/env/IP"
	echo "or /etc/pickdns/env/IP."
fi
if diff -u /etc/{dnscache,rbldns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and rbldns can't work on the same"
	echo "IP address. You have to edit either /etc/dnscache/env/IP"
	echo "or /etc/rbldns/env/IP."
fi
if diff -u /etc/{dnscache,tinydns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and tinydns can't work on the same"
	echo "IP address. You have to edit either /etc/dnscache/env/IP"
	echo "or /etc/tinydns/env/IP."
fi
if diff -u /etc/{dnscache,walldns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and walldns can't work on the same"
	echo "IP address. You have to edit either /etc/dnscache/env/IP"
	echo "or /etc/walldns/env/IP."
fi

%preun dnscache
if [ "$1" = "0" ]; then
	svc -d /service/dnscache
fi

%postun dnscache
if [ "$1" = "0" ]; then
	/usr/sbin/userdel dnscache
fi

%pre tinydns
if [ -n "`id -u tinydns 2>/dev/null`" ]; then
	if [ "`id -u tinydns`" != "34" ]; then
		echo "Error: user tinydns doesn't have uid=34. Correct this before installing djbdns-tinydns." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 34 -r -d /etc/tinydns -s /bin/false -c "djbdns User" -g djbdns tinydns 1>&2
fi

%post tinydns
if diff -u /etc/{dnscache,tinydns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and tinydns can't work on the same"
	echo "IP address. You have to edit either /etc/dnscache/env/IP"
	echo "or /etc/tinydns/env/IP."
fi
if diff -u /etc/{pick,tiny}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: pickdns and tinydns can't work on the same"
	echo "IP address. You have to edit either /etc/pickdns/env/IP"
	echo "or /etc/tinydns/env/IP."
fi
if diff -u /etc/{rbl,tiny}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: rbldns and tinydns can't work on the same"
	echo "IP address. You have to edit either /etc/rbldns/env/IP"
	echo "or /etc/tinydns/env/IP."
fi
if diff -u /etc/{tiny,wall}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: tinydns and walldns can't work on the same"
	echo "IP address. You have to edit either /etc/tinydns/env/IP"
	echo "or /etc/walldns/env/IP."
fi

%preun tinydns
if [ "$1" = "0" ]; then
	svc -d /service/tinydns
fi

%postun tinydns
if [ "$1" = "0" ]; then
	/usr/sbin/userdel tinydns
fi

%pre pickdns
if [ -n "`id -u pickdns 2>/dev/null`" ]; then
	if [ "`id -u pickdns`" != "35" ]; then
		echo "Error: user pickdns doesn't have uid=35. Correct this before installing djbdns-pickdns." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 35 -r -d /etc/pickdns -s /bin/false -c "djbdns User" -g djbdns pickdns 1>&2
fi

%post pickdns
if diff -u /etc/{dnscache,pickdns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and pickdns can't work on the same"
	echo "IP address. You have to edit either /etc/dnscache/env/IP"
	echo "or /etc/pickdns/env/IP."
fi
if diff -u /etc/{pick,rbl}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: pickdns and rbldns can't work on the same"
	echo "IP address. You have to edit either /etc/pickdns/env/IP"
	echo "or /etc/rbldns/env/IP."
fi
if diff -u /etc/{pick,tiny}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: pickdns and tinydns can't work on the same"
	echo "IP address. You have to edit either /etc/pickdns/env/IP"
	echo "or /etc/tinydns/env/IP."
fi
if diff -u /etc/{pick,wall}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: pickdns and walldns can't work on the same"
	echo "IP address. You have to edit either /etc/pickdns/env/IP"
	echo "or /etc/walldns/env/IP."
fi

%preun pickdns
if [ "$1" = "0" ]; then
	svc -d /service/pickdns
fi

%postun pickdns
if [ "$1" = "0" ]; then
	/usr/sbin/userdel pickdns
fi

%pre walldns
if [ -n "`id -u walldns 2>/dev/null`" ]; then
	if [ "`id -u walldns`" != "36" ]; then
		echo "Error: user walldns doesn't have uid=36. Correct this before installing djbdns-walldns." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 36 -r -d /etc/walldns -s /bin/false -c "djbdns User" -g djbdns walldns 1>&2
fi

%post walldns
if diff -u /etc/{dnscache,walldns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and walldns can't work on the same"
	echo "IP address. You have to edit either /etc/dnscache/env/IP"
	echo "or /etc/walldns/env/IP."
fi
if diff -u /etc/{pick,wall}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: pickdns and walldns can't work on the same"
	echo "IP address. You have to edit either /etc/pickdns/env/IP"
	echo "or /etc/walldns/env/IP."
fi
if diff -u /etc/{rbl,wall}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: rbldns and walldns can't work on the same"
	echo "IP address. You have to edit either /etc/rbldns/env/IP"
	echo "or /etc/walldns/env/IP."
fi
if diff -u /etc/{tiny,wall}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: tinydns and walldns can't work on the same"
	echo "IP address. You have to edit either /etc/tinydns/env/IP"
	echo "or /etc/walldns/env/IP."
fi

%preun walldns
if [ "$1" = "0" ]; then
	svc -d /service/walldns
fi

%postun walldns
if [ "$1" = "0" ]; then
	/usr/sbin/userdel walldns
fi

%pre rbldns
if [ -n "`id -u rbldns 2>/dev/null`" ]; then
	if [ "`id -u rbldns`" != "37" ]; then
		echo "Error: user rbldns doesn't have uid=37. Correct this before installing djbdns-rbldns." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 37 -r -d /etc/rbldns -s /bin/false -c "djbdns User" -g djbdns rbldns 1>&2
fi

%post rbldns
if diff -u /etc/{dnscache,rbldns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and rbldns can't work on the same"
	echo "IP address. You have to edit either /etc/dnscache/env/IP"
	echo "or /etc/rbldns/env/IP."
fi
if diff -u /etc/{pick,rbl}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: pickdns and rbldns can't work on the same"
	echo "IP address. You have to edit either /etc/pickdns/env/IP"
	echo "or /etc/rbldns/env/IP."
fi
if diff -u /etc/{rbl,tiny}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: rbldns and tinydns can't work on the same"
	echo "IP address. You have to edit either /etc/rbldns/env/IP"
	echo "or /etc/tinydns/env/IP."
fi
if diff -u /etc/{rbl,wall}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: rbldns and walldns can't work on the same"
	echo "IP address. You have to edit either /etc/rbldns/env/IP"
	echo "or /etc/walldns/env/IP."
fi

%preun rbldns
if [ "$1" = "0" ]; then
	svc -d /service/rbldns
fi

%postun rbldns
if [ "$1" = "0" ]; then
	/usr/sbin/userdel rbldns
fi

%pre axfrdns
if [ -n "`id -u axfrdns 2>/dev/null`" ]; then
	if [ "`id -u axfrdns`" != "38" ]; then
		echo "Error: user axfrdns doesn't have uid=38. Correct this before installing djbdns-axfrdns." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 38 -r -d /etc/axfrdns -s /bin/false -c "djbdns User" -g djbdns axfrdns 1>&2
fi

%preun axfrdns
if [ "$1" = "0" ]; then
	svc -d /service/axfrdns
fi

%postun axfrdns
if [ "$1" = "0" ]; then
	/usr/sbin/userdel axfrdns
fi

%files
%defattr(644,root,root,755)
%doc CHANGES TODO MULTIPLEIP TINYDNS doc/*
%attr(755,root,root) %{_bindir}/cachetest
%attr(755,root,root) %{_bindir}/dns[f-t]*
%attr(755,root,root) %{_bindir}/axfr-get
%{_mandir}/man[15]/*
%{_mandir}/man8/axfr-get*

%files dnscache
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
%{_mandir}/man8/dnscache*
/service/dnscache

%files tinydns
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
%{_mandir}/man8/tinydns*
/service/tinydns

%files pickdns
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
%{_mandir}/man8/pickdns*
/service/pickdns

%files walldns
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
%{_mandir}/man8/walldns*
/service/walldns

%files rbldns
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
%{_mandir}/man8/rbldns*
/service/rbldns

%files axfrdns
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
%{_mandir}/man8/axfrdns*
/service/axfrdns
