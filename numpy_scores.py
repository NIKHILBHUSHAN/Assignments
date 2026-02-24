import numpy as np

#Task-1
np.random.seed(42)
scores=np.random.randint(50,101,(5,4))
print(scores)
print("The score of the 3rd student in the 2nd subject",scores[2,1])
print("All scores of the last 2 students (all subjects):")
print(scores[[3,4],:])
print("All scores for the first 3 students in subjects 2 and 3 only:")
print(scores[0:3,[1,2]])


#Task2
avg_score_per_subject=np.round(scores.mean(axis=0),2)
print("Average scores per subject:")
print(avg_score_per_subject)
curvedscores=scores+[5,3,7,2]
result_curvedscores=np.clip(curvedscores,50,100)
print("Curved Scores:")
print(result_curvedscores)
print("row wise max:",result_curvedscores.max(axis=1))


#Task3
min=result_curvedscores.min(axis=0)
max=result_curvedscores.max(axis=0)
normalize=(result_curvedscores-min)/(max-min)
print("Normalized scores:")
print(normalize)
row,col=np.unravel_index(np.argmax(normalize),normalize.shape)
print("student index (row) and subject index (column) of the single highest value across the entire array:",row,col)
mask=result_curvedscores>90
mask1d=mask.reshape(-1)
print("Scores that are strictly above 90:")
print(mask1d)