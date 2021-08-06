# encoding = utf -8
# 定义整个框架中所需要的一些全局常亮值，
import os

# 获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#cookie路径
# cookiePath_master=parentDirPath+"\\datas\\token_master.txt"
# cookiePath_brench=parentDirPath+"\\datas\\token_branch.txt"

# json数据绝对路径
jsonPath = parentDirPath + "\\datas\\"


#报告数据的绝对路径
reportPath = parentDirPath+"\\report\\"

# 测试数据文件存放绝对路径
# dataFilePath = parentDirPath + "\\testData\\126邮箱发送邮件.xlsx"
#

