import heapq

class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()
        free_rooms = list(range(n))
        busy_rooms = []
        count = [0] * n
        
        for start, end in meetings:
            # Free up rooms that have finished by the start of the current meeting
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                # Assign the free room with the lowest index
                room = heapq.heappop(free_rooms)
            else:
                # Delay the meeting until the earliest room gets free
                end_time, room = heapq.heappop(busy_rooms)
                end += end_time - start
            
            # Book the room
            heapq.heappush(busy_rooms, (end, room))
            count[room] += 1
        
        # Find the room with the maximum bookings
        max_booked = max(count)
        for i in range(n):
            if count[i] == max_booked:
                return i
