"""This function returns the average of the provided scores."""
def average_scores(scores):
  total = 0
  for score in scores:
    total += score
  return total/len(scores)

avg1 = average_scores([10, 20]) # 15.0
avg2 = average_scores([90, 80, 70]) # 80.0
avg3 = average_scores([8.9, 7.2]) # 8.05