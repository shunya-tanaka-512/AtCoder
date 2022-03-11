function main(input) {
  input = input.split(""); //[ '1', '0', '1' ]
  //１が書かれてたらカウント、それ以外ならカウントしない
  var a = 0;
  for (let i = 0; i < input.length; i++) {
    if (input[i] == 1) {
      a += 1;
    }
  }
  console.log(a);
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
