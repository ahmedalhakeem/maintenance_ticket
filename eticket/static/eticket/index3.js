//final ticket conversion
document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('.final-convert-ticket').addEventListener('submit', event => tic_solution());
    document.querySelectorAll('.row-tickets').forEach(function(tr){
        if(tr.children[4].textContent=== 'unaccomplished'){
            tr.style.color = '#f05337';

        }else{
            tr.style.color = '#0ec414';
        }
    })
    var table = document.getElementById('table_id');
    var rows = document.getElementsByTagName('tr');
    for (i=0; i<rows.length; i++){
        row = table.rows[i];
        row.onclick = function() {
            var cell = this.getElementsByTagName('td')[0];
            document.getElementById('ticketnumber').value = cell.textContent;
        }
    }
});
function tic_solution(){
    //event.preventDefault();
    const id = document.querySelector('#ticketnumber').value;
    console.log(id);
    var s = document.getElementById('select-status');
    var status = s.options[s.selectedIndex].value;
    const solution = document.querySelector('#solution').value;
    console.log(status);
    const url = window.location.href;
    console.log(url);
    const data = {'id': id, "status": status, "solution": solution}
    //make ajax request with the server
    fetch(`${url}/submit_ticket`,{
        method: 'PUT',
        headers: {
            'Content-TYPE' : 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(resp => resp.json())
    .then(result => {
        console.log(result);
    })
    alert('this ticket is accomplished perfectly')
}
