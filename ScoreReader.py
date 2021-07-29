import csv
from Score import Score
import CourseInfo

class ScoreReader():
  def __init__(self, filename):
      self.filename = filename
      
  def read_scores(self):
    header = []
    course_info = []
    data = []
    if self.filename is not None:
      with open(self.filename, "r") as infile:
        reader = csv.reader(infile)
        header = next(reader)
        course_info = next(reader)
        try:
          data = list(reader)
          return header, course_info, data
        except Exception as e:
          print(e)
