## 2022-Fundamental-of-Data-Science-Project
此项目为南京大学软件学院“数据科学基础2022”大作业

主题：文本扩增

组长：201250067 赵简

组员：201250044 王星云、201250044 薛瑞宸

邮箱：201250044@smail.nju.edu.cn

开源链接：https://github.com/NebularW/text_amplification

小组分工：

- 爬虫模块：薛瑞宸
- 文本扩增模块：徐浩钦、王星云
- 评价指标模块：赵简
- 数据处理与分析：赵简，薛瑞宸，王星云
- 文档撰写：王星云

------

[TOC]

------

### 项目开始

#### 解决的问题：

构建司法相关文本的文本扩增应用。其主要功能模块包括：

1. ##### **爬虫模块：**

   利用自动化爬虫工具从浙江省人民政府网站爬取大量的政务报告，并且划分为短文本，作为数据源。

2. ##### **文本模块：**

   对传入的文本，通过自然语言处理，以回译、EDA的方式生成扩增文本。

3. ##### **评价指标模块：**

   对扩增的文本使用BLEU评价指标进行评价，完美匹配的得分为1.0，而完全不匹配则得分为0.0。

#### 解决思路：

1. ##### **爬虫模块：**

   //TODO
   
2. ##### **文本扩增模块：**

   1. 使用百度翻译api，以回译的方式（将文本翻译为其他语言，再翻译回来）扩增文本
   1. 使用nlpcda，以随机同义词替换、等价字替换、随机字删除的方式扩增文本
   1. 将扩增的文本保存在本地的output文件夹内
   
3. ##### **评价指标模块：**

   //TODO

------

### 项目构建

#### 爬虫模块：**`crawler.py`**

运行后会在相同目录下生成新的text文件夹，保存300份政务相关文本于该文件夹中。

```python
def Crawler()
```

#### 文本扩增模块：**`amplification_back_translate.py` `amplification_eda.py`**

**函数说明：**

1.传入文件所在路径（相对路径、绝对路径皆可），和文件命名（无.txt后缀），返回回译扩增的文本，并保存至本地

```python
def back_translate(filepath, filename)
```

2.传入文件所在路径（相对路径、绝对路径皆可），和文件命名（无.txt后缀），返回eda扩增的文本，并保存至本地

```python
def eda(filepath, filename)
```

#### 评价模块：**`evaluate_bleu.py`** 

传入参考文本和需要被评价文本的文件路径，返回BLEU评价值

```python
def evaluate_bleu(candidate_filepath, references_filepath)
```



------

### 项目测试

1. ##### **爬虫模块：**

   写有供手工测试用的main函数。

   测试方法：

   1. 运行即可开始自动爬虫，保存文本至本地。

2. ##### **文本扩增模块：**

   写有供手工测试用的main函数。

   测试方法：

   1. 手工修改main函数中文件路径。
   2. 运行即可生成测试结果。
   
3. ##### **评价指标模块：**

   写有供手工测试用的main函数。

   测试方法：

   1. 手工修改main函数中文件路径。
   2. 运行即可生成测试结果。

------

### 环境配置

1. ##### **爬虫模块：**

   1. requests库，安装方法：在Windows系统cmd中 `pip install requests`
   2. BeautifulSoup库，安装方法：在Windows系统cmd中 `pip install BeautifulSoup4`
   3. lxml库，安装方法：在Windows系统cmd中`pip install lxml`

2. ##### **文本扩增模块：**

   1. requests库，安装方法：在Windows系统cmd中 `pip install requests`
   2. codecs库，安装方法：在Windows系统cmd中 `pip install codecs`
   3. nlpcda库，安装方法：在Windows系统cmd中 `pip install nlpcda`

3. ##### **评价指标模块：**

   1. codecs库，安装方法：在Windows系统cmd中 `pip install codecs`



------

### 相关功能的思考

1. ##### **爬虫模块：**

   - ​	//TODO
   
2. ##### **文本扩增模块：**

   - 使用回译方法扩增文本的速度较快，但是文本评价指标低
   - 使用eda方法扩增文本的速度较慢，第一次运行可能需要一定时间加载模型，但是文本评价指标较高

3. ##### **评价指标模块：**

   - //TODO   可以说些中文、文本长度过长导致的困难和解决思路



