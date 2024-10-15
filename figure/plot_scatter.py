import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

# 创建随机数据
np.random.seed(10)
data_train = np.random.randn(200, 2)
data_test = np.random.randn(200, 2) + 2

# 设置图形风格
sns.set_style("darkgrid")

# 使用 jointplot 创建带有边缘密度曲线的散点图（训练集）
g = sns.jointplot(x=data_train[:, 0], y=data_train[:, 1], kind='scatter', color='blue', s=30, alpha=0.5, label="Train Dataset")

# 清除默认的边缘图
g.ax_marg_x.clear()
g.ax_marg_y.clear()

# 在边缘位置绘制训练集的密度曲线
sns.kdeplot(x=data_train[:, 0], ax=g.ax_marg_x, color="blue", fill=True)
sns.kdeplot(y=data_train[:, 1], ax=g.ax_marg_y, color="blue", fill=True)

# 在相同的 jointplot 图上添加测试集的数据
g.ax_joint.scatter(x=data_test[:, 0], y=data_test[:, 1], color='red', s=30, alpha=0.5, label="Test Dataset")

# 绘制测试集的密度曲线
sns.kdeplot(x=data_test[:, 0], ax=g.ax_marg_x, color="red", fill=True)
sns.kdeplot(y=data_test[:, 1], ax=g.ax_marg_y, color="red", fill=True)

# 添加对角线，表示预测值与实际值的比较标准
min_val = min(np.min(data_train), np.min(data_test))
max_val = max(np.max(data_train), np.max(data_test))
g.ax_joint.plot([min_val, max_val], [min_val, max_val], 'black', linestyle="-")

# 计算并显示训练集和测试集的 RMSE 和 MAE
rmse_train = np.sqrt(mean_squared_error(data_train[:, 0], data_train[:, 1]))
mae_train = mean_absolute_error(data_train[:, 0], data_train[:, 1])
rmse_test = np.sqrt(mean_squared_error(data_test[:, 0], data_test[:, 1]))
mae_test = mean_absolute_error(data_test[:, 0], data_test[:, 1])

train_text = f"N = {len(data_train)}\nMAE = {mae_train:.2f}\nRMSE = {rmse_train:.2f}"
test_text = f"N = {len(data_test)}\nMAE = {mae_test:.2f}\nRMSE = {rmse_test:.2f}"

g.ax_joint.text(0.95, 0.05, train_text, horizontalalignment='right', verticalalignment='bottom',
                transform=g.ax_joint.transAxes, fontsize=10, color='blue')
g.ax_joint.text(0.95, 0.20, test_text, horizontalalignment='right', verticalalignment='bottom',
                transform=g.ax_joint.transAxes, fontsize=10, color='red')

# 设置新的坐标轴标签
g.ax_joint.set_xlabel('Predicted')
g.ax_joint.set_ylabel('Actual')

# 移除边缘图的标签和刻度
g.ax_marg_x.set_ylabel('')
g.ax_marg_y.set_xlabel('')
g.ax_marg_x.set_yticks([])
g.ax_marg_y.set_xticks([])

# 添加图例
g.ax_joint.legend(loc="upper left")

# 使用 tight_layout 自动调整布局以防止内容重叠
plt.tight_layout()

# 对于更精细的调整，可以使用 subplots_adjust
g.fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# 显示图形
plt.show()
