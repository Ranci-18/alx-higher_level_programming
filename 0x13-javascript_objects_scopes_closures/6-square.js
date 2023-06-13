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

      for (i = 0; i < this.size; i++) {
        row = '';
        for (j = 0; j < this.size; j++) {
          row += 'C';
        }
        console.log(row);
      }
    }
  }
}

module.exports = Square;
