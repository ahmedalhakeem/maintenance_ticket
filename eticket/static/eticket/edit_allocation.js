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
            tr.innerHTML +=`<td id="date_${value.id}">${value.allocate_date}</td><td id="driver_name_${value.id}">${value.driver_name_id}</td><td id="car_${value.id}">${value.car_id}</td><td><a class=${value.id} onclick="edit_allocation(${value.id},this)" href="#" type="button"><i class='far fa-edit' style='font-size:24px'></i></a></td>`
            table.append(tr)
        })
        wrap_allocations.append(table)
    })
    
})
function edit_allocation(id,e){
    e.innerHTML=''
    console.log(e.parentElement);
    const parent = e.parentElement
    
    const save_button = document.createElement('button')
    const cancel_button = document.querySelector('button')
    save_button.innerHTML = 'حفظ'
    cancel_button.innerHTML = 'الغاء'
    e.append(save_button)
    e.append(cancel_button)
    const driver= document.querySelector(`#driver_name_${id}`)
    const car = document.querySelector(`#car_${id}`)
    driver.innerHTML=""
    car.innerHTML= ""
    const allocate_date = document.querySelector(`#date_${id}`)
    console.log(allocate_date.innerHTML);
    allocate_date.innerHTML= `<input id='allocate_date_${id}' type="date" class="inputform style-uniform" value=${allocate_date.innerHTML}>`
    allocate_date.style.border = 'none'
    const select_car = document.createElement('select')
    select_car.id = `car_selected_${id}`
    const select_driver = document.createElement('select')
    select_driver.id =`driver_selected_${id}`
    car.append(select_car)
    driver.append(select_driver)
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
    save_button.addEventListener('click', (x)=>{
        save_after_edit(x, id)
    })
    cancel_button.addEventListener('click', (z)=>{
        cancel_change(z)
    })
}
// cancel button
const cancel_change = (e)=>{
    window.location
    return false
}
// Save after edit
const save_after_edit = (e, id)=>{
    const parent = e.target.parentElement
    const grand_parent = parent.parentElement
    console.log(grand_parent);
    const date = document.querySelector(`#allocate_date_${id}`)
    const driver = document.querySelector(`#driver_selected_${id}`)
    const car = document.querySelector(`#car_selected_${id}`)
    
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