#! /usr/bin/env python
import csv

def read_cross_section(filename, width, sigma):
    with open(filename, 'r') as csvfile:
        cross_reader = csv.DictReader(csvfile, delimiter='\t') #csv.reader(csvfile, delimiter=' ')
        cross_reader = filter(lambda x: x['Gamma/MQ(%)']==width, cross_reader)
        keys = {'MQ',sigma}
        result = []
        #print cross_reader
        for row in cross_reader:
            result.append({'MQ':row['MQ'],'sigma':row[sigma]})

        print result
        return result


if __name__ == "__main__":
    print read_cross_section('SingleX/CrossSections_SingleX_bW_b_FW.txt','1','sigma(bW_bj)(fb)')
    
