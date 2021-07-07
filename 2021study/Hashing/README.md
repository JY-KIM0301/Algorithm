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
```
## 리스트로 해쉬 테이블 구현 
```python
class HashTable:
  # 크기 8을 가지는 해쉬 테이블 초기화 
  def __init__(self):
    self.hash_table = list([0 for i in range(8)])
    
  def hash_function(self, key):
    return key % 8
  
  # key, value값을 해쉬 테이블에 삽입 
  def insert(self, key, value):
    hash_value = self.hash_function(hash(key))
    self.hash_table[hash_value] = value
  
  # key값을 이용해 value값을 얻는 read() 함수 
  def read(self, key):
    hash_value = self.hash_function(hash(key))
    return self.hash_table[hash_value]    
  
  def print(self):
    print(self.hash_table)
```

## 충돌 해결 알고리즘
- 위의 해쉬테이블 코드에서 같은 key값에 서로다른 데이터가 들어가면, 충돌이 발생할 것이다. 
- 이러한 충돌(Collision)문제를 해결하기 위한 3가지 방법이 있다. 

### 1. Chaining 기법 
- Open Hashing 기법 중 하나로, 해쉬테이블 저장공간 외에 공간을 더 추가해서 사용하는 방법.  
- 충돌이 발생하면, Linked List로 데이터를 추가적으로 뒤에 연결시킨다. 
```python
class HashTable_Chaining:
  def __init__(self):
    self.hash_table = list([0 for i in range(8)])
    
  def hash_function(self, key):
    return key % 8
  
  # key, value값을 해쉬 테이블에 삽입 
  def insert(self, key, value):
    gen_key = hash(key)
    hash_value = self.function(gen_key)
    
    # hash value의 index를 이미 사용중인 경우 (충돌발생) 
    if self.hash_table[hash_value] != 0:
      for i in range(len(self.hash_table[hash_value])):
        # 이미 같은 키가 존재한다면, value를 교체
        if self.hash_table[hash_value][i][0] == gen_key:
          self.hash_table[hash_value][i][1] = value
          return 
      # 같은 키가 존재하지 않는경우, [key, value]를 삽입 
      self.hash_table[hash_value].append([gen_key, value])
    # 해당 hash_value를 사용하고 있지 않은 경우 
    else:
      self.hash_table[hash_value] = [[gen_key, value]]
  
  def read(self, key):
    gen_key = hash(key)
    hash_value = self.function(gen_key)   
    
    # 해당 해쉬값index에 데이터가 들어있는 경우 
    if self.hash_table[hash_value] != 0: 
    
      # 해당 해쉬 값 index에 데이터가 존재할 때, 
      for i in range(len(self.hash_table[hash_value])): 
        if self.hash_table[hash_value][i][0] == gen_key: 
        # 키와 동일할 경우 -> 해당 value return return 
          self.hash_table[hash_value][i][1] 
      # 동일한 키가 존재하지 않으면 None return 
      return None 
    else: 
      # 해당 해쉬 값 index에 데이터가 없을 때, 
      return None

  def print(self):
    print(self.hash_table)
```
