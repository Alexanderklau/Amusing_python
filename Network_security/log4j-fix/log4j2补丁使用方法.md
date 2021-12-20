# log4j2 补丁使用方法

在 infinity里面，涉及到log4j2使用的只有ElasticSearch

有风险的log4j2版本为

```
2.0 <= Apache log4j2 <= 2.16.1
```

infinity使用的es版本为6.3.2

log4j2的版本为log4j2-14

所以需要进行修复

## 脚本使用方法

### 验证风险

```shell
bash log4j-fix.sh check
```

此处会遍历Es或者其他java家族的安装目录，需要等待几秒

如果检测到log4j2的版本小于15.1版本，则会马上提示需要替换文件


### 替换文件并且更新

停止Elasticsearch服务

```shell
systemctl stop elasticsearch
```


执行脚本

```shell
bash log4j-fix.sh update 
```

此处会从我们的log4j2-15文件夹进行替换，将替换所有小于15.1版本的jar包

替换完毕会返回**替换成功**的提示

此时需要重启elasticsearch

```shell
systemctl start elasticsearch
```

### 出现问题后的回退

在替换文件夹下会出现一个备份文件夹，名为**bak**

替换前的文件都会被迁移到这里，如果出现问题

可以参照replace.log文件进行回滚

