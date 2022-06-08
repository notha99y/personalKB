class HashMap:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    
    def hash_function(self, x):
        """Does not handle collision
        """
        h = 0
        for char in x:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.hash_function(key)
        self.arr[h] = value

    def __getitem__(self, key):
        return self.arr[self.hash_function(key)]