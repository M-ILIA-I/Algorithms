from typing import List


class Solution:
    """
    Problem description:
    There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

    arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
    timei is the time needed to prepare the order of the ith customer.
    When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time. The chef prepares food for customers in the order they were given in the input.

    Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.
    """
    # def averageWaitingTime(self, customers: List[List[int]]) -> float:
    #     n = len(customers)
    #     tmp_sum = customers[0][1]
    #     for i in range(1,n):
    #         if customers[i][0] >= customers[i-1][0] + customers[i-1][1]:
    #             tmp_sum += customers[i][1]
    #         else:
    #             tmp_sum += customers[i-1][0] + customers[i-1][1] - customers[i][0] + customers[i][1]
    #             customers[i][0] += customers[i-1][0] + customers[i-1][1] - customers[i][0]
    #     return tmp_sum / n


    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        current_time = 0
        total_time = 0

        for s_time, waiting in customers:
            current_time = max(s_time, current_time)
            current_time += waiting
            total_time += current_time - s_time

        return total_time/n