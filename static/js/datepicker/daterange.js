var nowTemp = new Date();
var now = new Date(nowTemp.getFullYear(), nowTemp.getMonth(), nowTemp.getDate(), 0, 0, 0, 0);
    

    // Month wise check in out
    var from=$(".from").datepicker( {
        format: "mm-yyyy",
        viewMode: "months",
        minViewMode: "months"
    });
    // end ---------------------------------------

    // Date wise check in checkout 
    var checkin = $('#dpd1').datepicker({
        format: "mm-dd-yyyy",     
        onRender: function(date) {
            return date.valueOf() < now.valueOf() ? 'disabled' : '';
        }
    }).on('changeDate', function(ev) {
        if (ev.date.valueOf() > checkout.date.valueOf()) {
            var newDate = new Date(ev.date)
            newDate.setDate(newDate.getDate() + 1);
            checkout.setValue(newDate);
        }
        checkin.hide();
        $('#dpd2')[0].focus();
    }).data('datepicker');


    var checkout = $('#dpd2').datepicker({
        format: "mm-dd-yyyy",
      
        onRender: function(date) {
            return date.valueOf() <= checkin.date.valueOf() ? 'disabled' : '';
        }
    }).on('changeDate', function(ev) {
    checkout.hide();
    }).data('datepicker');
// end-------------


var minyears = new Date();
minyears.setFullYear(nowTemp.getFullYear()-18);
    $('#dob').datepicker({
        format: "mm-dd-yyyy",
        viewMode: 2,     
        onRender: function(date) {
            return date.valueOf() > minyears.valueOf() ? 'disabled' : '';
        }
    })


var checkins = $('#dpd11').datepicker({
        format: "mm-dd-yyyy",     
        
    }).on('changeDate', function(ev) {
        if (ev.date.valueOf() > checkouts.date.valueOf()) {
            var newDate = new Date(ev.date)
            newDate.setDate(newDate.getDate() + 1);
            checkouts.setValue(newDate);
        }
        checkins.hide();
        $('#dpd2')[0].focus();
    }).data('datepicker');


    var checkouts = $('#dpd22').datepicker({
        format: "mm-dd-yyyy",
      
        onRender: function(date) {
            return date.valueOf() <= checkins.date.valueOf() ? 'disabled' : '';
        }
    }).on('changeDate', function(ev) {
    checkouts.hide();
    }).data('datepicker');