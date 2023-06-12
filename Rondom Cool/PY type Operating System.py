import platform

import sys
import matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('Operating System: ' + platform.system() + platform.release())
print('Python Version: ' + platform.python_version())
print('←————————————————————————————————————————→')
print(f"Python Version: {sys.version}")
print(f"NumPy Version: {np.__version__}")
print(f"Pandas Version: {pd.__version__}")
print(f"Matplotlib Version: {matplotlib.__version__}")
