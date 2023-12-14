from django.test import TestCase

# Create your tests here.
import re
import numpy


def result(number):
    if number >= 100000:
        return 3
    elif 1000 <= number <= 99999:
        return 2
    else:
        return 1


def group_mmr(text):
    return re.findall(r'MMR: (\d+.\d+)', text)


def team_type(text):
    return re.findall(r'team type: (\d+)', text)


def cost_time(text):
    return re.findall(r'cost time (\d+)s', text)


if __name__ == '__main__':
    text =  """
Group448 MMR: 976.00, player count: 5, team type: 3, cost time 30s
|         1e8d8b66-2346-493b-8a5f-7221117458b3 MMR: 976.00 cost time 30s
|         610c83a2-92d7-416a-a4ca-1be8a19c5c41 MMR: 700.00 cost time 30s
|         643c79ab-ec00-4b9f-be65-f925a8c18b7e MMR: 137.00 cost time 30s
|         2c1c1728-c057-4887-9854-d08eeab98151 MMR: 352.00 cost time 30s
|         b30e27d6-cdc7-412f-b97d-7e7d2dfe557c MMR: 109.00 cost time 30s
"""

    MMR_list = [float(i) for i in group_mmr(text)]
    print(MMR_list)
    group_mmr = MMR_list[0]
    player_mmr = MMR_list[1:]

    team_type = int(team_type(text)[0])
    print(team_type)

    # cost_time_list = cost_time(text)
    # group_cost_time = cost_time_list[0]
    # player_cost_time = cost_time_list[1:]

    s = numpy.var(numpy.array(player_mmr))
    print(result(s))
    print(f"队员MMR为：{s}, ", f"队伍MMR为{team_type}, ", result(s) == team_type)


