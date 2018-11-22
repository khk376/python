import pymongo
from pymongo import MongoClient

conn = MongoClient('localhost',27017)
db = conn['ysDB']
collection = db['ys']

print("관리자 모드 1.입장  0.모드 종료")
first = int(input())
while(first !=0):
    print("1.옷 검색 2.옷 추가  3.옷 삭제  4.정보 변경  5.폐점  0.종료")
    second = int(input())
    if(second == 1):
        print("총 ",collection.count_documents({}),"개의 의류가 있습니다.")
        print(list(collection.find()))
        
    elif(second == 2):
        print("하나씩만 추가 가능 => 종류, 색, 사이즈 입력")
        kind, color, size = map(str, input().split(","))
        collection.insert({"kind" : kind, 
                        "color" : color,
                        "size" : size})
        print("추가 완료")
        print("총 ",collection.count_documents({}),"개의 의류가 있습니다.")
        
    elif(second == 3):
        delSize = int(input("삭제하고싶은 사이즈 : "))
        collection.delete_one({"size" : delSize})
        print("삭제 완료")
        
    elif(second == 4):
        whatType = int(input("변경을 원하는 타입 : 종류를 원하면 100, 색깔을 원하면 아무 문자나 입력해주세요. "))
        if(whatType == 100):
            upKind1 = input("어떤 종류를?")
            upKind2 = input("어떤 종류로 변경? ")
            collection.update({"kind" : upKind1}, {"$set" : {"kind" : upKind2}})
            print(list(collection.find({"kind" : upKind2})))
            print("총 ",collection.count_documents({"kind":upKind2}),"개의 의류가 있습니다.")
            
        else:
            upColor1 = input("어떤 종류를?")
            upColor2 = input("어떤 색으로 변경? ")
            collection.update({"color" : upColor1}, {"$set" : {"kind" : upColor2}})
            print(list(collection.find({"kind" : upColor2})))
            print("총 ",collection.count_documents({"kind":upColor2}),"개의 의류가 있습니다.")
            
    elif(second == 5):
        collection.drop()
    elif(second == 0):
        print("모드를 종료합니다.")
        break
    else:
        print("해당 모드가 없습니다. 다시 입력해주세요.")