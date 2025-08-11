import abc
class SortStrategy(abc.ABC):
    @abc.abstractmethod
    def sort(self, data):
        pass

class BubleSortStrategy(SortStrategy):

    def sort(self, data):
        print("Sort data by buble sort algo")
        return sorted(data)

class QuickSortStrategy(SortStrategy):

    def sort(self, data):
        print("Sort data by quick sort algo")
        return sorted(data)

class Context:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self.strategy = strategy

    def do_smth_with_strategy(self, data):
        return self.strategy.sort(data)

data_to_sort = [1,4,6,1,2,3,0,5,6]

context = Context(QuickSortStrategy())
print(context.do_smth_with_strategy(data_to_sort))

print(f"Change strategy to Bubble")
context.set_strategy(BubleSortStrategy())

print(context.do_smth_with_strategy(data_to_sort))
