#!/usr/bin/node
if (process.argv.length <= 3) console.log(0);
else {
  const arr = process.argv.slice(2).map(Number)
    .sort((a, b) => b - a);
  console.log(arr[1]);
}
