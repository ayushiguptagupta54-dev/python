import heapq

hospital = []
#  lower number = higher priority
heapq.heappush(hospital, (3, "Broken finger"))
heapq.heappush(hospital, (1, "Broken heart"))
heapq.heappush(hospital, (2, "Broken human"))

print(heapq.heappop(hospital))
print(heapq.heappop(hospital))
print(heapq.heappop(hospital))


#  heapq.heappush(queue, item)



