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
  const [yen500Num, yen100Num, yen50Num, yenSum] = input_lines;
  const FIVE_HUNDRED = 500;
  const ONE_HUNDRED = 100;
  const FIFTY = 50;
  let count = 0;
  for (let i = 0; i <= yen500Num; i++) {
    //答えゼロパターン：合計金額に持っている硬貨が足りない時
    if (yen500Num * FIVE_HUNDRED + yen100Num * ONE_HUNDRED + yen50Num * FIFTY < yenSum) {
      break;
    }
    //答えゼロパターン：合計金額が150円とかなのに50円持ってない時
    else if ((yenSum / 50) % 2 != 0 && yen50Num == 0) {
      break;
    } else {
      if (FIVE_HUNDRED * i > yenSum) {
        break;
      }
      let targetSum = yenSum - FIVE_HUNDRED * i;
      for (let j = 0; j <= yen100Num; j++) {
        if (ONE_HUNDRED * j > targetSum) {
          break;
        }
        if (targetSum - ONE_HUNDRED * j <= 50 * yen50Num) {
          count += 1;
        }
      }
    }
  }

  console.log(count);
});
