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
