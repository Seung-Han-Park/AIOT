import numpy as np

heights = [1.83, 1.76, 1.69, 1.86, 1,77, 1.73]
weights = [86, 74, 59, 95, 80, 68]

np_heights = np.array(heights)
np_weights = np.array(weights)

bmi = np_weights/(np_heights ** 2)
print(bmi)

import numpy as np

heights = [1.83, 1.76, 1.69, 1.86, 1.77, 1.73]  # ← 여기도 1,77 → 1.77 수정!
weights = [86, 74, 59, 95, 80, 68]

np_heights = np.array(heights)
np_weights = np.array(weights)  # ✅ 변수명 올바르게 수정

bmi = np_weights / (np_heights ** 2)
print(bmi)
