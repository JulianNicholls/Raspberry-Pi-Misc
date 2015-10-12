var Blynk = require('blynk-library');
var AUTH  = 'ff55533a7af8492e83f77a6d434cc01a';

var blynk = new Blynk.Blynk(AUTH, options = {
    certs_path: './certs/'
});

var v1      = new blynk.VirtualPin(1);
var v9      = new blynk.VirtualPin(9);
var term    = new blynk.WidgetTerminal(3);

v1.on('write', function(param) {
    console.log('V1: ', param[0]);
});

v9.on('read', function() {
    v9.write(new Date().getSeconds());
});

term.on('write', function(data) {
    term.write('You wrote: ' + data + '\n');
    blynk.notify('HAHA! ' + data);
});

