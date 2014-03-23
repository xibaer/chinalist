#!/usr/bin/env node
// Origional by: https://gist.github.com/Ajnasz/3558891

var crypto = require('crypto'), fs = require('fs'), sys = require('sys');

console.log ('ABP Filter Sign-tool');

if (process.argv.length < 3)
    process.exit (1, console.log('Usage: node checksum.js input [output(Overwrite)]'));
if (process.argv.length < 4)
    process.argv.push (process.argv[2]);

fs.readFile(process.argv[2], function (er, data) {
    if (er) throw er;

    data = data.toString()
        .replace(/(^\s*|\s*$)/, '')
        .replace(/\r/g, '')
        .replace(/\n+/g, '\n')
        .replace(/^\s*!\s*checksum[\s\-:]+([\w\+\/=]+).*\n/gim, '');
    
    var lines = data.split('\n'), hash;
    hash = crypto.createHash('md5');
    hash.update(data);
    hash = hash.digest('base64').replace(/\=+$/, '');
    lines.splice(1, 0, '! Checksum: ' + hash);
    sys.puts(lines.join('\n'));
    fs.writeFile(process.argv[3], lines.join('\n'), {}, function (er) {
        console.log ('Write to file: ' + (er ? 'Failed;\n'+er : 'Success.'));
    });
});
