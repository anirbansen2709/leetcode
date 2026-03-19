# There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.
# You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of
# this new language. Derive the order of letters in this language. If the order is invalid, return an empty string. If there are 
# multiple valid order of letters, return any of them. A string a is lexicographically smaller than a string b if either of the 
# following is true: The first letter where they differ is smaller in a than in b. a is a prefix of b and a.length < b.length.

# The code implements a solution for the classic Alien Dictionary problem using Topological Sorting (specifically Kahn's Algorithm) on
# a Directed Acyclic Graph (DAG).
# Here is an outline of the algorithm:
# 1. Graph Initialization - Adjacency List (adj): Creates a dictionary mapping each unique character in the input words to a set of its
# "neighbor" characters. This represents the directed edges (rules of order) between letters. Indegree Tracker (indegree): Initializes 
# a dictionary to keep track of the number of incoming edges (prerequisites) for every unique character, starting at 0.
# 2. Building the Graph - The code iterates through adjacent pairs of words (w1 and w2). Edge Case Check: It checks if w1 is longer than
# w2 and w2 is a complete prefix of w1. If true, the dictionary is invalid according to normal lexicographical rules, so it immediately
# returns an empty string "". Determine Order: It compares w1 and w2 character by character until it finds the first difference.
# The first differing character in w1 comes before the differing character in w2. If this relationship (directed edge) hasn't been 
# recorded yet, it adds the w2 character to the w1 character's adjacency set and increments the indegree of the w2 character.
# It then breaks out of the character comparison loop, as only the first difference defines the ordering rule between the two words.
# 3. Topological Sort (Kahn's Algorithm) - Queue Setup (q): A queue is initialized with all characters that have an indegree of 0.
# These are the characters that have no dependencies and can appear first. Breadth-First Search (BFS): While the queue is not empty:
# Pop a character from the queue and add it to the result list (res). For each of its neighbors in the adjacency graph, decrement
# their indegree by 1. If a neighbor's indegree drops to 0, it means all its prerequisites are met, so it is added to the queue.
# 4. Cycle Detection & Result
# After the queue is exhausted, the code checks if the length of the result list matches the total number of unique characters.
# Cycle Found: If the lengths do not match, it means a cycle exists in the graph (e.g., 'a' comes before 'b', and 'b' comes before 'a'),
# indicating an invalid dictionary. It returns "". Success: If they match, it joins the characters in the result list into a single 
# string and returns the valid topological order.

class Solution:
    def foreignDictionary(self, words):
        # initialization
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}
        # graph building
        for i in range(len(words) - 1):
            #edge case
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            # determine order
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        # topo sort - kahn's algorithm
        q = deque([c for c in indegree if indegree[c] == 0]) # no dependency
        res = []
        # bfs
        while q:
            char = q.popleft()
            res.append(char)
            for neighbor in adj[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        # cycle detection
        if len(res) != len(indegree):
            return ""

        return "".join(res)

