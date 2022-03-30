#!/usr/bin/python3
import click
import gffutils
import gffutils.gffwriter as gffwriter
import csv
import re


db = gffutils.create_db('example.gff3', dbfn='example.db',force=True,keep_order=True,merge_strategy='merge',sort_attribute_values=True)

