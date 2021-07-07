'''
https://www.acmicpc.net/problem/10930

백준 10930: SHA-256 
문자열 S가 주어졌을 때, SHA-256 해시값을 구하는 프로그램을 작성하시오. 

Baekjoon

9944e1862efbb2a4e2486392dc6701896416b251eccdecb8332deb7f4cf2a857
'''
# SHA함수들을 가지고 있는 라이브러리 hashlib 사용
import hashlib

data = str(input()).encode()
hash_object = hashlib.sha256()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)
