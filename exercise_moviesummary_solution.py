"""
This function accepts a single parameter, a dictionary with the following keys:
* title (a string)
* duration (a number)
* actors (list of strings)
It then returns a string of the form:
"<title> lasts for <duration> minutes. Stars: <actor, actor>"
"""
def movie_summary(movie):
  return movie["title"] + " lasts for " + str(movie["duration"]) + " minutes. Stars: " + ", ".join(movie["actors"])
  # Alternative using f-strings:
  # return f"{movie['title']} lasts for {movie['duration']} minutes. Stars: {', '.join(movie['actors'])}"


puff = {
    "title": "Puff the Magic Dragon",
    "duration": 30,
    "actors": ["Puff", "Jackie", "Living Sneezes"]
}
# This should store "Puff the Magic Dragon lasts for 30 minutes. Stars: Puff, Jackie, Living Sneezes."
summary1 = movie_summary(puff)

arrival = {
  "title": "Arrival",
  "duration": "118",
  "actors": ["Amy Adams", "Jeremy Renner"]
}
# This should store "Puff the Magic Dragon lasts for 30 minutes. Stars: Puff, Jackie, Living Sneezes."
summary2 = movie_summary(arrival)