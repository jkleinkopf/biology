#!/usr/bin/perl -w 

#usage: Move this script into the directory containing all the fasta files you want to convert into nexus, and make sure terminal is in this same directory. Change permissions to this script if needed (ie, "chmod +x fasta2nexusLoop.pl"). Finally, run the script by simply typing "fasta2nexusLoop.pl" in the command line. All fasta files in the directory will be converted to nexus, and will be the original name plus ".nexus" at the end (ie, "CL24.fasta" becomes "CL24.fasta.nexus")


#modified from josephhughes, https://github.com/josephhughes/Sequence-manipulation/blob/master/Fasta2Nexus.pl

use Bio::AlignIO;
#Bioperl for format conversions

@files = <*.fasta>;
foreach $file (@files) {
	$infile=$file;
	$output=$file.".nexus";

	#$infile=$ARGV[0];
	#$output=$ARGV[1];
	print "$infile\n$output\n";

	#open (MYFILE, "$infile" ) || die;
	#open (DATA, ">$output" )  ||die;

	use Bio::AlignIO;
	$in  = Bio::AlignIO->new(-file => "$infile" , '-format' => 'fasta');
	$out = Bio::AlignIO->new(-file => ">$output" , '-format' => 'nexus');
    	# note: we quote -format to keep older perls from complaining.

	while ( my $aln = $in->next_aln() ) {
    	$aln->uppercase();
    	$out->write_aln($aln);
	}
}
