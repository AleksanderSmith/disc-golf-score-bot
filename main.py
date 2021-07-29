from openpyxl import Workbook, load_workbook
from ScoreWatcher import ScoreWatcher


scorefileName = "dgtour_2021_scores.xlsx"
dropboxPath = "E:\\Dropbox\\Dropbox\\discgolf\\dg_maraton\\round-1"
scorePath = r'E:\\dev\\python\\dg\\ScoreCardExtractor\\scorecards\\snake.csv'
ScoreWatcher(dropboxPath).run()


    
  
