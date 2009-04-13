#!/usr/bin/perl
#
# Generate test block
#

print "test {\n";
print "# image file\t\t\toutput file\n";
foreach $yuv (@ARGV) {
	if ($yuv =~ m<^\.\./(\w+)/(\w+)/.*$>) {
		$result = "Results/$1$2.ppm";
	}
	print "\"$yuv\"\t\"$result\"\n";
}
print "}\n";
