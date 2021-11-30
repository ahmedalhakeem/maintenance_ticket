document.addEventListener('DOMContentLoaded', function(){
    const start = document.querySelector('#start');
    const tour_days = document.querySelector('#tour-days');
    const end = document.querySelector('#end');
        // console.log();
        const ticket_form = document.querySelector('#ticket-form')
        console.log(ticket_form.children);
        document.querySelector('#memo_info').style.display = 'none'
        

 
    tour_days.addEventListener('focusout', (e)=>{
        const start = document.querySelector('#start');
        // const tour_days = document.querySelector('#tour-days');
        const end = document.querySelector('#end');
        const days = e.target.value
        const num = Number(days)
        // console.log(`type of ${typeof(num)}`);
        const end_date = new Date(start.value)
        if(num > 1){
            end_date.setDate(end_date.getDate()+ num-1)
            const x_format = end_date.getFullYear()+ '-'+ (end_date.getMonth()+1)+ '-'+ (end_date.getDate()<=9?'0'+end_date.getDate():end_date.getDate());
            // const x_format = (end_date.getMonth()+1)+'-'+ end_date.getDate()+'-'+end_date.getFullYear();
            console.log(typeof(x_format));
            end.value = x_format
            // end.value = x_format
        }else{
            x_format = end_date.getFullYear()+ '-'+ (end_date.getMonth()+1)+ '-'+ end_date.getDate();
            end.value = x_format;
            console.log(x_format);
        }
        
    })
})  

function show_memo(){
    if(document.querySelector('#memo_info').style.display === 'none'){
        document.querySelector('#memo_info').style.display = 'block';
    }else{
        document.querySelector('#memo_info').style.display = 'none';
    }
    
    
    return
    // text.placeholder= 'الرجاء كتابة اسم المذكرة وتاريخها'
    // ticket_form.append(text)
}