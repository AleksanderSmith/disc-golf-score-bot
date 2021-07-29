import os
from watchdog.events import RegexMatchingEventHandler
import ScoreReader
# import CourseInfo
# import Score
# from ScoreUtils import ScoreUtils

class FileEventHandler(RegexMatchingEventHandler):
  CSV_REGEX = [r".*[^_filename]\.csv$"]

  def __init__(self):
    super().__init__(self.CSV_REGEX)

  def on_created(self, event):
    self.process(event)

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
        
  def process(self, event):
    # Open and read new file:
    filename, ext = os.path.splitext(event.src_path)
    header, course_info, score_data = self.read_scores()

    #extract data from file
    course = CourseInfo.CourseInfo(course_info)
    scores = sorted(ScoreUtils.Convert_data_to_score(score_data))
    
    # insert scores into db
    DbHandler.Insert scores
    


filepath

self.workbook = load_workbook(filename=self.filename)

# Iterate directory
for _, dirs, files in os.walk(filepath)


# Read scores
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

# Write scores to Excel

self.workbook.save(self.filename)
