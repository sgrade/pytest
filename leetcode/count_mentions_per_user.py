# 3433. Count Mentions Per User
# https://leetcode.com/problems/count-mentions-per-user/


# Based on Editorial's Approach: Playback After Sorting
class Solution:
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        events.sort(key=lambda e: (int(e[1]), e[0] == "MESSAGE"))

        counter = [0] * numberOfUsers
        next_online = [0] * numberOfUsers
        for event in events:
            cur_time = int(event[1])
            if event[0] == "MESSAGE":
                if event[2] == "ALL":
                    for user_id in range(numberOfUsers):
                        counter[user_id] += 1
                elif event[2] == "HERE":
                    for user_id, next_online_time in enumerate(next_online):
                        if next_online_time <= cur_time:
                            counter[user_id] += 1
                else:
                    for str_id in event[2].split():
                        user_id = int(str_id[2:])
                        counter[user_id] += 1
            else:
                user_id = int(event[2])
                next_online[user_id] = cur_time + 60
        return counter
