function main(input) {
  input = input.split("\n"); //[ '1', '2 3', 'mami' ]改行区切りで文字列配列に分割
  tmp = input[1].split(" "); //['2', '3']
  //文字列から10進数に変換
  var a = parseInt(input[0]);
  var b = parseInt(tmp[0], 10);
  var c = parseInt(tmp[1], 10);
  var s = input[2];
  console.log("%d %s", a + b + c, s);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
