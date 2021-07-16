import pickle # (객체, 텍스트)를 직렬화, 역직렬화

# 파일 이름과 데이터
bfilename = 'D:\Django\\workspace\\WebCrawling\\C3_DataProcessing\\test.bin'
tfilename = 'D:\Django\\workspace\\WebCrawling\\C3_DataProcessing\\test.txt'

data1 = 77
data2 = "Hello, world!"
data3 = ["car", "apple", "house"]

# 바이너리 쓰기
with open(bfilename, 'wb') as f:
    pickle.dump(data1, f) # dumps는 문자열을 직렬화
    pickle.dump(data2, f)
    pickle.dump(data3, f)


with open(tfilename, 'wt') as f:
    f.write(str(data1))
    f.write('\n') # 줄바꿈
    f.write(str(data2))
    f.write('\n') # 줄바꿈
    # f.write(str(data3)) # write는 텍스트만 쓸 수 있지만 리스트는 텍스트가 아니기 때문에 오류가 난다.
    f.writelines('\n'.join(data3)) # join을 하지 않는다면 carapplehouse로 작성된다.

# 바이너리 읽기
with open(bfilename, 'rb') as f:
    b = pickle.load(f) # loads는 문자열을 역직렬화
    print(type(b), ' Binary Read1 | ', b)
    b = pickle.load(f) # loads는 문자열을 역직렬화
    print(type(b), ' Binary Read2 | ', b)
    b = pickle.load(f) # loads는 문자열을 역직렬화
    print(type(b), 'Binary Read3 | ', b)

# 바이너리 형식은 <class 'int'>, <class 'str'>, <class 'list'> 클래스의 형식을 보존해주기 때문에 자료를 전송하고 수신받으면 그대로 사용할 수 있지만
# 텍스트 형식은 자료형이 텍스트 형태로 고정되기 때문에 읽어오면 그냥 스트링의 형태로 불러와진다.

# 텍스트 읽기
with open(tfilename, 'rt') as f:
    for i, line in enumerate(f, 1):
        print(type(line), 'Text Read' + str(i) + ' | ', line, end ='')
