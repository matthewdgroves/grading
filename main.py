import pandas as pd
import matplotlib.pyplot as plt
from numpy import interp

# 135
# LTgrades = pd.read_csv("Physics_Outcomes_Summative2324_1.csv", header=0)

LTgrades = pd.read_csv("Physics_Outcomes_Summative2324evens.csv", header=0)
#LTgrades.head(n=50)

droppedColumns = [i for i in LTgrades if "mastery points" in i]
droppedColumns.append("Student ID")
droppedColumns.append("Student SIS ID")

LTgrades = LTgrades.drop(droppedColumns, axis=1)
LTgrades = LTgrades.dropna(
    how='all',
    axis=1,
)

LTgrades_w_avg = LTgrades.copy()
LTgrades_w_avg['LT Average'] = LTgrades_w_avg.mean(numeric_only=True, axis=1)


def percentGrade(LT_grade):
  #Students with LT_grade in the 3.0-3.19 range could be either Honors B+ or regular A
  #This function assumes they would rather have the Honors B+

  #Honors
  if 3.5 <= LT_grade < 4:
    pctGrade = interp(LT_grade, [3.5, 4.0], [93, 100])
    return ([pctGrade, "Honors A"])
  if 3.20 <= LT_grade < 3.4999:
    pctGrade = interp(LT_grade, [3.20, 3.49], [90, 92])
    return ([pctGrade, "Honors A-"])
  if 3.0 <= LT_grade < 3.1999:
    pctGrade = interp(LT_grade, [3.0, 3.19], [87, 89])
    return ([pctGrade, "Honors B+"])

  #Regular
  if 3.0 <= LT_grade < 3.1999:
    pctGrade = interp(LT_grade, [3.0, 3.19], [93, 100])
    return ([pctGrade, "A"])
  if 2.8 <= LT_grade < 2.9999:
    pctGrade = interp(LT_grade, [2.8, 2.99], [90, 92])
    return ([pctGrade, "A-"])
  if 2.6 <= LT_grade < 2.7999:
    pctGrade = interp(LT_grade, [2.6, 2.79], [87, 89])
    return ([pctGrade, "B+"])
  if 2.4 <= LT_grade < 2.5999:
    pctGrade = interp(LT_grade, [2.4, 2.59], [83, 86])
    return ([pctGrade, "B"])
  if 2.2 <= LT_grade < 2.3999:
    pctGrade = interp(LT_grade, [2.2, 2.39], [80, 82])
    return ([pctGrade, "B-"])
  if 2.0 <= LT_grade < 2.1999:
    pctGrade = interp(LT_grade, [2.0, 2.19], [77, 79])
    return ([pctGrade, "C+"])
  if 1.8 <= LT_grade < 1.9999:
    pctGrade = interp(LT_grade, [1.8, 1.99], [73, 76])
    return ([pctGrade, "C"])
  if 1.60 <= LT_grade < 1.7999:
    pctGrade = interp(LT_grade, [1.60, 1.79], [70, 72])
    return ([pctGrade, "C-"])
  if 0.0 <= LT_grade < 1.5999:
    pctGrade = interp(LT_grade, [0, 1.59], [50, 69])
    return ([pctGrade, "F"])


gradePercentage = []
gradeLetter = []

for num in LTgrades_w_avg['LT Average']:

  pct = percentGrade(num)[0]
  gradePercentage.append(pct)

  lett = percentGrade(num)[1]
  gradeLetter.append(lett)

  #print(num, pct, lett)

LTgrades_w_avg['LT Letter Grade'] = gradeLetter
LTgrades_w_avg['Summative Pct Grade'] = gradePercentage

#MAKE SURE THAT THE TEST STUDENT IS DELETED FROM THE DF FIRST SO THE LAST FEW IN THE ALPHABET LINE UP RIGHT
formativeGrades = [
    89.35, 84.06, 76.27, 81.65, 90.07, 98.53, 92, 97.46, 87.75, 89.47, 93.2,
    89.94, 94.13, 87.47, 90.4, 86.83, 92.47, 95.67, 95.44, 82.87, 91.08, 84.94,
    93.93, 94.87, 80.8, 92.88, 95.87, 97, 86.6, 80.13, 97.33, 81.33, 89.51,
    84.49, 94.6
]

# for user-generated formativeGrades: formativeGrades = [float(x) for x in input().split()]

LTgrades_w_avg['Formative Pct Grade'] = formativeGrades

totalModGrade = (.4 * LTgrades_w_avg['Formative Pct Grade']) + (
    .6 * LTgrades_w_avg['Summative Pct Grade'])
LTgrades_w_avg['Total Mod Pct Grade'] = totalModGrade

finalCleaning = [i for i in LTgrades_w_avg if "result" in i]
finalDB = LTgrades_w_avg.drop(finalCleaning, axis=1)

#finalDB.to_csv("Mod 1 Physics Grades 135.csv")
finalDB.to_csv("Mod 1 Physics Grades 246.csv")

finalDB.head(n=500)
#print(finalDB)
finalDB.hist()
plt.show()