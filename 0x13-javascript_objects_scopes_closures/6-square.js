#!/usr/bin/node
const OldSquare = require('./5-square');

class Square extends OldSquare {
  charPrint (c) {
    let x = c;
    if (c === undefined) {
      x = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += x;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
