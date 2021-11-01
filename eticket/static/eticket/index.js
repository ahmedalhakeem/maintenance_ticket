document.addEventListener('DOMContentLoaded', function(){
    //document.querySelector('.ticket-details').style.display = 'none';
    //console.log(sender);
        
        const form = document.querySelector('#compose-ticket');
        const user_id = form.parentElement.id;
        console.log(user_id);
        
        const url = window.location.href;
        console.log(url);
        //console.log(form);
        form.onsubmit = function(){
            const sender = document.querySelector("#sender").value;
            const title = document.querySelector("#title").value;
            const description = document.querySelector("#description").value;
            var x = document.querySelector("#priority").selectedIndex;
            const selected_priority = document.getElementsByTagName("option")[x].value;
            //document.querySelector('#priority').onchange = this.value;
            //console.loq(this.value);
            const data = {'sender': sender, 'title': title, 'description': description, 'priority': selected_priority}
        //console.log(sender);
            fetch(`${url}/tickets`, {
                method: "POST",
                headers: {
                    'Content-TYPE' : 'application/json',
                },
                body: JSON.stringify(data),

                })
                .then(response => response.json())
                .then(data => {
                   console.log(data);
                   console.log(sender);
                })
                /*.catch((error) => {
                    console.log("error:" ,error)
                  });*/
                
            alert('Ticket converted successfully')      
        };

});