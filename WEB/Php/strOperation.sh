use strict;
use warnings;

my $str = "hello world";
print "Original string: $str\n";

my $len = length($str);
print "Length of string: $len\n";


my $lc = lc($str);  
print "Lowercased: $lc\n";

my $replaced = $str;
$replaced =~ s/hello/hi/g;  
print "Replaced: $replaced\n";

my @word = split(/\s+/, $str); 
print "Words in string: @word\n";

my $joined = join(",", @word);  
print "Joined string with commas: $joined\n";
