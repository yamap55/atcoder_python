const debug_flag = false;
const log = (...args) => (debug_flag ? console.log(...args) : "");
const print = log;
const answer = (...args) => console.log(...args);
// ※最初のrowの長さで返されるので注意
const zip = (...rows) => [...rows[0]].map((_, c) => rows.map((row) => row[c]));
const gcd = (a, b) => (b === 0 ? a : gcd(b, a % b)); // 最大公約数

// inputに入力データ全体が入る
function Main(input) {
  // 1行目がinput[0], 2行目がinput[1], …に入る
  const rows = input.split("\n").slice(0, -1);
  const [a, b] = rows[0].split(" ").map((a) => parseInt(a));
  log(a, b);
  const x = a % 2019;
  const y = b % 2019;

  const xx = Math.min(x, y);
  const yy = Math.max(x, y);

  let result = (xx * (xx + 1)) % 2019;

  // x .. y -1
  for (i = xx; i < yy; i++) {
    const z = (i * (i + 1)) % 2019;
    print(i, i + 1);
    result = Math.min(result, z);
  }

  // const result = 0;
  answer(result);
}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main(require("fs").readFileSync("/dev/stdin", "utf8"));

// NOTE: サンプルは通るがすべての答えは通らない。
// ループの部分で仮に i と i+1 で回していると、4 * 505 みたいなパターンに気づけないため。残念！
