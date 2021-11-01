document.addEventListener('DOMContentLoaded', function(){
   //const container = document.querySelector('#ticket-container');
   document.querySelector('.done_tickets').style.display = 'none';
   document.querySelector('.undone_tickets').style.display = 'none';

   //container.style.display = "none";
   //const getUndonetickets = container.children[1];
   //console.log(getUndonetickets);
   //show all done tickets
   document.querySelector('#done').addEventListener('click', ()=> {
        document.querySelector('.done_tickets').style.display = 'block';
        document.querySelector('.undone_tickets').style.display = 'none';

       
   });
   //show all undone tickets 
   document.querySelector('#undone').addEventListener('click', ()=> {
        
        document.querySelector('.undone_tickets').style.display = 'block';
        document.querySelector('.done_tickets').style.display = 'none';


       
   })
   //document.querySelector('#undone').addEventListener('click', ()=> load_undone())

});
