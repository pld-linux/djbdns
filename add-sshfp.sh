#!/bin/sh
# Script to convert SSHFP Bind format records to djbdns tinydns.
#
# Author: Elan Ruusamäe <glen@pld-linux.org>
#
# Inspired from Perl version
# http://dank.qemfd.net/dankwiki/index.php/SSHFP

# convert decimal to octal
dec2oct() {
	echo "ibase=10; obase=8; $1" | bc -l
}

# convert hex to octal
hex2oct() {
	# bc wants uppercase hex
	local i=$(echo "$1" | tr [a-f] [A-F])
	echo "ibase=16; obase=8; $i" | bc -l
}

hostalias=$1
ssh-keygen -f /etc/ssh/ssh_host_rsa_key.pub -r $hostalias | \
while read host in sshfp alg fptype fp; do
	out="\\"$(printf "%03d" $(dec2oct $alg))
	out=$out"\\"$(printf "%03d" $(dec2oct $fptype))

	while [ "$fp" ]; do
		# temp chop off two bytes
		t=${fp#??}
		# take the bytes
		ch=${fp%$t}
		out=$out"\\"$(printf "%03d" $(hex2oct $ch))
		# continue fp
		fp=$t
	done
	printf ":%s:44:%s:\n" $host $out
done
