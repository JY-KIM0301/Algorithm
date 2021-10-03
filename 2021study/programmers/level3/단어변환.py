def solution(begin, target, words):
    if target not in words:
        return 0

    stack = []
    cnt = 0

    stack.append(begin)

    while True:
        cnt += 1

        for st in stack:
            one_diff = []  # 한글자만 다른 단어 저장할 리스트
            for word in words:
                diff_cnt = 0
                for i in range(0, len(begin)):
                    if st[i] != word[i]:  # begin, word 한글자씩 비교해서 다른경우만 카운트+1
                        diff_cnt += 1
                    else:
                        continue
                    if diff_cnt > 1:  # 한글자 초과하여 차이나는 경우
                        break
                if diff_cnt == 1:  # 한글자 차이나는 경우
                    one_diff.append(word)  # 해당 단어를 one_diff에 저장
                    words.remove(word)  # 사용한 단어는 words에서 제거

        if target not in one_diff:
            stack = one_diff  # begin이 계속해서 업데이트
        else:
            return cnt

# (다른풀이) DFS 재귀사용
def check(word1, word2):
    diff_cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_cnt += 1
    return diff_cnt

def dfs(word, words, target, ch, cnt):
    global arr
    if word == target:
        return arr.append(cnt)

    for i in range(len(words)):
        if check(words[i], word) == 1:
            if ch[i] == 1:
                continue
            ch[i] = 1
            # print(cnt, words[i])
            dfs(words[i], words, target, ch, cnt+1)
            ch[i] = 0

def solution(begin, target, words):
    global arr
    # target이 words에 없으면 리턴0, 종료
    if target not in words:
        return 0

    cnt = 0
    ch = [0] * len(words)
    arr = []
    dfs(begin, words, target, ch, cnt)
    return min(arr)

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))