import matplotlib.pyplot as plt
import pandas as pd
fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(nrows=2,ncols=2)
ax1.plot([1,2,3],[4,5,6])
omg=pd.DataFrame({1:{2:3,4:5},6:{7:8,9:10}})
print(omg)
ax2.plot(omg)
plt.show()