class FoodRatings:
    # def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
    #     self.food_cuisine = dict()
    #     self.rating_system1,self.rating_system2 = dict(),dict()
        
    #     for i in range(len(foods)):
    #         self.food_cuisine[foods[i]] = cuisines[i]

    #         if cuisines[i] not in self.rating_system1:
    #             self.rating_system1[cuisines[i]] = dict()
    #         if ratings[i] not in self.rating_system1[cuisines[i]]:
    #             self.rating_system1[cuisines[i]][ratings[i]] = []
    #         heapq.heappush(self.rating_system1[cuisines[i]][ratings[i]],foods[i])

    #         if cuisines[i] not in self.rating_system2:
    #             self.rating_system2[cuisines[i]] = dict()
    #         self.rating_system2[cuisines[i]][foods[i]] = ratings[i]

    # def changeRating(self, food: str, newRating: int) -> None:
    #     cuisine = self.food_cuisine[food]
    #     oldRating = self.rating_system2[cuisine][food]

    #     self.rating_system1[cuisine][oldRating].remove(food)
    #     if not self.rating_system1[cuisine][oldRating]:
    #         del self.rating_system1[cuisine][oldRating]
    #     else:
    #         heapq.heapify(self.rating_system1[cuisine][oldRating])

    #     if newRating not in self.rating_system1[cuisine]:
    #         self.rating_system1[cuisine][newRating] = []
    #     heapq.heappush(self.rating_system1[cuisine][newRating],food)

    #     self.rating_system2[cuisine][food] = newRating

    # def highestRated(self, cuisine: str) -> str:
    #     return self.rating_system1[cuisine][max(self.rating_system1[cuisine])][0]
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = {}
        self.rated_cuisine = defaultdict(list)

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.foods[food] = (rating, cuisine)
            self.rated_cuisine[cuisine].append((-rating, food))
        
        for cuisine in self.rated_cuisine:
            heapq.heapify(self.rated_cuisine[cuisine])


    def changeRating(self, food: str, newRating: int) -> None:
        _, curr_cuisine = self.foods[food]
        self.foods[food] = (newRating, curr_cuisine)
        heapq.heappush(self.rated_cuisine[curr_cuisine], (-newRating, food))


    def highestRated(self, cuisine: str) -> str:
        while self.rated_cuisine[cuisine][0][0] != -self.foods[self.rated_cuisine[cuisine][0][1]][0]:
            heapq.heappop(self.rated_cuisine[cuisine])
        return self.rated_cuisine[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)