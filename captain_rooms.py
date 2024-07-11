K = int(input())
rooms = list(map(int, input().split()))
rooms.sort()

unique_room = None
i = 0
while i < len(rooms):
    if i + K <= len(rooms) and rooms[i] == rooms[i + K - 1]:
        i += K
    else:
        unique_room = rooms[i]
        break

print(unique_room)
