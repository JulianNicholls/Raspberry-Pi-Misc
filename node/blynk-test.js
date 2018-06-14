const Blynk = require('blynk-library');

const AUTH ='b97354f421994b838c04b1a3517d6d56';

const blynk = new Blynk.Blynk(AUTH, options = {
    connector: new Blynk.TcpClient()
});

const v1   = new blynk.VirtualPin(1);
const v9   = new blynk.VirtualPin(9);
const term = new blynk.WidgetTerminal(4);

let   v1Value;

v1.on('write', (param) => {
    v1Value = param[0];
    console.log(`V1: ${v1Value}`);
});

v9.on('read', () => {
    const seconds = new Date().getSeconds();

    v9.write(`${seconds}: v1Value`);
});

term.on('write', (data) => {
    term.write(`Rcv: ${data}`);
    console.log(`Term: ${data}`);
    blynk.notify(`TERM: ${data}`);
});

