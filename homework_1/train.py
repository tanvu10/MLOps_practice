from model import AI, DeepLearning
from dataset import DataSet

ds = DataSet(input_data=[1,2,3,4,5], labels=[1])
ai1 = AI(algorithm='lr', model_type='linear')
print(ai1.algorithm)
