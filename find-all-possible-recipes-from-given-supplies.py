class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(len(recipes)):
            for ing in ingredients[i]:
                graph[ing].append(recipes[i])
                indegree[recipes[i]] += 1

        queue = deque(supplies)

        recipes = set(recipes)

        ans = []
        while queue:
            length = len(queue)

            for _ in range(length):
                curr = queue.popleft()

                if curr in recipes:
                    ans.append(curr)

                for child in graph[curr]:
                    indegree[child] -= 1

                    if not indegree[child]:
                        queue.append(child)

        return ans