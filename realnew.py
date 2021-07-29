import os
import csv
from openpyxl import Workbook

# filename = "C:\\scores\\scores.xlsx"
# filepath = "C:\\scores\\"

filepath = "E:\\dev\\python\\dg\\maraton\\scorecards\\"
filename = "E:\\dev\\python\\dg\\maraton\\realnew.xlsx"
# def printPlayerScore(score, sheet, index):
#   sheet[f'A{index}'] = score[0]
#   sheet[f'B{index}'] = score[1]
#   sheet[f'C{index}'] = score[2]
  
def read_scores(filename):
  data = []
  if filename is not None:
    with open(filename, "r") as infile:
      reader = csv.reader(infile)
      _ = next(reader) # Discard header
      _ = next(reader) # Discard course info
      try:
        data = list(reader)
        return data
      except Exception as e:
        print(e)

def getScoresFromFiles(filepath):
  data = []
  for root, dirs, files in os.walk(filepath):
    for name in files:
      cur_path = os.path.join(root, name)
      print(name)
      print('\n')
      data.append(read_scores(cur_path))

def printScores(scores):
  for entry in scores:
    print(entry)
    print('\n')
  

data = getScoresFromFiles(filepath)
printScores(data)

# workbook = Workbook(filename=filename)
# ws = workbook.active

# workbook.save(filename)
