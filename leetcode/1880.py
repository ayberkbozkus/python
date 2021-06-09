class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first = [char for char in firstWord]
        second =[char for char in secondWord]
        target = [char for char in targetWord]
        alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
        numbers = range(27)
        alp_list = dict(zip(alphabet, numbers))
        first_num, second_num, target_num = 0,0,0
        k = 0.1
        for i in first:
            k *= 10
        for i in first:
            first_num += int(alp_list[i]*k)
            k /= 10
        k = 0.1
        for i in second:
            k *= 10
        for i in second:
            second_num += int(alp_list[i]*k)
            k /= 10
        k = 0.1
        for i in target:
            k *= 10
        for i in target:
            target_num += int(alp_list[i]*k)
            k /= 10
        
        return first_num + second_num == target_num