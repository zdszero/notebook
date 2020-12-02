# clipboard种类

x window system中有两种剪切板，被称为selection机制。

1. PRIMARY：当鼠标选中文本时，选中的文本自动被复制到剪切板，按下鼠标中间的按键进行粘贴。
2. CLIPBOARD：一般的剪切板，同windows的剪切板。

除此之外，linux中还有一个cut buffer机制，xclip默认使用的是cut
buffer机制，加上`-selection cliobaord`字段使用clipboard selection

# xclip uasge

```sh
# paste image
xclip -selection clipboard -t image/png -o > test.png
# copy image
xclip -selection clipboard -i test.png
# use xclip with pipe
echo 'Hello world' | xclip
```
