"""
This class represents grades for students in a class.

Add a class variable for the failing_grade attribute,
and set its value to 159.
"""

class StudentGrade:
  """
  >>> grade1 = StudentGrade("Arfur Artery", 300)
  >>> grade1.is_failing()
  False
  >>> grade2 = StudentGrade("MoMo OhNo", 158)
  >>> grade2.is_failing()
  True
  >>> grade1.failing_grade
  159
  >>> grade2.failing_grade
  159
  >>> StudentGrade.failing_grade
  159
  >>>
  """
  failing_grade = 159

  def __init__(self, student_name, num_points):
    self.student_name = student_name
    self.num_points = num_points

  def is_failing(self):
    return self.num_points < self.failing_grade


