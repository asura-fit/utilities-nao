#!/usr/bin/perl
#
# Generate train block
#

open(IN, "ignorelist.txt");
while (<IN>) {
    push(@ignoreList, $_);
}
close(IN);


print "train{\n";
print "# image file\t\t\tlabel file\n";
foreach $label (@ARGV) {
	foreach $ignorepattern (@ignoreList) {
		if (0 <= index($label, $ignorepattern)) {
			print STDERR "# IGNORE $label. MatchPattern ``$ignorepattern''\n";
			$label = null;
			break;
		}
	}
	if ($label) {
		if ($label =~ m<^(.+/)label.ppm>) {
			$yuv = "$1imageyuv.ppm";
			print "\"$yuv\"\t\"$label\"\n";
		}
	}
}
print "}\n";
