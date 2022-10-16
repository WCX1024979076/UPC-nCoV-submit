# UPC-nCoV-submit
## 自动填写中国石油大学（华东）疫情防控通

### 一、说明

本程序仅供研究交流使用，如果填报表中任意情况发生变化，比如地点发生变化，请务必在程序运行之前手动打卡。

### 二、本地服务器填报方法

使用方法：

1. 修改 `自动填表/用户信息.txt` 里面的账号密码信息

2. 修改 `自动填表/疫情.py` 中的路径信息

3. 运行 `自动填表/疫情.py`

注：可以将代码git clone到Linux服务器中，通过crontab定时运行py文件，食用性更佳。

### 三、利用 Github Action自动填报

使用方法：

1. 将本仓库代码Fork到自己的用户名下

2. 添加secret token

![screencapture-github-WCX1024979076-UPC-nCoV-submit-settings-secrets-actions-2021-09-26-17_50_19.png](https://i.loli.net/2021/09/26/yxGTg5UdpOSR2r4.png)

转到仓库目录以后，按照图示顺序添加secret token，名称为USER，内容为数字石大账号和密码信息，示例如下：

```json
{"username": "学号","password": "数字石大密码"}
```

![image.png](https://i.loli.net/2021/09/26/ekzrAtZMNTo3Wxb.png)

3. 等待第二天的运行结果，本脚本定时运行于每日八点，可以从Action界面查看运行结果。

![image.png](https://i.loli.net/2021/09/26/6j98LFcuHJ4Geit.png)
