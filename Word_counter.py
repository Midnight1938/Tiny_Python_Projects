Lines = int(input("Enter the number of paragraphs you have: (numeric)"))
lines = ''
i = 0
while i in range(Lines):
    lines += input()+"\n"
    Text = str(input("Input text in your para number {}: \n".format(i+1)))
    i += 1

Split_lines = lines.split("\n")
Split_words = lines.split(" ")


print("The text is {} words and spans {} lines".format(
    len(Split_words), len(Split_lines)))
