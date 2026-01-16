# A7Q7
# Question: Write a function that takes a number as an input parameter and returns
#           the corresponding text in words, e.g., on input 452, returns 'Four Five Two'.
#           Use a dictionary for mapping digits to their string representation.
# Name: Satyajeet Nayak
# Appl No: 25C200429

def number_to_text(number):
    digit_map = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }
    
    number_str = str(number)
    text_result = []
    
    for digit in number_str:
        if digit in digit_map:
            text_result.append(digit_map[digit])
        else:
            text_result.append(digit)
            
    return ' '.join(text_result)

num = 492
print(number_to_text(num))
