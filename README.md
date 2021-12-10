# TaobaoRobot
淘宝定时抢购脚本

## 详细步骤

### STEP1. 克隆代码到本地

```shell script
git clone https://github.com/QixinLi/TaobaoRobot.git
```

如没有安装git，可直接在网页上点击download zip，并解压

### STEP2. 安装python

自行百度（版本任意，我用的3.8）

### STEP3. 安装python依赖

```shell script
pip install selenium
```

看到Successfully installed就ok，如有error可以不用管

### STEP4. 下载并配置chromedriver

[下载安装方式自行百度](https://blog.csdn.net/qq_40604853/article/details/81388078)

在```fuck.py```第```11```行中，将""内的地址改为自己chromedriver的绝对路径

### STEP5. 配置抢购时间

在```fuck.py```第```48```行中，修改时间为抢购时间

注意格式：```YYYY-MM-DD hh:mm:ss```

### STEP6. 运行

```shell script
python fuck.py
```

准备好淘宝app，在弹出框中扫码登录

### STEP7. 安静等待抢购结束
