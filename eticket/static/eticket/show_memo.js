document.addEventListener('DOMContentLoaded', function(){
    const start = document.querySelector('#start');
    start.addEventListener('change', (e)=>{
        // console.log(e.target.value);
        const date = new Date(e.target.value)
        date.setDate(date.getDate() + 3);
        console.log(date);

    })
    // console.log();
    const ticket_form = document.querySelector('#ticket-form')
    console.log(ticket_form.children);
    document.querySelector('#memo_info').style.display = 'none'
    ticket_form.children[10].addEventListener('click', ()=>{
    // document.querySelector('#memo_info').style.display = 'none';
    }) 
}) 
function show_memo(){
    if(document.querySelector('#memo_info').style.display === 'none'){
        document.querySelector('#memo_info').style.display = 'block';
    }else{
        document.querySelector('#memo_info').style.display = 'none';
    }
    const ticket_form = document.querySelector('#ticket-form')
    
    return
    // text.placeholder= 'الرجاء كتابة اسم المذكرة وتاريخها'
    // ticket_form.append(text)
}