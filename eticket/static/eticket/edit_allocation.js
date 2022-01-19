document.addEventListener('DOMContentLoaded', ()=>{
    console.log('worked!');
})
$('.view-btn').on('click', function(e){
    const wrap_allocations = document.querySelector('#wrap-allocations')
    wrap_allocations.innerHTML=""
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
        const table = document.createElement('table')
        table.className = 'table table-bordered'
        const thead = document.createElement('thead')
        thead.innerHTML = '<tr class="table-primary"><th>تاريخ الجولة</th><th>اسم السائق </th> <th>نوع المركبة</th><th>تعديل</th></tr>'
        table.append(thead)
        data.data.forEach(value=>{
            const tr= document.createElement('tr')
            tr.innerHTML +=`<td><span id="date_${value.id}">${value.allocate_date}</span></td><td><span id="driver_name_${value.id}">${value.driver_name_id}</span></td><td><span id="car_${value.id}">${value.car_id}</span></td><td><a id="edit_${value.id}" onclick="edit_allocation(${value.id},this)" href="#" type="button"><i class='far fa-edit' style='font-size:24px'></i></a></td>`
            table.append(tr)
        })
        wrap_allocations.append(table)
    })
    
})
function edit_allocation(id,e){
    const driver= document.querySelector(`#driver_name_${id}`)
    const car = document.querySelector(`#car_${id}`)
    const allocate_date = document.querySelector(`#date_${id}`)
    const edit_btn = document.querySelector(`#edit_${id}`)
    console.log(edit_btn);
    driver.style.display= 'none'
    car.style.display = 'none'
    allocate_date.style.display = 'none'
    edit_btn.style.display = 'none'
    const td_button = e.parentElement
    const tr_row = td_button.parentElement
    console.log(tr_row.children);
    // e.innerHTML=''
    // console.log(id);
    // // Take all td elements
    const new_date = tr_row.children[0];
    const new_driver = tr_row.children[1]
    const new_car = tr_row.children[2]
    const btn = tr_row.children[3]
    // create a new save btn and append it to the event element <a>
    const save_link = document.createElement('a')
    save_link.innerHTML = '<i class="fa fa-save" style="font-size=24px"></i>'
    btn.append(save_link)
    // // get all span elements from allocation row and assign each one to a variable, and then hide them

    // // allocate_date.style.display= 'none'
    // // Create new elements, then append them to the row elements
    // new_date.innerHTML = `<input id='allocate_date_${id}' type="date" class="inputform style-uniform" value="${allocate_date.innerHTML}">`
    const select_car = document.createElement('select')
    const select_driver = document.createElement('select')
    const date = document.createElement('input')
    date.id = `new_date_${id}`
    date.value = allocate_date.innerHTML
    date.type = 'date'
    new_date.append(date)
    select_car.id = `car_selected_${id}`
    new_car.append(select_car)
    select_driver.id =`driver_selected_${id}`
    new_driver.append(select_driver)
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
            select_driver.innerHTML += `<option>${value.driver_name}</option>`
        })
        data.cars.forEach(value=>{
            select_car.innerHTML += `<option>${value.car_type}</option>`
        })
    })
    save_link.addEventListener('click', ()=>{
        save_after_edit(id)
    })
   
}
// cancel button

// Save after edit
const save_after_edit = (id)=>{
    console.log(id);    
    const date = document.querySelector(`#new_date_${id}`)
    // console.log(date.value);
    const driver = document.querySelector(`#driver_selected_${id}`)
    const car = document.querySelector(`#car_selected_${id}`)
    console.log(car.value);
    fetch(`./edit_allocated_saved/${id}?date=${date.value}&car=${car.value}&driver=${driver.value}`)
    .then(res=>{
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

$('.edit-btn').on('click', function(e){
    const wrapping_content = document.querySelector('#wrapping-content')
    wrapping_content.innerHTML='';

    const currentRow = $(this).closest('tr')
    const id = currentRow.find('td:eq(0)').text();
    const tour_days= currentRow.find('td:eq(5)').text();
    days = Number(tour_days)
    // console.log();
    for(i=1; i<=days; i++){
        const day = document.createElement('div')
        day.id = `day${i}`
        day.innerHTML = `اليوم ${i}`
        day.style.display = 'flex'
        day.style.margin = '50px'
        wrapping_content.append(day)
        const button = document.createElement('button')
        button.innerHTML = 'تعديل'
        const select_car = document.createElement('select')
        const select_driver = document.createElement('select')
        const car_choices = document.createElement('option')
        car_choices.value = '0'
        car_choices.innerHTML='اختر نوع المركبة من القائمة'
        const driver_choices = document.createElement('option')
        driver_choices.value = '0'
        driver_choices.innerHTML = "اختر اسم السائق من القائمة"
        select_car.append(car_choices)
        select_driver.append(driver_choices)
        fetch(`./get_allocations`)
        .then(res=>{
            if(res.ok) return res.json()
            return res.json()
            .then(error=>{
                console.log(error);
            })
        })
        .then(data=>{
            // adding  a select driver list 
            data.drivers.forEach(value=>{
                select_driver.innerHTML += `<option>${value.driver_name}</option>`
            })
            day.append(select_driver)
            //  adding a select car list
            data.cars.forEach(value=>{
                select_car.innerHTML += `<option>${value.car_type}</option>`
            })
            day.append(select_car)
            day.append(button)
        })
    }
    
})