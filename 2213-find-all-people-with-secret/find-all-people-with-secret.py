class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        known_set = set([0, firstPerson])
        
        sorted_meetings = []
        meetings.sort(key=lambda x:x[2])

        seen_time = set()
        
        for meeting in meetings:
            if meeting[2] not in seen_time:
                seen_time.add(meeting[2])
                sorted_meetings.append([])
            sorted_meetings[-1].append((meeting[0], meeting[1]))

        for meeting_group in sorted_meetings:
            people_know_secret = set()
            graph = defaultdict(list)
            
            for p1, p2 in meeting_group:
                graph[p1].append(p2)
                graph[p2].append(p1)
                if p1 in known_set:
                    people_know_secret.add(p1)
                if p2 in known_set:
                    people_know_secret.add(p2)
                    
            queue = deque((people_know_secret))
        
            while queue:
                curr = queue.popleft()
                known_set.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in known_set:
                        known_set.add(neighbor)
                        queue.append(neighbor)

        return list(known_set)
        
# Example usage:
sol = Solution()
print(sol.findAllPeople(6, [[1,2,5],[2,3,8],[1,5,10]], 1))  # Output: [0,1,2,3,5]
print(sol.findAllPeople(4, [[3,1,3],[1,2,2],[0,3,3]], 3))  # Output: [0,1,3]
print(sol.findAllPeople(5, [[3,4,2],[1,2,1],[2,3,1]], 1))  # Output: [0,1,2,3,4]
