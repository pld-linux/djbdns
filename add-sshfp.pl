#!/usr/bin/perl

use strict;

open IN, "ssh-keygen -f /etc/ssh/ssh_host_rsa_key.pub -r $ARGV[0] |";
my $FP = <IN>;
close IN;
chop $FP;
my ($host, $in, $sshfp, $alg, $fptype, $fp) = split " ", $FP;
my $out = sprintf("\\%03o\\%03o", $alg, $fptype);
for (my $i = 0; $i < length($fp); $i += 2) {
	$out .= sprintf("\\%03o", hex substr($fp, $i, 2));
}
printf(":%s:44:%s:\n", $host, $out);
