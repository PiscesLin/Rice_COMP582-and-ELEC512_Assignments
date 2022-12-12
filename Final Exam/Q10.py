# Hsuan-You Lin Final Exam Question 10.

from collections import defaultdict

def DFS(courses, request):
    courseDict = defaultdict(list)
    checked = [False] * courses
    path = [False] * courses

    for relation in request:
        next_course, prev_course = relation[0], relation[1]
        courseDict[prev_course].append(next_course)

    for curr_course in range(courses):
        if is_cyclic(curr_course, courseDict, checked, path):
            return False
    return True


def is_cyclic(curr_course, courseDict, checked, path):
    if checked[curr_course]:
        return False
    if path[curr_course]:
        return True

    path[curr_course] = True
    ret = False
    
    for child in courseDict[curr_course]:
        ret = is_cyclic(child, courseDict, checked, path)
        if ret: break

    path[curr_course] = False

    checked[curr_course] = True
    return ret
    
if __name__ == "__main__" :
    courses = 4
    request = [(1, 0), (2, 1), (3, 2), (1, 3)]
    print(DFS(courses, request)) # should print False

