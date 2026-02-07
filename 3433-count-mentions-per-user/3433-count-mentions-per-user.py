class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        mentions = [0] * numberOfUsers
        online_time = [0] * numberOfUsers
        for event in events:
            etype, timestamp_str, data = event
            ts = int(timestamp_str)
            if etype == "OFFLINE":
                user_id = int(data)
                online_time[user_id] = ts + 60
            elif etype == "MESSAGE":
                if data == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif data == "HERE":
                    for i in range(numberOfUsers):
                        if ts >= online_time[i]:
                            mentions[i] += 1
                else:
                    ids = data.split()
                    for token in ids:
                        user_id = int(token[2:])
                        mentions[user_id] += 1 
        return mentions