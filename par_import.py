#!usr/bin/python
import csv, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for f in os.listdir(os.getcwd()):
  if ".par" in f:
    bp = open("%s_parameters.csv"%f[:-4], 'w+')
    wr = csv.writer( bp, delimiter = ',', quoting = csv.QUOTE_ALL) ##writing header
    ip = open(f, 'r+')
    par = ip.read().split('\n')
    wr.writerow(filter(None,par[2].split(' ')))
    if ((par[6].split(' ')[0].split('-')[0] == 'G') && (par[7].split(' ')[0].split('-')[0] == 'A') &&(par[8].split(' ')[0].split('-')[0] == 'A') && \
         (par[9].split(' ')[0].split('-')[0] == 'T') && (par[10].split(' ')[0].split('-')[0] == 'T') && (par[11].split(' ')[0].split('-')[0] == 'C')):
       for j in range(6,12):
	wr.writerow(filter(None, par[j].split(' ')))
    else:
      print f
    bp.close()
    ip.close()
