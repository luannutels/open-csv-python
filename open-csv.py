import csv  
with open("file.csv") as file:
  content = csv.reader(file)
  for row in content:
    print(row)
    
    ['index', 'key', 'value']
    ['1', 'a', 'data']
    ['2', 'b', 'Hi']