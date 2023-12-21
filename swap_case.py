def swap_case(str):
    result_str = ""

    for char in str:
        if 'a' <= char <= 'z':
            result_str += chr(ord(char) - 32)  
        elif 'A' <= char <= 'Z':
            result_str += chr(ord(char) + 32)  
        else:
            result_str += char  

    return result_str
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)