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
  input_lines.push(line); //[ '3', '8 12 40' ]ここで、input_lines配列に、標準入力から渡されたデータが入る
});

// ーーーー出力ーーーー
reader.on("close", () => {
  //受け取ったデータを用いて処理を行う
  var arr = input_lines[1].split(" "); //[ '8', '12', '40' ]
  var count = 0;
  var isOdd = false;
  while (true) {
    for (let i = 0; i < arr.length; i++) {
      //奇数だったら次の処理へ
      if (arr[i] % 2 !== 0) {
        isOdd = true;
        break;
      }
    }
    //奇数だったらwhileを抜ける
    if (isOdd) {
      break;
    }
    //arrを2で割って配列へ代入
    arr = arr.map((value) => value / 2);
    count += 1;
  }

  console.log(count);
});
