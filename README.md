 # R I M E B R E W
The Canonical RIME Schema Manager.

![Peek 2020-10-11 23-52](https://user-images.githubusercontent.com/20123683/95703540-23415080-0c1d-11eb-8663-1af78e76d624.gif)


# 使用方法

Python 3.6+。把整个源码包丢到 用户的配置文件夹 下面，按上图操作

```
./rimebrew
```

# 相关链接

进度和想法 <https://github.com/users/shenlebantongying/projects/2>

仓库地址 <https://github.com/rimebrew/rime_bundle>

# 发行方案

+ Windows 预计使用 Cython 转换成 C 后编译发行。备用方案是从观望上下载 embed 版 py（压缩包15mb）

+ 我会按照 RPM + Homebrew -> Windows -> pypi 的顺序来制作
+ Ubuntu/Debian -> 暂无计划，需要其他人

# Plan

+ 向朋友推荐 RIME 的时候，可以配合这个工具几分钟以内完成安装，且迅速地尝试多种输入方案
+ 设计了新的输入法，不需要用户读任何说明来安装

+ 创建一个 Index 来收集现有的诸多方案
+ 配置功能，rimebrew 要能够理解配置文件以此来
+ 实现 [plum #4](https://github.com/rime/plum/issues/4)


## FAQ

### Why python？

+ 真正的 ** 跨三大平台**
+ Windows 没有 bash
+ C/C++ 可行，但开源项目没人愿意看一堆指针
+ 那为何不用 Go/Rust，历史太短，且更新活跃。
  + 对比之下 Python 上有 PyYAML, click ,Bottle这种打磨了十多年的库
  + 这些库的存在完美的解决了跨平台问题
+ Tcl/Lua/Perl 这些现代的人可能不太会用了

### 为什么重写, 不用 /plum/？

+ Bash 自身缺陷诸多，项目稍微大一点就无法维护，[什么是“脚本语言”]<http://www.yinwang.org/blog-cn/2013/03/29/scripting-language>
+ Bash 没有任何工具支持，不能像py一样可以随意重构，需要开发者极高的bash使用经验。
+ Windows 上不是所有人都有 wsl/cygwin/mysys2 之类的东西，额外维护一套 cmd/powershell 又需要更多精力和知识

### 图形界面？

+ 正在做，web_ui
+ Python 自带一个 http.server，启动后直接用浏览器操作就可以了
+ 可以复用一些之前 @lotem 的代码 [rimekit]<https://github.com/lotem/rimekit>

### 为什么闷声不响地做出来

+ 现有的大部分包管理器都是有缺陷的
    + Py 的 pip 无法管理版本号，只能大概给个依赖关系 -> 需要 requirement.txt/virtualenv 来隔离环境+锁定版本
    + Flatpak 软件和特定版本的“运行环境”绑定 -> 如果一个软件不及时更新 -> 一个小软件都要下载一大个运行环境
    + Ocaml 的 OPAM 很严谨，但是一旦升级一个软件，就要下载重新编译一连串的整个依赖，并且严格地拒绝安装不兼容的软件包
    + NPM -> node_modules
    + Debian/RHEL/openSUSE Leap -> 依赖操作系统的大版本，将 kernal 之类的固定版本，大部分软件落后后 upstream 几个版本
    + ArchLinux/openSUSE TW -> 滚动升级，不一定那天就挂了

+ 由此许多设计上的问题会有好有坏，很难讨论出结果

REF: 

[Managing the Complexity of Large Free and Open Source Package-Based Software Distributions](https://hal.archives-ouvertes.fr/file/index/docid/149566/filename/ase.pdf)

<https://book.douban.com/subject/25881855/>

#### RIME 和其他的包管理需求上区别

+ 不需要版本管控 -> 包与包之间依赖不大
+ 一次性 -> 大部分人只会用几次，刚安装啥东西都尝试一下，或者想换口味的时候用一波
+ 虽然RIME标榜定制性极强，但其强大的功能不能发挥出来，即给非程序员使用。

#### 为什么和直接把几个 py 的库丢到源码里？

包含的几个都是经过多年开发几乎不更新的库，要升级 diff 一下就可以。而且这样没有任何依赖纯粹 python 做的可以轻松用 Cython 翻译成 C 语言后给 Windows。

    
