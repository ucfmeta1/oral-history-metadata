import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook, SpreadsheetFile, FileBlob } from '@oai/artifact-tool';

const spec = JSON.parse(await fs.readFile(process.argv[2], 'utf8'));
const workbook = spec.input ? await SpreadsheetFile.importXlsx(await FileBlob.load(spec.input)) : Workbook.create();
for (const item of spec.input ? [] : spec.sheets) {
  const sheet = workbook.worksheets.add(item.name);
  const data = [item.headers, ...item.rows];
  const range = sheet.getRangeByIndexes(0, 0, data.length, item.headers.length);
  range.values = data;
  range.format.font = {name: 'Arial', size: 10};
  range.format.wrapText = true;
  range.format.verticalAlignment = 'top';
  range.format.rowHeight = item.name === 'Quality_Review' ? 200 :
    item.name === 'Generated_Metadata' ? 150 :
    ['Evidence_Sources','Description_Evidence','Keyword_Evidence','FAST_Selection'].includes(item.name) ? 140 : 70;
  const header = sheet.getRangeByIndexes(0, 0, 1, item.headers.length);
  header.format.fill = '#17365D';
  header.format.font = {name:'Arial', size:10, bold:true, color:'#FFFFFF'};
  header.format.rowHeight = 32;
  sheet.freezePanes.freezeRows(1);
  sheet.showGridLines = false;
  for (let c = 0; c < item.headers.length; c++) {
    const label = item.headers[c];
    const width = label === 'Video' ? 55 : /Transcript|Description|Passage|Text|Issues|Observation/.test(label) ? 70 :
      ['people','locations','organizations','themes','perspective'].includes(label.toLowerCase()) ? 40 : 30;
    sheet.getRangeByIndexes(0,c,data.length,1).format.columnWidth = width;
  }
}
workbook.recalculate();
if (spec.input) {
  for (const item of spec.sheets) {
    const check = await workbook.inspect({kind:'region',sheetId:item.name,range:item.previewRange,maxChars:1600,tableMaxRows:2,tableMaxCols:6});
    console.log(check.ndjson);
  }
}
if (spec.previewDir) {
  await fs.mkdir(spec.previewDir, {recursive:true});
  for (const item of spec.sheets) {
    const previewRange = item.previewRange ?? `A1:C${Math.min(3,item.rows.length+1)}`;
    const image = await workbook.render({sheetName:item.name, range:previewRange, scale:1,format:'png'});
    await fs.writeFile(path.join(spec.previewDir,`${item.name}.png`),new Uint8Array(await image.arrayBuffer()));
  }
}
if (!spec.renderOnly) {
  const output = await SpreadsheetFile.exportXlsx(workbook);
  await fs.mkdir(path.dirname(spec.output),{recursive:true});
  await output.save(spec.output);
  console.log(`Saved ${spec.sheets.length} worksheet(s).`);
}
