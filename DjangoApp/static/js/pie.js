var a = [{
    "category": "Lithuania",
    "litres": 501.9
  }, {
    "category": "Czech Republic",
    "litres": 301.9
  }, {
    "category": "Ireland",
    "litres": 201.1
  }, {
    "category": "Germany",
    "litres": 165.8
  }, {
    "category": "Australia",
    "litres": 139.9
  }
  ];

var chart = AmCharts.makeChart("chartdiv", {
  "type": "pie",
  "theme": "light",
  "dataProvider": a,
  "valueField": "litres",
  "titleField": "category",
  "export": {
    "enabled": true
  }
});

chart.addListener("rollOverSlice", function(e) {
  handleRollOver(e);
});


function handleRollOver(e){
  var wedge = e.dataItem.wedge.node;

  wedge.parentNode.appendChild(wedge);
}