import sqlite3

# 데이터베이스 연결
# 외부 파일로 생성된 일반 binary file과 sqlite 기능 연동
filePath = "encore.sqlite"
conn=sqlite3.connect(filePath)

# table 생성
'''
 python으로 RDBMS 들을 사용할 경우
 접속 후에 반드시 DB의 내부 table 활용을 위한 포인터와 같은 
 cursor를 생성 및 반환 
'''
cur=conn.cursor()
cur.execute("""drop table if exists books""")
cur.executescript("""create table books(key text primary key, title text, content text)""")

# 데이터 저장
cur.execute("insert into books values('001','data01', 'data01 이해하기')")
cur.execute("insert into books values('002','data02', 'data02 이해하기')")
conn.commit()

# 모든 데이터 검색
# 필요 API - execute() / fetchall()
# 데이터가 다수. 따라서 for in 문장 사용
cur.execute("select * from books")
for data in cur.fetchall():
     print(data)

# 조건에 맞는 데이터
cur.execute("select * from books where key='001'")
print(cur.fetchone())
# 자원반환

conn.close()





