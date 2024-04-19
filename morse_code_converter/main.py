from morse_converter import MorseCodeConverter


print("Welcome in the Text to Morse Code converter!\n")
input_text = input("Please enter your text:\n")
morse_code = MorseCodeConverter().convert_string(input_text)
print(morse_code)


