#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i;
      let j;
      let row;

      for (i = 0; i < this.height; i++) {
        row = '';
        for (j = 0; j < this.width; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
}

module.exports = Square;
