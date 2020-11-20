# A. The Doors

n = int(input())
doors = ''.join(list(input().split()))
print(min(doors.rfind('1'), doors.rfind('0')) + 1)
