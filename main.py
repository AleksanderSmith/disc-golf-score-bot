from ScoreReader import ScoreReader
from ScoreUtils import ScoreUtils
from CourseInfo import CourseInfo
  
# Open and read new file:
filename = "E:\\dev\\python\\dg\\maraton\\scorecards\\snake.csv"
reader = ScoreReader(filename)
header, course_info, score_data = reader.read_scores()

# Extract data from file
course = CourseInfo(course_info)
scores = sorted(ScoreUtils.Convert_data_to_score(score_data))

print(scores)

# Insert scores into db
# DbHandler.Insert scores
