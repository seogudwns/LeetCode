class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        know = [False for _ in range(n)]
        know[0] = True
        know[firstPerson] = True
        meetings = sorted(meetings, key = lambda x: x[2])
        meetings.append([0,0,meetings[-1][2]+1])
        curr_time = meetings[0][2]
        many_meeting = defaultdict(set)
        people = set()
            
        for i,j,time in meetings:
            if time == curr_time:
                many_meeting[i].add(j)
                many_meeting[j].add(i)
                people.add(i)
                people.add(j)
            else:
                curr_time = time
                already = set()
                while people:
                    x = people.pop()
                    if know[x] and x not in already:
                        already.add(x)
                        for k in many_meeting[x]: 
                            if not know[k]:
                                know[k] = True
                                people.add(k)
                                
                many_meeting = defaultdict(set)
                many_meeting[i].add(j)
                many_meeting[j].add(i)
                people={i,j}
        
        return [i for i in range(n) if know[i] == True]