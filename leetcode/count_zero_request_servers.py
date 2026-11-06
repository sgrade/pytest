# 2747. Count Zero Request Servers
# https://leetcode.com/problems/count-zero-request-servers/


# Based on Editorial's Approach: Sorting and Sliding Window
class Solution:
    def countServers(
        self, n: int, logs: list[list[int]], x: int, queries: list[int]
    ) -> list[int]:
        # Sort logs by time, and query indices by query time, so the window
        # [query - x, query] only moves forward.
        logs.sort(key=lambda log: log[1])
        query_order = sorted(range(len(queries)), key=lambda i: queries[i])

        ans = [0] * len(queries)
        requests_per_server = [0] * (n + 1)
        active_servers = 0  # Servers with at least one request in the window.
        window_start = window_end = (
            0  # Window is logs[window_start:window_end].
        )

        for query_index in query_order:
            query_time = queries[query_index]

            # Add logs with time <= query_time to the window.
            while window_end < len(logs) and logs[window_end][1] <= query_time:
                server_id = logs[window_end][0]
                if requests_per_server[server_id] == 0:
                    active_servers += 1
                requests_per_server[server_id] += 1
                window_end += 1

            # Remove logs with time < query_time - x from the window.
            while (
                window_start < window_end
                and logs[window_start][1] < query_time - x
            ):
                server_id = logs[window_start][0]
                requests_per_server[server_id] -= 1
                if requests_per_server[server_id] == 0:
                    active_servers -= 1
                window_start += 1

            ans[query_index] = n - active_servers

        return ans
