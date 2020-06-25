class CropRatio:

    def __init__(self):
        self._crops = {}
        self._total_weight = 0

    def add(self, name, crop_weight):
        curr_crop_weight = 0

        if name not in self._crops:
            self._crops[name] = curr_crop_weight
            curr_crop_weight = curr_crop_weight + crop_weight
        else:
            self._crops[name] = self._crops[name] + crop_weight
        self._total_weight += 1

    def proportion(self, name):
        print('Hi')
        print(self._crops[name])

        #return self._crops[name]/self._total_weight


#To see the output, uncomment the lines below:
crop_ratio = CropRatio()
crop_ratio.add('Wheat', 4)
crop_ratio.add('Wheat', 5)
crop_ratio.add('Rice', 1)



hobbies = {
  "John": ['Piano', 'Puzzles', 'Yoga'],
  "Adam": ['Drama', 'Fashion', 'Pets'],
  "Mary": ['Magic', 'Pets', 'Reading']
};



print(crop_ratio.proportion('Wheat'))