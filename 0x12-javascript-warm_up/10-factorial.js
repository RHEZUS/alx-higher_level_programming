#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length < 3)
{
	console.log(1);
}
else 
{
	let n = parseInt(argv[2]);
	
	if (n === 0 || n === 1)
	{
		conole.log(1);
	}
	else
	{
		let fact = 1;
		for (let i = 2; i <= n; i++)
		{
			fact *= i;
		}
		console.log(fact);
	}
}
