#!/usr/bin/node
exports.esrever = function (list) {
  let i;
  let j;
  let tmp;

  for (i = 0, j = list.length; i < j; i++, j--) {
    tmp = list[i];
    list[i] = list[j - 1];
    list[j - 1] = tmp;
  }
  return list;
};
