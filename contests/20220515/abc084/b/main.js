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
  const [a, b] = rows[0].split(" ").map(a => parseInt(a))
  const c = [...rows[1]]

  const f = function(e, i) {
    log(e, Boolean(parseInt(e)), parseInt(e))
    if(i === a) {
      return e === "-"
    }
    return !isNaN(e)
  }

  const result = c.every(f) ? "Yes" : "No"
  answer(result)

}
//*この行以降は編集しないでください（標準入出力から一度に読み込み、Mainを呼び出します）
Main(require("fs").readFileSync("/dev/stdin", "utf8"));
