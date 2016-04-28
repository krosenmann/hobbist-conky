#!/usr/bin/perl -w
use strict;
use warnings;
use LWP::Simple;
use HTML::TableExtract;
use Text::Table;

my $page = get(""); #add here link to your dotabuff page
my $headers = ['Type', 'Matches', 'Win Rate'];
my $extracter = HTML::TableExtract->new(headers => $headers);
my $stats_output = Text::Table->new(@$headers);

$extracter->parse($page);
my ($stats) = $extracter->tables;

for my $row ($stats->rows) {
    $stats_output->load($row); }
print($stats_output);
#open(STATS, '>stats');
#print(STATS "$stats_output");
#close(STATS);
