# R I M E B R E W
A RIME Schema Manager prototype. 

**I think what we really want is something like YaST that you can just point and click, everything is done. No search anything, No read any manual, No terminal.**

**I currently working on a GUI client rather than a console interface ->** [rimebrew_qt](https://github.com/rimebrew/rimebrew_qt)

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

### 为什么重写, 不用 /plum/？

+ Bash 自身缺陷诸多，项目稍微大一点就无法维护，[什么是“脚本语言”]<http://www.yinwang.org/blog-cn/2013/03/29/scripting-language>
+ Bash 没有任何工具支持，不能像py一样可以随意重构，需要开发者极高的bash使用经验。
+ Windows 上不是所有人都有 wsl/cygwin/mysys2 之类的东西，额外维护一套 cmd/powershell 又需要更多精力和知识

+ 现有的大部分包管理器都是有缺陷的
    + Py 的 pip 无法管理版本号，只能大概给个依赖关系 -> 需要 requirement.txt/virtualenv 来隔离环境+锁定版本
    + Flatpak 软件和特定版本的“运行环境”绑定 -> 如果一个软件不及时更新 -> 一个小软件都要下载一大个运行环境
    + Ocaml 的 OPAM 很严谨，但是一旦升级一个软件，就要下载重新编译一连串的整个依赖，并且严格地拒绝安装不兼容的软件包
    + NPM -> node_modules
    + Debian/RHEL/openSUSE Leap -> 依赖操作系统的大版本，将 kernal 之类的固定版本，大部分软件落后后 upstream 几个版本
    + ArchLinux/openSUSE TW -> 滚动升级，不一定那天就挂了

+ 由此许多设计上的问题会有好有坏，讨论来讨论去，很难讨论出结果，要做一些 trade-offs


#### RIME 和其他的包管理需求上区别

+ 不需要版本管控 -> 包与包之间依赖不大
+ 一次性 -> 大部分人只会用几次，刚安装啥东西都尝试一下，或者想换口味的时候用一波，其余时间可能就是自动更新词库
+ 虽然RIME标榜定制性极强，但其强大的功能不能发挥出来，即给非程序员使用。


#### 版本控制

+ 输入法会更新，但不会像其他软件一样打破兼容性。一切以最新版为主。
+ 唯一的版本控制就是：在本地更新前创建一个当前的配置的 snapshot，如果更新破坏了，就直接 rollback
+ 另外一旦失败就打印一份详细的出错说可以用来复制粘贴

# Updated New Plan

被 plum 带歪了, recipe 或者任何的类似 spec 的文件可以是不必要的。

rime 里面的输入法就是 一个 xxx.custom.yaml + 字典文件，当然有几个特殊的带了 opencc 或者 lua 的文件，这些特殊的处理，现有的仓库都有约定成俗的目录结构。从一个仓库里面直接“猜”出来有哪些 xxx.custom.yaml 是可行的。

plum 里面剩下的内容是重复的，而且 patch_file 那行并不是很灵活，<https://github.com/rime/rime-emoji/blob/master/customize.recipe.yaml>。

有必要的话，可能需要给 [schema.yaml](<https://github.com/LEOYoon-Tsaw/Rime_collections/blob/master/Rime_description.md>) 里面添加一个额外的参数。

简而又简 :)

至于“混合体”输入法，据说直接在dependency 里面添加一行即可，但是现实情况会比较tricky。


# Update on Copy & Paste replacement

After user installed an app, you can register a custom url schema (i.e. browser protocols) like below:

```
x-github-client://openRepo/https://github.com/rimebrew/rimebrew
atom://settings-view/show-package?package=teletype
```
So that users can just click the link, the launch the app automatieclly.

like:
```
x-rimebrew://package/v1?package=luna-pinyin-schema.yaml
```
There are two RFCs related to this

[rfc7595](https://tools.ietf.org/html/rfc7595)

[rfc8252](https://tools.ietf.org/html/rfc8252)

A how to guide:
<https://support.shotgunsoftware.com/hc/en-us/articles/219031308-Launching-applications-using-custom-browser-protocols>

Apple's offical guide

<https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app?language=objc>

You can actually just insert related content to the `.plist` inside the `.app`.


ArchLinux wiki:
<https://wiki.archlinux.org/index.php/XDG_MIME_Applications>

As it says, you can just modify the `mimeapps.list` file for browsers to support it.

MSDN:
<https://docs.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa767914(v=vs.85)?redirectedfrom=MSDN>


# Note:

Use a command line is too **Nerd** and complex for a simple app. Its not a serious pkg manager like the ones for an OS.

Its should be as simple as Drag -> Drop then finished!

Just write something like GNOMEs' but simpler. <https://addons.mozilla.org/en-CA/firefox/addon/gnome-shell-integration/>

Drag an icon or a link from browser to a window, Done.

What else is required? A config windows.

# How to create an Firefox extension that can communicaet with local machine

https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Native_messaging
