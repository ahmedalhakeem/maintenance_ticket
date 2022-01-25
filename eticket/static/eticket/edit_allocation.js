document.addEventListener('DOMContentLoaded', ()=>{
    console.log('worked!');
})
$('.view-btn').on('click', function(e){
    const wrap_allocations = document.querySelector('#wrap-allocations')
    const allocation_rows = document.querySelector('#allocation-rows')
    // const view_info = document.querySelector('#view-info')
    console.log(allocation_rows);
    allocation_rows.innerHTML=''    
    wrap_allocations.style.display = 'flex'
    const this_row = $(this).closest('tr')
    const index_0 = this_row.find('td:eq(0)').text()
    ticket_id = Number(index_0)
    fetch(`./view_allocations/${ticket_id}`)
    .then(res=>{
        if(res.ok) return res.json()
        return res.json()
        .then(error=>{
            console.log(error);
        })
    })
    
    .then(data=>{
       data.data.forEach(value=>{
        allocation_rows.innerHTML +=`<tr id="row-${value.id}"><td id="date-${value.id}">${value.allocate_date}</td><td id="driver-${value.id}">${value.driver_name_id}</td><td id="car-${value.id}">${value.car_id}</td>
        <td id="edit-btn-${value.id}"><a id="edit-${value.id}" onclick="edit_allocation(${value.id},this)" href="#" type="button"><i class='far fa-edit' style='font-size:24px'></i></a>
        <a id="save-${value.id}" type="button" style="display:none"><i class="fa fa-save" style="font-size=24px"></i></a><a id="cancel-${value.id}" type="button" style="display:none"><i class="fa fa-times" style="font-size=24px"></i></a></tr>`
       })
    })
})
function edit_allocation(id,e){
    // collect all innerHTML
    const eidted_row = document.querySelector(`#row-${id}`)
    const date_info = document.querySelector(`#date-${id}`).innerHTML
    const driver_info = document.querySelector(`#driver-${id}`).innerHTML
    const car_info = document.querySelector(`#car-${id}`).innerHTML
    const edit_info = document.querySelector(`#edit-btn-${id}`).innerHTML
    const save_btn = document.querySelector(`#save-${id}`)
    const cancel_btn = document.querySelector(`#cancel-${id}`)
    const edit_btn = document.querySelector(`#edit-${id}`)
    edit_btn.style.display = 'none'
    cancel_btn.style.display = 'block'
    save_btn.style.display = 'block'
    cancel_btn.addEventListener('click', ()=>{
        cancel_btns(e, id, driver_info, car_info, date_info )
    })
    // collect all tds
    const date = document.querySelector(`#date-${id}`)
    const driver = document.querySelector(`#driver-${id}`)
    const car = document.querySelector(`#car-${id}`)
    const edit = document.querySelector(`#edit-btn-${id}`)
    // date.style.display = 'none'
    // driver.style.display = 'none'
    // car.style.display = 'none'
    date.innerHTML = ""
    driver.innerHTML = ""
    car.innerHTML = ""
    console.log(date_info);
    console.log(typeof(date_info));
    console.log(typeof(edit_info));
    date.innerHTML = `<input id="selected-date-${id}" type='date' value=${date_info}>`
    const driver_select = document.createElement('select')
    // 
    const driver_value = document.createElement('option')
    driver_value.value = driver_info
    driver_value.innerHTML = driver_info
    driver_select.append(driver_value)
    const car_value = document.createElement('option')
    car_value.value = car_info
    car_value.innerHTML = car_info
    // 
    const car_select = document.createElement('select')
    driver_select.id = `driver-select-${id}`
    car_select.id  = `car-select-${id}`
    car_select.append(car_value)
    driver.append(driver_select)
    car.append(car_select)
    fetch(`./get_allocations`)
    .then(res=>{
    if(res.ok) return res.json()
    return res.json()
    .then(error=>{
        console.log(error);
        })
    })
    .then(data=>{
        data.drivers.forEach(value=>{
            driver_select.innerHTML += `<option>${value.driver_name}</option>`
        })
        data.cars.forEach(value=>{
            car_select.innerHTML += `<option>${value.car_type}</option>`
        })
    })
    save_btn.addEventListener('click', ()=>{
        save_after_edit(id)
    })    

}   


// cancel button
const cancel_btns= (e, id, driver_info, car_info, date_info)=>{
    console.log(id);
    console.log(driver_info);
    console.log(car_info);
    console.log(date_info);
    document.querySelector(`#cancel-${id}`).style.display='none'
    document.querySelector(`#save-${id}`).style.display='none'
    document.querySelector(`#edit-${id}`).style.display='block'
    

    const driver = document.querySelector(`#driver-${id}`)
    const car = document.querySelector(`#car-${id}`)
    const date = document.querySelector(`#date-${id}`)
    car.innerHTML = car_info
    driver.innerHTML = driver_info
    date.innerHTML = date_info

}

// Save after edit
const save_after_edit = (id)=>{
    // console.log(id);    
    const selcted_driver = document.querySelector(`#driver-select-${id}`)
    const selcted_car = document.querySelector(`#car-select-${id}`)
    const selected_date = document.querySelector(`#selected-date-${id}`)
    console.log(selcted_car);
    // console.log(selcted_driver.value, selcted_car.value, selected_date.value);
    fetch(`./edit_allocated_saved/${id}?date=${selected_date.value}&car=${selcted_car.value}&driver=${selcted_driver.value}`)
    .then(res=>{
        if(res.ok) return res.json()
        return res.json()
        .then(error=>{
            console.log(error);
        })
    })
    .then(data=>{
        // console.log(data);

    })
    const row = document.querySelector(`#row-${id}`)
    console.log(row);
    document.querySelector(`#edit-${id}`).style.display = 'block'
    document.querySelector(`#cancel-${id}`).style.display = 'none'
    document.querySelector(`#save-${id}`).style.display = 'none'

    row.children['0'].innerHTML = selected_date.value
    row.children['1'].innerHTML = selcted_driver.value
    row.children['2'].innerHTML = selcted_car.value
    selected_date.style.display= 'none'
    selcted_driver.style.display = 'none'
    selcted_car.style.display = 'none'
}

// $('.edit-btn').on('click', function(e){
//     const wrapping_content = document.querySelector('#wrapping-content')
//     wrapping_content.innerHTML='';

//     const currentRow = $(this).closest('tr')
//     const id = currentRow.find('td:eq(0)').text();
//     const tour_days= currentRow.find('td:eq(5)').text();
//     days = Number(tour_days)
//     // console.log();
//     for(i=1; i<=days; i++){
//         const day = document.createElement('div')
//         day.id = `day${i}`
//         day.innerHTML = `اليوم ${i}`
//         day.style.display = 'flex'
//         day.style.margin = '50px'
//         wrapping_content.append(day)
//         const button = document.createElement('button')
//         button.innerHTML = 'تعديل'
//         const select_car = document.createElement('select')
//         const select_driver = document.createElement('select')
//         const car_choices = document.createElement('option')
//         car_choices.value = '0'
//         car_choices.innerHTML='اختر نوع المركبة من القائمة'
//         const driver_choices = document.createElement('option')
//         driver_choices.value = '0'
//         driver_choices.innerHTML = "اختر اسم السائق من القائمة"
//         select_car.append(car_choices)
//         select_driver.append(driver_choices)
//         fetch(`./get_allocations`)
//         .then(res=>{
//             if(res.ok) return res.json()
//             return res.json()
//             .then(error=>{
//                 console.log(error);
//             })
//         })
//         .then(data=>{
//             // adding  a select driver list 
//             data.drivers.forEach(value=>{
//                 select_driver.innerHTML += `<option>${value.driver_name}</option>`
//             })
//             day.append(select_driver)
//             //  adding a select car list
//             data.cars.forEach(value=>{
//                 select_car.innerHTML += `<option>${value.car_type}</option>`
//             })
//             day.append(select_car)
//             day.append(button)
//         })
//     }
    
// })