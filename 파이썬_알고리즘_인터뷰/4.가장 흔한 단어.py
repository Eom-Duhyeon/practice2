"""
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.
입력:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
출력:
"ball"
"""

import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."

banned = ["hit"]

words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() \
             if word not in banned]
counts = collections.Counter(words)

"""Counter 는 ('단어', 횟수) 형태의 튜플로 보여준다. 이 때 most_common은 그저 정렬이다. 
인덱스를 붙여줘야 가장 큰 것을 찾을 수 있다."""
print(counts.most_common(1)[0][0])