const f=50, poles=4, nr=1440;
const ns=120*f/poles;
const slip=(ns-nr)/ns;
console.log('PETA MESIN LISTRIK');
console.log('Trafo -> Motor DC -> Motor Induksi -> Mesin Sinkron -> Analisis integratif');
console.log(`Ns=${ns} rpm, slip=${(100*slip).toFixed(2)}%`);
console.log('Kendali: latching | forward-reverse | star-delta | protection');