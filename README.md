# Note:

Use a command line is too **Nerd** and complex for a simple app. Its not a serious pkg manager like the ones for an OS.

Its should be as simple as Drag -> Drop then finished!

Just write something like GNOMEs' but simpler. <https://addons.mozilla.org/en-CA/firefox/addon/gnome-shell-integration/>

Drag an icon or a link from browser to a window, Done.

What else is required? A config windows.

# R I M E B R E W
The Canonical RIME Schema Manager.

[![PyPI version](https://badge.fury.io/py/rime-brew.svg)](https://pypi.org/project/rime-brew/)
[![opensuse](https://img.shields.io/badge/openSUSE-testing-green?style=flat-square&logo=openSUSE&link=https://build.opensuse.org/package/binaries/home:slbtongying/rimebrew/openSUSE_Leap_15.2)](https://build.opensuse.org/package/binaries/home:slbtongying/rimebrew/openSUSE_Leap_15.2
)
[![windows_testing](https://img.shields.io/badge/Windows-Testing-9cf?style=flat&logo=Windows)](https://github.com/rimebrew/rimebrew/releases/tag/v1.0_win
)
![demo](https://user-images.githubusercontent.com/20123683/95703540-23415080-0c1d-11eb-8663-1af78e76d624.gif)


# 使用方法

## Windows
```
下载
https://github.com/rimebrew/rimebrew/releases/tag/v1.0_win
```
## pip
```
# python3.6+
pip install rime-brew
```

## package managers

### openSUSE

```
https://build.opensuse.org/package/binaries/home:slbtongying/rimebrew/openSUSE_Leap_15.2

```

目前只实现了三个简单的功能
```
./rimebrew update
           list
           install
```

# 相关链接

在线查看已经收录的包 <https://rimebrew.github.io/index.html>

进度和想法 <https://github.com/users/shenlebantongying/projects/2>

仓库地址 <https://github.com/rimebrew/rime_bundle>

# 发行方案

+ 我会按照 RPM + Homebrew -> Windows 的顺序来制作
+ Ubuntu/Debian -> 暂无计划，需要其他人

# Plan

+ 实现 plum 的所有功能。

+ 向朋友推荐 RIME 的时候，可以配合这个工具几分钟以内完成安装，且迅速地尝试多种输入方案
+ 设计了新的输入法，不需要用户读任何说明来安装
+ 提供简洁的升级方案
+ 创建一个 Index 来收集现有的诸多方案
+ 配置功能，rimebrew 要能够理解配置文件以此来
+ 实现 [plum #4](https://github.com/rime/plum/issues/4)

+ Profile_switcher?
+ 云输入？用户可以选择上传自己的字典。

+ 完成后发布 1.0


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
+ Python 自带一个 http.server，启动后直接用浏览器操作就可以了 （就和 Jupyter 一样）
+ 可以复用一些之前 @lotem 的代码 [rimekit]<https://github.com/lotem/rimekit>
+ possible design: https://github.com/rime/home/issues/336#issuecomment-473100326
+ ~~浏览器插件不现实，不是每个人都用 Firefox 和 Chrome~~

### 为什么闷声不响地做出来

+ 现有的大部分包管理器都是有缺陷的
    + Py 的 pip 无法管理版本号，只能大概给个依赖关系 -> 需要 requirement.txt/virtualenv 来隔离环境+锁定版本
    + Flatpak 软件和特定版本的“运行环境”绑定 -> 如果一个软件不及时更新 -> 一个小软件都要下载一大个运行环境
    + Ocaml 的 OPAM 很严谨，但是一旦升级一个软件，就要下载重新编译一连串的整个依赖，并且严格地拒绝安装不兼容的软件包
    + NPM -> node_modules
    + Debian/RHEL/openSUSE Leap -> 依赖操作系统的大版本，将 kernal 之类的固定版本，大部分软件落后后 upstream 几个版本
    + ArchLinux/openSUSE TW -> 滚动升级，不一定那天就挂了

+ 由此许多设计上的问题会有好有坏，讨论来讨论去，很难讨论出结果，要做一些 trade-offs

REF: 

[Managing the Complexity of Large Free and Open Source Package-Based Software Distributions](https://hal.archives-ouvertes.fr/file/index/docid/149566/filename/ase.pdf)

<https://book.douban.com/subject/25881855/>

#### RIME 和其他的包管理需求上区别

+ 不需要版本管控 -> 包与包之间依赖不大
+ 一次性 -> 大部分人只会用几次，刚安装啥东西都尝试一下，或者想换口味的时候用一波，其余时间可能就是自动更新词库
+ 虽然RIME标榜定制性极强，但其强大的功能不能发挥出来，即给非程序员使用。

#### 为什么和直接把几个 py 的库丢到源码里？

包含的几个都是经过多年开发几乎不更新的库，要升级 diff 一下就可以。而且这样没有任何依赖纯粹 python 做的可以轻松用 Cython 翻译成 C 语言后给 Windows。


#### 版本控制

+ 输入法会更新，但不会像其他软件一样打破兼容性。一切以最新版为主。
+ 唯一的版本控制就是：在本地更新前创建一个当前的配置的 snapshot，如果更新破坏了，就直接 rollback
+ 另外一旦失败就打印一份详细的出错说可以用来复制粘贴

