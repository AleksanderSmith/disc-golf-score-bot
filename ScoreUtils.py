import Score
class ScoreUtils():
  # Score utility functions
  def Convert_data_to_score(data):
    scores = []
    try:
      for row in data:
        score = Score.Score(row)
        scores.append(score)
    except Exception as e:
      print(e)
    
    return scores