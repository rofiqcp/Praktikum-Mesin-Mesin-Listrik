const fs=require('fs');
const path=process.argv[2] || __dirname+'/lab_data.csv';
const lines=fs.readFileSync(path,'utf8').trim().split(/\r?\n/);
const head=lines[0].split(',');
const rows=lines.slice(1).map(l=>Object.fromEntries(l.split(',').map((v,i)=>[head[i],v])));
const maxI=rows.reduce((a,b)=>Number(a.I)>Number(b.I)?a:b);
const maxT=rows.reduce((a,b)=>Number(a.temp)>Number(b.temp)?a:b);
console.log(JSON.stringify({samples:rows.length,max_current:{test:maxI.test,I:Number(maxI.I)},max_temp:{test:maxT.test,temp:Number(maxT.temp)},notes:rows.filter(r=>!['normal','baseline'].includes(r.note)).map(r=>({test:r.test,note:r.note}))},null,2));