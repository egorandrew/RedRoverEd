file_name = 'test_file_1.txt'
file_name_2 = 'test_file_2.txt'
file_name_3 = 'test_file_1.txt'
# file = open(file_name_2, "w", encoding="utf-8")
with open(file_name_3, encoding="utf-8") as f:
    content = [i.strip() for i in f.readlines()]
# content = file.read()
# content = file.readline()
# content = [i.strip() for i in file.readlines()]
# print(content)
# file.write("11111111111111")
for i in content:
    print(i)
# file.close()
