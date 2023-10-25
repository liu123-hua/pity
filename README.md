[English](https://github.com/wuranxu/pity/blob/main/README_EN.md)

### Docker部署

1. 安装Docker Desktop
2. 打开终端并进入pity目录
3. 执行以下命令，安静等待pity启动即可（不需要额外安装mysql redis等，一键启动直接起飞）

  **docker镜像由卫衣哥（QYZHG倾情制作👏👏👏）**

```bash
docker-compose -f .\ops\docker-compose.yaml up
```

### 🎉 二次开发

1. 拉取代码

```bash
$ git clone https://github.com/wuranxu/pity
$ cd pity
```

2. 安装依赖

```bash
# 可换豆瓣源或者清华源安装依赖
$ pip install -r requirements.txt
```

3. 安装并启动redis

4. 安装并启动mysql

5. 修改conf/dev.env

修改其中mysql和redis连接信息，redis虽然可以不开启，但是会导致`定时任务重复执行`（基于redis实现了分布式锁）。

6. 启动服务

```bash
$ python pity.py
```

7. 注册用户

打开浏览器输入: `http://localhost:7777`进入登录页。

点击注册按钮，第一个注册的用户会成为`超级管理员`，拥有一切权限。

![](https://static.pity.fun/picture%2F%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20220504235808.png)

登录后就可以开启pity之旅啦！


### 😊 已有功能

+ [x] 🔥 完善的用户登录/注册机制，提供第三方(github)登录
- [x] 🀄 完善的项目管理机制
* [x] 🚴 结合FastApi，利用asyncio让Python代码也可以起飞
- [x] 💎 完整的接口测试流程
- [x] 📝 强大的数据构造器, 解决接口数据依赖问题
- [x] 🎨 在线调试http请求，堪比网页版本postman
- [x] 🍷 完善的全局变量机制，拒绝case中的死数据
- [x] 🚀 速度还挺快的
- [x] 🐍 在线redis请求
- [x] 🐎 测试计划/集合
- [x] 🙈 在线数据库ide，数据库管理功能
- [x] 📰 漂亮的邮件通知
- [x] 😹 定时构建测试用例
- [x] 🐧 精美的测试报告展示页面

## 🙋 待开发的功能

- [ ] 💀 app管理功能，支持app的导入和导出

* [ ] 😼 ~~代码覆盖率增量/全量统计功能~~

- [ ] 🐘 微服务化
- [ ] 🐄 数据工厂，强大的造数功能
- [ ] 🐸 用例支持har，jmx等格式导入
- [ ] 👍 CI/CD，类pipeline功能
- [ ] 🌼 推送功能，支持钉钉/企信推送
- [ ] 🌛 支持dubbo/grpc
- [ ] 🐛 打通yapi
- [ ] 🌽 等等等等
