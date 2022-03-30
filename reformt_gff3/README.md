# Gff file manipulation
Some existing genome annotation files (Gff3) need to the description field to the column 9 after the blast process.

## Dependencies
In order to reformat the gff3 file, the [gffutils](https://pythonhosted.org/gffutils/index.html) python library needs to be installed.

## Installation
The gffutils is tested with Python 2.7 and Python 3.3. 

```

pip install gffutils

```

## Usage

1. Example file ( gff3 format )
2. Gene Description file ( tabular format)
3. gff3_db.py - Prepare gffutils database using gff3 file for query ( gffutils db format)
4. gff3_handler.py - Append description(note) to the existing gff3 file ( gff3 format )

### Example File

```

gbr_scaffold1   .       mRNA    7181    18854   .       -       .       ID=gbr.1.1.t1;Parent=gbr.1.1
gbr_scaffold1   .       three_prime_UTR 7181    8157    .       -       .       ID=gbr.1.1.t1.utr3p1;Parent=gbr.1.1.t1
gbr_scaffold1   .       exon    7181    8397    .       -       .       ID=gbr.1.1.t1.exon10;Parent=gbr.1.1.t1
gbr_scaffold1   .       CDS     8158    8397    .       -       0       ID=cds.gbr.1.1.t1;Parent=gbr.1.1.t1
gbr_scaffold1   .       CDS     10089   10234   .       -       2       ID=cds.gbr.1.1.t1;Parent=gbr.1.1.t1
gbr_scaffold1   .       exon    10089   10234   .       -       .       ID=gbr.1.1.t1.exon9;Parent=gbr.1.1.t1
gbr_scaffold1   .       CDS     10760   10954   .       -       2       ID=cds.gbr.1.1.t1;Parent=gbr.1.1.t1
gbr_scaffold1   .       exon    10760   10954   .       -       .       ID=gbr.1.1.t1.exon8;Parent=gbr.1.1.t1
gbr_scaffold1   .       CDS     11318   11457   .       -       1       ID=cds.gbr.1.1.t1;Parent=gbr.1.1.t1
gbr_scaffold1   .       exon    11318   11457   .       -       .       ID=gbr.1.1.t1.exon7;Parent=gbr.1.1.t1
gbr_scaffold1   .       CDS     12155   12261   .       -       0       ID=cds.gbr.1.1.t1;Parent=gbr.1.1.t1
gbr_scaffold1   .       exon    12155   12261   .       -       .       ID=gbr.1.1.t1.exon6;Parent=gbr.1.1.t1
gbr_scaffold1   .       CDS     13918   14043   .       -       0       ID=cds.gbr.1.1.t1;Parent=gbr.1.1.t1
gbr_scaffold1   .       exon    13918   14043   .       -       .       ID=gbr.1.1.t1.exon5;Parent=gbr.1.1.t1
gbr_scaffold1   .       CDS     14954   15096   .       -       2       ID=cds.gbr.1.1.t1;Parent=gbr.1.1.t1
gbr_scaffold1   .       exon    14954   15096   .       -       .       ID=gbr.1.1.t1.exon4;Parent=gbr.1.1.t1
gbr_scaffold1   .       CDS     15772   16024   .       -       0       ID=cds.gbr.1.1.t1;Parent=gbr.1.1.t1
gbr_scaffold1   .       exon    15772   16024   .       -       .       ID=gbr.1.1.t1.exon3;Parent=gbr.1.1.t1
gbr_scaffold1   .       CDS     16298   16825   .       -       0       ID=cds.gbr.1.1.t1;Parent=gbr.1.1.t1
gbr_scaffold1   .       exon    16298   16865   .       -       .       ID=gbr.1.1.t1.exon2;Parent=gbr.1.1.t1
gbr_scaffold1   .       exon    18680   18854   .       -       .       ID=gbr.1.1.t1.exon1;Parent=gbr.1.1.t1
gbr_scaffold1   .       five_prime_UTR  18680   18854   .       -       .       ID=gbr.1.1.t1.utr5p1;Parent=gbr.1.1.t1

```

### Gene Description File

```

Gene ID Description
gbr.1.1.t1      ATP-dependent DNA helicase PIF1

```

### Prepare gffutils database
This script takes the gff3 file as input and generate a database file ends with ".db" suffix.

```
python3 gff3_db.py

```

### Append the description to the existing gff3 file

```

python3 gff3_handler.py > gene_with_description.gff3


```



