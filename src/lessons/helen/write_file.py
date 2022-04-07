with open("csvfile.csv", "w") as file:
    for line in text:
        file.write(line)
        file.write("\n")
