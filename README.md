# python-
学习简明python后，书中要求的第一个程序

#那些经验#

1、cPickle的load函数读取文件为空文件，则报错：EOFError
2、cPickle的load函数读取文件，文件以“a"的方式打开则报错：IOError: [Errno 0] Error
3、命令行运行程序，报错：print IOError: [Errno 0] Error，不识别中文，编码格式的问题（需要解决）
4、一开始将load函数放在了循环内，导致无法将结果写入文件中。按照continue的逻辑，应该是直接回到while循环，导致永远无法将结果保存到文件，理论上来讲应该是输入4，跳出循环，执行最后的语句，但是在idle中如果直接中断进程也能保存结果到文件！（该怎么查看程序运行内存中结果的变化呢？）
5、a_b【name】不要用引号括起来name，否则无法保存结果
