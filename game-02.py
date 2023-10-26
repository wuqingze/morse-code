import random

# 定义摩斯电码字母和对应的编码
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----'
}

import os

def clear_terminal():
    #os.system('clear')  # For macOS and Linux
    os.system('cls')  # For Windows

# 获取摩斯电码字母列表
morse_code_letters = list(morse_code_dict.keys())

def generate_random_morse_code(asked_morse_codes):
    # 从摩斯电码字母列表中随机选择一个尚未被问过的字母
    remaining_letters = [letter for letter in morse_code_letters if letter not in asked_morse_codes]
    if not remaining_letters:
        return None, None
    random_letter = random.choice(remaining_letters)
    asked_morse_codes.append(random_letter)
    
    # 获取对应的摩斯电码
    morse_code = morse_code_dict[random_letter]
    return random_letter, morse_code

def main():
    asked_morse_codes = []  # 存储已经被问过的摩斯电码
    idx = 1
    while True:
        random_letter, morse_code = generate_random_morse_code(asked_morse_codes)
        
        if random_letter is None:
            print("已经问过所有的摩斯电码，程序结束。")
            break

        print(f"{idx},摩斯电码: {morse_code}")
        user_input = input("请输入对应字母的摩斯电码（不区分大小写）: ").upper()
        
        while user_input != random_letter:
            user_input = input("输入错误，重新输入（不区分大小写）: ").upper()
        clear_terminal()
        print("输入正确，继续下一个摩斯电码\n")
        idx += 1
if __name__ == "__main__":
    main()
