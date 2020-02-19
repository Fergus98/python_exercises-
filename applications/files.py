file = open("teams.txt", "w")
outfile = "Brighton & Hove\n Nothing\n Arsenal\n Liverpool\n Madrid\n"
file.write(outfile)
file.close()

file = open("teams.txt", "r")

for line in range(1,4):
	print(file.readline())



