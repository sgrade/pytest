# A. Elevator or Stairs?

x, y, z, t1, t2, t3 = map(int, input().split())

floors = abs(x - y)

time_stairs = floors * t1

time_elevator = abs(x - z) * t2 + floors * t2 + 3 * t3

if time_elevator <= time_stairs:
    print("YES")    
else:
    print("NO")
