## github-md-toc

> GitHub没有提供 `[TOC]` 类似的功能来为 Markdown 文件(如`README.md`)自动生成目录（TOC），这一点很遗憾；
> 这尤其在一些较长的 Markdown 文件中就显得更伤人了，因此造一些辅助工具必不可少。

查阅了很多资料，具体的参考文献有[下面这些](#reference)，有兴趣的可以多看看

总结一下，基础的TOC生成并不难，但其中有很多小细节处理起来有些麻烦：

* 标题中的特殊字符，如`&`、`#`、`.`、`(`、`)`，甚至`空格`等的处理是不同的，举例来说，`.`当做 `不存在` 来处理(换言之，将其删去)，`&`当做 `不存在` 来处理；
* 标题中的所有大写字母应当全部转成小写字母处理。

## Usage

> 支持 `python 2.\*` 与 `python 3.\*`，所以`python2` 与 `python3`之间的切换随你的意都行

```shell
python github-md-toc.py </path/to/your/file.md> [<tab_length>]
```

相信可以看懂上面几个选项的含义，如 `[<tab_length>]`指的是`TAB键`代表的空格数

![](http://pcx2lec2u.bkt.clouddn.com/201808050117_701.gif)

直接点击`run.bat` 即可执行脚本，毕竟其中的内容同上面的shell指令是一致的，用文本编辑器打开就知道了

![](http://pcx2lec2u.bkt.clouddn.com/201808050120_594.gif)

上面动图中用的都是`python35`(即`python3`)，但若是出现下面这样的问题，建议尝试切回 `python2` 去试试，如果还是不行，欢迎在 [issues](https://github.com/zhouie/github-md-toc/issues) 提问交流

```shell
$ python35 github-md-toc.py ./test_dir/EXAMPLE.md 2
Traceback (most recent call last):
  File "github-md-toc.py", line 11, in <module>
    lines = f.readlines()
UnicodeDecodeError: 'gbk' codec can't decode byte 0x89 in position 226: illegal multibyte sequence
```

## License

MIT license

## Reference

* [psmiraglia - mdtocgen](https://github.com/psmiraglia/mdtocgen)
* [sk1418 - ghtoc](https://github.com/sk1418/ghtoc)
* [zhangzhongjun - AutoToc](https://github.com/zhangzhongjun/AutoToc)
* [zhangdanzhu - github_markdown_toc](https://github.com/zhangdanzhu/github_markdown_toc)
* [Sl0v3C - github-toc](https://github.com/Sl0v3C/github-toc)
* [gtaifu - gfm_toc_generator](https://github.com/gtaifu/gfm_toc_generator)