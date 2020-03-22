import pickle
import numpy as np

with open("CKD", "rb") as f:
    deepLearningModel = pickle.load(f)

print("Working")

model_inputs = [0.75, 0.2, 0.033898, 0.836735, 0.717949, 1.0]

print()

temp_array = np.array(model_inputs).reshape(1, 6)
pred = deepLearningModel.predict(temp_array)
pred = [1 if y >= 0.5 else 0 for y in pred]
