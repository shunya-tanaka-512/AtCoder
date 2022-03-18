process.stdin.resume();
process.stdin.setEncoding("utf8");

var input_lines = []; //標準入力から受け取ったデータを格納する配列
var reader = require("readline").createInterface({
  //requireという処理でreadlineという機能を用いて標準入力からデータを受け取る
  input: process.stdin,
  output: process.stdout,
});

// ーーーー入力ーーーー

reader.on("line", (line) => {
  //line変数には標準入力から渡された一行のデータが格納されている
  input_lines.push(line); //ここで、input_lines配列に、標準入力から渡されたデータが入る
});

// ーーーー出力ーーーー
reader.on("close", () => {
  //受け取ったデータを用いて処理を行う
  const [a, b, c, x] = input_lines;
  let count = 0;
  for (let i = 0; i <= a; i++) {
    if (500 * i > x) {
      break;
    }
    tmp = x - 500 * i;
    for (let j = 0; j <= b; j++) {
      if (100 * j > tmp) {
        break;
      }
      if (tmp - 100 * j <= 50 * c) {
        count += 1;
      }
    }
  }

  console.log(count);
});
