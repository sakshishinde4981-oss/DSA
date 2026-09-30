import heapq

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available = []

    def push(self, val: int) -> None:

        # Remove stacks from heap that are already full
        while self.available and (
            self.available[0] >= len(self.stacks) or
            len(self.stacks[self.available[0]]) == self.capacity
        ):
            heapq.heappop(self.available)

        # If there is a stack with space
        if self.available:
            index = self.available[0]
            self.stacks[index].append(val)

            # If stack becomes full, remove it from heap
            if len(self.stacks[index]) == self.capacity:
                heapq.heappop(self.available)

        else:
            # Create a new stack
            self.stacks.append([val])

            # If it still has space, add its index to heap
            if self.capacity > 1:
                heapq.heappush(self.available, len(self.stacks) - 1)

    def pop(self) -> int:

        # Remove empty stacks from the right
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        # If all stacks are empty
        if not self.stacks:
            return -1

        # Rightmost non-empty stack
        index = len(self.stacks) - 1

        value = self.stacks[index].pop()

        # This stack now has space
        heapq.heappush(self.available, index)

        # Remove empty stacks from right
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return value

    def popAtStack(self, index: int) -> int:

        # Invalid index or empty stack
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1

        # Remove top element
        value = self.stacks[index].pop()

        # Stack now has free space
        heapq.heappush(self.available, index)

        return value