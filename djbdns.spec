# TODO
#  - warning: Installed (but unpackaged) file(s) found:
#   /etc/rbldns/data
#   /usr/bin/random-ip
Summary:	DJB DNS
Summary(pl.UTF-8):   DJB DNS
Name:		djbdns
Version:	1.05
Release:	22.1
License:	http://cr.yp.to/distributors.html (free to use)
Group:		Networking/Daemons
Source0:	http://cr.yp.to/djbdns/%{name}-%{version}.tar.gz
# Source0-md5:	3147c5cd56832aa3b41955c7a51cbeb2
Source1:	%{name}-doc.tar.gz
# Source1-md5:	1d6aed1a5d3d3eda3958fa3e7d808fc8
Source2:	ftp://ftp.innominate.org/gpa/djb/%{name}-%{version}-man.tar.gz
# Source2-md5:	2b4e71fa4592858e4508538f78d50f61
Source3:	http://www.sericyb.com.au/tinydns-notify
# NoSource3-md5:	2213bdc8c58c10cb8770b7e5b0d67aea
Source4:	http://www.sericyb.com.au/tinydns-log
# NoSource4-md5:	a9af7707a7cb7c41e855f441e242e422
Patch0:		dnscache-1.05-multiple-ip.patch
# adds IPv6 support
Patch1:		http://www.fefe.de/dns/%{name}-1.05-test22.diff.bz2
Patch3:		http://iksz.hu/package/djbdns-conf/%{name}-1.05-multi_tinydns_data.patch
Patch4:		%{name}-srv.patch
Patch5:		%{name}-glibc.patch
# http://www.iecc.com/rbldns-patch.txt
Patch6:		%{name}-rbldns_a.patch
# http://core.segfault.pl/~hobbit/tinydns-include.patch
Patch8:		%{name}-tinydns-include.patch
Patch9:		%{name}-tinydns-log-ipv6.patch
# http://romana.now.ie/software/djbdns-cachestats.patch
Patch10:	%{name}-cachestats.patch
URL:		http://cr.yp.to/djbdns.html
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.202
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Provides:	group(djbdns)
Provides:	nameserver
Provides:	user(dnslog)
Obsoletes:	caching-nameserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of DNS servers with security in mind. If you find a
security hole you can get a prize.

This package contains some basic DNS debugging tools and some
documentation. If you need a DNS server install one of the following
packages:

 - djbdns-dnscache - a local DNS cache
 - djbdns-tinydns - a DNS server
 - djbdns-tinydns-notify - a tool to send NOTIFY requests
 - djbdns-pickdns - a DNS load-balancing server
 - djbdns-walldns - a reverse DNS wall
 - djbdns-rbldns - an IP-address-listing DNS server
 - djbdns-axfrdns - a DNS zone transfer server

%description -l de.UTF-8
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

%description -l pl.UTF-8
Jest to alternatywny zestaw serwerów DNS'u, którego głównym celem jest
bezpieczeństwo. Za znalezienie dziury w tym systemie została
wyznaczona nawet nagroda.

Ten pakiet zawiera kilka podstawowych narzędzi DNS oraz trochę
dokumentacji. Jeśli potrzebujesz serwera DNS zainstaluj jeden z
następujących pakietów:

 - djbdns-dnscache - lokalny cache DNS
 - djbdns-tinydns - serwer DNS
 - djbdns-tinydns-notify - narzędzie do wysyłania komunikatów NOTIFY
 - djbdns-pickdns - serwer DNS do równoważenia obciążeń
 - djbdns-walldns - ściana dla odwrotnych zapytań DNS
 - djbdns-rbldns - serwer DNS list adresów IP
 - djbdns-axfrdns - serwer transferów stref DNS

%package dnscache
Summary:	DJB's local DNS cache
Summary(de.UTF-8):   DJBs lokaler DNS-Cache
Summary(pl.UTF-8):   Lokalny cache DNS od DJB
Group:		Networking/Daemons
Requires(post):	diffutils
Requires(post):	fileutils
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(preun):	daemontools
Requires:	%{name} = %{version}-%{release}
Requires:	daemontools >= 0.70-5
Provides:	user(dnscache)
Obsoletes:	dnscache

%description dnscache
dnscache is a local DNS cache from the djbdns package. It accepts
recursive DNS queries from local clients such as web browsers and mail
transfer agents. It collects responses from remote DNS servers. It
caches the responses to save time later.

%description dnscache -l de.UTF-8
dnscache ist ein lokaler DNS-Cache aus dem djbdns-Paket. Es empfängt
rekursive DNS-Fragen von den lokalen Klienten, zum Beispiel
Web-Browsers und Mail-Transfer-Agenten. Es sammelt die Antworten von
den Fern-DNS-Servers. Es merkt sich die Antworten, um die Zeit später
zu sparen.

%description dnscache -l pl.UTF-8
dnscache jest lokalnym cachem DNS z pakietu djbdns. Przyjmuje on
rekursywne zapytania DNS od lokalnych klientów takich, jak
przeglądarki WWW i agenci transferu poczty (MTA). Zbiera on odpowiedzi
od zdalnych serwerów DNS. Zapamiętuje on odpowiedzi, żeby później
oszczędzić czas.

%package tinydns
Summary:	DJB's DNS server
Summary(de.UTF-8):   DJBs DNS-Server
Summary(pl.UTF-8):   Serwer DNS od DJB
Group:		Networking/Daemons
Requires(post):	diffutils
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(preun):	daemontools
Requires:	%{name} = %{version}-%{release}
Requires:	daemontools >= 0.70-5
Requires:	make
Provides:	user(tinydns)
Obsoletes:	tinydns

%description tinydns
tinydns is a DNS server from the djbdns package. It accepts iterative
DNS queries from hosts around the Internet and responds with
locally-configured information.

%description tinydns -l de.UTF-8
tinydns ist ein DNS-Server aus dem djbdns-Paket. Es empfängt iterative
DNS-Fragen von dem Hosts aus allem Internet und antwortet mit den
lokal-konfigurierten Informationen.

%description tinydns -l pl.UTF-8
tinydns jest serwerem DNS z pakietu djbdns. Przyjmuje on iteracyjne
zapytania DNS od komputerów z całego Internetu i odpowiada przy użyciu
lokalnie skonfigurowanych informacji.

%package tinydns-notify
Summary:	DNS NOTIFY sending tool
Summary(pl.UTF-8):   Narzędzie do wysyłania komunikatów DNS NOTIFY
License:	Free to use
Group:		Networking/Daemons
URL:		http://www.sericyb.com.au/tinydns-notify
Requires:	%{name} = %{version}-%{release}
Requires:	perl-Net-DNS
Requires:	perl-modules
Obsoletes:	tinydns-notify

%description tinydns-notify
tinydns-notify is a tool written in Perl, which extracts zones and
their nameservers from tinydns-data files and sends DNS NOTIFY
requests to nameservers listed in notify-list file.

%description tinydns-notify -l pl.UTF-8
tinydns-notify jest napisanym w Perlu narzędziem, które czyta pliki
stref i odpowiadające im serwery nazw z plików tinydns-data, a
następnie wysyła żądania NOTIFY do serwerów wyspecyfikowanych w pliku
notify-list.

%package pickdns
Summary:	DJB's load-balancing DNS server
Summary(de.UTF-8):   DJBs Belastung ausgleichender DNS-Server
Summary(pl.UTF-8):   Serwer DNS równoważący obciążenie od DJB
Group:		Networking/Daemons
Requires(post):	diffutils
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(preun):	daemontools
Requires:	%{name} = %{version}-%{release}
Requires:	daemontools >= 0.70-5
Requires:	make
Provides:	user(pickdns)
Obsoletes:	pickdns

%description pickdns
pickdns is a DNS load-balancing server from the djbdns package. It
accepts iterative DNS queries from hosts around the Internet and
responds with a dynamic selection of locally configured IP addresses
with 5-second TTLs.

%description pickdns -l de.UTF-8
pickdns ist ein Belastung ausgleichender DNS-Server aus dem
djbdns-Paket. Es empfängt iterative DNS-Fragen von den Hosts aus allem
Internet und antwortet mit eine dynamische Auswahl von den
lokal-konfigurierten IP-Adressen mit 5-Sekunden-TTLs.

%description pickdns -l pl.UTF-8
pickdns jest równoważącym obciążenie serwerem DNS z pakietu djbdns.
Odbiera on iteracyjne zapytania DNS od komputerów z całego internetu i
odpowiada dynamicznym wyborem lokalnie skonfigurowanych adresów IP z
5-sekundowymi TTLami.

%package walldns
Summary:	DJB's reverse DNS wall
Summary(de.UTF-8):   DJBs Wand rückgekehrten DNSs
Summary(pl.UTF-8):   Ściana dla odwrotnych zapytań DNS od DJB
Group:		Networking/Daemons
Requires(post):	diffutils
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(preun):	daemontools
Requires:	%{name} = %{version}-%{release}
Requires:	daemontools >= 0.70-5
Provides:	user(walldns)
Obsoletes:	walldns

%description walldns
walldns is a reverse DNS wall from the djbdns package. It accepts
iterative DNS queries for in-addr.arpa domains from hosts around the
Internet and supplies generic responses that avoid revealing local
host information.

%description walldns -l de.UTF-8
walldns ist ein Wand rückgekehrten DNSs aus dem djbdns-Paket. Es
empfängt iterative DNS-Fragen für den in-addr.arpa-Domänen von den
Hosts aus allem Internet und liefert Antworte, die vermeiden
Informationen über die lokalen Hosts zu aufzudecken.

%description walldns -l pl.UTF-8
walldns jest ścianą dla odwrotnych zapytań DNS z pakietu djbdns.
Przyjmuje ona iteracyjne zapytania DNS dla domen in-addr.arpa od
komputerów z całego Internetu i dostarcza odpowiedzi, które unikają
ujawniania informacji o lokalnych komputerach.

%package rbldns
Summary:	DJB's IP-address-listing DNS server
Summary(de.UTF-8):   DJBs IP-Adressen-Listen-DNS-Server
Summary(pl.UTF-8):   Serwer DNS list adresów IP od DJB
Group:		Networking/Daemons
Requires(post):	diffutils
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(preun):	daemontools
Requires:	%{name} = %{version}-%{release}
Requires:	daemontools >= 0.70-5
Requires:	make
Provides:	user(rbldns)
Obsoletes:	rbldns
#Obsoletes:	rbldnsd

%description rbldns
rbldns is an IP-address-listing DNS server from the djbdns package. It
accepts iterative DNS queries from hosts around the Internet asking
about various IP addresses. It provides responses showing whether the
addresses are on a locally configured list, such as RBL or DUL.

%description rbldns -l de.UTF-8
rbldns ist ein IP-Adressen-Listen-DNS-Server aus dem djbdns-Paket. Es
empfängt iterative DNS-Fragen von den Hosts aus allem Internet
fragende nach verschiedene IP-Adresse. Es liefert Antworte, die zeugen
ob die Adresse sich auf einer lokal-konfigurierten Liste befinden, zum
Beispiel RBL oder DUL.

%description rbldns -l pl.UTF-8
rbldns jest serwerem DNS list adresów z pakietu djbdns. Przyjmuje on
iteracyjne zapytania DNS od komputerów z całego Internetu pytające o
różne adresy IP. Dostarcza on odpowiedzi pokazujących, czy adresy te
są na lokalnie skonfigurowanej liście takiej, jak RBL lub DUL.

%package axfrdns
Summary:	DJB's DNS zone-transfer server
Summary(de.UTF-8):   DJBs DNS-Zonen-Transfer-Server
Summary(pl.UTF-8):   Serwer transferów stref DNS od DJB
Group:		Networking/Daemons
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(preun):	daemontools
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-tinydns = %{version}-%{release}
Requires:	daemontools >= 0.70-5
Requires:	make
Requires:	ucspi-tcp
Provides:	user(axfrdns)
Obsoletes:	axfrdns

%description axfrdns
axfrdns is a DNS zone transfer server from the djbdns package. It
reads a zone-transfer request in DNS-over-TCP format from its standard
input and responds with locally configured information.

%description axfrdns -l de.UTF-8
axfrdns ist ein DNS-Zonen-Transfer-Server aus dem djbdns-Paket. Es
liest ein Zonen-Transfer-Ersuchen im DNS-over-TCP-Format von seinem
standarden Eingabe und antwortet mit den lokal-konfigurierten
Informationen.

%description axfrdns -l pl.UTF-8
axfrdns jest serwerem transferów stref DNS z pakietu djbdns. Wczytuje
on ze standardowego wejścia prośbę o transfer strefy w formacie
DNS-over-TCP i odpowiada przy użyciu lokalnie skonfigurowanych
informacji.

%prep
%setup -q -a1 -a2
install %{SOURCE3} .
install %{SOURCE4} .

%patch1 -p1
%patch0 -p1
%patch3 -p1
%patch4 -p1
%patch5
%patch6 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
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

install tinydns-notify	$RPM_BUILD_ROOT%{_bindir}
install tinydns-log		$RPM_BUILD_ROOT%{_bindir}

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

make_supervise_service() {
	%{?debug:set -x}
	local service="$1"
	local svcdir=$RPM_BUILD_ROOT%{_sysconfdir}/$service
	local logdir=$RPM_BUILD_ROOT/var/log/djbdns/$service

	install -d $svcdir/supervise $svcdir/log/supervise $logdir
	touch $logdir/{lock,state}

	touch $svcdir/log/supervise/{lock,status}
	mkfifo $svcdir/log/supervise/{control,ok}
	touch $svcdir/supervise/{lock,status}
	mkfifo $svcdir/supervise/{control,ok}
}

##### DNSCACHE #####
make_supervise_service dnscache
s=$RPM_BUILD_ROOT%{_sysconfdir}/dnscache
mkdir $s/env
echo %{_sysconfdir}/dnscache/root > $s/env/ROOT
echo 127.0.0.1                    > $s/env/IP
echo 0.0.0.0                      > $s/env/IPSEND
echo 1000000                      > $s/env/CACHESIZE
echo 3000000                      > $s/env/DATALIMIT
touch $s/env/IGNOREIP
cat>$s/run<<'EOF'
#!/bin/sh
exec 2>&1
exec <seed
exec envdir ./env sh -c '
  exec envuidgid dnscache softlimit -o250 -d "$DATALIMIT" %{_bindir}/dnscache
'
EOF
cat>$s/log/run<<'EOF'
#!/bin/sh
exec setuidgid dnslog multilog t /var/log/djbdns/dnscache
EOF
mkdir $s/root
mkdir $s/root/ip
touch $s/root/ip/127.0.0.1
mkdir $s/root/servers
ln $RPM_BUILD_ROOT%{_sysconfdir}/dnsroots.global $s/root/servers/@
dd if=/dev/zero of=$s/seed bs=128c count=1

##### TINYDNS #####
make_supervise_service tinydns
s=$RPM_BUILD_ROOT%{_sysconfdir}/tinydns
cat>$s/log/run<<EOF
#!/bin/sh
exec setuidgid dnslog multilog t /var/log/djbdns/tinydns
EOF
mkdir $s/env
echo %{_sysconfdir}/tinydns/root > $s/env/ROOT
echo 127.0.0.1                   > $s/env/IP
cat>$s/run<<EOF
#!/bin/sh
exec 2>&1
exec envuidgid tinydns envdir ./env softlimit -d300000 %{_bindir}/tinydns
EOF
mkdir $s/root
touch $s/root/data
cat>$s/root/add-ns<<'EOF'
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add ns ${1+"$@"}
EOF
cat>$s/root/add-childns<<'EOF'
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add childns ${1+"$@"}
EOF
cat>$s/root/add-host<<'EOF'
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add host ${1+"$@"}
EOF
cat>$s/root/add-host6<<'EOF'
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add host6 ${1+"$@"}
EOF
cat>$s/root/add-alias<<'EOF'
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add alias ${1+"$@"}
EOF
cat>$s/root/add-alias6<<'EOF'
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add alias6 ${1+"$@"}
EOF
cat>$s/root/add-mx<<'EOF'
#!/bin/sh
exec %{_bindir}/tinydns-edit data data.new add mx ${1+"$@"}
EOF
cat>$s/root/Makefile<<'EOF'
data.cdb: data
	%{_bindir}/tinydns-data
EOF

##### PICKDNS #####
make_supervise_service pickdns
s=$RPM_BUILD_ROOT%{_sysconfdir}/pickdns
cat>$s/log/run<<EOF
#!/bin/sh
exec setuidgid dnslog multilog t /var/log/djbdns/pickdns
EOF
mkdir $s/env
echo %{_sysconfdir}/pickdns/root > $s/env/ROOT
echo 127.0.0.1                   > $s/env/IP
cat>$s/run<<EOF
#!/bin/sh
exec 2>&1
exec envuidgid pickdns envdir ./env softlimit -d250000 %{_bindir}/pickdns
EOF
mkdir $s/root
touch $s/root/data
cat>$s/root/Makefile<<EOF
data.cdb: data
	%{_bindir}/pickdns-data
EOF

##### WALLDNS #####
make_supervise_service walldns
s=$RPM_BUILD_ROOT%{_sysconfdir}/walldns
cat>$s/log/run<<EOF
#!/bin/sh
exec setuidgid dnslog multilog t ./main
EOF
mkdir $s/env
echo %{_sysconfdir}/walldns/root > $s/env/ROOT
echo 127.0.0.1                   > $s/env/IP
cat>$s/run<<EOF
#!/bin/sh
exec 2>&1
exec envuidgid walldns envdir ./env softlimit -d250000 %{_bindir}/walldns
EOF
mkdir $s/root

##### RBLDNS #####
make_supervise_service rbldns
s=$RPM_BUILD_ROOT%{_sysconfdir}/rbldns
cat>$s/log/run<<EOF
#!/bin/sh
exec setuidgid dnslog multilog t /var/log/djbdns/rbldns
EOF
mkdir $s/env
echo %{_sysconfdir}/rbldns/root > $s/env/ROOT
echo 127.0.0.1                  > $s/env/IP
echo in-addr.arpa               > $s/env/BASE
cat>$s/run<<EOF
#!/bin/sh
exec 2>&1
exec envuidgid rbldns envdir ./env softlimit -d250000 %{_bindir}/rbldns
EOF
mkdir $s/root
touch $s/root/data
cat>$s/root/Makefile<<EOF
data.cdb: data
	%{_bindir}/rbldns-data
EOF
cat>$s/data<<EOF
# example
# !10.11.12.13:See http://bad.example.com
# :127.0.0.2:blacklisted"
# 1.2.3.0/24
EOF



##### AXFRDNS #####
make_supervise_service axfrdns
s=$RPM_BUILD_ROOT%{_sysconfdir}/axfrdns
cat>$s/log/run<<EOF
#!/bin/sh
exec setuidgid dnslog multilog t /var/log/djbdns/axfrdns
EOF
mkdir $s/env
echo %{_sysconfdir}/tinydns/root > $s/env/ROOT
echo 127.0.0.1                   > $s/env/IP
cat>$s/run<<'EOF'
#!/bin/sh
exec 2>&1
exec envdir ./env sh -c '
  exec envuidgid axfrdns softlimit -d300000 tcpserver -vDRHl0 -x tcp.cdb -- "$IP" 53 %{_bindir}/axfrdns
'
EOF
cat>$s/Makefile<<'EOF'
tcp.cdb: tcp
	tcprules tcp.cdb tcp.tmp < tcp
EOF
cat>$s/tcp<<'EOF'
# sample line:  1.2.3.4:allow,AXFR="heaven.af.mil/3.2.1.in-addr.arpa"
:deny
EOF

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
%groupadd -g 32 -r -f djbdns
%useradd -u 32 -r -d / -s /bin/false -c "djbdns User" -g djbdns dnslog

%postun
if [ "$1" = "0" ]; then
	%userremove dnslog
	%groupremove djbdns
fi

%pre dnscache
%useradd -P %{name}-dnscache -u 33 -r -d /etc/dnscache -s /bin/false -c "djbdns User" -g djbdns dnscache

%post dnscache
if [ ! -s %{_sysconfdir}/dnscache/seed ]; then
	dd if=/dev/urandom of=%{_sysconfdir}/dnscache/seed bs=128c count=1
fi
if diff -u %{_sysconfdir}/{dnscache,pickdns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and pickdns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/dnscache/env/IP"
	echo "or %{_sysconfdir}/pickdns/env/IP."
fi
if diff -u %{_sysconfdir}/{dnscache,rbldns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and rbldns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/dnscache/env/IP"
	echo "or %{_sysconfdir}/rbldns/env/IP."
fi
if diff -u %{_sysconfdir}/{dnscache,tinydns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and tinydns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/dnscache/env/IP"
	echo "or %{_sysconfdir}/tinydns/env/IP."
fi
if diff -u %{_sysconfdir}/{dnscache,walldns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and walldns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/dnscache/env/IP"
	echo "or %{_sysconfdir}/walldns/env/IP."
fi

if [ -f /service/dnscache/supervise/lock ]; then
	svc -t /service/dnscache{,/log}
fi

%preun dnscache
if [ "$1" = "0" ]; then
	# http://cr.yp.to/daemontools/faq/create.html#remove
	if [ -f /service/dnscache/supervise/lock ]; then
		cd /service/dnscache
		rm /service/dnscache
		svc -dx . log
	fi
fi

%postun dnscache
if [ "$1" = "0" ]; then
	%userremove dnscache
fi

%pre tinydns
%useradd -P %{name}-tinydns -u 34 -r -d /etc/tinydns -s /bin/false -c "djbdns User" -g djbdns tinydns

%post tinydns
if diff -u %{_sysconfdir}/{dnscache,tinydns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and tinydns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/dnscache/env/IP"
	echo "or %{_sysconfdir}/tinydns/env/IP."
fi
if diff -u %{_sysconfdir}/{pick,tiny}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: pickdns and tinydns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/pickdns/env/IP"
	echo "or %{_sysconfdir}/tinydns/env/IP."
fi
if diff -u %{_sysconfdir}/{rbl,tiny}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: rbldns and tinydns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/rbldns/env/IP"
	echo "or %{_sysconfdir}/tinydns/env/IP."
fi
if diff -u %{_sysconfdir}/{tiny,wall}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: tinydns and walldns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/tinydns/env/IP"
	echo "or %{_sysconfdir}/walldns/env/IP."
fi

if [ -f /service/tinydns/supervise/lock ]; then
	svc -t /service/tinydns{,/log}
fi

%preun tinydns
if [ "$1" = "0" ]; then
	# http://cr.yp.to/daemontools/faq/create.html#remove
	if [ -f /service/tinydns/supervise/lock ]; then
		cd /service/tinydns
		rm /service/tinydns
		svc -dx . log
	fi
fi

%postun tinydns
if [ "$1" = "0" ]; then
	%userremove tinydns
fi

%pre pickdns
%useradd -P %{name}-pickdns -u 35 -r -d /etc/pickdns -s /bin/false -c "djbdns User" -g djbdns pickdns

%post pickdns
if diff -u %{_sysconfdir}/{dnscache,pickdns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and pickdns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/dnscache/env/IP"
	echo "or %{_sysconfdir}/pickdns/env/IP."
fi
if diff -u %{_sysconfdir}/{pick,rbl}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: pickdns and rbldns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/pickdns/env/IP"
	echo "or %{_sysconfdir}/rbldns/env/IP."
fi
if diff -u %{_sysconfdir}/{pick,tiny}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: pickdns and tinydns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/pickdns/env/IP"
	echo "or %{_sysconfdir}/tinydns/env/IP."
fi
if diff -u %{_sysconfdir}/{pick,wall}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: pickdns and walldns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/pickdns/env/IP"
	echo "or %{_sysconfdir}/walldns/env/IP."
fi

if [ -f /service/pickdns/supervise/lock ]; then
	svc -t /service/pickdns{,/log}
fi

%preun pickdns
if [ "$1" = "0" ]; then
	# http://cr.yp.to/daemontools/faq/create.html#remove
	if [ -f /service/pickdns/supervise/lock ]; then
		cd /service/pickdns
		rm /service/pickdns
		svc -dx . log
	fi
fi

%postun pickdns
if [ "$1" = "0" ]; then
	%userremove pickdns
fi

%pre walldns
%useradd -P %{name}-walldns -u 36 -r -d /etc/walldns -s /bin/false -c "djbdns User" -g djbdns walldns

%post walldns
if diff -u %{_sysconfdir}/{dnscache,walldns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and walldns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/dnscache/env/IP"
	echo "or %{_sysconfdir}/walldns/env/IP."
fi
if diff -u %{_sysconfdir}/{pick,wall}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: pickdns and walldns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/pickdns/env/IP"
	echo "or %{_sysconfdir}/walldns/env/IP."
fi
if diff -u %{_sysconfdir}/{rbl,wall}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: rbldns and walldns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/rbldns/env/IP"
	echo "or %{_sysconfdir}/walldns/env/IP."
fi
if diff -u %{_sysconfdir}/{tiny,wall}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: tinydns and walldns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/tinydns/env/IP"
	echo "or %{_sysconfdir}/walldns/env/IP."
fi

if [ -f /service/walldns/supervise/lock ]; then
	svc -t /service/walldns{,/log}
fi

%preun walldns
if [ "$1" = "0" ]; then
	# http://cr.yp.to/daemontools/faq/create.html#remove
	if [ -f /service/walldns/supervise/lock ]; then
		cd /service/walldns
		rm /service/walldns
		svc -dx . log
	fi
fi

%postun walldns
if [ "$1" = "0" ]; then
	%userremove walldns
fi

%pre rbldns
%useradd -P %{name}-rbldns -u 37 -r -d /etc/rbldns -s /bin/false -c "djbdns User" -g djbdns rbldns

%post rbldns
if diff -u %{_sysconfdir}/{dnscache,rbldns}/env/IP >/dev/zero 2>&1;then
	echo "Warning: dnscache and rbldns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/dnscache/env/IP"
	echo "or %{_sysconfdir}/rbldns/env/IP."
fi
if diff -u %{_sysconfdir}/{pick,rbl}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: pickdns and rbldns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/pickdns/env/IP"
	echo "or %{_sysconfdir}/rbldns/env/IP."
fi
if diff -u %{_sysconfdir}/{rbl,tiny}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: rbldns and tinydns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/rbldns/env/IP"
	echo "or %{_sysconfdir}/tinydns/env/IP."
fi
if diff -u %{_sysconfdir}/{rbl,wall}dns/env/IP >/dev/zero 2>&1;then
	echo "Warning: rbldns and walldns can't work on the same"
	echo "IP address. You have to edit either %{_sysconfdir}/rbldns/env/IP"
	echo "or %{_sysconfdir}/walldns/env/IP."
fi

if [ -f /service/rbldns/supervise/lock ]; then
	svc -t /service/rbldns{,/log}
fi

%preun rbldns
if [ "$1" = "0" ]; then
	# http://cr.yp.to/daemontools/faq/create.html#remove
	if [ -f /service/rbldns/supervise/lock ]; then
		cd /service/rbldns
		rm /service/rbldns
		svc -dx . log
	fi
fi

%postun rbldns
if [ "$1" = "0" ]; then
	%userremove rbldns
fi

%pre axfrdns
%useradd -P %{name}-axfrdns -u 38 -r -d /etc/axfrdns -s /bin/false -c "djbdns User" -g djbdns axfrdns

%preun axfrdns
if [ "$1" = "0" ]; then
	# http://cr.yp.to/daemontools/faq/create.html#remove
	if [ -f /service/axfrdns/supervise/lock ]; then
		cd /service/axfrdns
		rm /service/axfrdns
		svc -dx . log
	fi
fi

%postun axfrdns
if [ "$1" = "0" ]; then
	%userremove axfrdns
fi

%files
%defattr(644,root,root,755)
%doc CHANGES TODO MULTIPLEIP TINYDNS doc/*
%attr(755,root,root) %{_bindir}/cachetest
%attr(755,root,root) %{_bindir}/dns[f-t]*
%attr(755,root,root) %{_bindir}/axfr-get
%{_mandir}/man[15]/*
%{_mandir}/man8/axfr-get*
%dir %attr(751,root,root) %dir /var/log/djbdns

%files dnscache
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dnscache*
%config %{_sysconfdir}/dnsroots.global
%dir %attr(1755,root,root) %{_sysconfdir}/dnscache
%attr(700,root,root) %dir %{_sysconfdir}/dnscache/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/dnscache/supervise/*

%dir %attr(1755,root,root) %{_sysconfdir}/dnscache/log
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dnscache/log/run
%attr(700,root,root) %dir %{_sysconfdir}/dnscache/log/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/dnscache/log/supervise/*
%attr(751,dnslog,djbdns) %dir /var/log/djbdns/dnscache
%attr(600,dnslog,djbdns) %ghost /var/log/djbdns/dnscache/lock
%attr(640,dnslog,djbdns) %ghost /var/log/djbdns/dnscache/state

%dir %attr(2755,root,root) %{_sysconfdir}/dnscache/env
%config %{_sysconfdir}/dnscache/env/*
%attr(755,root,root) %{_sysconfdir}/dnscache/run
%dir %{_sysconfdir}/dnscache/root
%dir %{_sysconfdir}/dnscache/root/ip
%dir %{_sysconfdir}/dnscache/root/servers
%config %attr(600,root,root) %{_sysconfdir}/dnscache/root/ip/*
%config %{_sysconfdir}/dnscache/root/servers/*
%ghost %attr(600,root,root) %{_sysconfdir}/dnscache/seed
%{_mandir}/man8/dnscache*
/service/dnscache

%files tinydns
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tinydns*
%dir %attr(3755,root,root) %{_sysconfdir}/tinydns
%attr(700,root,root) %dir %{_sysconfdir}/tinydns/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/tinydns/supervise/*

%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tinydns/log/run
%dir %attr(1755,root,root) %{_sysconfdir}/tinydns/log
%attr(700,root,root) %dir %{_sysconfdir}/tinydns/log/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/tinydns/log/supervise/*
%attr(751,dnslog,djbdns) %dir /var/log/djbdns/tinydns
%attr(600,dnslog,djbdns) %ghost /var/log/djbdns/tinydns/lock
%attr(640,dnslog,djbdns) %ghost /var/log/djbdns/tinydns/state

%dir %attr(2755,root,root) %{_sysconfdir}/tinydns/env
%config %{_sysconfdir}/tinydns/env/*
%attr(755,root,root) %{_sysconfdir}/tinydns/run
%dir %attr(2755,root,root) %{_sysconfdir}/tinydns/root
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tinydns/root/Makefile
%config %{_sysconfdir}/tinydns/root/data
%attr(755,root,root) %{_sysconfdir}/tinydns/root/add-*
%{_mandir}/man8/tinydns*
/service/tinydns

%files tinydns-notify
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tinydns-notify

%files pickdns
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pickdns*
%dir %attr(3755,root,root) %{_sysconfdir}/pickdns
%attr(700,root,root) %dir %{_sysconfdir}/pickdns/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/pickdns/supervise/*

%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pickdns/log/run
%dir %attr(1755,root,root) %{_sysconfdir}/pickdns/log
%attr(700,root,root) %dir %{_sysconfdir}/pickdns/log/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/pickdns/log/supervise/*
%attr(751,dnslog,djbdns) %dir /var/log/djbdns/pickdns
%attr(600,dnslog,djbdns) %ghost /var/log/djbdns/pickdns/lock
%attr(640,dnslog,djbdns) %ghost /var/log/djbdns/pickdns/state

%dir %attr(2755,root,root) %{_sysconfdir}/pickdns/env
%config %{_sysconfdir}/pickdns/env/*
%attr(755,root,root) %{_sysconfdir}/pickdns/run
%dir %attr(2755,root,root) %{_sysconfdir}/pickdns/root
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/pickdns/root/Makefile
%config %{_sysconfdir}/pickdns/root/data
%{_mandir}/man8/pickdns*
/service/pickdns

%files walldns
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/walldns*
%dir %attr(3755,root,root) %{_sysconfdir}/walldns
%attr(700,root,root) %dir %{_sysconfdir}/walldns/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/walldns/supervise/*

%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/walldns/log/run
%dir %attr(1755,root,root) %{_sysconfdir}/walldns/log
%attr(700,root,root) %dir %{_sysconfdir}/walldns/log/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/walldns/log/supervise/*
%attr(751,dnslog,djbdns) %dir /var/log/djbdns/walldns
%attr(600,dnslog,djbdns) %ghost /var/log/djbdns/walldns/lock
%attr(640,dnslog,djbdns) %ghost /var/log/djbdns/walldns/state

%dir %attr(2755,root,root) %{_sysconfdir}/walldns/env
%config %{_sysconfdir}/walldns/env/*
%attr(755,root,root) %{_sysconfdir}/walldns/run
%dir %attr(2755,root,root) %{_sysconfdir}/walldns/root
%{_mandir}/man8/walldns*
/service/walldns

%files rbldns
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rbldns*
%dir %attr(3755,root,root) %{_sysconfdir}/rbldns
%attr(700,root,root) %dir %{_sysconfdir}/rbldns/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/rbldns/supervise/*

%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rbldns/log/run
%dir %attr(1755,root,root) %{_sysconfdir}/rbldns/log
%attr(700,root,root) %dir %{_sysconfdir}/rbldns/log/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/rbldns/log/supervise/*
%attr(751,dnslog,djbdns) %dir /var/log/djbdns/rbldns
%attr(600,dnslog,djbdns) %ghost /var/log/djbdns/rbldns/lock
%attr(640,dnslog,djbdns) %ghost /var/log/djbdns/rbldns/state

%dir %attr(2755,root,root) %{_sysconfdir}/rbldns/env
%config %{_sysconfdir}/rbldns/env/*
%attr(755,root,root) %{_sysconfdir}/rbldns/run
%dir %attr(2755,root,root) %{_sysconfdir}/rbldns/root
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rbldns/root/Makefile
%config %{_sysconfdir}/rbldns/root/data
%{_mandir}/man8/rbldns*
/service/rbldns

%files axfrdns
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/axfrdns*
%dir %attr(3755,root,root) %{_sysconfdir}/axfrdns
%attr(700,root,root) %dir %{_sysconfdir}/axfrdns/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/axfrdns/supervise/*

%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/axfrdns/log/run
%dir %attr(1755,root,root) %{_sysconfdir}/axfrdns/log
%attr(700,root,root) %dir %{_sysconfdir}/axfrdns/log/supervise
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %ghost %{_sysconfdir}/axfrdns/log/supervise/*
%attr(751,dnslog,djbdns) %dir /var/log/djbdns/axfrdns
%attr(600,dnslog,djbdns) %ghost /var/log/djbdns/axfrdns/lock
%attr(640,dnslog,djbdns) %ghost /var/log/djbdns/axfrdns/state

%dir %attr(2755,root,root) %{_sysconfdir}/axfrdns/env
%config %{_sysconfdir}/axfrdns/env/*
%attr(755,root,root) %{_sysconfdir}/axfrdns/run
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/axfrdns/Makefile
%config %{_sysconfdir}/axfrdns/tcp
%{_mandir}/man8/axfrdns*
/service/axfrdns
