#!/usr/bin/node

exports.esrever = function (list) {
    var reversedArray = [];
    for (var i = list.length - 1; i >= 0; i--) {
      reversedArray.push(list[i]);
    }
    list = reversedArray;
    return list;
};
