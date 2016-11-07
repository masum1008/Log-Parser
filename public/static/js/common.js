/**
 * Created by masum on 11/6/16.
 */
var editor; // use a global for the submit and return data rendering in the examples


function createTable(demoData) {

    var tableHtml = '<tr>';
    for(var i=0;i<demoData.data.length;i++){
        tableHtml += '<td>'+demoData.data[i].first_name+' '+demoData.data[i].last_name+'</td>'+
            '<td>'+demoData.data[i].position+'</td>'+
            '<td>'+demoData.data[i].office+'</td>'+
            '<td>'+demoData.data[i].extn+'</td>'+
            '<td>'+demoData.data[i].start_date+'</td>'+
            '<td>'+demoData.data[i].salary+'</td>';
        tableHtml += '<tr>';
    }

    //alert($('#example').html());
    $('#a').html(tableHtml);
};

// var data = {{ data }};
// console.log(data)

var demoData ={
    "data": [
        {
      "DT_RowId": "row_1",
      "first_name": "Tiger",
      "last_name": "Nixon",
      "position": "System Architect",
      "email": "t.nixon@datatables.net",
      "office": "Edinburgh",
      "extn": "5421",
      "age": "61",
      "salary": "320800",
      "start_date": "2011-04-25"
    },
    {
      "DT_RowId": "row_2",
      "first_name": "Garrett",
      "last_name": "Winters",
      "position": "Accountant",
      "email": "g.winters@datatables.net",
      "office": "Tokyo",
      "extn": "8422",
      "age": "63",
      "salary": "170750",
      "start_date": "2011-07-25"
    },
    {
      "DT_RowId": "row_3",
      "first_name": "Ashton",
      "last_name": "Cox",
      "position": "Junior Technical Author",
      "email": "a.cox@datatables.net",
      "office": "San Francisco",
      "extn": "1562",
      "age": "66",
      "salary": "86000",
      "start_date": "2009-01-12"
    },
    {
      "DT_RowId": "row_4",
      "first_name": "Cedric",
      "last_name": "Kelly",
      "position": "Senior Javascript Developer",
      "email": "c.kelly@datatables.net",
      "office": "Edinburgh",
      "extn": "6224",
      "age": "22",
      "salary": "433060",
      "start_date": "2012-03-29"
    },
    {
      "DT_RowId": "row_5",
      "first_name": "Airi",
      "last_name": "Satou",
      "position": "Accountant",
      "email": "a.satou@datatables.net",
      "office": "Tokyo",
      "extn": "5407",
      "age": "33",
      "salary": "162700",
      "start_date": "2008-11-28"
    },
    {
      "DT_RowId": "row_6",
      "first_name": "Brielle",
      "last_name": "Williamson",
      "position": "Integration Specialist",
      "email": "b.williamson@datatables.net",
      "office": "New York",
      "extn": "4804",
      "age": "61",
      "salary": "372000",
      "start_date": "2012-12-02"
    },
    {
      "DT_RowId": "row_7",
      "first_name": "Herrod",
      "last_name": "Chandler",
      "position": "Sales Assistant",
      "email": "h.chandler@datatables.net",
      "office": "San Francisco",
      "extn": "9608",
      "age": "59",
      "salary": "137500",
      "start_date": "2012-08-06"
    },
    {
      "DT_RowId": "row_8",
      "first_name": "Rhona",
      "last_name": "Davidson",
      "position": "Integration Specialist",
      "email": "r.davidson@datatables.net",
      "office": "Tokyo",
      "extn": "6200",
      "age": "55",
      "salary": "327900",
      "start_date": "2010-10-14"
    },
    {
      "DT_RowId": "row_9",
      "first_name": "Colleen",
      "last_name": "Hurst",
      "position": "Javascript Developer",
      "email": "c.hurst@datatables.net",
      "office": "San Francisco",
      "extn": "2360",
      "age": "39",
      "salary": "205500",
      "start_date": "2009-09-15"
    },
    {
      "DT_RowId": "row_10",
      "first_name": "Sonya",
      "last_name": "Frost",
      "position": "Software Engineer",
      "email": "s.frost@datatables.net",
      "office": "Edinburgh",
      "extn": "1667",
      "age": "23",
      "salary": "103600",
      "start_date": "2008-12-13"
    },
    {
      "DT_RowId": "row_11",
      "first_name": "Jena",
      "last_name": "Gaines",
      "position": "Office Manager",
      "email": "j.gaines@datatables.net",
      "office": "London",
      "extn": "3814",
      "age": "30",
      "salary": "90560",
      "start_date": "2008-12-19"
    },
    {
      "DT_RowId": "row_12",
      "first_name": "Quinn",
      "last_name": "Flynn",
      "position": "Support Lead",
      "email": "q.flynn@datatables.net",
      "office": "Edinburgh",
      "extn": "9497",
      "age": "22",
      "salary": "342000",
      "start_date": "2013-03-03"
    },
    {
      "DT_RowId": "row_13",
      "first_name": "Charde",
      "last_name": "Marshall",
      "position": "Regional Director",
      "email": "c.marshall@datatables.net",
      "office": "San Francisco",
      "extn": "6741",
      "age": "36",
      "salary": "470600",
      "start_date": "2008-10-16"
    },
    {
      "DT_RowId": "row_14",
      "first_name": "Haley",
      "last_name": "Kennedy",
      "position": "Senior Marketing Designer",
      "email": "h.kennedy@datatables.net",
      "office": "London",
      "extn": "3597",
      "age": "43",
      "salary": "313500",
      "start_date": "2012-12-18"
    },
    {
      "DT_RowId": "row_15",
      "first_name": "Tatyana",
      "last_name": "Fitzpatrick",
      "position": "Regional Director",
      "email": "t.fitzpatrick@datatables.net",
      "office": "London",
      "extn": "1965",
      "age": "19",
      "salary": "385750",
      "start_date": "2010-03-17"
    }
  ],
  "options": [],
  "files": []
};
createTable(demoData);