var express = require('express');
var router = express.Router();

// PowerBI report
var reportIframe = "https://app.powerbi.com/reportEmbed?reportId=df7dbc26-049c-4613-a755-5ca32243a9d6&autoAuth=true&ctid=6edb49c1-bf72-4eea-8b3f-a7fd0a25b68c"

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Plant Conditions report', iframeUrl: reportIframe });
});

module.exports = router;
