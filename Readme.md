# 颜色分类器

## 环境说明

python版本： python3.6(pytorch_cpu)

IDE：PyCharm 2019.3.4

## 功能

用户判断给出的随机颜色的喜欢与否。程序根据用户的选择进行学习，进而预测用户对于一些新产生的随机颜色的喜欢与否。

## 运行方法

在anaconda虚拟python环境下安装pytorch包之后，导入project并执行main.py，程序按顺序运行。

## 原理

这是一个最简单最基础的分类器算法：设颜色的特征向量为 $[R, G, B]$ ，则预测函数为

![h](https://github.com/XuShen97/ColorClassify/tree/master/img/h.png)

损失函数：
![j](https://github.com/XuShen97/ColorClassify/tree/master/img/j.png)

使用梯度下降法求解最优值，更新方法：

![theta](https://github.com/XuShen97/ColorClassify/tree/master/img/theta.png)

其中x, y是向量，以确保同时更新θ

参数表

|α|[θ_0, θ_1, θ_2, θ_3 ]|ε|
|:---:|:---:|:---:|
|1e-5|[-1, -1, -1, -1]|1e-3|

作者为其写了一些输入输出的图形界面，以便于使用。

## 不足与反思

1. 参数值仍有待改进。参数选择还没有经过反复测试，有时会在计算时出现数据溢出的情况，且有些时候梯度下降会较慢。
2. 我曾尝试将其封装为exe程序便于移植，但受困于pytorch包，封装的程序不能运行。
3. 程序结构上，大量依赖外部txt等文档，不利于程序移植性。当然，在移植问题上，pytorch是主要原因。
