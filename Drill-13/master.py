import server
import user1
import user2

for i in range(10):
    if i % 2 == 1:
        user1.add(i)
    else:
        user2.add(i)


print(server.data)