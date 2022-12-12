# Hsuan-You Lin Final Exam Question 8.
def merge_meetings(meetings):
    meetings.sort(key=lambda x: x[0])

    merged = []
    for meeting in meetings:
        if not merged or merged[-1][1] < meeting[0]:
            merged.append(meeting)
        else:
            merged[-1][1] = max(merged[-1][1], meeting[1])

    return merged
    
if __name__ == "__main__" :
    meetings = [[730, 900], [1500, 1630], [800, 1100]]

    print(merge_meetings(meetings)) # should print [(730, 1100), (1500, 1630)]
    
