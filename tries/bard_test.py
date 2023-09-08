from multiprocessing import freeze_support
import multiprocessing

class Agent:
    def __init__(self, name, capacity, cost):
        self.name = name
        self.capacity = capacity
        self.cost = cost

    def make_bid(self, price):
        if price > self.cost:
            return self.capacity
        else:
            return 0

class Market:
    def __init__(self, capacity, demand):
        self.capacity = capacity
        self.demand = demand
        self.producers = [
            Agent("Producer 1", 1000, 20),
            Agent("Producer 2", 2000, 15),
            Agent("Producer 3", 3000, 10),
            Agent("Producer 4", 4000, 5),
        ]
        self.price = 17

    def run(self):
        # Create a pool of workers.
        pool = multiprocessing.Pool()

        # Submit jobs to the pool.
        jobs = [pool.apply_async(agent.make_bid, args=(self.price,)) for agent in self.producers]

        # Wait for the jobs to finish.
        bids = [job.get() for job in jobs]

        # Select the winning bids.
        winning_bids = sorted(bids, reverse=True)[:self.demand]

        # Calculate the total cost of the winning bids.
        total_cost = sum(winning_bids)

        # Return the market price, the winning bids, and the total cost.
        return self.price, winning_bids, total_cost

if __name__ == "__main__":
    # Freeze the main module before starting any child processes.
    freeze_support()


    # Create the market.
    market = Market(5000, 1000)

    # Run the market.
    price, winning_bids, total_cost = market.run()

    # Print the results.
    print("Market price:", price)
    print("Winning bids:", winning_bids)
    print("Total cost:", total_cost)
