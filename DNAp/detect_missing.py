import csv, os, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
miss = open("Missing_bases.csv", 'w+')
for f in os.listdir(os.getcwd()):
  if '.out' in f:
    wr = csv.writer(miss , delimiter = ',', quoting = csv.QUOTE_ALL) ##writing header
    wr.writerow(["ID", "Base Number", "Missing Base(s)", "Other Details"])
    fil = open(f, 'r+')
    x = 523
    for i,j in enumerate(fil.read().split('****************************************************************************')[5].split('\n')[4:-1]):
      m = re.search(r"(\d+)_\W+\w+\](\w).*\)(\D+)", j)
      elif(int(m.group(1))-x!=1):
        wr.writerow([f[:-4], m.group(1)-1,])
        x+=1
      x+=1
    fil.close()
miss.close()
