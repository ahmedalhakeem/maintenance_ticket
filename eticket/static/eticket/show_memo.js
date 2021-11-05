document.addEventListener('DOMContentLoaded', function(){
    const start = document.querySelector('#start');
    const tour_days = document.querySelector('#tour-days');
    const end = document.querySelector('#end');
 
    tour_days.addEventListener('focusout', (e)=>{
        const days = e.target.value
        const num = Number(days)
        console.log(`type of ${typeof(num)}`);
        const end_date = new Date(start.value)
        end_date.setDate(end_date.getDate()+ num)
        console.log(end_date);
        const x_format = end_date.getFullYear()+ '-'+ (end_date.getMonth()+1)+ '-'+ end_date.getDate();
        end.value = x_format
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