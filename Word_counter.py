Text = str(input("Input text to count: \n"))

Split_lines = Text.split("\n")
Split_words = Text.split(" ")

print("The text is {} words and spans {} lines".format(len(Split_words), len(Split_lines)))