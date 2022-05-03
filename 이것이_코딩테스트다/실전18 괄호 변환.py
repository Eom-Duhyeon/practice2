"""
p	result
"(()())()"	"(()())()"
")("	"()"
"()))((()"	"()(())()"

"""

p = ")("

# 괄호쌍 검사하는 가장 편한 방법
def check_right(u):
    count = 0
    for i in u:
        if i == "(":
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def check_balanced(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1

        if count == 0 :
            return i



def solution(p):
    if p == "":
        return ""
    index = check_balanced(p)
    u = p[:index+1]
    v = p[index+1:]

    if check_right(u):
        answer = u + solution(v)
    else:
        u = list(u[1:-1])
        if len(u) == 2:
            answer = "(" + solution(v) +")"
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer = "(" + solution(v) + ")" + "".join(u)

    return answer

print(solution(p))