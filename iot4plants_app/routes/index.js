var express = require('express');
var router = express.Router();

const fs = require("fs");
const csvParser = require("csv-parser");

// PowerBI report
var reportIframe = "https://app.powerbi.com/reportEmbed?reportId=df7dbc26-049c-4613-a755-5ca32243a9d6&autoAuth=true&ctid=6edb49c1-bf72-4eea-8b3f-a7fd0a25b68c"

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Plant Conditions report', iframeUrl: reportIframe });
});

router.get("/dataSource", async (req, res) => {
  try {
    const csv = await parseCSV("public/data/conditionsData.csv"); // your CSV parser

    res.render("dataSource", {
      columns: csv.columns,
      rows: csv.rows
    });

  } catch (err) {
    console.error("CSV load error:", err);
    res.status(500).send("Error loading CSV");
  }
});

function parseCSV(path) {
  return new Promise((resolve, reject) => {
    const rows = [];
    let columns = [];

    fs.createReadStream(path)
      .pipe(csvParser())
      .on("headers", (headers) => {
        columns = headers;
      })
      .on("data", (data) => rows.push(data))
      .on("end", () => resolve({ columns, rows }))
      .on("error", reject);
  });
}

module.exports = router;
