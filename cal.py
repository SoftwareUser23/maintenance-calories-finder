  
def mainCal():
	weight = int(input("Enter your weight(in kgs) -:\n"))
	j= weight * 2.2
	p_intake = j*1.4
	protein_cal = p_intake * 4
	carbs_cal = p_intake* 4
	print(f"Protein calories are {protein_cal} and Carbs calories are {carbs_cal}\n")

	# fat intake

	fat_intake = p_intake % 4
	fat_cal = fat_intake *9
	print(f"Fats calories are {fat_cal}\n")

	# total calories
	total_calories = fat_cal +protein_cal +carbs_cal
	print(f"Total Maintaince calories are {total_calories}"

)


mainCal()	
