document.getElementById('height_unit').addEventListener('change', function() {
    var unit = this.value;
    if (unit === 'feet_inches') {
        document.getElementById('height_input').style.display = 'none';
        document.getElementById('feet_inches_input').style.display = 'block';
    } else {
        document.getElementById('height_input').style.display = 'block';
        document.getElementById('feet_inches_input').style.display = 'none';
    }
});
