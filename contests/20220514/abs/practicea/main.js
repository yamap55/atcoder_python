const debug_flag = false
const log = (...args) => debug_flag ? console.log(...args) : ""
const print = log
const answer = (...args) => console.log(...args)
// ※最初のrowの長さで返されるので注意
const zip = (...rows) => [...rows[0]].map((_,c) => rows.map(row => row[c]))
const gcd = (a, b) => b === 0 ? a : gcd(b, a % b) // 最大公約数

// inputに入力データ全体が入る
function Main(input) {
  // 1行目がinput[0], 2行目がinput[1], …に入る
  const rows = input.split("\n").slice(0, -1);
  parseInt(rows[0])
  const b = [...rows[0].split(" "), ...rows[1].split(" ")]
  log(b)
  const c = b.map(a=> parseInt(a)).reduce((x,y)=>x+y, 0)

  const result = `${c} ${rows[2]}`
  answer(result)

}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main(require("fs").readFileSync("/dev/stdin", "utf8"));
