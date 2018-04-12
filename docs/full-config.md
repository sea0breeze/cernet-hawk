# 安装

在干净的Ubuntu系统中执行以下命令

```shell
sudo apt install git
git clone https://github.com/sea0breeze/cernet-hawk.git
chmod +x cli/install.sh
chmod +x cli/iptables.sh
chmod +x do.sh

./cli/iptables.sh
./cli/install.sh
```

# 配置

配置相关的文件均存在于``cernet-hawk/config``文件夹中，其中除了 ``./config/cernet.conf`` 和 ``./config/cernetv6.conf``，均配置了合适的默认配置。

## celery.py

- ``backend`` amqp连接地址，系统默认连接本地amqp，如需自定义amqp配置，请修改
- ``broker`` amqp连接地址，系统默认连接本地amqp，如需自定义amqp配置，请修改
- ``flower`` flower运行地址，如需自定义flower，请修改
- ``apitasks``flower运行地址，如需自定义flower，请修改
- ``TIMELIIMIT`` 单个任务运行时间，单位为秒，到达该限制后会强制结束
- ``SOFTTIMELIIMIT``  单个任务运行时间，单位为秒，到达该限制后会发起结束信号
- ``RATELIMIT`` 每小时最大任务数
- ``MAXRUNLIMIT`` 最多运行任务数
- ``ZMAPLIMIT`` 执行ZMAP的进程上限
- ``NMAPLIMIT`` 执行NMAP的进程上限
- ``SERVICESLIMIT`` 执行端口扫描的进程上限

## common.py

- ``NMAP_CMD`` NMAP执行命令
- ``ZMAP_CMD`` ZMAP执行命令
- ``PORTS`` 扫描端口
- ``CONSOLE_PRINT`` 输出日志的debug等级
- ``pause`` 每次分发任务等待时间
- ``servicesShouldHandle`` 会加载的模块

## mode.py

配置模式，可指定``PRODUCT``/``TEST``/``LOCAL``三种模式

## paths.py

各种字典和文件的默认目录配置，请勿修改

## websrv.py

Web服务器相关配置，请勿随意修改

## cernet.conf

请在``config``目录下创建该文件，把要扫描的ipv4或网段加入该文件中，每行一个ip或者CIDR格式的子网，且每行带上换行符。样例如下：

```
8.8.8.8/24
1.1.1.1
```

## cernetv6.conf

请在``config``目录下创建该文件，把要扫描的ipv6或网段加入该文件中，每行一个ipv6，且每行带上换行符

```

```

# 运行

开启数据库

```
service mongodb start
service rabbitmq start
```

简单启动所有服务

```
./do.sh startall
```

启动worker

```
./do.sh startworker
```

启动任务分发

```
./do.sh startd
```

启动flower监控

```
./do.sh flower
```

启动web服务器

```
./do.sh web
```

# 监控

启动Flower后，可以在本机的5555端口查看当前运行情况。
启动Web服务器后，可以在本机8888端口查看运行结果。
