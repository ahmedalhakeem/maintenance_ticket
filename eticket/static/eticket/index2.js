document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('.convert-form').addEventListener('submit', event => convert_ticket());
    //change the row color of unaccomplished tickets
    document.querySelectorAll('.row-ticket').forEach(function(tr){
        if(tr.children[4].textContent==='unaccomplished'){
            tr.style.color='#f05337';
        
        }else{
            tr.style.color='#0ec414';
        }
         
    })
    var table = document.getElementById('tableid');
    var rows = document.getElementsByTagName('tr');
    for (i=0; i<rows.length; i++){
        row = table.rows[i];
        row.onclick = function() {
            var cell = this.getElementsByTagName('td')[0];
            document.getElementById('ticket-number').value = cell.textContent;
            alert(`id: ${di}`)
        }
    }

});
function convert_ticket(){
    //event.preventDefault();
    const id = document.querySelector('#ticket-number').value;
    //console.log(id);
    
    var s = document.getElementById('selected-solver');
    var strUser = s.options[s.selectedIndex].value;
    if (id===""){
        alert('you must specify the ticket number')
        return false;
    }
    if (strUser ==="") {
        alert('Please, choose one of your IT experts ');
        return false;
    }
    console.log(strUser);
    var status = document.getElementById('select-status');
    var strStatus = status.options[status.selectedIndex].text;
    console.log(strStatus);
    //Get the current url.
    const url = window.location.href;
    console.log(url);
    const data = {'id': id, 'it_user': strUser, 'status': strStatus}
    //make ajax request with server
    fetch(`${url}/convert_ticket`, {
        method: 'PUT',
        headers: {
            'Content-TYPE': 'application/json',
        },
        body: JSON.stringify(data), 
    })
    .then(res => res.json())
    .then(result => {
        console.log(result);
    })
    alert(`ticket converted to ${strUser} successfully`);
    
}
