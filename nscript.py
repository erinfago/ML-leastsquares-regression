# Erin Fago
# Machine Learning - Prof. Hu
# HW # 2

#nscript.py

#randomly splits the data set  into 5 parts and calls reg.py 5 times performing 5-fold cross-validation
import os
import random

def main():
	#open og file that you will base your new files on
	train = open("syn_train.txt", "r")

	overallresults=[]

	total = train.readlines()

	groupings = round(len(total)/5)

	#evenly distribute groups
	group1 = total[0: groupings]
	group2 = total[groupings: groupings*2]
	group3 = total[groupings*2: groupings*3]
	group4 = total[groupings*3: groupings*4]
	group5 = total[groupings*4: groupings*5]

	totgroups = [group1, group2, group3, group4, group5]

	#close train now that you have its data
	train.close()

	# 5-fold
	for i in range(5):
		#open file each time and overwrite previous
		newtrain = open("training.txt", "w")
		newvalid = open("valid.txt", "w")

		#generate random # to pick which group will be the validation data
		num = random.randint(1, 5)

		#go through all the groups and write to the file respectively
		for j in range(len(totgroups)):
			# one group will be the validation set
			if j == num:
				for item in totgroups[j]:
					newvalid.write(str(item))
			# otherwise its the training set
			else:
				for item in totgroups[j]:
					newtrain.write(str(item))


		#each time close files so you can then run the script with them and ensure changes comitted
		newvalid.close()
		newtrain.close()


		# do for n from 1 - 10
		for degree in range(1,11):
			#system call run the file
			os.system("python reg.py training.txt valid.txt " + str(degree))


main()
