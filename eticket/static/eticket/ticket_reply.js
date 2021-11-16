document.addEventListener('DOMContentLoaded', ()=>{
    const select = document.querySelector('#choose-day')
    console.log(select);
    const wrap = document.querySelector('#wrap')
    wrap.style.display = 'none'
    const tour_wrapper = document.querySelector('.tour_wrapper')
    console.log(tour_wrapper);

        $('.allocate-btn').on('click', function(e){
            select.innerHTML= ''
            if(wrap.style.display === 'none'){
                wrap.style.display = 'block'
            }
            wrap.innerHTML=''
            const currentRow = $(this).closest('tr')
            const col1 = currentRow.find('td:eq(0)').text();
            const col2 = currentRow.find('td:eq(1)').text();
            const col5 = currentRow.find('td:eq(5)').text();
            const num = Number(col5)
            const id = Number(col1)
            tour_wrapper.innerHTML=''
           
            for(i=1; i<=num; i++){
                const div = document.createElement('div')
                div.className = `day${i}`
                div.innerHTML +=  `اليوم ${i}`
                tour_wrapper.append(div)
            }
            get_allocations(id, num)
        })

    const get_allocations = (id, num) =>{
        
        // console.log(num);
        for(i=1;i<=num;i++){
            const cont = document.querySelector(`.day${i}`)
            cont.style.display='flex'
            cont.style.margin= '50px'
            // ADD Car and Driver select, add input type date, and add assign btn
            const assign_btn= document.createElement('button')
            assign_btn.className = 'btn btn-primary allocated' 
            assign_btn.innerHTML = 'تخصيص'
            
            // console.log(assign_btn.innerHTML);
            const input_date = document.createElement('input')
            input_date.type = 'date'
            const car_select= document.createElement('select')
            const driver_select = document.createElement('select')
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
          
    $('#get-data').on('click', function(){
        const arr = []
        $('#tableid tbody tr').each(function(){
            const currentRow = $(this)
            const col1 = currentRow.find('td:eq(0)').text();
            const col2 = currentRow.find('td:eq(1)').text();
            const col5 = currentRow.find('td:eq(5)').text();

            const obj = {}
            obj.col1 = col1
            obj.col2 = col2
            obj.col5 = col5
            if(currentRow.find('.chk').is(":checked")){
                arr.push(obj)
                
            }
        })
        console.log(arr);
    });
    
   
});
$('.send-memo-status').on('click', function(){
    const currentRow = $(this).closest('tr');
    const col1 = currentRow.find('td:eq(0)').text()
    const notes = currentRow.find('td:eq(7)').text()
    
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
            console.log(data.data.id)
            allocate_per_day(data.data.id)
        
        })
        // console.log(currentRow.children);
        currentRow.css("background-color", "green")
        currentRow.find('td:eq(8)').text('dd')
        // console.log(col8);
        // check_delivery(currentRow)
    })
    const allocate = document.querySelector('.allocated')
console.log(allocate);

})


// 