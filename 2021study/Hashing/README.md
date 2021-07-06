# Hash Table
## 해쉬 구조란?
- key, value쌍으로 이루어진 데이터 구조를 의미함 
- key를 이용해서 데이터를 찾기 때문에 속도가 빠르다 
- 파이썬의 딕셔너리가 해쉬 테이블과 구조가 같음 
- 기본적으로, 해시 테이블 크기만큼 배열을 선언해야한다. 공간은 많이 차지하지만, 시간이 빠름 
- 여러 키의 주소가 동일한 경우, 충돌을 해결하는 별도의 알고리즘이 존재함 
### 시간 복잡도 
- 충돌이 없는 일반적인 경우: O(1)
- 모든 경우 충돌이 발생하는 최악의 경우: O(n)
### 용어 
- Hash: 임의 값을 고정길이로 변환하는 것을 의미 
- Hash Function: key를 받아 value를 가진 공간의 주소로 바꾸어주는 함수 
- Slot: 한개의 데이터를 저장하는 공간 

## 해쉬 함수와 키 생성 함수 
### SHA(Secure Hash Algorithm)
- 어떠한 데이터도 고정된 크기의 유일한 값으로 반환시키는 알고리즘 
### SHA-1
- 해쉬값의 크기를 160으로 고정하는 알고리즘 
- 코드 
```python
# SHA함수들을 가지고 있는 라이브러리 hashlib 사용
import hashlib

# 'test'의 SHA-1 해시값을 구하는 알고리즘 
data = 'test'.encode()
hash_object = hashlib.sha1()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)

# a94a8fe5ccb19ba61c4c0873d391e987982fbbd3
