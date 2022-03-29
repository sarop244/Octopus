string = "Hello, My name is Gihyeon Kang"

print(string.upper())         #대문자
print(string.lower())         #소문자
print(string.title())         #문자첫글자만 대문자
print(len(string))            #문자열길이
print()

print(string.count('i'))            #i 개수 
print(string.endswith('k'))         #마지막 문자가 k인지
print(string.startswith('h'))       #첫번재 문자가 h 인지
print(string.lower.startswith('h')) #소문자로 바꾼다음에 h 가있는지 여부
print()

string_1 = string.split()           #공백을 기준으로 자른다
string_2 = string.split(',')        #, 을 기준으로 자른다
print(string_1)
print(string_2)
