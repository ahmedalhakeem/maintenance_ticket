document.addEventListener('DOMContentLoaded', ()=>{
    
    const wrap = document.querySelector('#wrap')
    wrap.style.display = 'none'
    // console.log(tour_wrapper);
    const tour_wrapper = document.querySelector('.tour_wrapper')
    console.log(tour_wrapper.children);
     
    
    
     
});
$('.close-allocation_page').on('click', function(){
    location.reload()
})

$('.send-memo-status').on('click', function(){
    const currentRow = $(this).closest('tr');
    const col1 = currentRow.find('td:eq(0)').text()
    const notes = currentRow.find('td:eq(7)').text()
    const col10 = currentRow.find('td:eq(10)').html()
    console.log(col10);
    // const col9 = currentRow.find('td:eq(9)').attr('id')
    
    const id = Number(col1)
    console.log(id);

    // when submit
    $('.send').on('click', function(){
        const memo_state = document.querySelector('#memo-select').value;
        const memo_note = document.querySelector('#memo-note').value;
        
        fetch(`./send_memo_status/${id}?memo_state=${memo_state}&memo_note=${memo_note}`)
        .then((res)=>{
            if(res.ok) return res.json();
            return res.json()
            .then((error)=>{
                console.log(error);
            })
        })
        .then((data)=>{
            
            console.log(data);
            
            
        })
        // location.reload();
             
    })
 
})

    $('.allocate-btn').on('click', function(e){
        const parent_td = e.target.parentElement
        const parent_tr = parent_td.parentElement
        console.log(parent_tr.children[4].innerHTML);
        if(wrap.style.display === 'none'){
            wrap.style.display = 'block'
        }
        
        const tour_wrapper = document.querySelector('.tour_wrapper')
        wrap.innerHTML=''
        const currentRow = $(this).closest('tr')
        const col1 = currentRow.find('td:eq(0)').text();
        const col2 = currentRow.find('td:eq(1)').text();
        // Total tour_days
        const col5 = currentRow.find('td:eq(5)').text();
        // The unallocated_remaining_days
        const col6 = currentRow.find('td:eq(6)').text()
        // const col10 = currentRow.find('td:eq(10)').attr('id')
        const col11 = currentRow.find('td:eq(11)').attr('id')

        const num = Number(col6)
        const id = Number(col1)
        tour_wrapper.innerHTML=''
        if(col6 ==='0'){
            const allocate_wrapper = document.querySelector('.tour_wrapper')
            tour_wrapper.innerHTML='<h1> تم تخصيص الكل</h1>'
        }
        
        for(i=1; i<=num; i++){
            const div = document.createElement('div')
            div.className = `day${i}`
            div.innerHTML +=  `اليوم ${i}`
            tour_wrapper.append(div)
        }
        get_allocations(id, num, col11, parent_tr)
        check_allocation_status(id)
    })

const get_allocations = (id, num, col11, parent_tr) =>{

for(i=1;i<=num;i++){
    const cont = document.querySelector(`.day${i}`)
    cont.style.display='flex'
    cont.style.margin= '50px'
    // ADD Car and Driver select, add input type date, and add assign btn
    const assign_btn= document.createElement('button')
    assign_btn.className = `${col11}`

    assign_btn.addEventListener('click', (e)=>{
        get_reply_ticket(e)
    })
    //     
    // assign_btn.onclick = allocation_per_day(e) 
    assign_btn.innerHTML = 'تخصيص جولة'
    const input_date = document.createElement('input')
    input_date.type = 'date'
    input_date.lang = 'ar_SA'
    console.log(parent_tr.children[4].innerHTML);
    const start_date_value = new Date(parent_tr.children[4].innerHTML)
    const end_date_value = new Date(parent_tr.children[7].innerHTML)
    const str_start_date_value = start_date_value.getFullYear()+ '-'+ (start_date_value.getMonth()+1)+ '-'+ start_date_value.getDate();
    const str_end_date_value = end_date_value.getFullYear()+ '-'+ (end_date_value.getMonth()+1)+ '-'+ end_date_value.getDate();
    input_date.defaultValue = str_start_date_value
    input_date.setAttribute('min', str_start_date_value)
    input_date.setAttribute('max', str_end_date_value)
    const car_select= document.createElement('select')
    const driver_select = document.createElement('select')
    input_date.className= 'enter-date'
    driver_select.className = 'form-select-sm'
    car_select.className='form-select-sm'
    const default_d_choice = document.createElement('option')
    const default_c_choice = document.createElement('option')
    default_d_choice.value='0'
    default_c_choice.value = '0'
    default_c_choice.innerHTML = 'اختر نوع المركبة من القائمة'
    default_d_choice.innerHTML = 'اختر اسم السائق من القائمة'
    driver_select.append(default_d_choice)
    car_select.append(default_c_choice)

    // fetch the required query object from the server
    fetch(`./get_allocations?id=${id}`)
    .then((res)=>{
    if(res.ok) return res.json()
    return res.json()
    .then((error)=>{
        console.log(error);
    })
    })
.then((data)=>{
    data.cars.forEach((value)=>{
        car_select.innerHTML += `<option style="border:1px solid black">${value.car_type}</option>`
    })
    cont.append(car_select)
    data.drivers.forEach(value=>{
        driver_select.innerHTML += `<option style="border:1px solid black">${value.driver_name}</option>`
    })
    cont.append(driver_select)
    cont.appendChild(assign_btn) 

})
cont.appendChild(input_date)            
    }
}


const get_reply_ticket = (e)=>{
    const parent = e.target.parentElement
            console.log(e.target.className);
            console.log(parent.children[0].value);
            console.log(parent.children[1].value);
            if(parent.children[0].value===""){
             alert('الرجاء ملء الحقول قبل التخصيص')    
            }else{
                fetch(`./allocate_per_day/${e.target.className}?date=${parent.children[0].value}&car=${parent.children[1].value}&driver=${parent.children[2].value}`)
            .then((res)=>{
            if(res.ok) return res.json()
            return res.json()
            .then(error=>{
                console.log(error);
            })
        })
        .then(data=>{
            console.log(data);
        })
    } 
    alert('تم التخصيص')
} 
const check_allocation_status = (id)=>{
    console.log(id);
    fetch(`./check_allocation_status/${id}`)
    .then(res=>{
        if(res.ok) return res.json()
        return res.json()
        .then(error=>{
            console.log(error);
        })
    })
    .then(data=>{
        data.forEach(value=>{
            console.log(value);
        })
    })
}
// $('#get-data').on('click', function(){
    //     const arr = []
    //     $('#tableid tbody tr').each(function(){
    //         const currentRow = $(this)
    //         const col1 = currentRow.find('td:eq(0)').text();
    //         const col2 = currentRow.find('td:eq(1)').text();
    //         const col5 = currentRow.find('td:eq(5)').text();

    //         const obj = {}
    //         obj.col1 = col1
    //         obj.col2 = col2
    //         obj.col5 = col5
    //         if(currentRow.find('.chk').is(":checked")){
    //             arr.push(obj)
                
    //         }
    //     })
    //     console.log(arr);
    // });
    
   
// });
// 