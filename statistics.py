
def calculateStats(numbers):
  # implement the computation of statistics here and return the results
  if numbers:
      stats["avg"] = sum(numbers)/len(numbers)
      stats["Max"] = max(numbers)
      stats["min"] = min(numbers)
  else:
      stats["avg"] = float(numbers)/len(numbers)
      stats["Max"] = float(numbers)
      stats["min"] = float(numbers)
  return stats
