class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [[pos, speed] for pos, speed in zip(position, speed)]
        pos_speed.sort(reverse = True)

        stack = []
        for position, speed in pos_speed:
            remaining = target - position
            time = remaining / speed
            if (not stack) or (stack and  stack[-1] < time):
                stack.append(time)

        return len(stack)
