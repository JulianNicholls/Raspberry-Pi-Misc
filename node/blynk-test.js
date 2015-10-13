#!/usr/bin/env node

var Blynk = require('blynk-library');
var AUTH  = 'ff55533a7af8492e83f77a6d434cc01a';

var blynk = new Blynk.Blynk(AUTH, options = {
    certs_path: './certs/'
});

var value   = 0;
var v1      = new blynk.VirtualPin(1);
var v4      = new blynk.VirtualPin(4);
var v9      = new blynk.VirtualPin(9);
var term    = new blynk.WidgetTerminal(3);

v1.on('write', function(param) {
    value = param[0];
    console.log('V1: ', value);
});

v4.on('read', function() {
    v4.write(value);
});

v9.on('read', function() {
    v9.write(new Date().getSeconds());
});

term.on('write', function(data) {
    term.write('You wrote: ' + data + '\n');
    blynk.notify('HAHA! ' + data);
});

blynk.on('connect', function() { console.log("Blynk ready."); });
blynk.on('disconnect', function() { console.log("DISCONNECT"); });

