def calculate_grade(*scores,**adjustment):
    avg=sum(scores)/len(scores)
    for value in adjustment.values():
        avg+=value
    print(f"Average:{avg:.2f}%")
calculate_grade(85,90,78)
calculate_grade(70,65,80,attendance=5,project=10)