#!/usr/bin/node

// script that prints argument passed to it

if (process.argv.length < 3) {
	console.log('No argument');
} else if ( process.argv.length === 3) {
	console.log('Argument found');
} else if (process.argv.length > 3) {
	console.log('Arguments found');
}
