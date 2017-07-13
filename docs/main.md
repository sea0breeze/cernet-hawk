# Hawk

## 目录

1. Hawk是什么
2. 安装
3. 运行
4. 目录结构
5. 运行机制
6. 插件编写
7. 其他

## 1. Hawk是什么

1.1 简介

分布式服务扫描工具

## 2. 安装

数据库服务器

安装mongo

扫描服务器

安装nmap

Web服务器

安装python

任务分发服务器

安装celery

## 3. 运行

## 4. 目录结构

- common: 公共库函数以及全局需要用到的比如说配置文件
    - config: 配置目录
    - constant: 常量相关目录
    - utils: 工具函数库
    core: 核心函数
    log: 日志相关函数
- doc: 放置文档的目录
- extension: 预留扩展层
- tmp
  - log: 日志文件，pid文件存放目录
  - pickle: 临时文件存放
- orm: 数据库的配置和定义文件
    - schema: 数据库定义文件
    - tables: 存放orm
- module: 分布式扫描相关目录
    - nmap: nmap相关目录
    - scan: 服务扫描放置目录
- thirdparty: 第三方依赖库目录
- toolkit: 一些工具目录
    - install: 安装脚本目录
- websrv: Web服务相关目录
    - controller: Web Controller目录
    - static: 静态文件放置目录
        - bower: bower放置目录
        - css
        - images
        - js
        - templates

## 5. 运行机制

每天

启动nmap，获取端口信息，存入数据库
拉取数据库信息，分配任务给子模块，存入数据库

## 6. 插件编写


## 7. 其它

代码规范请遵守PEP8