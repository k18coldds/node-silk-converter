# 格式转换器：silk <=> PCM

## 如何在项目中引入改项目？

1. 使用下面命令进行安装


		npm install git+http://10.10.10.232:3000/wechat_crm/node_silk_converter.git -S --build-from-source --runtime=electron --target=2.0.2 --dist-url=https://atom.io/download/electron

2. 使用以下指令在install后重新构建

		electron-rebuild -f -w silk_converter
	

在我使用的项目中，我在package.json配置文件中增加配置如下：

```json
"scripts": {
    "preinstall": "npm install git+http://10.10.10.232:3000/wechat_crm/node_silk_converter -S --build-from-source --runtime=electron --target=2.0.2 --dist-url=https://atom.io/download/electron",
    "postinstall": "npm rebuild",
    "rebuild": "electron-rebuild -f -w silk_converter"
  },
```

## API使用

``` js
const silk_converter = require('silk_converter');

var silk_file_path = '';
var pcm_file_path = '';

var code = silk_converter.decode(silk_file_path, pcm_file_path);
if (code == 0) {
  console.log('success');
}

code = silk_converter.encode(pcm_file_path, silk_file_path);
if (code == 0) {
  console.log('success');
}
```
