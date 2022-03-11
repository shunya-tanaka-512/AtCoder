function main(input) {
  input = input.split(" ");
  var a = parseInt(input[0], 10);
  var b = parseInt(input[1], 10);
  //積を２で割った余が０ならEven、それ以外をOddで出力
  if ((a * b) % 2 == 0) {
    console.log("Even");
  } else {
    console.log("Odd");
  }
}
main(require("fs").readFileSync("/dev/stdin", "utf8"));
