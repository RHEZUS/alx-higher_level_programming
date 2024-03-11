#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length == 2)
{
	console.log(0);
}
else 
{
	let numbers = [];
	for (let i = 2; i < argv.length; i++)
	{
		numbers = [...numbers, parseInt(argv[i])];
	}
	numbers.sort((a, b) => b - a);
	const uniqueNumbers = [...new Set(numbers)];
	console.log(uniqueNumbers[1]);
}
