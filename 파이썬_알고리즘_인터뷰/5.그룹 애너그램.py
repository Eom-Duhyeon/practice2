"""
문자열 배열을 받아 애너그램 단위로 그룹핑하라.
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
import collections
strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs): #self 주석 삭제
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            # 이 때 ''.join을 쓰는 이유는 sorted가 리스트로 값을 반환하기 때문이다.
        return anagrams.values()


print(groupAnagrams(strs))
