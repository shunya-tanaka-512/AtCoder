process.stdin.resume();
process.stdin.setEncoding('utf8');

var input_lines = [];  //標準入力から受け取ったデータを格納する配列
var reader = require('readline').createInterface({  //requireという処理でreadlineという機能を用いて標準入力からデータを受け取る
  input: process.stdin,
  output: process.stdout
});

// ーーーー入力ーーーー

reader.on('line', (line) => {  //line変数には標準入力から渡された一行のデータが格納されている
  input_lines.push(line);  //ここで、input_lines配列に、標準入力から渡されたデータが入る
});


// ーーーー出力ーーーー
reader.on('close', () => {  //受け取ったデータを用いて処理を行う
  tmp = input_lines[1].split(" ");
  var a = parseInt(input_lines[0]);
  var b = parseInt(tmp[0]);
  var c = parseInt(tmp[1]);
  var s = input_lines[2];
  console.log(a + b + c, s);
});
