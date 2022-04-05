#!/usr/bin/node
let nbArgPrint = 0;

exports.logMe = function (item) {
	console.log(`${nbArgPrint}: ${item}`);
	nbArgPrint++;
}