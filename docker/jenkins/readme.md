# 第1章 导读

    版本控制系统+持续集成工具+部署工具=持续交付
    
# 第2章 Gitlab模块

## GitLab介绍

什么是gitlab

    gitlab是一个开源分布式版本控制系统
    开发语义ruby
    功能管理项目源代码,版本控制,代码复用与查找
    
gitlab与github的不同

    github分布式在线代码托管仓库,个人版本可直接在先免费使用,企业版本收费且需要服务器安装
    gitlab分布式在线代码仓库托管软件,分社区免费版本与企业收费,都需要服务器安装
    
gitlab的优势和应用场景

    开源免费,适合中小型公司将代码放置在该系统中
    差异化的版本管理,离线同步以及强大分支管理功能
    便捷的gui操作界面以及强大的账户权限管理功能
    集成度很高,能够集成接大多数的开发工具
    支持内置ha,保证在高并发下仍旧实现高可用性
    
gitlab主要服务构成

    nginx静态web服务器
    gitlab-workhorse 轻量级的反向代理服务器
    gitlab-shell 用于处理git命令和修改authorized keys列表
    logrotate 日志文件管理工具
    postgresql 数据库
    redis 缓存服务器
    
## GitLab工作流程

    创建并克隆项目
    
    创建项目feature分支
    
    编写代码并提交至该分支
    
    推送该项目分支至远程gitlab服务器
    
    进行代码检查并提交master主分支合并申请
    
    项目领导审查代码并确认合并申请

## GitLab安装配置管理

利用virtualbox创建测试服务器

安装gitlab前系统预配置准备工作

    1\关闭firewalld防火墙
        # systemctl stop firewalld  关闭防火墙
        # sysemctl disable firwalld  禁止开机启动
        
    2\关闭selinux并重启系统,强制访问控制安全策略
        # vi /etc/sysconfig/selinux
        
        ...
        selinux=disabled
        ...
    
        # reboot 重启
        
安装 Omnibus gitlab-ce package,快速安装所有gitlab组件

    1\安装gitlab组件
        # yum -y install curl policycoreutils openssh-server openssh-clients postfix
        
    2\配置yum仓库
        # curl - sS https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.rpm.sh | sudo bash
        
    3\启动postfix邮件服务
        # systemctl start postfix && systemctl enable postfix
        
    4\安装gitlab-ce社区版本
        # yum install -y gitlab-ce
        
Omnibus gitlab等相关配置初始化并完成安装

    1\证书创建与配置加载
    2\nginx ssl代理服务配置
    3\初始化gitlab相关服务并完成安装

    