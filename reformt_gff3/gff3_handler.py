#!/usr/bin/python3
import click
import gffutils
import gffutils.gffwriter as gffwriter
import csv
import re


def createDict(input_file):
    d={}
    with open(input_file) as fin:
        for row in csv.reader(fin, delimiter='\t'):
            d[row[0]] = row[1:]
    return d

def findNote(gff3_id,dict_note):
    try:
        tmp_str1=str(dict_note[gff3_id])[1:-1]
        tmp_str1=tmp_str1.replace('\'','')
        return tmp_str1
    except KeyError:
        return

def findNote_utr3p1(gff3_id,dict_note):
    try:
        stripUTR3p1 = re.sub('.utr3p1','',gff3_id)
        stripUTR3p1 = stripUTR3p1.replace('\'','')
        tmp_str3=str(dict_note[stripUTR3p1])[1:-1]
        tmp_str3=tmp_str3.replace('\'','')
        return tmp_str3
    except KeyError:
        return


def findNote_utr5p1(gff3_id,dict_note):
    try:
        stripUTR5p1 = re.sub('.utr5p1','',gff3_id)
        stripUTR5p1 = stripUTR5p1.replace('\'','')
        tmp_str3=str(dict_note[stripUTR5p1])[1:-1]
        tmp_str3=tmp_str3.replace('\'','')
        return tmp_str3
    except KeyError:
        return

def findNote_exon(gff3_id,dict_note):
    try:
        stripExon = re.sub('.exon[0-9]+','',gff3_id)
        stripExon = stripExon.replace('\'','')
        tmp_str3=str(dict_note[stripExon])[1:-1]
        tmp_str3=tmp_str3.replace('\'','')
        return tmp_str3
    except KeyError:
        return

def findNote_CDS(gff3_id,dict_note):
    try:
        stripCDS = gff3_id.replace("cds.","")
        stripCDS = re.sub('_[0-9]+','',stripCDS)
        tmp_str2=str(dict_note[stripCDS])[1:-1]
        tmp_str2=tmp_str2.replace('\'','')
        return tmp_str2
    except KeyError:
        return

def findNote_gene(gff3_id,dict_note):
    try:
        # add .t1 to the suffix of gff3_id
        gff3_id = '.'.join([gff3_id,'t1'])
        return str(dict_note[gff3_id])[1:-1]
    except KeyError:
        return

def checkFeatureType(type_in):
    if type_in == "CDS":
       print("It is CDS")
    elif type_in == "mRNA":
       print("It is mRNA")
    elif type_in == "exon":
       print("It is exon")
    elif type_in == "five_prime_UTR":
       print("It is five_prime_UTR")
    elif type_in == "three_prime_UTR":
       print("It is three_prime_UTR")
    else:
       print("Unknown feature type.")


#remove NA record from the description file
#grep -v "\---NA---" description.txt > description_rm.txt
mydict=createDict('test-data/description.txt')

db = gffutils.FeatureDB('test-data/example.db', keep_order=True)

suffix="t1"
suffix_exon="exon"

# python gff3_handler.py > new_annotation.gff3
count=0

for feature in db.all_features():
    tmp=feature.id
    if not tmp.endswith(suffix) and not bool(re.search('exon[0-9]?',tmp)) and not bool(re.search('cds.',tmp)) and not bool(re.search('utr5p1',tmp)) and not bool(re.search('utr3p1',tmp)):
       note=findNote_gene(tmp,mydict)
       feature['Note'] = str(note)
       print(feature)
    else:
       if feature.featuretype == 'CDS':
          note=findNote_CDS(tmp,mydict)
          feature['Note'] = str(note)
          print(feature)
       elif feature.featuretype == 'exon':
          note=findNote_exon(tmp,mydict)
          feature['Note'] = str(note)
          print(feature)
       elif feature.featuretype == 'five_prime_UTR':
          note=findNote_utr5p1(tmp,mydict)
          feature['Note'] = str(note)
          print(feature)
       elif feature.featuretype == 'three_prime_UTR':
          note=findNote_utr3p1(tmp,mydict)
          feature['Note'] = str(note)
          print(feature)
       else:
          note=findNote(tmp,mydict)
          feature['Note'] = str(note)
          print(feature)
    count+=1
quit()

for gene in db.features_of_type('gene', order_by='start'):
    print(gene)
    for i in db.children(gene, featuretype='mRNA', order_by='start'):
        print(i)
        print(i.id)
        print(i.attributes)
